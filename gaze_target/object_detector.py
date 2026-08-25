"""Open-vocabulary object detection with OWLv2 (ONNX, no PyTorch).

Model: onnx-community/owlv2-base-patch16-ensemble-ONNX (quantized, ~163 MB)
Paper: Scaling Open-Vocabulary Object Detection -- https://arxiv.org/abs/2306.09683

This exists so targets can be found automatically from text prompts instead of
being clicked by hand: you say "water bottle" and it finds it. Unlike a COCO
detector (fixed 80 classes) it handles things like "medicine strip" or
"calling bell" that have no COCO category.

It runs **once at setup**, not per frame, because the bedside scene is static.
That is why a heavyweight model is acceptable here: at ~2-4 s on CPU its latency
is irrelevant to runtime throughput.

Verified I/O contract:

  inputs
    pixel_values    float32[1, 3, 960, 960]     see _preprocess_image for the
                                                exact rescale/pad/resize/normalize
    input_ids       int64[num_queries, 16]      CLIP BPE, padded to max_length=16
    attention_mask  int64[num_queries, 16]

  outputs
    logits          float32[1, 3600, num_queries]   sigmoid -> confidence
    pred_boxes      float32[1, 3600, 4]             cxcywh, normalized to the
                                                    PADDED SQUARE, not the frame

The padding detail matters: Owlv2ImageProcessor pads to a square (bottom/right)
before resizing, so boxes must be scaled by max(H, W) rather than by H and W
independently. Getting this wrong silently misplaces every box.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import cv2
import numpy as np
import onnxruntime as ort

# CLIP normalization constants, from preprocessor_config.json.
IMAGE_MEAN = np.array([0.48145466, 0.4578275, 0.40821073], dtype=np.float32)
IMAGE_STD = np.array([0.26862954, 0.26130258, 0.27577711], dtype=np.float32)
INPUT_SIZE = 960
MAX_TEXT_LEN = 16
PAD_VALUE = 0.5  # grey padding, applied after rescaling to 0..1


@dataclass
class ObjectDetection:
    label: str
    """The text prompt that matched, e.g. "water bottle"."""
    box: tuple[int, int, int, int]
    score: float

    @property
    def area(self) -> int:
        x1, y1, x2, y2 = self.box
        return max(0, x2 - x1) * max(0, y2 - y1)


def _nms(boxes: np.ndarray, scores: np.ndarray, iou_threshold: float) -> list[int]:
    """Greedy NMS in numpy, to avoid a torchvision dependency."""
    if len(boxes) == 0:
        return []
    x1, y1, x2, y2 = boxes[:, 0], boxes[:, 1], boxes[:, 2], boxes[:, 3]
    areas = np.maximum(0.0, x2 - x1) * np.maximum(0.0, y2 - y1)
    order = scores.argsort()[::-1]

    keep: list[int] = []
    while order.size > 0:
        i = order[0]
        keep.append(int(i))
        if order.size == 1:
            break
        rest = order[1:]
        xx1 = np.maximum(x1[i], x1[rest])
        yy1 = np.maximum(y1[i], y1[rest])
        xx2 = np.minimum(x2[i], x2[rest])
        yy2 = np.minimum(y2[i], y2[rest])
        inter = np.maximum(0.0, xx2 - xx1) * np.maximum(0.0, yy2 - yy1)
        iou = inter / np.maximum(1e-9, areas[i] + areas[rest] - inter)
        order = rest[iou <= iou_threshold]
    return keep


class OpenVocabDetector:
    def __init__(
        self,
        model_dir: str | Path,
        providers: list[str] | None = None,
    ) -> None:
        from tokenizers import Tokenizer  # local import: optional dependency

        self.model_dir = Path(model_dir)
        model_path = self.model_dir / "model_quantized.onnx"
        tok_path = self.model_dir / "tokenizer.json"
        for p in (model_path, tok_path):
            if not p.is_file():
                raise FileNotFoundError(
                    f"missing {p}\n  run: ./scripts/download_owlv2.sh"
                )

        self.tokenizer = Tokenizer.from_file(str(tok_path))
        self.tokenizer.enable_padding(length=MAX_TEXT_LEN, pad_id=0, pad_token="!")
        self.tokenizer.enable_truncation(max_length=MAX_TEXT_LEN)

        self.session = ort.InferenceSession(
            str(model_path), providers=providers or ["CPUExecutionProvider"]
        )

    # ------------------------------------------------------------- preprocess

    @staticmethod
    def _preprocess_image(frame_bgr: np.ndarray) -> tuple[np.ndarray, int]:
        """Replicate Owlv2ImageProcessor. Returns the tensor and the padded side
        length, which is the scale factor needed to decode boxes."""
        rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB).astype(np.float32) / 255.0
        h, w = rgb.shape[:2]

        # Pad to a square, bottom and right, with grey.
        side = max(h, w)
        padded = np.full((side, side, 3), PAD_VALUE, dtype=np.float32)
        padded[:h, :w] = rgb

        resized = cv2.resize(
            padded, (INPUT_SIZE, INPUT_SIZE), interpolation=cv2.INTER_CUBIC
        )
        normalized = (resized - IMAGE_MEAN) / IMAGE_STD
        chw = normalized.transpose(2, 0, 1)
        return np.ascontiguousarray(chw[None, ...], dtype=np.float32), side

    def _encode_prompts(self, prompts: list[str]) -> tuple[np.ndarray, np.ndarray]:
        # OWL models are trained with this prompt template.
        texts = [f"a photo of a {p}" for p in prompts]
        encodings = self.tokenizer.encode_batch(texts)
        ids = np.array([e.ids for e in encodings], dtype=np.int64)
        mask = np.array([e.attention_mask for e in encodings], dtype=np.int64)
        return ids, mask

    # ---------------------------------------------------------------- detect

    def detect(
        self,
        frame_bgr: np.ndarray,
        prompts: list[str],
        score_threshold: float = 0.15,
        iou_threshold: float = 0.4,
        max_per_prompt: int = 3,
        dedupe_across_labels: bool = True,
    ) -> list[ObjectDetection]:
        """
        dedupe_across_labels:
            NMS is per-prompt, so with a large vocabulary two *different* labels
            routinely claim the same region (a bright rectangle scoring as both
            "television" and "tissue box"). When true, overlapping boxes from
            different labels are collapsed to the highest-scoring one.
        """
        if not prompts:
            return []

        frame_h, frame_w = frame_bgr.shape[:2]
        pixel_values, side = self._preprocess_image(frame_bgr)
        input_ids, attention_mask = self._encode_prompts(prompts)

        logits, pred_boxes = self.session.run(
            ["logits", "pred_boxes"],
            {
                "pixel_values": pixel_values,
                "input_ids": input_ids,
                "attention_mask": attention_mask,
            },
        )

        scores = 1.0 / (1.0 + np.exp(-logits[0]))  # sigmoid -> [3600, n_prompts]
        boxes_cxcywh = pred_boxes[0]  # [3600, 4], normalized to the padded square

        # cxcywh -> xyxy, then scale by the padded side (NOT by w and h separately).
        cx, cy, bw, bh = boxes_cxcywh.T
        xyxy = np.stack(
            [
                (cx - bw / 2) * side,
                (cy - bh / 2) * side,
                (cx + bw / 2) * side,
                (cy + bh / 2) * side,
            ],
            axis=1,
        )

        results: list[ObjectDetection] = []
        for qi, prompt in enumerate(prompts):
            col = scores[:, qi]
            cand = np.where(col >= score_threshold)[0]
            if cand.size == 0:
                continue
            keep = _nms(xyxy[cand], col[cand], iou_threshold)
            for k in keep[:max_per_prompt]:
                idx = cand[k]
                x1, y1, x2, y2 = xyxy[idx]
                # Clip into the real frame: padding lay outside it.
                x1 = int(np.clip(x1, 0, frame_w - 1))
                y1 = int(np.clip(y1, 0, frame_h - 1))
                x2 = int(np.clip(x2, 0, frame_w))
                y2 = int(np.clip(y2, 0, frame_h))
                if x2 - x1 < 4 or y2 - y1 < 4:
                    continue
                results.append(
                    ObjectDetection(label=prompt, box=(x1, y1, x2, y2),
                                    score=float(col[idx]))
                )

        results.sort(key=lambda d: d.score, reverse=True)

        if dedupe_across_labels and len(results) > 1:
            boxes = np.array([r.box for r in results], dtype=np.float32)
            scores = np.array([r.score for r in results], dtype=np.float32)
            keep = _nms(boxes, scores, iou_threshold)
            results = [results[i] for i in sorted(keep)]
            results.sort(key=lambda d: d.score, reverse=True)

        return results

    def best_per_prompt(
        self, frame_bgr: np.ndarray, prompts: list[str], **kwargs
    ) -> dict[str, ObjectDetection]:
        """One detection per prompt -- the shape target registration needs."""
        best: dict[str, ObjectDetection] = {}
        for det in self.detect(frame_bgr, prompts, **kwargs):
            if det.label not in best or det.score > best[det.label].score:
                best[det.label] = det
        return best
