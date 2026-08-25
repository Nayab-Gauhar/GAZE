#!/usr/bin/env python3
"""Register targets AUTOMATICALLY from text prompts, instead of clicking boxes.

Uses OWLv2 open-vocabulary detection: you name what to look for ("water bottle",
"medicine strip") and it finds them in the frame. Runs once at setup, so its
~3.5 s CPU latency does not affect runtime throughput.

Each communication label can have several prompts, because objects vary -- WATER
might be a bottle, a glass, or a cup -- and the best-scoring match wins.

    # camera, default vocabulary
    python scripts/auto_register.py --camera 0 --out config/targets.json

    # a still image, custom labels
    python scripts/auto_register.py --image frame.jpg \
        --label WATER "water bottle" "drinking glass" \
        --label PHONE "mobile phone"

    # review before saving
    python scripts/auto_register.py --image frame.jpg --preview out/proposed.png

Important limitation: abstract needs (PAIN, TOILET) have no physical object to
detect. Use printed symbol cards for those and register them with
`register_targets.py`, or add a prompt describing the card itself.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import cv2
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from gaze_target import Target, TargetSet  # noqa: E402
from gaze_target.object_detector import OpenVocabDetector  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

# label -> candidate prompts, best score wins.
DEFAULT_VOCAB: dict[str, list[str]] = {
    "WATER": ["water bottle", "drinking glass", "cup of water"],
    "FOOD": ["bowl of food", "plate of food", "fruit"],
    "MEDICINE": ["medicine strip", "pill bottle", "blister pack of pills"],
    "PHONE": ["mobile phone", "smartphone"],
    "BELL": ["call bell", "small bell", "push button"],
}

# Never register these as communication targets even if detected -- they are
# body parts or furniture, and the patient's own hand often scores highly right
# next to the object they are holding.
BLOCKLIST = {"person", "hand", "face", "arm", "head", "bed", "wall", "window"}


def grab_frame(args) -> np.ndarray | None:
    if args.image:
        return cv2.imread(args.image)
    cap = cv2.VideoCapture(int(args.camera))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)
    if not cap.isOpened():
        print(f"[ERROR] cannot open camera {args.camera}")
        return None
    print("Arrange the objects, then press SPACE to capture (q to quit).")
    frame = None
    while True:
        ok, live = cap.read()
        if not ok:
            break
        prev = live.copy()
        cv2.putText(prev, "SPACE = capture, q = quit", (10, 26),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow("auto register", prev)
        k = cv2.waitKey(1) & 0xFF
        if k == ord(" "):
            frame = live.copy()
            break
        if k == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
    return frame


def main() -> int:
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group()
    src.add_argument("--camera", default=0)
    src.add_argument("--image", default=None)
    ap.add_argument("--width", type=int, default=640)
    ap.add_argument("--height", type=int, default=480)
    ap.add_argument("--label", nargs="+", action="append", metavar=("LABEL", "PROMPT"),
                    help="repeatable: --label WATER 'water bottle' 'glass'")
    ap.add_argument("--threshold", type=float, default=0.12,
                    help="detection confidence floor")
    ap.add_argument("--out", default="config/targets.json")
    ap.add_argument("--preview", default=None, help="write an annotated PNG")
    ap.add_argument("--no-save", action="store_true")
    args = ap.parse_args()

    vocab = DEFAULT_VOCAB
    if args.label:
        vocab = {}
        for group in args.label:
            if len(group) < 2:
                print(f"[ERROR] --label needs a label and >=1 prompt: {group}")
                return 1
            vocab[group[0].upper()] = group[1:]

    frame = grab_frame(args)
    if frame is None:
        print("[ERROR] no frame captured")
        return 1
    if frame.shape[1] != args.width or frame.shape[0] != args.height:
        frame = cv2.resize(frame, (args.width, args.height))
    H, W = frame.shape[:2]

    print(f"\nframe {W}x{H}")
    print(f"labels: {', '.join(vocab)}")
    flat_prompts = sorted({p for ps in vocab.values() for p in ps})
    print(f"prompts ({len(flat_prompts)}): {', '.join(flat_prompts)}\n")

    detector = OpenVocabDetector(ROOT / "models" / "owlv2")
    print("detecting (OWLv2, ~3-5 s on CPU, runs once)...")
    best = detector.best_per_prompt(frame, flat_prompts, score_threshold=args.threshold)

    print(f"\n{'prompt':<26} {'score':>6}  box")
    for prompt in flat_prompts:
        d = best.get(prompt)
        print(f"{prompt:<26} {d.score:>6.3f}  {d.box}" if d
              else f"{prompt:<26} {'--':>6}  not found")

    # Pick the best-scoring prompt for each label.
    chosen: dict[str, tuple[tuple[int, int, int, int], float, str]] = {}
    missing: list[str] = []
    for label, prompts in vocab.items():
        cands = [
            (best[p].box, best[p].score, p)
            for p in prompts
            if p in best and p.lower() not in BLOCKLIST
        ]
        if not cands:
            missing.append(label)
            continue
        chosen[label] = max(cands, key=lambda c: c[1])

    print(f"\n{'label':<12} {'via prompt':<26} {'score':>6}  box")
    for label, (box, score, prompt) in chosen.items():
        print(f"{label:<12} {prompt:<26} {score:>6.3f}  {box}")
    for label in missing:
        print(f"{label:<12} {'NOT FOUND':<26}")

    if missing:
        print(f"\n  {len(missing)} label(s) not detected: {', '.join(missing)}")
        print("  Options: lower --threshold, reword the prompt, improve lighting,")
        print("  or register those with scripts/register_targets.py (needed anyway")
        print("  for abstract needs like PAIN and TOILET, which have no object).")

    if len(chosen) < 2:
        print("\n[ERROR] need at least 2 targets; nothing saved")
        return 1

    target_set = TargetSet(
        targets=[Target(label=k, box=v[0]) for k, v in chosen.items()],
        frame_size=(W, H),
    )

    if args.preview:
        vis = frame.copy()
        for label, (box, score, prompt) in chosen.items():
            x1, y1, x2, y2 = box
            cv2.rectangle(vis, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(vis, f"{label} {score:.2f}", (x1, max(12, y1 - 6)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
        Path(args.preview).parent.mkdir(parents=True, exist_ok=True)
        cv2.imwrite(args.preview, vis)
        print(f"\npreview -> {args.preview}")

    # The feasibility gate. Auto-detection makes it MORE important, not less:
    # a detector will happily return two boxes that the 64x64 gaze heatmap
    # cannot possibly tell apart.
    rep = target_set.resolution_report(W, H)
    print("\n--- layout feasibility (64x64 heatmap gate) ---")
    print(f"1 cell = {rep['heatmap_cell_px'][0]} x {rep['heatmap_cell_px'][1]} px")
    print(f"{'target':<12} {'cells':>8}  status")
    for t in rep["targets"]:
        print(f"{t['label']:<12} {t['cells_total']:>8}  "
              f"{'ok' if t['reliable'] else 'TOO SMALL'}")
    print(f"\n{'pair':<28} {'cells':>7}  status")
    for p in rep["pairs"][:6]:
        print(f"{p['pair']:<28} {p['dist_cells']:>7}  "
              f"{'ok' if p['separable'] else 'TOO CLOSE'}")
    if rep["warnings"]:
        print("\nWARNINGS:")
        for w in rep["warnings"]:
            print(f"  - {w}")
    else:
        print("\nlayout OK")

    if args.no_save:
        print("\n--no-save: config not written")
        return 0

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    target_set.to_json(out)
    print(f"\nsaved {len(chosen)} targets -> {out}")
    print(f"next: python scripts/run_live.py --targets {out} --camera 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
