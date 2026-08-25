#!/usr/bin/env python3
"""Capture frames from the camera to build a custom detection dataset.

Aim for variety, not volume. With a fixed object set in a fixed scene, ~40-80
images per object is plenty for fine-tuning -- but they must vary in object
position, lighting, occlusion and camera angle, or the detector will overfit to
one arrangement and fail the moment anything moves.

    python scripts/capture_dataset.py --out data/raw --interval 1.5
    python scripts/capture_dataset.py --out data/raw --manual

Keys: SPACE capture (manual mode), q quit
"""

from __future__ import annotations

import argparse
import time
from datetime import datetime
from pathlib import Path

import cv2

PROMPTS = [
    "Move the objects to new positions",
    "Change the lighting (curtain, lamp, overhead)",
    "Partially occlude one object",
    "Shift the camera angle slightly",
    "Sit/lie in a different posture",
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--camera", default=0)
    ap.add_argument("--out", default="data/raw")
    ap.add_argument("--width", type=int, default=1280,
                    help="capture wide: small targets need resolution (see plan_layout.py)")
    ap.add_argument("--height", type=int, default=720)
    ap.add_argument("--interval", type=float, default=2.0,
                    help="seconds between automatic captures")
    ap.add_argument("--manual", action="store_true", help="only capture on SPACE")
    ap.add_argument("--limit", type=int, default=0, help="stop after N images")
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    session = datetime.now().strftime("%Y%m%d_%H%M%S")

    cap = cv2.VideoCapture(int(args.camera))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)
    if not cap.isOpened():
        print(f"[ERROR] cannot open camera {args.camera}")
        return 1

    actual_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    actual_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"capturing {actual_w}x{actual_h} -> {out_dir}")
    if actual_w < 1280:
        print("  NOTE: camera gave less than 1280 wide. Small targets such as a"
              " medicine strip may be unresolvable -- check scripts/plan_layout.py")
    print("  SPACE = capture, q = quit\n")

    saved = 0
    last = 0.0
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            prompt = PROMPTS[(saved // 10) % len(PROMPTS)]
            hud = frame.copy()
            cv2.rectangle(hud, (0, 0), (hud.shape[1], 62), (0, 0, 0), -1)
            cv2.putText(hud, f"saved: {saved}", (12, 26),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.putText(hud, f"vary: {prompt}", (12, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 220, 255), 1, cv2.LINE_AA)
            cv2.imshow("capture dataset", hud)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

            now = time.time()
            due = (not args.manual and now - last >= args.interval) or key == ord(" ")
            if due:
                path = out_dir / f"{session}_{saved:04d}.jpg"
                cv2.imwrite(str(path), frame)
                saved += 1
                last = now
                print(f"  {path.name}")
                if args.limit and saved >= args.limit:
                    break
    finally:
        cap.release()
        cv2.destroyAllWindows()

    print(f"\n{saved} images -> {out_dir}")
    print(f"next: python scripts/autolabel.py --images {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
