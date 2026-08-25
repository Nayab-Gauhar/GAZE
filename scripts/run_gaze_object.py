#!/usr/bin/env python3
"""FULLY AUTOMATIC: point the camera, it names the object being looked at.

No config file, no pre-registered boxes, no labels to define. The scene is
scanned for objects in the background, the gaze stage runs at full frame rate,
and the object capturing the gaze is displayed.

    python scripts/run_gaze_object.py --camera 0
    python scripts/run_gaze_object.py --video clip.mp4 --headless
    python scripts/run_gaze_object.py --camera 0 --vocab "water bottle" "phone" "book"

How the two speeds are reconciled: the object detector costs ~5 s on CPU, so it
runs on a background thread every `--refresh` seconds while the gaze stage keeps
running per frame against the most recent object list. Bedside objects move
rarely, so a slightly stale list is fine -- and a moved object or knocked camera
self-heals within one refresh interval.
"""

from __future__ import annotations

import argparse
import sys
import time
from collections import deque
from pathlib import Path

import cv2
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from gaze_target import (  # noqa: E402
    GazelleONNX,
    GazeStateFilter,
    HeadDetector,
    NONE_LABEL,
    TemporalConfig,
)
from gaze_target.object_detector import OpenVocabDetector  # noqa: E402
from gaze_target.registry import DEFAULT_VOCAB, ObjectRegistry  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
MODELS = ROOT / "models"
GAZE_MODELS = {
    "atto": "gazelle_hgnetv2_atto_inout_distill_1x3x320x320_1xNx4.onnx",
    "femto": "gazelle_hgnetv2_femto_inout_distill_1x3x416x416_1xNx4.onnx",
    "pico": "gazelle_hgnetv2_pico_inout_distill_1x3x640x640_1xNx4.onnx",
    "x": "gazelle_dinov3_vits16plus_inout_1x3x640x640_1xNx4.onnx",
}


def draw(frame, objects, head, gaze, belief, top, emitted, fps, registry, show_hm):
    canvas = frame.copy()

    if show_hm and gaze is not None:
        hm = np.clip(gaze.heatmap * 255, 0, 255).astype(np.uint8)
        canvas = cv2.addWeighted(
            canvas, 1.0, cv2.applyColorMap(hm, cv2.COLORMAP_JET), 0.38, 0.0
        )

    for obj in objects:
        x1, y1, x2, y2 = obj.box
        active = obj.label == top or top.startswith(obj.label)
        colour = (0, 255, 0) if active else (165, 165, 165)
        cv2.rectangle(canvas, (x1, y1), (x2, y2), colour, 3 if active else 1)
        p = belief.get(obj.label, 0.0)
        cv2.putText(canvas, f"{obj.label} {p:.2f}", (x1, max(13, y1 - 6)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.48, colour, 2, cv2.LINE_AA)

    if head is not None:
        x1, y1, x2, y2 = head.box
        cv2.rectangle(canvas, (x1, y1), (x2, y2), (255, 200, 0), 2)
        if gaze is not None:
            cv2.arrowedLine(canvas, ((x1 + x2) // 2, (y1 + y2) // 2), gaze.peak_xy,
                            (255, 255, 255), 2, tipLength=0.04)
            cv2.circle(canvas, gaze.peak_xy, 10, (255, 255, 255), 2)

    h, w = canvas.shape[:2]
    cv2.rectangle(canvas, (0, 0), (w, 74), (0, 0, 0), -1)

    looking = top if top != NONE_LABEL else "-- nothing --"
    colour = (0, 255, 0) if top != NONE_LABEL else (150, 150, 150)
    cv2.putText(canvas, "LOOKING AT:", (12, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.62, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(canvas, looking.upper(), (176, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.82, colour, 2, cv2.LINE_AA)
    cv2.putText(canvas,
                f"{fps:4.1f} FPS | {len(objects)} objects | scan #{registry.scan_count}"
                f" ({registry.seconds_since_refresh:.0f}s ago)",
                (12, 58), cv2.FONT_HERSHEY_SIMPLEX, 0.46, (190, 190, 190), 1, cv2.LINE_AA)

    if emitted:
        cv2.rectangle(canvas, (0, h - 52), (w, h), (0, 130, 0), -1)
        cv2.putText(canvas, f">>> {emitted.upper()}", (14, h - 16),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2, cv2.LINE_AA)
    return canvas


def main() -> int:
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group()
    src.add_argument("--camera", default=None)
    src.add_argument("--video", default=None)
    ap.add_argument("--model", default="atto", choices=list(GAZE_MODELS))
    ap.add_argument("--vocab", nargs="+", default=None,
                    help="objects to look for (default: built-in bedside vocabulary)")
    ap.add_argument("--refresh", type=float, default=6.0,
                    help="seconds between background object scans")
    ap.add_argument("--obj-threshold", type=float, default=0.18)
    ap.add_argument("--max-objects", type=int, default=6)
    ap.add_argument("--width", type=int, default=640)
    ap.add_argument("--height", type=int, default=480)
    ap.add_argument("--dwell-frames", type=int, default=10)
    ap.add_argument("--detect-every-n", type=int, default=5)
    ap.add_argument("--headless", action="store_true")
    ap.add_argument("--max-frames", type=int, default=0)
    args = ap.parse_args()

    if args.camera is None and args.video is None:
        args.camera = 0

    vocab = args.vocab or DEFAULT_VOCAB
    print(f"vocabulary ({len(vocab)}): {', '.join(vocab)}")

    gaze_path = MODELS / GAZE_MODELS[args.model]
    if not gaze_path.is_file():
        print(f"[ERROR] missing {gaze_path.name} -- run ./scripts/download_models.sh")
        return 1

    head_det = HeadDetector(MODELS / "deimv2_head.onnx")
    gaze_model = GazelleONNX(gaze_path)
    registry = ObjectRegistry(
        detector=OpenVocabDetector(MODELS / "owlv2"),
        vocab=list(vocab),
        score_threshold=args.obj_threshold,
        refresh_seconds=args.refresh,
        max_objects=args.max_objects,
    )

    source = int(args.camera) if args.camera is not None else args.video
    cap = cv2.VideoCapture(source)
    if args.camera is not None:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)
    if not cap.isOpened():
        print(f"[ERROR] cannot open source: {source}")
        return 1

    ok, first = cap.read()
    if not ok:
        print("[ERROR] cannot read first frame")
        cap.release()
        return 1
    if first.shape[1] != args.width or first.shape[0] != args.height:
        first = cv2.resize(first, (args.width, args.height))
    if args.camera is not None:
        first = cv2.flip(first, 1)

    print("\nfirst object scan (blocking, ~5 s on CPU)...")
    t0 = time.perf_counter()
    dets = registry.scan_now(first)
    print(f"done in {time.perf_counter() - t0:.1f} s -- {len(dets)} objects:")
    for d in dets:
        print(f"   {d.label:<18} {d.score:.3f}  {d.box}")
    if not dets:
        print("   (nothing found -- lower --obj-threshold or add --vocab terms)")

    registry.start()

    cfg = TemporalConfig(dwell_frames=args.dwell_frames, min_inout=0.20)
    filt: GazeStateFilter | None = None
    filt_labels: list[str] = []
    cached_head = None
    times: deque[float] = deque(maxlen=30)
    show_hm = True
    frame_no = 0
    last_announced: str | None = None
    print("\nrunning" + ("" if args.headless else "  (q quit, h heatmap, r reset)"))

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            frame_no += 1
            if args.camera is not None:
                frame = cv2.flip(frame, 1)
            if frame.shape[1] != args.width or frame.shape[0] != args.height:
                frame = cv2.resize(frame, (args.width, args.height))
            registry.submit_frame(frame)

            t_start = time.perf_counter()

            if frame_no % args.detect_every_n == 0 or cached_head is None:
                found = head_det.primary_head(frame)
                cached_head = found if found is not None else None
            head = cached_head

            objects = registry.objects
            target_set = registry.as_target_set((args.width, args.height))
            labels = target_set.labels

            # The object list can change between scans, so the state space of the
            # filter can change too. Rebuild only when the label set actually
            # differs; this resets dwell, which is acceptable because scans are
            # seconds apart and the set is usually stable.
            if filt is None or labels != filt_labels:
                filt = GazeStateFilter(labels=labels or ["_none_"], config=cfg)
                filt_labels = labels

            gaze = None
            if head is not None and labels:
                results = gaze_model(frame, [head.box])
                if results:
                    gaze = results[0]

            if gaze is not None:
                posterior = target_set.score(gaze.heatmap, gaze.inout, gaze.peak_xy)
                decision = filt.update(posterior, inout=gaze.inout)
            else:
                decision = filt.update({NONE_LABEL: 1.0}, inout=0.0)

            times.append(time.perf_counter() - t_start)
            fps = 1.0 / max(1e-6, float(np.mean(times)))

            if decision.emitted:
                print(f"  [{frame_no:5d}]  >>> LOOKING AT: {decision.emitted}")
            elif decision.top_label != last_announced and args.headless:
                print(f"  [{frame_no:5d}]  top={decision.top_label} "
                      f"({decision.top_prob:.2f})")
            last_announced = decision.top_label

            if not args.headless:
                cv2.imshow("gaze object", draw(
                    frame, objects, head, gaze, decision.belief, decision.top_label,
                    decision.emitted, fps, registry, show_hm))
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q"):
                    break
                if key == ord("h"):
                    show_hm = not show_hm
                if key == ord("r") and filt is not None:
                    filt.reset()

            if args.max_frames and frame_no >= args.max_frames:
                break
    finally:
        registry.stop()
        cap.release()
        if not args.headless:
            cv2.destroyAllWindows()

    print(f"\n{frame_no} frames, mean "
          f"{1.0 / max(1e-6, float(np.mean(times))) if times else 0:.1f} FPS, "
          f"{registry.scan_count} object scans")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
