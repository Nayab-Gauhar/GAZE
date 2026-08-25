# Gaze-Target Prototype — Option 3 (scene heatmap)

Detects which registered target a person is looking at from a **single RGB camera**,
with an explicit `NONE` class. Built as the first milestone of the assistive
communication system reviewed in **[`docs/research-review.md`](docs/research-review.md)** —
read that for the comparison of all five candidate approaches, the datasets, the
clinical constraints, and the decision records explaining why this one was built first.

This is **Option 3** from that review: a scene-level gaze heatmap model
(distilled [Gaze-LLE](https://arxiv.org/abs/2412.09586), CVPR 2025) whose output is
associated with registered target boxes. It was chosen to build first because it
requires **no per-patient calibration**, so it can be tested immediately.

> **Not a medical device.** Output is a *communication act* routed to a caregiver,
> never an instruction to act. See "Clinical safety" below.

## Pipeline

```
frame
 ├─ head detection            DEIMv2 Wholebody34 pico, class 7   (cached, see below)
 ├─ gaze heatmap + in/out     distilled Gaze-LLE (ONNX)
 ├─ heatmap → target scoring  posterior over targets + NONE
 └─ sticky HMM + dwell        temporal evidence, abstention, refractory
      └─ emitted label
```

## Install

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Model weights are not committed (the 31M model is 128 MB, over GitHub's limit)
./scripts/download_models.sh          # pico gaze model + head detector, ~21 MB
./scripts/download_models.sh --all    # also the 31M model (128 MB, needs a GPU)

# Optional: verification images with known gaze targets
python scripts/fetch_testdata.py
```

## Quickstart

Registering targets can be **automatic** (name the objects, OWLv2 finds them) or
**manual** (click boxes). Auto is zero-setup; manual is fully reliable and can
represent abstract needs. They write the same config, so you can mix them.

```bash
# 1a. AUTOMATIC -- name what to look for, it finds them
./scripts/download_owlv2.sh                    # 163 MB, one time
pip install tokenizers
python scripts/auto_register.py --camera 0 --out config/targets.json

# 1b. MANUAL -- click a box around each target
python scripts/register_targets.py --camera 0 --out config/targets.json

# 2. Run live
python scripts/run_live.py --targets config/targets.json --camera 0

# Offline on a recording, logging every selection
python scripts/run_live.py --targets config/targets.json --video clip.mp4 \
    --headless --log events.csv
```

### Automatic target registration

Uses **OWLv2** open-vocabulary detection ([arXiv:2306.09683](https://arxiv.org/abs/2306.09683)),
so you can name anything — including things no COCO detector knows, like
`"medicine strip"` or `"call bell"`. Several prompts per label are allowed and the
best-scoring match wins:

```bash
python scripts/auto_register.py --image frame.jpg \
    --label WATER "water bottle" "drinking glass" \
    --label PHONE "mobile phone" \
    --preview out/proposed.png
```

It runs **once at setup**, so its ~3.5 s CPU latency is irrelevant to runtime
throughput — which is exactly why a heavyweight model is acceptable here.

Verified end to end on a real photo: auto-detected `LAPTOP` (0.564) and `COFFEE`
(0.286) from text alone, then the gaze stage correctly predicted **LAPTOP**
(P=0.858 vs COFFEE 0.049).

**Two real limitations, both worth knowing before you rely on it:**

- **Abstract needs have no object.** `PAIN` and `TOILET` cannot be detected because
  there is nothing to detect. Use printed symbol cards and `register_targets.py`
  for those.
- **Detection can just fail.** On one test photo `PHONE` was correctly reported as
  not found (there was no phone), but a transparent water bottle against white
  linen is genuinely hard. The script tells you which labels it missed rather than
  silently registering nothing, and you can fall back to manual for those.

Body parts and furniture are blocklisted as targets, because the patient's own hand
often scores highly right next to the object they are holding.

### Start with the notebook

If you want to understand the pipeline before running it live, work through
**[`notebooks/01_explore_on_images.ipynb`](notebooks/01_explore_on_images.ipynb)**.
It runs each stage on still images and plots what the model actually produced — the
raw 64×64 heatmap, the 64×64 grid drawn over the frame, the target posterior as a
bar chart, and belief curves over time. There is a cell at the end for dropping in
your own photo.

```bash
pip install jupyter matplotlib
jupyter notebook notebooks/01_explore_on_images.ipynb
```

Verification scripts (no camera needed):

```bash
python scripts/verify_gaze.py testdata/*.jpg --out out/   # gaze localisation only
python scripts/verify_targets.py                          # full stack + assertions
python scripts/benchmark_models.py                        # latency + correctness
```

## Measured performance

All 8 gaze variants, benchmarked on **8-core CPU, no GPU, 640×480** frames via
`scripts/benchmark_models.py`. `+det FPS` assumes head detection every 5th frame.
AUC is the published GazeFollow figure. `peak_ok` = heatmap peak still landed on
the known ground-truth target.

| Variant | Params | Size | Input | ms | gaze FPS | +det FPS | AUC | peak_ok |
|---|---|---|---|---|---|---|---|---|
| **Atto** (CNN) | 2.93 M | 12 M | 320² | **17.3** | 57.9 | **38.5** | 0.9267 | yes |
| **Femto** (CNN) | 3.15 M | 13 M | 416² | 26.4 | 37.9 | 28.5 | 0.9391 | yes |
| Pico (CNN) | 3.51 M | 16 M | 640² | 82.0 | 12.2 | 11.0 | 0.9491 | yes |
| N (CNN) | 4.61 M | 16 M | 640² | 85.5 | 11.7 | 10.6 | 0.9481 | yes |
| S (ViT) | 8.17 M | 35 M | 640² | 253.9 | 3.9 | 3.8 | 0.9545 | yes |
| M (ViT) | 12.37 M | 52 M | 640² | 292.8 | 3.4 | 3.3 | 0.9564 | yes |
| L (ViT) | 24.33 M | 100 M | 640² | 602.9 | 1.7 | 1.6 | 0.9593 | yes |
| X (ViT) | 31.43 M | 128 M | 640² | 956.8 | 1.0 | 1.0 | 0.9604 | yes |

Head detector (DEIMv2 pico, 6 MB): **43.5 ms**.

**The key result: input resolution dominates CPU latency far more than parameter
count.** Atto (2.93 M @ 320²) and Pico (3.51 M @ 640²) are similarly sized, yet Atto
is **~4.7× faster** — almost entirely because 320² is a quarter of the pixels of
640². And every variant localised correctly on the test image, so on CPU the extra
capacity buys ~3% AUC for 4-55× the latency. **Atto is therefore the default.**

The ViT variants need a GPU to be practical; the CNN variants (Atto/Femto/Pico/N)
are the CPU-viable set.

End-to-end measured throughput:

| Config | Throughput |
|---|---|
| Atto, `--detect-every-n 5` | **35.0 FPS** |
| Pico, `--detect-every-n 5` | 10.0 FPS |
| Pico, `--detect-every-n 1` | 7.1 FPS |

Head caching is nearly free in accuracy terms because a bed-bound patient's head
barely moves between frames. **The latency requirement is loose anyway** — the
~0.5-1 s dwell window dominates response time, so throughput buys *evidence*
(frames to filter over), not responsiveness.

## Verification results

`scripts/verify_gaze.py` on three CC-licensed images with known gaze targets:

| Image | Head score | In-frame score | Gaze peak landed on |
|---|---|---|---|
| Woman looking at phone (photo) | 0.879 | 0.767 | **the phone in her raised hand** ✅ |
| Boy drinking (cartoon illustration) | 0.862 | 0.151 | **the cup at his mouth** ✅ |
| Man reading (photo of an antique framed photo) | 0.778 | 0.170 | **the book/table** ✅ |

Gaze localisation was correct on all three — including a cartoon and a
photo-of-a-photo, both far outside the training domain. Localisation is more
robust than expected.

`scripts/verify_targets.py`, with the correct target plus three spatial decoys:

```
PHONE   P=0.879   WINDOW P=0.001   WATER P=0.000   BELL P=0.000   NONE P=0.120
argmax: PHONE  (ground truth: PHONE)                              PASS
emitted 'PHONE' at frame 12 with dwell_frames=10                  PASS
blank frames -> P(NONE) = 1.000                                   PASS
```

On the synthetic 100-frame sequence (look / absent / look), the system emitted
**exactly 2 selections for 2 looking episodes and zero during the absent stretch.**

## Findings that matter

**1. The `inout` score is not a reliable `NONE` signal on its own.** It measured
0.767 / 0.151 / 0.170 on the three images above — *low even where the subject was
genuinely looking at an in-frame object*. A naive `min_inout=0.35` gate would have
wrongly forced `NONE` on two correct cases. `--min-inout` therefore defaults to a
permissive 0.20, and the primary evidence is **heatmap mass captured by registered
targets**, which is the more direct signal.

**2. The 64×64 heatmap is a hard resolution ceiling.** Confirmed empirically from
the ONNX graph (`heatmap float32[heads, 64, 64]`). At 640×480 one cell covers
10×7.5 px, so a small object like a medicine strip spans only a few cells and
cannot be discriminated from a neighbour. `TargetSet.resolution_report()` gates
this before you trust any prediction, and `register_targets.py` prints it at setup:

```
target      cells  reliable          pair                cells  separable
WATER       118.1  yes               WATER <-> PAIN       19.97  yes
```

This is the feasibility check to run **before** collecting data — an unresolvable
layout cannot be fixed by a better model.

The gate checks **each dimension separately, not just area**. That matters: a real
auto-detected coffee glass measured 19×79 px = 20 cells of area, which passes an
area-only test, but it is just **1.9 cells wide** and therefore unreliable along
that axis. Tall thin objects are a trap.

**3. Depth ambiguity is structural.** The heatmap lives in 2D image space, so two
targets at different distances but similar image positions are not separable. This
is the main reason Option 3 is the cold-start path rather than the primary one.

## Configuration

`config/targets.json`:

```json
{
  "frame_size": [640, 480],
  "pad_ratio": 0.15,
  "targets": [{ "label": "WATER", "box": [76, 163, 179, 249] }]
}
```

`pad_ratio` dilates boxes before scoring, because heatmaps routinely peak slightly
off an object rather than dead-centre on it.

Key tuning flags on `run_live.py`: `--dwell-frames` (longer = fewer false
activations, slower), `--commit-threshold`, `--min-inout`, `--detect-every-n`,
`--model {pico,big}`.

## Default target vocabulary

`register_targets.py` defaults to `WATER TOILET PAIN HELP` rather than the original
`water/food/medicine/phone/bell`. Reasons, from §12.3 of the research report:
**TOILET** is among the most frequent and dignity-critical needs of a bed-bound
patient; **PAIN** replaces MEDICINE because medication is staff-scheduled and a
false `MEDICINE` is the highest-risk misfire. Override with `--labels`.

## Clinical safety

- Post-stroke **dysphagia** is common. A `WATER` output must never be read as
  "give fluids" — a caregiver checks the diet plan.
- Every output needs **two-step confirmation** before being acted on. The dwell +
  refractory logic here reduces false activation but does not replace confirmation.
- Patients with **gaze palsy or neglect** may be unable to direct gaze at what they
  intend. The system should declare "not servable" rather than guess.
- **Not validated on post-stroke patients.** All numbers above come from healthy,
  mostly camera-facing subjects. Treat them as upper bounds.

## Known limitations

- No per-patient adaptation (by design — that is Option 2's job).
- Single-subject assumption: `primary_head` picks the largest head, so a caregiver
  leaning closer than the patient would be tracked instead.
- **Head detection is a hard dependency.** If the head is not visible the pipeline
  produces `NONE` and nothing else — verified on a photo where the subject's head
  was cropped out (head score 0.032 while the *body* scored 0.908). This is a safe
  failure rather than a wrong answer, but for a bed-bound patient partially hidden
  by pillows or lines it is a real risk. A body-box fallback is not implemented.
- Emits nothing while `refractory` is active.
- `verify_targets.py` scores the same still frame repeatedly, so it validates
  correctness and plumbing, not temporal robustness on real motion.

## Credits

- **Gaze-LLE** — Ryan et al., CVPR 2025. [arXiv:2412.09586](https://arxiv.org/abs/2412.09586) · [fkryan/gazelle](https://github.com/fkryan/gazelle)
- **Distilled ONNX exports + DEIMv2 head detector** — [PINTO0309/gazelle-dinov3](https://github.com/PINTO0309/gazelle-dinov3), [PINTO_model_zoo](https://github.com/PINTO0309/PINTO_model_zoo)
- Test images from Wikimedia Commons (CC0 / CC BY 2.0 / no restrictions); see
  `scripts/` history for the exact files.
