#!/usr/bin/env python3
"""Fine-tune a small YOLO detector on your corrected labels, and export ONNX.

Why fine-tune at all, when OWLv2 already does open-vocabulary detection?

  * **Reliability.** OWLv2 missed MEDICINE entirely and produced spurious
    CALLING_BELL boxes. A detector trained on *your* actual objects will not.
  * **Speed.** OWLv2 costs ~5 s/frame on CPU so it must run on a background
    thread. A fine-tuned YOLO-nano runs in ~10-20 ms, fast enough to run every
    frame, which removes the staleness compromise entirely.
  * **Reproducibility.** For a paper, a fixed trained detector is a controlled
    component; a foundation model queried by text prompt is a moving target.

What it does NOT fix: the 64x64 gaze heatmap ceiling. A perfect detector still
cannot make an 11-pixel-tall medicine strip separable. Fix that with camera
distance and resolution -- see scripts/plan_layout.py.

    python scripts/train_detector.py --data data/yolo/data.yaml
    python scripts/train_detector.py --data data/yolo/data.yaml --epochs 100 --model yolo11s.pt

Requires: pip install ultralytics   (this pulls in PyTorch, ~2 GB -- needed for
TRAINING only. Inference stays on onnxruntime via the exported ONNX.)
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True, help="path to data.yaml")
    ap.add_argument("--model", default="yolo11n.pt",
                    help="pretrained checkpoint to fine-tune from")
    ap.add_argument("--epochs", type=int, default=80)
    ap.add_argument("--imgsz", type=int, default=640,
                    help="must match the resolution you will deploy at")
    ap.add_argument("--batch", type=int, default=8)
    ap.add_argument("--device", default="cpu", help="'cpu', '0' for first GPU")
    ap.add_argument("--freeze", type=int, default=0,
                    help="freeze the first N layers; try 10 for very small datasets")
    ap.add_argument("--patience", type=int, default=25)
    ap.add_argument("--project", default="runs/detect")
    ap.add_argument("--name", default="targets")
    ap.add_argument("--out", default="models/target_detector.onnx")
    ap.add_argument("--no-export", action="store_true")
    args = ap.parse_args()

    try:
        from ultralytics import YOLO
    except ImportError:
        print("[ERROR] ultralytics not installed.\n  pip install ultralytics")
        return 1

    data_path = Path(args.data)
    if not data_path.is_file():
        print(f"[ERROR] no data.yaml at {data_path}")
        print("  run scripts/autolabel.py first")
        return 1

    print(f"data      : {data_path}")
    print(f"base model: {args.model}")
    print(f"epochs    : {args.epochs}   imgsz: {args.imgsz}   device: {args.device}")
    if args.device == "cpu":
        print("  NOTE: CPU training is slow. A GPU or Colab is strongly preferred.")
    print()

    model = YOLO(args.model)
    model.train(
        data=str(data_path),
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        device=args.device,
        freeze=args.freeze or None,
        patience=args.patience,
        project=args.project,
        name=args.name,
        exist_ok=True,
        # A fixed scene with a handful of objects overfits easily, so lean on
        # geometric and photometric augmentation rather than more epochs.
        hsv_h=0.015, hsv_s=0.7, hsv_v=0.4,
        degrees=8.0, translate=0.15, scale=0.4, shear=2.0,
        fliplr=0.5, flipud=0.0,          # never flip vertically: scenes are upright
        mosaic=1.0, erasing=0.2,
        verbose=True,
    )

    metrics = model.val(data=str(data_path), device=args.device, verbose=False)
    try:
        print("\nvalidation")
        print(f"  mAP50    : {metrics.box.map50:.4f}")
        print(f"  mAP50-95 : {metrics.box.map:.4f}")
        names = metrics.names if hasattr(metrics, "names") else {}
        if hasattr(metrics.box, "ap50") and len(metrics.box.ap50):
            print(f"\n  {'class':<16} {'AP50':>8}")
            for i, ap50 in enumerate(metrics.box.ap50):
                label = names.get(i, str(i)) if isinstance(names, dict) else str(i)
                flag = "   <-- weak, add more images" if ap50 < 0.5 else ""
                print(f"  {label:<16} {ap50:>8.4f}{flag}")
    except Exception as exc:  # noqa: BLE001
        print(f"  (could not summarise metrics: {exc})")

    if args.no_export:
        return 0

    print("\nexporting ONNX...")
    onnx_path = model.export(format="onnx", imgsz=args.imgsz, opset=17, simplify=False)
    dest = ROOT / args.out
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(onnx_path, dest)
    print(f"  {dest}")
    print(f"\nUse it:\n  python scripts/run_gaze_object.py --camera 0 "
          f"--detector {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
