#!/usr/bin/env python3
"""Sanity-check head detection + gaze heatmap on still images.

No targets required: this answers the prior question "does the gaze model
actually point at the right thing on real photographs?" before any target
scoring is layered on top.

Usage:
    python scripts/verify_gaze.py testdata/*.jpg --out out/
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import cv2
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from gaze_target import GazelleONNX, HeadDetector  # noqa: E402

MODELS = Path(__file__).resolve().parent.parent / "models"
DEFAULT_GAZE = MODELS / "gazelle_dinov3_vits16plus_inout_1x3x640x640_1xNx4.onnx"
DEFAULT_DET = MODELS / "deimv2_head.onnx"


def annotate(frame: np.ndarray, head_box, peak_xy, inout: float, heatmap) -> np.ndarray:
    out = frame.copy()

    hm8 = np.clip(heatmap * 255.0, 0, 255).astype(np.uint8)
    out = cv2.addWeighted(out, 1.0, cv2.applyColorMap(hm8, cv2.COLORMAP_JET), 0.45, 0.0)

    x1, y1, x2, y2 = head_box
    cv2.rectangle(out, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(out, "head", (x1, max(0, y1 - 6)), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                (0, 255, 0), 1, cv2.LINE_AA)

    px, py = peak_xy
    hx, hy = (x1 + x2) // 2, (y1 + y2) // 2
    cv2.arrowedLine(out, (hx, hy), (px, py), (255, 255, 255), 2, tipLength=0.05)
    cv2.circle(out, (px, py), 11, (255, 255, 255), 2)
    cv2.circle(out, (px, py), 3, (0, 0, 255), -1)

    cv2.putText(out, f"in-frame score: {inout:.3f}", (10, 24),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("images", nargs="+")
    ap.add_argument("--gaze-model", default=str(DEFAULT_GAZE))
    ap.add_argument("--det-model", default=str(DEFAULT_DET))
    ap.add_argument("--out", default="out")
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    det = HeadDetector(args.det_model)
    gaze = GazelleONNX(args.gaze_model)
    print(f"gaze model input: {gaze.in_w}x{gaze.in_h}\n")

    failures = 0
    for path_str in args.images:
        path = Path(path_str)
        frame = cv2.imread(str(path))
        if frame is None:
            print(f"[SKIP] unreadable: {path}")
            failures += 1
            continue

        h, w = frame.shape[:2]
        heads = det(frame)
        print(f"=== {path.name}  ({w}x{h})")
        print(f"    heads detected: {len(heads)}")
        if not heads:
            print("    [FAIL] no head detected\n")
            failures += 1
            continue

        primary = max(heads, key=lambda d: d.area)
        print(f"    primary head: box={primary.box} score={primary.score:.3f}")

        results = gaze(frame, [primary.box])
        if not results:
            print("    [FAIL] gaze model returned nothing\n")
            failures += 1
            continue

        r = results[0]
        px, py = r.peak_xy
        print(f"    in-frame score: {r.inout:.3f}")
        print(f"    heatmap peak:   ({px}, {py})  "
              f"= ({px / w:.2f}, {py / h:.2f}) normalized")
        print(f"    heatmap max:    {r.heatmap.max():.3f}   sum: {r.heatmap.sum():.1f}")

        dest = out_dir / f"{path.stem}_gaze.jpg"
        cv2.imwrite(str(dest), annotate(frame, primary.box, r.peak_xy, r.inout, r.heatmap))
        print(f"    wrote {dest}\n")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
