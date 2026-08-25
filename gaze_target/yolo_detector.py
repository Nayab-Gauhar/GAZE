"""Inference for a fine-tuned YOLO detector exported to ONNX.

Deliberately exposes the same `detect()` / `best_per_prompt()` surface as
`OpenVocabDetector`, so a trained detector drops into `ObjectRegistry` and the
pipeline with no other changes. The difference is that the class list is fixed at
training time, so the `prompts` argument acts as a *filter* over trained classes
rather than an open query.

Ultralytics detect exports have output `[1, 4 + nc, N]`:
  rows 0..3   cxcywh in input-pixel coordinates (NOT normalized)
  rows 4..    per-class scores, already activated (no objectness row in v8+)

Preprocessing is letterboxed (aspect preserved, grey padding), which differs
from both other models in this project -- Gaze-LLE stretches, OWLv2 pads to a
square then resizes. Each undo is therefore different, and getting it wrong
silently misplaces boxes.
"""

from __future__ import annotations

from pathlib import Path

import cv2
import numpy as np
import onnxruntime as ort

from .object_detector import ObjectDetection, _nms


class TrainedYoloDetector:
    def __init__(
        self,
        model_path: str | Path,
        class_names: list[str] | None = None,
        providers: list[str] | None = None,
    ) -> None:
        self.model_path = Path(model_path)
        if not self.model_path.is_file():
            raise FileNotFoundError(
                f"trained detector not found: {self.model_path}\n"
                "  train one with scripts/train_detector.py"
            )
        self.session = ort.InferenceSession(
            str(self.model_path), providers=providers or ["CPUExecutionProvider"]
        )
        inp = self.session.get_inputs()[0]
        self._input_name = inp.name
        _, _, self.in_h, self.in_w = inp.shape
        if not isinstance(self.in_h, int):  # dynamic axes
            self.in_h = self.in_w = 640

        # Ultralytics stores the class names in ONNX metadata as a dict literal.
        self.class_names = class_names or self._names_from_metadata()

    def _names_from_metadata(self) -> list[str]:
        meta = self.session.get_modelmeta().custom_metadata_map or {}
        raw = meta.get("names")
        if raw:
            try:
                import ast

                parsed = ast.literal_eval(raw)
                if isinstance(parsed, dict):
                    return [parsed[k] for k in sorted(parsed)]
                if isinstance(parsed, list):
                    return list(parsed)
            except (ValueError, SyntaxError, KeyError):
                pass
        # Fall back to indices; caller can pass class_names explicitly.
        out = self.session.get_outputs()[0].shape
        nc = (out[1] - 4) if isinstance(out[1], int) else 0
        return [str(i) for i in range(nc)]

    # ------------------------------------------------------------- preprocess

    def _letterbox(self, frame_bgr: np.ndarray) -> tuple[np.ndarray, float, int, int]:
        h, w = frame_bgr.shape[:2]
        scale = min(self.in_w / w, self.in_h / h)
        nw, nh = int(round(w * scale)), int(round(h * scale))
        resized = cv2.resize(frame_bgr, (nw, nh), interpolation=cv2.INTER_LINEAR)
        canvas = np.full((self.in_h, self.in_w, 3), 114, dtype=np.uint8)
        dx, dy = (self.in_w - nw) // 2, (self.in_h - nh) // 2
        canvas[dy:dy + nh, dx:dx + nw] = resized

        rgb = cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB).astype(np.float32) / 255.0
        chw = rgb.transpose(2, 0, 1)
        return np.ascontiguousarray(chw[None, ...], dtype=np.float32), scale, dx, dy

    # ---------------------------------------------------------------- detect

    def detect(
        self,
        frame_bgr: np.ndarray,
        prompts: list[str] | None = None,
        score_threshold: float = 0.25,
        iou_threshold: float = 0.45,
        max_per_prompt: int = 3,
        dedupe_across_labels: bool = True,
    ) -> list[ObjectDetection]:
        frame_h, frame_w = frame_bgr.shape[:2]
        blob, scale, dx, dy = self._letterbox(frame_bgr)
        raw = self.session.run(None, {self._input_name: blob})[0]

        pred = raw[0]                      # [4 + nc, N]
        if pred.shape[0] < pred.shape[1]:  # already [4+nc, N]
            boxes_xywh = pred[:4].T
            scores_all = pred[4:].T
        else:                              # [N, 4+nc]
            boxes_xywh = pred[:, :4]
            scores_all = pred[:, 4:]

        cls_ids = scores_all.argmax(axis=1)
        cls_scores = scores_all.max(axis=1)
        keep_mask = cls_scores >= score_threshold
        if not keep_mask.any():
            return []

        boxes_xywh = boxes_xywh[keep_mask]
        cls_ids = cls_ids[keep_mask]
        cls_scores = cls_scores[keep_mask]

        cx, cy, bw, bh = boxes_xywh.T
        # Undo the letterbox: remove padding, then the scale.
        x1 = (cx - bw / 2 - dx) / scale
        y1 = (cy - bh / 2 - dy) / scale
        x2 = (cx + bw / 2 - dx) / scale
        y2 = (cy + bh / 2 - dy) / scale
        xyxy = np.stack([x1, y1, x2, y2], axis=1)

        allowed = None
        if prompts:
            wanted = {p.lower() for p in prompts}
            allowed = {
                i for i, n in enumerate(self.class_names) if n.lower() in wanted
            }

        results: list[ObjectDetection] = []
        for cid in np.unique(cls_ids):
            if allowed is not None and int(cid) not in allowed:
                continue
            idx = np.where(cls_ids == cid)[0]
            keep = _nms(xyxy[idx], cls_scores[idx], iou_threshold)
            name = (
                self.class_names[int(cid)]
                if int(cid) < len(self.class_names)
                else str(int(cid))
            )
            for k in keep[:max_per_prompt]:
                j = idx[k]
                bx1 = int(np.clip(xyxy[j, 0], 0, frame_w - 1))
                by1 = int(np.clip(xyxy[j, 1], 0, frame_h - 1))
                bx2 = int(np.clip(xyxy[j, 2], 0, frame_w))
                by2 = int(np.clip(xyxy[j, 3], 0, frame_h))
                if bx2 - bx1 < 3 or by2 - by1 < 3:
                    continue
                results.append(
                    ObjectDetection(label=name, box=(bx1, by1, bx2, by2),
                                    score=float(cls_scores[j]))
                )

        results.sort(key=lambda d: d.score, reverse=True)

        if dedupe_across_labels and len(results) > 1:
            b = np.array([r.box for r in results], dtype=np.float32)
            s = np.array([r.score for r in results], dtype=np.float32)
            keep = _nms(b, s, iou_threshold)
            results = [results[i] for i in sorted(keep)]
            results.sort(key=lambda d: d.score, reverse=True)
        return results

    def best_per_prompt(
        self, frame_bgr: np.ndarray, prompts: list[str] | None = None, **kwargs
    ) -> dict[str, ObjectDetection]:
        best: dict[str, ObjectDetection] = {}
        for det in self.detect(frame_bgr, prompts, **kwargs):
            if det.label not in best or det.score > best[det.label].score:
                best[det.label] = det
        return best
