#!/usr/bin/env python3
"""Physical layout planner: how big must each object be, and how far apart?

Answers a question that must be settled BEFORE recording a dataset, because it
cannot be fixed afterwards by a better model. Two hard constraints combine:

  1. The gaze heatmap is 64x64 regardless of input size, so a target smaller
     than ~2.5 cells per side cannot be reliably localised.
  2. Two targets closer than ~3 cells apart fall inside the heatmap's own blur
     and cannot be separated.

Both constraints are in *pixels*, so the physical answer depends on camera
distance, field of view and frame resolution.

    python scripts/plan_layout.py
    python scripts/plan_layout.py --distance 0.8 --fov 60 --width 640
    python scripts/plan_layout.py --objects "medicine strip:8x3" "water bottle:7x22"
"""

from __future__ import annotations

import argparse
import math

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from gaze_target.targets import (  # noqa: E402
    HEATMAP_SIDE,
    MIN_CELLS_PER_SIDE,
    MIN_RELIABLE_CELLS,
)

# label -> (width_cm, height_cm) as the object appears facing the camera.
# Sizes are typical real-world dimensions of the project's vision targets.
DEFAULT_OBJECTS: dict[str, tuple[float, float]] = {
    "WATER (bottle)": (7.0, 22.0),
    "MEDICINE (blister strip)": (8.0, 3.0),
    "FOOD (bowl)": (15.0, 8.0),
    "PHONE": (7.0, 15.0),
    "CALLING_BELL": (7.0, 7.0),
    "TISSUE (box)": (22.0, 11.0),
}


def parse_objects(specs: list[str]) -> dict[str, tuple[float, float]]:
    out: dict[str, tuple[float, float]] = {}
    for spec in specs:
        try:
            name, dims = spec.rsplit(":", 1)
            w, h = dims.lower().split("x")
            out[name] = (float(w), float(h))
        except ValueError:
            raise SystemExit(f"bad --objects spec: {spec!r}  (use 'name:WxH' in cm)")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--distance", type=float, default=1.0,
                    help="camera-to-object distance in metres")
    ap.add_argument("--fov", type=float, default=60.0,
                    help="camera horizontal field of view in degrees")
    ap.add_argument("--width", type=int, default=640, help="frame width in px")
    ap.add_argument("--height", type=int, default=480, help="frame height in px")
    ap.add_argument("--objects", nargs="+", default=None, help="name:WxH in cm")
    args = ap.parse_args()

    objects = parse_objects(args.objects) if args.objects else DEFAULT_OBJECTS

    # Horizontal extent of the scene visible at this distance.
    scene_w_cm = 2.0 * args.distance * math.tan(math.radians(args.fov) / 2.0) * 100.0
    px_per_cm = args.width / scene_w_cm
    cell_w_px = args.width / HEATMAP_SIDE
    cell_h_px = args.height / HEATMAP_SIDE

    min_w_px = MIN_CELLS_PER_SIDE * cell_w_px
    min_h_px = MIN_CELLS_PER_SIDE * cell_h_px
    min_w_cm = min_w_px / px_per_cm
    min_h_cm = min_h_px / px_per_cm
    sep_px = 3.0 * cell_w_px
    sep_cm = sep_px / px_per_cm

    print(f"camera {args.distance:.2f} m away, {args.fov:.0f} deg FOV, "
          f"{args.width}x{args.height} frame")
    print(f"  visible scene width : {scene_w_cm:.0f} cm")
    print(f"  scale               : {px_per_cm:.2f} px/cm")
    print(f"  heatmap cell        : {cell_w_px:.1f} x {cell_h_px:.1f} px "
          f"= {cell_w_px / px_per_cm:.1f} x {cell_h_px / px_per_cm:.1f} cm")
    print()
    print(f"  MINIMUM object size : {min_w_px:.0f} x {min_h_px:.0f} px "
          f"= {min_w_cm:.1f} x {min_h_cm:.1f} cm")
    print(f"  MINIMUM separation  : {sep_px:.0f} px = {sep_cm:.1f} cm "
          f"(centre to centre)")
    print()

    hdr = f"{'target':<26} {'real cm':>10} {'px in frame':>13} {'cells':>12}  verdict"
    print(hdr)
    print("-" * len(hdr))

    failures = []
    for name, (w_cm, h_cm) in objects.items():
        w_px = w_cm * px_per_cm
        h_px = h_cm * px_per_cm
        cx = w_px / cell_w_px
        cy = h_px / cell_h_px
        area_ok = (cx * cy) >= MIN_RELIABLE_CELLS
        sides_ok = cx >= MIN_CELLS_PER_SIDE and cy >= MIN_CELLS_PER_SIDE
        ok = area_ok and sides_ok
        if not ok:
            failures.append(name)
        verdict = "ok" if ok else ("TOO SMALL" if not area_ok else "TOO THIN")
        print(f"{name:<26} {f'{w_cm:.0f}x{h_cm:.0f}':>10} "
              f"{f'{w_px:.0f}x{h_px:.0f}':>13} {f'{cx:.1f}x{cy:.1f}':>12}  {verdict}")

    print()
    if failures:
        print(f"{len(failures)} target(s) will NOT work at this distance: "
              f"{', '.join(failures)}")
        # Solve for the distance at which every object clears both constraints.
        needed = args.distance
        for _ in range(400):
            s_w = 2.0 * needed * math.tan(math.radians(args.fov) / 2.0) * 100.0
            ppc = args.width / s_w
            if all(
                (w * ppc) >= MIN_CELLS_PER_SIDE * cell_w_px
                and (h * ppc) >= MIN_CELLS_PER_SIDE * cell_h_px
                and ((w * ppc) / cell_w_px) * ((h * ppc) / cell_h_px) >= MIN_RELIABLE_CELLS
                for w, h in objects.values()
            ):
                break
            needed -= 0.005
        if needed > 0.05:
            print(f"Fixes, any one of:")
            print(f"  - move the camera to <= {needed:.2f} m")
            factor = args.distance / max(needed, 1e-6)
            print(f"  - raise frame width to ~{int(args.width * factor)} px "
                  f"(keeps camera at {args.distance:.2f} m)")
            print(f"  - enlarge the failing target(s), e.g. mount a blister strip "
                  f"on a card of at least {min_w_cm:.0f} x {min_h_cm:.0f} cm")
        else:
            print("  no practical distance works -- enlarge the targets or use "
                  "printed cards")
    else:
        print("All targets clear both constraints at this distance.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
