"""Gaze-LLE (distilled, DINOv3/HGNetV2) ONNX wrapper.

Model source: https://github.com/PINTO0309/gazelle-dinov3 (distillations of
Gaze-LLE, CVPR 2025 -- https://arxiv.org/abs/2412.09586)

I/O contract, verified empirically against the released ONNX graphs and the
upstream reference implementation:

  inputs
    image_bgr        float32[1, 3, 640, 640]   BGR, raw 0-255, NO /255 scaling,
                                               plain stretch resize (no letterbox)
    bboxes_x1y1x2y2  float32[1, heads, 4]      head boxes normalized to 0..1

  outputs
    heatmap          float32[heads, 64, 64]    gaze heatmap, values in 0..1
    inout            float32[heads]            1.0 => gaze target is inside frame

The 64x64 heatmap is the model's hard spatial-resolution limit: at a 640x480
frame each heatmap cell covers ~10x7.5 px, so targets smaller than a few cells
cannot be reliably discriminated. `TargetSet.resolution_report` quantifies this.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import cv2
import numpy as np
import onnxruntime as ort


@dataclass
class GazeResult:
    """Per-head gaze output, already mapped back to full frame coordinates."""

    heatmap: np.ndarray  # float32[H, W], values 0..1, frame-sized
    inout: float  # 1.0 => target inside frame
    head_box: tuple[int, int, int, int]  # x1, y1, x2, y2 in frame pixels
    peak_xy: tuple[int, int]  # argmax of heatmap, frame pixels
    raw_heatmap: np.ndarray  # float32[64, 64], pre-resize


class GazelleONNX:
    """Runs a distilled Gaze-LLE ONNX model on CPU (or CUDA if available)."""

    def __init__(self, model_path: str | Path, providers: list[str] | None = None) -> None:
        self.model_path = Path(model_path)
        if not self.model_path.is_file():
            raise FileNotFoundError(f"Gaze-LLE model not found: {self.model_path}")

        self.session = ort.InferenceSession(
            str(self.model_path),
            providers=providers or ["CPUExecutionProvider"],
        )

        inputs = self.session.get_inputs()
        self._image_input = inputs[0].name
        self._bbox_input = inputs[1].name
        # Static spatial dims are baked into the export (640/416/320).
        _, _, self.in_h, self.in_w = inputs[0].shape

        out_names = [o.name for o in self.session.get_outputs()]
        self._heatmap_idx = out_names.index("heatmap")
        self._inout_idx = out_names.index("inout")

    def _preprocess(self, frame_bgr: np.ndarray) -> np.ndarray:
        """Stretch-resize to the model's input size. No normalization: the
        released graphs fold normalization inside the model."""
        resized = cv2.resize(
            frame_bgr, (self.in_w, self.in_h), interpolation=cv2.INTER_LINEAR
        )
        chw = resized.transpose(2, 0, 1)
        return np.ascontiguousarray(chw[None, ...], dtype=np.float32)

    def __call__(
        self,
        frame_bgr: np.ndarray,
        head_boxes: list[tuple[int, int, int, int]],
    ) -> list[GazeResult]:
        if not head_boxes:
            return []

        frame_h, frame_w = frame_bgr.shape[:2]
        if frame_h == 0 or frame_w == 0:
            return []

        norm_boxes: list[list[float]] = []
        kept: list[tuple[int, int, int, int]] = []
        for x1, y1, x2, y2 in head_boxes:
            nx1 = float(np.clip(x1 / frame_w, 0.0, 1.0))
            ny1 = float(np.clip(y1 / frame_h, 0.0, 1.0))
            nx2 = float(np.clip(x2 / frame_w, 0.0, 1.0))
            ny2 = float(np.clip(y2 / frame_h, 0.0, 1.0))
            if nx2 <= nx1 or ny2 <= ny1:
                continue  # degenerate after clipping
            norm_boxes.append([nx1, ny1, nx2, ny2])
            kept.append((x1, y1, x2, y2))

        if not norm_boxes:
            return []

        outputs = self.session.run(
            None,
            {
                self._image_input: self._preprocess(frame_bgr),
                self._bbox_input: np.asarray([norm_boxes], dtype=np.float32),
            },
        )
        heatmaps = outputs[self._heatmap_idx]
        inouts = outputs[self._inout_idx]

        results: list[GazeResult] = []
        for i, box in enumerate(kept):
            raw = np.clip(heatmaps[i].astype(np.float32), 0.0, 1.0)
            # Heatmap covers the whole frame because preprocessing was a plain
            # stretch resize -- there is no letterbox padding to undo.
            full = cv2.resize(raw, (frame_w, frame_h), interpolation=cv2.INTER_LINEAR)
            py, px = np.unravel_index(int(np.argmax(full)), full.shape)
            results.append(
                GazeResult(
                    heatmap=full,
                    inout=float(inouts[i]),
                    head_box=box,
                    peak_xy=(int(px), int(py)),
                    raw_heatmap=raw,
                )
            )
        return results
