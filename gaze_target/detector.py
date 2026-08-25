"""Head detector: DEIMv2 HGNetV2-Pico Wholebody34 ONNX.

Model source: https://github.com/PINTO0309/PINTO_model_zoo/tree/main/472_DEIMv2-Wholebody34

I/O contract, verified against the released graph and upstream reference:

  input   input_bgr          float32[N, 3, H, W]  BGR, raw 0-255, NO resize
                                                 (spatial dims are dynamic, so the
                                                 native frame size is fed directly)
  output  label_xyxy_score   float32[N, 340, 6]   per row: [classid, x1, y1, x2, y2, score]
                                                  xyxy normalized to 0..1

Class id 7 is `head` in the Wholebody34 label set (id 0 is the whole body).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import onnxruntime as ort

HEAD_CLASS_ID = 7
BODY_CLASS_ID = 0


@dataclass
class Detection:
    box: tuple[int, int, int, int]  # x1, y1, x2, y2 in frame pixels
    score: float

    @property
    def area(self) -> int:
        x1, y1, x2, y2 = self.box
        return max(0, x2 - x1) * max(0, y2 - y1)


class HeadDetector:
    def __init__(
        self,
        model_path: str | Path,
        score_threshold: float = 0.35,
        providers: list[str] | None = None,
    ) -> None:
        self.model_path = Path(model_path)
        if not self.model_path.is_file():
            raise FileNotFoundError(f"Head detector model not found: {self.model_path}")
        self.score_threshold = score_threshold
        self.session = ort.InferenceSession(
            str(self.model_path),
            providers=providers or ["CPUExecutionProvider"],
        )
        self._input = self.session.get_inputs()[0].name

    def __call__(self, frame_bgr: np.ndarray) -> list[Detection]:
        frame_h, frame_w = frame_bgr.shape[:2]
        chw = frame_bgr.transpose(2, 0, 1)
        blob = np.ascontiguousarray(chw[None, ...], dtype=np.float32)

        raw = self.session.run(None, {self._input: blob})[0][0]  # [340, 6]

        dets: list[Detection] = []
        for row in raw:
            classid = int(row[0])
            score = float(row[5])
            if classid != HEAD_CLASS_ID or score < self.score_threshold:
                continue
            x1 = int(max(0.0, row[1]) * frame_w)
            y1 = int(max(0.0, row[2]) * frame_h)
            x2 = int(min(1.0, row[3]) * frame_w)
            y2 = int(min(1.0, row[4]) * frame_h)
            if x2 <= x1 or y2 <= y1:
                continue
            dets.append(Detection(box=(x1, y1, x2, y2), score=score))

        dets.sort(key=lambda d: d.score, reverse=True)
        return dets

    def primary_head(self, frame_bgr: np.ndarray) -> Detection | None:
        """Pick the single head to track.

        A bedside camera is a single-subject scene, but a caregiver or visitor
        may enter frame. Largest-area head is a better heuristic than
        highest-score here, because the patient is nearest the camera and
        therefore appears largest; a passing visitor is further away.
        """
        dets = self(frame_bgr)
        if not dets:
            return None
        return max(dets, key=lambda d: d.area)
