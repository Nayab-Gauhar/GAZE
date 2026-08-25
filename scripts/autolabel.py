#!/usr/bin/env python3
"""Pre-label a dataset with OWLv2, in YOLO format, for you to correct.

Annotating from scratch is the slow part of custom detection. OWLv2 already
knows roughly what a water bottle looks like, so it can propose most boxes and
leave you correcting rather than drawing. In practice that is several times
faster, and the classes it is weakest on (MEDICINE, CALLING_BELL) are exactly
the ones worth your manual attention.

    python scripts/autolabel.py --images data/raw --out data/yolo
    python scripts/autolabel.py --images data/raw --out data/yolo --preview
    python scripts/autolabel.py --images data/raw --out data/yolo --threshold 0.08

Output is a standard YOLO detection dataset:

    data/yolo/
      data.yaml
      images/train/*.jpg   labels/train/*.txt
      images/val/*.jpg     labels/val/*.txt
      preview/*.jpg                  (optional, for eyeballing quality)

**Then correct the labels before training.** These are proposals, not ground
truth. Use labelImg, CVAT or Roboflow; all read this layout directly.
"""

from __future__ import annotations

import argparse
import random
import shutil
import sys
from collections import Counter
from pathlib import Path

import cv2

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from gaze_target.object_detector import OpenVocabDetector  # noqa: E402
from gaze_target.registry import (  # noqa: E402
    APPLIANCE_TARGETS,
    BODY_TARGETS,
    PROJECT_TARGETS,
)

ROOT = Path(__file__).resolve().parent.parent
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".bmp"}


def build_vocab(include_appliances: bool, include_body: bool) -> dict[str, list[str]]:
    vocab = dict(PROJECT_TARGETS)
    if include_appliances:
        vocab.update(APPLIANCE_TARGETS)
    if include_body:
        vocab.update(BODY_TARGETS)
    return vocab


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--images", required=True, help="folder of captured images")
    ap.add_argument("--out", default="data/yolo")
    ap.add_argument("--threshold", type=float, default=0.10,
                    help="low on purpose: a spurious box is faster to delete "
                         "than a missing one is to draw")
    ap.add_argument("--val-split", type=float, default=0.2)
    ap.add_argument("--preview", action="store_true")
    ap.add_argument("--appliances", action="store_true", help="also FAN, TV")
    ap.add_argument("--body", action="store_true",
                    help="also body parts, for pain localisation")
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()

    img_dir = Path(args.images)
    images = sorted(p for p in img_dir.iterdir() if p.suffix.lower() in IMAGE_EXT)
    if not images:
        print(f"[ERROR] no images in {img_dir}")
        return 1

    vocab = build_vocab(args.appliances, args.body)
    class_names = list(vocab)
    class_id = {name: i for i, name in enumerate(class_names)}
    prompt_to_label = {p: label for label, ps in vocab.items() for p in ps}
    prompts = list(prompt_to_label)

    print(f"{len(images)} images, {len(class_names)} classes: {', '.join(class_names)}")
    print(f"{len(prompts)} detection prompts\n")

    out = Path(args.out)
    for split in ("train", "val"):
        (out / "images" / split).mkdir(parents=True, exist_ok=True)
        (out / "labels" / split).mkdir(parents=True, exist_ok=True)
    if args.preview:
        (out / "preview").mkdir(parents=True, exist_ok=True)

    rng = random.Random(args.seed)
    shuffled = list(images)
    rng.shuffle(shuffled)
    n_val = max(1, int(len(shuffled) * args.val_split)) if len(shuffled) > 1 else 0
    val_set = set(shuffled[:n_val])

    detector = OpenVocabDetector(ROOT / "models" / "owlv2")
    counts: Counter[str] = Counter()
    empty: list[str] = []

    for i, path in enumerate(images, 1):
        frame = cv2.imread(str(path))
        if frame is None:
            print(f"  [skip] unreadable: {path.name}")
            continue
        h, w = frame.shape[:2]
        split = "val" if path in val_set else "train"

        dets = detector.detect(frame, prompts, score_threshold=args.threshold)

        # Keep the single best detection per canonical label: the project's
        # targets are one-of-each in a fixed scene, so duplicates are errors.
        best: dict[str, tuple] = {}
        for d in dets:
            label = prompt_to_label.get(d.label)
            if label is None:
                continue
            if label not in best or d.score > best[label][1]:
                best[label] = (d.box, d.score)

        lines = []
        for label, (box, score) in best.items():
            x1, y1, x2, y2 = box
            cx = ((x1 + x2) / 2) / w
            cy = ((y1 + y2) / 2) / h
            bw = (x2 - x1) / w
            bh = (y2 - y1) / h
            if bw <= 0 or bh <= 0:
                continue
            lines.append(f"{class_id[label]} {cx:.6f} {cy:.6f} {bw:.6f} {bh:.6f}")
            counts[label] += 1

        shutil.copy2(path, out / "images" / split / path.name)
        (out / "labels" / split / f"{path.stem}.txt").write_text("\n".join(lines) + "\n"
                                                                if lines else "")
        if not lines:
            empty.append(path.name)

        if args.preview:
            vis = frame.copy()
            for label, (box, score) in best.items():
                x1, y1, x2, y2 = box
                cv2.rectangle(vis, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(vis, f"{label} {score:.2f}", (x1, max(14, y1 - 6)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.imwrite(str(out / "preview" / path.name), vis)

        print(f"  [{i}/{len(images)}] {path.name} ({split}): "
              f"{len(lines)} boxes -> {', '.join(best) or 'NONE'}")

    yaml = (
        f"# Auto-generated by scripts/autolabel.py -- CORRECT THE LABELS BEFORE TRAINING\n"
        f"path: {out.resolve()}\n"
        f"train: images/train\n"
        f"val: images/val\n"
        f"nc: {len(class_names)}\n"
        f"names:\n" + "".join(f"  {i}: {n}\n" for i, n in enumerate(class_names))
    )
    (out / "data.yaml").write_text(yaml)

    print(f"\ndataset -> {out}")
    print(f"  train: {len(images) - n_val}   val: {n_val}")
    print(f"\n{'class':<16} {'proposals':>10}  coverage")
    for name in class_names:
        c = counts[name]
        pct = 100.0 * c / max(1, len(images))
        flag = "" if c >= max(10, 0.3 * len(images)) else "   <-- WEAK, label these by hand"
        print(f"{name:<16} {c:>10}  {pct:5.1f}%{flag}")

    if empty:
        print(f"\n{len(empty)} image(s) got NO proposals: "
              f"{', '.join(empty[:6])}{' ...' if len(empty) > 6 else ''}")

    print("\nNEXT STEPS")
    print("  1. Correct the labels -- these are proposals, not ground truth.")
    print(f"       labelImg {out / 'images' / 'train'} "
          f"(classes from {out / 'data.yaml'})")
    print("     Pay most attention to any class flagged WEAK above.")
    print(f"  2. Train:  python scripts/train_detector.py --data {out / 'data.yaml'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
