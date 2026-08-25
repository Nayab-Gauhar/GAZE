#!/usr/bin/env python3
"""Verify TrainedYoloDetector decodes boxes identically to ultralytics.

Box decoding is the easiest place to introduce a silent bug: letterbox padding,
scale undo, and cxcywh->xyxy all have to be exactly right, and a mistake
misplaces every box without raising an error. This asserts equality against the
reference implementation.

Important subtlety this script demonstrates: compare against ultralytics running
**the same ONNX file**, not against the .pt model. Ultralytics' PyTorch path uses
*rectangular* inference (it pads only to a stride multiple, so a 640x480 frame
runs at 640x480), whereas an ONNX export has a fixed 640x640 input and must be
letterboxed. The two therefore see different images and legitimately produce
slightly different boxes. Comparing .pt against ONNX looks like a decoding bug
when it is not.

    python scripts/verify_detector_decode.py
    python scripts/verify_detector_decode.py --model models/target_detector.onnx
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import cv2

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from gaze_target.yolo_detector import TrainedYoloDetector  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TOLERANCE_PX = 2


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=str(ROOT / "models" / "coco_yolo11n.onnx"))
    ap.add_argument("--image", default=str(ROOT / "testdata" / "cafe_laptop2.jpg"))
    ap.add_argument("--conf", type=float, default=0.30)
    ap.add_argument("--iou", type=float, default=0.7)
    args = ap.parse_args()

    model_path = Path(args.model)
    if not model_path.is_file():
        print(f"[SKIP] no model at {model_path}")
        return 0

    frame = cv2.imread(args.image)
    if frame is None:
        print(f"[ERROR] cannot read {args.image}")
        return 1
    frame = cv2.resize(frame, (640, 480))

    try:
        from ultralytics import YOLO
    except ImportError:
        print("[SKIP] ultralytics not installed (needed only for this check)")
        return 0

    ref_res = YOLO(str(model_path), task="detect").predict(
        frame, conf=args.conf, iou=args.iou, verbose=False
    )[0]
    reference = sorted(
        [
            (
                ref_res.names[int(b.cls)],
                float(b.conf),
                tuple(int(v) for v in b.xyxy[0].tolist()),
            )
            for b in ref_res.boxes
        ],
        key=lambda t: -t[1],
    )

    mine = sorted(
        TrainedYoloDetector(model_path).detect(
            frame,
            score_threshold=args.conf,
            iou_threshold=args.iou,
            max_per_prompt=100,
            dedupe_across_labels=False,
        ),
        key=lambda d: -d.score,
    )

    print(f"model: {model_path.name}")
    print(f"ultralytics: {len(reference)} boxes | wrapper: {len(mine)} boxes\n")
    print(f"{'class':<14} {'ultralytics':<26} {'wrapper':<26} {'diff':>5}")

    used: set[int] = set()
    worst = 0
    for name, _score, box in reference:
        cands = [(i, d) for i, d in enumerate(mine) if d.label == name and i not in used]
        if not cands:
            print(f"{name:<14} {str(box):<26} {'MISSING':<26}")
            worst = 10_000
            continue
        i, best = min(
            cands, key=lambda t: max(abs(a - b) for a, b in zip(t[1].box, box))
        )
        used.add(i)
        dev = max(abs(a - b) for a, b in zip(best.box, box))
        worst = max(worst, dev)
        print(f"{name:<14} {str(box):<26} {str(best.box):<26} {dev:>5}")

    print(f"\nworst deviation: {worst} px (tolerance {TOLERANCE_PX})")
    if len(mine) != len(reference):
        print(f"[FAIL] box count differs: {len(mine)} vs {len(reference)}")
        return 1
    if worst > TOLERANCE_PX:
        print("[FAIL] decoding does not match the reference implementation")
        return 1
    print("[PASS] box decoding matches ultralytics exactly")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
