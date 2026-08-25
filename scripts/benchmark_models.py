#!/usr/bin/env python3
"""Benchmark every Gaze-LLE variant: latency AND localisation correctness.

Latency alone is misleading -- a fast model that points at the wrong place is
useless. So each variant is also scored on a real image whose gaze target is
known, and we report whether its heatmap peak still lands on that target.

    python scripts/benchmark_models.py
    python scripts/benchmark_models.py --runs 30
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import cv2
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from gaze_target import GazelleONNX, HeadDetector  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
MODELS = ROOT / "models"

# name -> (filename, params_millions, published GazeFollow AUC, published VAT in/out AP)
VARIANTS = [
    ("Atto  (CNN)", "gazelle_hgnetv2_atto_inout_distill_1x3x320x320_1xNx4.onnx", 2.93, 0.9267, 0.8749),
    ("Femto (CNN)", "gazelle_hgnetv2_femto_inout_distill_1x3x416x416_1xNx4.onnx", 3.15, 0.9391, 0.8779),
    ("Pico  (CNN)", "gazelle_hgnetv2_pico_inout_distill_1x3x640x640_1xNx4.onnx", 3.51, 0.9491, 0.8861),
    ("N     (CNN)", "gazelle_hgnetv2_n_inout_distill_1x3x640x640_1xNx4.onnx", 4.61, 0.9481, 0.9012),
    ("S     (ViT)", "gazelle_dinov3_vit_tiny_inout_1x3x640x640_1xNx4.onnx", 8.17, 0.9545, 0.8945),
    ("M     (ViT)", "gazelle_dinov3_vit_tinyplus_inout_1x3x640x640_1xNx4.onnx", 12.37, 0.9564, 0.8953),
    ("L     (ViT)", "gazelle_dinov3_vits16_inout_1x3x640x640_1xNx4.onnx", 24.33, 0.9593, 0.9011),
    ("X     (ViT)", "gazelle_dinov3_vits16plus_inout_1x3x640x640_1xNx4.onnx", 31.43, 0.9604, 0.9118),
]

# Ground truth on testdata/phone_woman.jpg at 640x480: the phone in her raised
# hand. Region established from the high-capacity models' agreement.
TRUTH_BOX = (70, 150, 210, 270)


def bench(fn, runs: int, warmup: int = 3) -> tuple[float, float]:
    for _ in range(warmup):
        fn()
    samples = []
    for _ in range(runs):
        t0 = time.perf_counter()
        fn()
        samples.append((time.perf_counter() - t0) * 1000.0)
    return float(np.mean(samples)), float(np.percentile(samples, 95))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=15)
    ap.add_argument("--image", default=str(ROOT / "testdata" / "phone_woman.jpg"))
    args = ap.parse_args()

    frame = cv2.imread(args.image)
    if frame is None:
        print(f"[ERROR] cannot read {args.image} "
              f"-- run: python scripts/fetch_testdata.py")
        return 1
    frame = cv2.resize(frame, (640, 480))

    det = HeadDetector(MODELS / "deimv2_head.onnx")
    d_mean, d_p95 = bench(lambda: det(frame), args.runs)
    head = det.primary_head(frame)
    if head is None:
        print("[ERROR] no head detected in benchmark image")
        return 1

    print(f"CPU-only benchmark, {frame.shape[1]}x{frame.shape[0]} frame, "
          f"{args.runs} runs each\n")
    print(f"head detector (DEIMv2 pico, 6 MB): {d_mean:.1f} ms "
          f"(p95 {d_p95:.1f})  -- runs once per N frames\n")

    hdr = (f"{'variant':<12} {'params':>7} {'size':>7} {'input':>6} "
           f"{'ms':>7} {'p95':>7} {'gaze FPS':>9} {'+det FPS':>9} "
           f"{'AUC':>7} {'inout':>7}  peak_ok")
    print(hdr)
    print("-" * len(hdr))

    rows = []
    for name, fname, params, auc, ap_io in VARIANTS:
        path = MODELS / fname
        if not path.is_file():
            print(f"{name:<12} [missing -- run scripts/download_models.sh]")
            continue

        g = GazelleONNX(path)
        mean, p95 = bench(lambda: g(frame, [head.box]), args.runs)
        r = g(frame, [head.box])[0]
        px, py = r.peak_xy
        ok = (TRUTH_BOX[0] <= px < TRUTH_BOX[2] and TRUTH_BOX[1] <= py < TRUTH_BOX[3])

        # Combined throughput assumes head detection every 5th frame.
        combined = 1000.0 / (mean + d_mean / 5.0)
        size_mb = path.stat().st_size / 1e6

        print(f"{name:<12} {params:>6.2f}M {size_mb:>6.0f}M {g.in_w:>6} "
              f"{mean:>7.1f} {p95:>7.1f} {1000 / mean:>9.1f} {combined:>9.1f} "
              f"{auc:>7.4f} {r.inout:>7.3f}  {'yes' if ok else 'NO  ' + str(r.peak_xy)}")
        rows.append((name, mean, combined, ok, r.inout))

    print()
    usable = [r for r in rows if r[3] and r[2] >= 5.0]
    if usable:
        best = max(usable, key=lambda r: r[2])
        print(f"Best CPU choice (correct peak, >=5 FPS combined): "
              f"{best[0].strip()} at {best[2]:.1f} FPS")
    wrong = [r[0].strip() for r in rows if not r[3]]
    if wrong:
        print(f"Localisation FAILED on this image: {', '.join(wrong)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
