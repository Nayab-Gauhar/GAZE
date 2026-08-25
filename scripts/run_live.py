#!/usr/bin/env python3
"""Run the Option 3 pipeline live on a webcam or a video file.

Usage
    python scripts/run_live.py --targets config/targets.json --camera 0
    python scripts/run_live.py --targets config/targets.json --video clip.mp4
    python scripts/run_live.py --targets config/targets.json --video clip.mp4 \
        --headless --log events.csv

Keys (windowed mode)
    q   quit
    r   reset the temporal filter
    h   toggle heatmap overlay
"""

from __future__ import annotations

import argparse
import csv
import sys
import time
from collections import deque
from pathlib import Path

import cv2
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from gaze_target import (  # noqa: E402
    GazeTargetPipeline,
    NONE_LABEL,
    TargetSet,
    TemporalConfig,
)

ROOT = Path(__file__).resolve().parent.parent
MODELS = ROOT / "models"
PICO = MODELS / "gazelle_hgnetv2_pico_inout_distill_1x3x640x640_1xNx4.onnx"
BIG = MODELS / "gazelle_dinov3_vits16plus_inout_1x3x640x640_1xNx4.onnx"

BAR_W = 190


def draw_overlay(frame, result, target_set, fps, show_heatmap: bool):
    canvas = frame.copy()

    if show_heatmap and result.gaze is not None:
        hm = np.clip(result.gaze.heatmap * 255.0, 0, 255).astype(np.uint8)
        canvas = cv2.addWeighted(
            canvas, 1.0, cv2.applyColorMap(hm, cv2.COLORMAP_JET), 0.40, 0.0
        )

    decision = result.decision
    top_label = decision.top_label if decision else NONE_LABEL

    for t in target_set.targets:
        x1, y1, x2, y2 = t.box
        active = t.label == top_label
        colour = (0, 255, 0) if active else (140, 140, 140)
        cv2.rectangle(canvas, (x1, y1), (x2, y2), colour, 3 if active else 1)
        cv2.putText(canvas, t.label, (x1, max(14, y1 - 6)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, colour, 2, cv2.LINE_AA)

    if result.head is not None:
        x1, y1, x2, y2 = result.head.box
        cv2.rectangle(canvas, (x1, y1), (x2, y2), (255, 200, 0), 2)
        if result.gaze is not None:
            hx, hy = (x1 + x2) // 2, (y1 + y2) // 2
            cv2.arrowedLine(canvas, (hx, hy), result.gaze.peak_xy,
                            (255, 255, 255), 2, tipLength=0.04)
            cv2.circle(canvas, result.gaze.peak_xy, 9, (255, 255, 255), 2)

    h, w = canvas.shape[:2]
    panel = canvas[:, w - BAR_W:]
    canvas[:, w - BAR_W:] = cv2.addWeighted(
        panel, 0.25, np.zeros_like(panel), 0.75, 0
    )
    x0 = w - BAR_W + 8
    y = 22
    cv2.putText(canvas, f"{fps:.1f} FPS", (x0, y), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255, 255, 255), 1, cv2.LINE_AA)
    y += 20
    if result.gaze is not None:
        cv2.putText(canvas, f"in-frame {result.gaze.inout:.2f}", (x0, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (200, 200, 200), 1, cv2.LINE_AA)
    y += 24

    if decision:
        for label in [*target_set.labels, NONE_LABEL]:
            p = decision.belief.get(label, 0.0)
            colour = (0, 255, 0) if label == decision.top_label else (170, 170, 170)
            cv2.putText(canvas, f"{label[:9]:<9} {p:4.2f}", (x0, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.42, colour, 1, cv2.LINE_AA)
            bar = int(p * (BAR_W - 24))
            cv2.rectangle(canvas, (x0, y + 4), (x0 + bar, y + 8), colour, -1)
            y += 22

        y += 6
        cv2.putText(canvas, f"dwell {decision.dwell_count}", (x0, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.42, (200, 200, 200), 1, cv2.LINE_AA)
        if decision.refractory:
            y += 18
            cv2.putText(canvas, "refractory", (x0, y), cv2.FONT_HERSHEY_SIMPLEX,
                        0.42, (0, 180, 255), 1, cv2.LINE_AA)

    return canvas


def main() -> int:
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group()
    src.add_argument("--camera", default=None)
    src.add_argument("--video", default=None)
    ap.add_argument("--targets", required=True)
    ap.add_argument("--model", default="pico", choices=["pico", "big"])
    ap.add_argument("--width", type=int, default=640)
    ap.add_argument("--height", type=int, default=480)
    ap.add_argument("--detect-every-n", type=int, default=5,
                    help="head detection interval; 1 = every frame")
    ap.add_argument("--dwell-frames", type=int, default=8)
    ap.add_argument("--commit-threshold", type=float, default=0.65)
    ap.add_argument("--min-inout", type=float, default=0.20,
                    help="in-frame score floor. Measured to vary a lot across "
                         "domains, so keep this permissive and rely on target mass.")
    ap.add_argument("--headless", action="store_true")
    ap.add_argument("--log", default=None, help="write emitted selections to CSV")
    ap.add_argument("--max-frames", type=int, default=0)
    args = ap.parse_args()

    if args.camera is None and args.video is None:
        args.camera = 0

    target_set = TargetSet.from_json(args.targets)
    print(f"targets: {', '.join(target_set.labels)}")

    pipe = GazeTargetPipeline(
        target_set=target_set,
        gazelle_model=PICO if args.model == "pico" else BIG,
        detector_model=MODELS / "deimv2_head.onnx",
        temporal_config=TemporalConfig(
            dwell_frames=args.dwell_frames,
            commit_threshold=args.commit_threshold,
            min_inout=args.min_inout,
        ),
        detect_every_n=args.detect_every_n,
    )

    source = int(args.camera) if args.camera is not None else args.video
    cap = cv2.VideoCapture(source)
    if args.camera is not None:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)
    if not cap.isOpened():
        print(f"[ERROR] cannot open source: {source}")
        return 1

    log_rows: list[dict] = []
    times: deque[float] = deque(maxlen=30)
    show_heatmap = True
    frame_no = 0
    t_start = time.time()

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            frame_no += 1
            if args.camera is not None:
                frame = cv2.flip(frame, 1)  # mirror for natural self-view
            if frame.shape[1] != args.width or frame.shape[0] != args.height:
                frame = cv2.resize(frame, (args.width, args.height))

            t0 = time.perf_counter()
            result = pipe.process(frame)
            times.append(time.perf_counter() - t0)
            fps = 1.0 / max(1e-6, float(np.mean(times)))

            if result.emitted:
                stamp = time.time() - t_start
                print(f"[{stamp:7.2f}s] frame {frame_no:5d}  ==> {result.emitted}")
                log_rows.append(
                    {
                        "time_s": round(stamp, 3),
                        "frame": frame_no,
                        "emitted": result.emitted,
                        "inout": round(result.gaze.inout, 4) if result.gaze else "",
                    }
                )

            if not args.headless:
                cv2.imshow("gaze target", draw_overlay(
                    frame, result, target_set, fps, show_heatmap))
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q"):
                    break
                if key == ord("r"):
                    pipe.reset()
                    print("filter reset")
                if key == ord("h"):
                    show_heatmap = not show_heatmap
            elif frame_no % 30 == 0:
                d = result.decision
                print(f"frame {frame_no:5d}  {fps:5.1f} FPS  "
                      f"top={d.top_label if d else '?'} "
                      f"p={d.top_prob if d else 0:.2f}")

            if args.max_frames and frame_no >= args.max_frames:
                break
    finally:
        cap.release()
        if not args.headless:
            cv2.destroyAllWindows()

    print(f"\nprocessed {frame_no} frames, "
          f"mean {1.0 / max(1e-6, float(np.mean(times))) if times else 0:.1f} FPS")
    print(f"emitted {len(log_rows)} selections")

    if args.log and log_rows:
        with open(args.log, "w", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=["time_s", "frame", "emitted", "inout"])
            writer.writeheader()
            writer.writerows(log_rows)
        print(f"log -> {args.log}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
