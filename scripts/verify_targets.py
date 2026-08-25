#!/usr/bin/env python3
"""End-to-end verification of target scoring, layout feasibility and dwell logic.

Uses a real photograph with a known ground-truth gaze target (a woman looking at
the phone in her raised hand) and registers that target plus three spatial decoys
laid out like a bedside communication board. The correct target must win.

Then drives the temporal filter to confirm that a selection actually fires, and
that belief collapses back to NONE once the subject leaves frame.
"""

from __future__ import annotations

import sys
from pathlib import Path

import cv2
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from gaze_target import (  # noqa: E402
    GazeTargetPipeline,
    NONE_LABEL,
    Target,
    TargetSet,
    TemporalConfig,
)

ROOT = Path(__file__).resolve().parent.parent
MODELS = ROOT / "models"
FRAME_W, FRAME_H = 640, 480

# Ground truth: the subject is looking at the phone in her raised hand.
# Boxes are given in normalized coords then scaled, so the layout is readable.
GROUND_TRUTH = "PHONE"
LAYOUT_NORM = {
    "PHONE": (0.12, 0.34, 0.28, 0.52),   # her hand holding the phone
    "WINDOW": (0.03, 0.02, 0.20, 0.18),  # decoy: upper left
    "WATER": (0.05, 0.65, 0.22, 0.82),   # decoy: lower left
    "BELL": (0.70, 0.70, 0.90, 0.88),    # decoy: lower right
}


def build_target_set() -> TargetSet:
    targets = [
        Target(
            label=label,
            box=(
                int(x1 * FRAME_W),
                int(y1 * FRAME_H),
                int(x2 * FRAME_W),
                int(y2 * FRAME_H),
            ),
        )
        for label, (x1, y1, x2, y2) in LAYOUT_NORM.items()
    ]
    return TargetSet(targets=targets, frame_size=(FRAME_W, FRAME_H))


def main() -> int:
    frame = cv2.imread(str(ROOT / "testdata" / "phone_woman.jpg"))
    if frame is None:
        print("[FAIL] test image missing")
        return 1
    frame = cv2.resize(frame, (FRAME_W, FRAME_H))

    target_set = build_target_set()
    failures: list[str] = []

    # ---------------------------------------------------------- layout feasibility
    print("=" * 68)
    print("LAYOUT FEASIBILITY (64x64 heatmap resolution gate)")
    print("=" * 68)
    rep = target_set.resolution_report(FRAME_W, FRAME_H)
    print(f"frame {rep['frame_size'][0]}x{rep['frame_size'][1]}, "
          f"one heatmap cell = {rep['heatmap_cell_px'][0]}x{rep['heatmap_cell_px'][1]} px\n")
    print(f"{'target':<10} {'box':<26} {'cells':>8}  reliable")
    for t in rep["targets"]:
        print(f"{t['label']:<10} {str(t['box_px']):<26} {t['cells_total']:>8}  "
              f"{'yes' if t['reliable'] else 'NO'}")
    print(f"\n{'pair':<26} {'px':>8} {'cells':>8}  separable")
    for p in rep["pairs"]:
        print(f"{p['pair']:<26} {p['dist_px']:>8} {p['dist_cells']:>8}  "
              f"{'yes' if p['separable'] else 'NO'}")
    if rep["warnings"]:
        print("\nwarnings:")
        for w in rep["warnings"]:
            print(f"  - {w}")
    else:
        print("\nlayout_ok: no warnings")

    # ---------------------------------------------------------------- scoring
    print("\n" + "=" * 68)
    print("SINGLE-FRAME SCORING")
    print("=" * 68)
    pipe = GazeTargetPipeline(
        target_set=target_set,
        gazelle_model=MODELS / "gazelle_hgnetv2_pico_inout_distill_1x3x640x640_1xNx4.onnx",
        detector_model=MODELS / "deimv2_head.onnx",
        temporal_config=TemporalConfig(dwell_frames=10, refractory_frames=5),
    )

    res = pipe.process(frame, use_temporal=False)
    if res.head is None or res.gaze is None:
        print("[FAIL] no head/gaze on test frame")
        return 1

    print(f"head box       : {res.head.box}  (score {res.head.score:.3f})")
    print(f"in-frame score : {res.gaze.inout:.3f}")
    print(f"heatmap peak   : {res.gaze.peak_xy}\n")
    print(f"{'target':<10} {'P':>7} {'mass':>7}  peak_inside")
    for d in res.detail:
        print(f"{d.label:<10} {d.probability:>7.3f} {d.mass:>7.3f}  "
              f"{'yes' if d.peak_inside else 'no'}")
    print(f"{NONE_LABEL:<10} {res.posterior[NONE_LABEL]:>7.3f}")

    top = max(res.posterior.items(), key=lambda kv: kv[1])
    print(f"\nargmax: {top[0]} ({top[1]:.3f})   ground truth: {GROUND_TRUTH}")
    if top[0] != GROUND_TRUTH:
        failures.append(f"single-frame argmax was {top[0]}, expected {GROUND_TRUTH}")
    else:
        print("PASS: correct target identified")

    # -------------------------------------------------------------- temporal
    print("\n" + "=" * 68)
    print("TEMPORAL FILTER / DWELL")
    print("=" * 68)
    pipe.reset()
    emit_frame = None
    print(f"{'frame':>5} {'top':<10} {'P':>7} {'margin':>7} {'dwell':>6}  emitted")
    for i in range(1, 16):
        r = pipe.process(frame)
        d = r.decision
        assert d is not None
        print(f"{i:>5} {d.top_label:<10} {d.top_prob:>7.3f} {d.margin:>7.3f} "
              f"{d.dwell_count:>6}  {d.emitted or ''}")
        if d.emitted and emit_frame is None:
            emit_frame = i
            if d.emitted != GROUND_TRUTH:
                failures.append(f"emitted {d.emitted}, expected {GROUND_TRUTH}")

    if emit_frame is None:
        failures.append("never emitted a selection across 15 frames")
    else:
        print(f"\nPASS: emitted '{GROUND_TRUTH}' at frame {emit_frame}")

    # Subject leaves frame -> belief must collapse to NONE.
    print("\nsubject leaves frame (blank frames):")
    blank = np.full((FRAME_H, FRAME_W, 3), 128, dtype=np.uint8)
    for i in range(1, 9):
        r = pipe.process(blank)
        d = r.decision
        assert d is not None
        if i % 2 == 0:
            print(f"  frame {i}: top={d.top_label} P={d.top_prob:.3f} "
                  f"P(NONE)={d.belief[NONE_LABEL]:.3f}")
    if d.top_label != NONE_LABEL:
        failures.append(f"after subject left, top was {d.top_label}, expected {NONE_LABEL}")
    else:
        print("PASS: belief collapsed to NONE")

    print("\n" + "=" * 68)
    if failures:
        print("FAILURES:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
