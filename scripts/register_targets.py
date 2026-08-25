#!/usr/bin/env python3
"""Register the target layout by clicking boxes on a live camera frame.

This is the only setup step Option 3 requires. It is a *site* calibration, not a
patient calibration: it records where the communication targets sit in the camera
view, and is reused unchanged for every patient in that bed.

Controls
    click-drag   draw a box around one target
    n            accept the box and move to the next label
    r            redraw the current box
    b            go back one label
    s            save and exit
    q            quit without saving

Usage
    python scripts/register_targets.py --camera 0 --out config/targets.json
    python scripts/register_targets.py --image frame.jpg --out config/targets.json
    python scripts/register_targets.py --labels WATER TOILET PAIN HELP
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import cv2
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from gaze_target import Target, TargetSet  # noqa: E402

# Clinically prioritised default set (see research report section 12.3):
# TOILET is included because it is among the most frequent and dignity-critical
# needs of a bed-bound patient, and PAIN replaces MEDICINE because medication is
# staff-scheduled and a false MEDICINE is the highest-risk misfire.
DEFAULT_LABELS = ["WATER", "TOILET", "PAIN", "HELP"]


class BoxDrawer:
    def __init__(self) -> None:
        self.start: tuple[int, int] | None = None
        self.current: tuple[int, int, int, int] | None = None
        self.dragging = False

    def on_mouse(self, event: int, x: int, y: int, flags: int, param) -> None:
        if event == cv2.EVENT_LBUTTONDOWN:
            self.start = (x, y)
            self.dragging = True
            self.current = None
        elif event == cv2.EVENT_MOUSEMOVE and self.dragging and self.start:
            self.current = (*self.start, x, y)
        elif event == cv2.EVENT_LBUTTONUP and self.start:
            self.dragging = False
            self.current = (*self.start, x, y)

    def normalized(self) -> tuple[int, int, int, int] | None:
        if not self.current:
            return None
        x1, y1, x2, y2 = self.current
        box = (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
        if box[2] - box[0] < 8 or box[3] - box[1] < 8:
            return None
        return box

    def clear(self) -> None:
        self.start = None
        self.current = None
        self.dragging = False


def grab_frame(args) -> np.ndarray | None:
    if args.image:
        return cv2.imread(args.image)
    cap = cv2.VideoCapture(int(args.camera))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)
    if not cap.isOpened():
        print(f"[ERROR] cannot open camera {args.camera}")
        return None
    print("Press SPACE to freeze the frame you want to register on, q to quit.")
    frame = None
    while True:
        ok, live = cap.read()
        if not ok:
            break
        preview = live.copy()
        cv2.putText(preview, "SPACE = freeze frame, q = quit", (10, 26),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow("register targets", preview)
        key = cv2.waitKey(1) & 0xFF
        if key == ord(" "):
            frame = live.copy()
            break
        if key == ord("q"):
            break
    cap.release()
    return frame


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--camera", default=0)
    ap.add_argument("--image", default=None, help="register on a still image instead")
    ap.add_argument("--width", type=int, default=640)
    ap.add_argument("--height", type=int, default=480)
    ap.add_argument("--labels", nargs="+", default=DEFAULT_LABELS)
    ap.add_argument("--out", default="config/targets.json")
    args = ap.parse_args()

    frame = grab_frame(args)
    if frame is None:
        print("[ERROR] no frame captured")
        return 1

    h, w = frame.shape[:2]
    drawer = BoxDrawer()
    cv2.namedWindow("register targets")
    cv2.setMouseCallback("register targets", drawer.on_mouse)

    boxes: dict[str, tuple[int, int, int, int]] = {}
    idx = 0

    while True:
        canvas = frame.copy()

        for label, (x1, y1, x2, y2) in boxes.items():
            cv2.rectangle(canvas, (x1, y1), (x2, y2), (0, 200, 0), 2)
            cv2.putText(canvas, label, (x1, max(14, y1 - 6)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 200, 0), 2, cv2.LINE_AA)

        pending = drawer.normalized()
        if pending:
            x1, y1, x2, y2 = pending
            cv2.rectangle(canvas, (x1, y1), (x2, y2), (0, 255, 255), 2)

        if idx < len(args.labels):
            prompt = f"Draw box for: {args.labels[idx]}  ({idx + 1}/{len(args.labels)})"
        else:
            prompt = "All labels done -- press 's' to save"
        cv2.rectangle(canvas, (0, 0), (w, 56), (0, 0, 0), -1)
        cv2.putText(canvas, prompt, (10, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(canvas, "n=next  r=redraw  b=back  s=save  q=quit", (10, 45),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (180, 180, 180), 1, cv2.LINE_AA)

        cv2.imshow("register targets", canvas)
        key = cv2.waitKey(20) & 0xFF

        if key == ord("q"):
            print("aborted, nothing saved")
            return 1
        if key == ord("r"):
            drawer.clear()
        elif key == ord("b") and idx > 0:
            idx -= 1
            boxes.pop(args.labels[idx], None)
            drawer.clear()
        elif key == ord("n") and idx < len(args.labels):
            box = drawer.normalized()
            if box is None:
                print("  draw a box first (drag with the left mouse button)")
            else:
                boxes[args.labels[idx]] = box
                print(f"  {args.labels[idx]}: {box}")
                idx += 1
                drawer.clear()
        elif key == ord("s"):
            if len(boxes) < 2:
                print("  need at least 2 targets before saving")
                continue
            break

    cv2.destroyAllWindows()

    target_set = TargetSet(
        targets=[Target(label=k, box=v) for k, v in boxes.items()],
        frame_size=(w, h),
    )

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    target_set.to_json(out_path)
    print(f"\nsaved {len(boxes)} targets -> {out_path}")

    # The feasibility gate is the whole point of running this before collecting
    # any data: an unresolvable layout cannot be fixed by a better model.
    rep = target_set.resolution_report(w, h)
    print("\n--- layout feasibility ---")
    print(f"one heatmap cell = {rep['heatmap_cell_px'][0]}x{rep['heatmap_cell_px'][1]} px")
    for t in rep["targets"]:
        print(f"  {t['label']:<10} {t['cells_total']:>7} cells  "
              f"{'ok' if t['reliable'] else 'TOO SMALL'}")
    print("  closest pairs:")
    for p in rep["pairs"][:3]:
        print(f"    {p['pair']:<26} {p['dist_cells']:>6} cells  "
              f"{'ok' if p['separable'] else 'TOO CLOSE'}")
    if rep["warnings"]:
        print("\n  WARNINGS:")
        for warn in rep["warnings"]:
            print(f"    - {warn}")
    else:
        print("\n  layout OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
