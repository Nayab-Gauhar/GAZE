# Vision-Based Gaze-to-Object Communication for Post-Stroke Patients

Research review of computer-vision approaches for the task:

> Given a single RGB camera view of a post-stroke patient and several candidate objects
> around them, identify which object the patient is looking at — or report that they are
> not clearly looking at any of them.

Target vocabulary: `WATER`, `FOOD`, `MEDICINE`, `PHONE`, `CALLING_BELL`, `NONE`.

---

## 1. How to frame the problem correctly

The literature calls this **Gaze Object Prediction (GOP)**, a specialisation of **gaze
target estimation** / **gaze following** (predicting *where* in an image a person looks),
which itself descends from the older robotics term **VFOA** (visual focus of attention).

Two framing decisions matter more than model choice:

**(a) This is classification over a tiny closed set, not free-form gaze regression.**
Most published gaze-following work predicts a continuous 2D point over an arbitrary scene.
You need one of six discrete labels. That is a *much* easier statistical problem and it
lets you trade spatial precision for reliability.

**(b) The scene is static and you control it.** Unlike in-the-wild benchmarks, the camera,
the bed, and the object positions are fixed for a given patient session. This is the single
biggest exploitable asset in the whole problem, and most of the research pipeline can be
moved *offline* into a per-patient calibration step. Approaches that look weak on public
benchmarks can be strong here for exactly this reason.

A useful consequence: **object detection does not need to run per frame.** Detect and
register the five objects once at setup (or every few seconds to catch a moved cup), and
spend the per-frame budget entirely on the patient's face and gaze.

---

## 2. Approach families

### A. Direct gaze-zone classification (face crop → one of N classes)

Train a CNN/ViT to map a face (or eye-region) crop directly to the object label. No gaze
angle, no 3D geometry, no object detector in the loop — the network learns the mapping from
appearance to *this specific spatial layout*.

The mature precedent is **driver gaze-zone estimation**, which is structurally the same
problem: one interior camera, a handful of fixed regions (mirrors, speedometer, road),
coarse output. Reported results are strong:

- [Vora et al., "Driver Gaze Zone Estimation using CNNs"](https://arxiv.org/abs/1802.02690) —
  95.18% accuracy in cross-subject testing on naturalistic driving data.
- [Sensors 22(15):5857](https://www.mdpi.com/1424-8220/22/15/5857/htm) — a
  position-invariant single-camera zone classifier; a 2D CNN on single frames reached
  74.96% mean average recall, while a 3D CNN over frame sequences reached 87.02%. The
  ~12-point gap from temporal modelling alone is the most actionable number in this table.
- [Sensors 24(22):7254](https://www.mdpi.com/1424-8220/24/22/7254) — YOLOv8 image
  classification applied to gaze zones, i.e. the task is tractable with commodity models.
- [ACM SMC 2020](https://dl.acm.org/doi/10.1109/SMC42975.2020.9283470) — handles the two
  failure cases that will bite you: self-occlusion, and head and eye directions not aligned.

**Advantages.** Highest achievable accuracy per unit of engineering, because the model
absorbs the geometry instead of you estimating it. Tiny and fast. Naturally supports a
`NONE` class as just another output. Directly optimises the metric you care about.

**Limitations.** Requires labelled data *from your setup*, and ideally from your patient.
Does not transfer if the camera or object layout moves — you retrain or recalibrate.
Provides no interpretable intermediate signal, which is a real problem for clinical trust
and debugging. Cannot handle a new object without new data.

**Real-time.** Trivially real-time. A MobileNet/EfficientNet-lite class backbone on a
128×128 face crop runs at hundreds of FPS on a GPU and comfortably >30 FPS on a Raspberry
Pi 5 or Jetson Orin Nano.

---

### B. 3D gaze vector + geometric ray–object intersection

Estimate the patient's 3D gaze direction from the face, estimate the 3D position of each
object, and pick the object whose direction from the eye best matches the gaze ray.

Components:

- **Gaze direction.** [L2CS-Net](https://arxiv.org/abs/2203.03339) is the practical default:
  ResNet-50, pitch and yaw each predicted as a 90-bin classification (4°/bin) then converted
  to a continuous angle by expectation. Reported 3.92° on MPIIGaze and 10.41° on Gaze360.
  Code at [Ahmednull/L2CS-Net](https://github.com/Ahmednull/L2CS-Net), also packaged as
  [py-feat/l2cs](https://huggingface.co/py-feat/l2cs). Newer options:
  [CapStARE](https://arxiv.org/html/2509.19936) (frozen ConvNeXt + capsules + GRU decoders,
  real-time) and [Alfa](https://arxiv.org/html/2603.08445v1) (low-rank filter adaptation for
  cross-domain personalisation).
- **Object 3D position.** Either measure once by hand at setup (most reliable), or use
  [Depth Anything V2](https://arxiv.org/abs/2406.09414) — its
  [metric indoor variants](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Large-hf)
  give absolute depth from one RGB image.

**Advantages.** Fully interpretable — you can show a clinician the gaze ray and the angular
margin to each candidate. Object-agnostic: add a sixth object by registering its position,
no retraining. Gives a natural confidence signal (angular margin), which is exactly what a
`NONE` decision and a dwell-time rule need. Generalises across patients out of the box.

**Limitations.** Error compounds: gaze angle error + eye-position error + object-position
error. The 10.41° Gaze360 figure is the honest in-the-wild number, and 10° at 60 cm is
~10.5 cm of lateral uncertainty — enough to confuse adjacent objects if you place them
carelessly. Head-pose and eye direction being non-aligned is a known degradation. Also
sensitive to camera intrinsics and to the eye-centre estimate.

**Do not substitute head pose for gaze.** The VFOA literature is explicit that this creates
ambiguity because the same head pose can serve different targets — see
[Sheikhi & Odobez, PRL 2015](https://dl.acm.org/doi/10.1016/j.patrec.2014.10.002) and
[Palinko et al.](https://www.researchgate.net/publication/312288317_Robot_reading_human_gaze_Why_eye_tracking_is_better_than_head_tracking_for_human-robot_collaboration),
who found eye-based gaze materially outperformed head-based in human-robot interaction.
Head pose is a useful *prior*, not a replacement. Note also that
[MediaPipe's own iris documentation](https://github.com/google-ai-edge/mediapipe/blob/master/docs/solutions/iris.md)
states iris tracking does not infer where a person is looking — landmarks alone are not gaze.

**Real-time.** L2CS-Net (ResNet-50) is ~10 ms/frame on a modern GPU; face detection adds a
few ms. Depth runs once at setup, not per frame. Easily 30+ FPS.

---

### C. Scene-based gaze target heatmap + object association

Run a gaze-following model that consumes the whole image plus the patient's head box and
outputs a 2D heatmap over the scene; then assign the heatmap mass to the nearest registered
object box.

**Gaze-LLE** ([CVPR 2025 Highlight, arXiv 2412.09586](https://arxiv.org/abs/2412.09586),
code at [fkryan/gazelle](https://github.com/fkryan/gazelle)) is the strongest and simplest
current option. It puts a lightweight transformer decoder on a **frozen DINOv2** backbone,
learning only ~2.8M parameters, and needs no depth or pose branch. Reported: GazeFollow
AUC 0.956 / Avg L2 0.104 (ViT-B), 0.958 / 0.099 (ViT-L); VideoAttentionTarget AUC 0.933,
Avg L2 0.107, and in/out-of-frame AP 0.897. It trains to state of the art in under 1.5 hours
on a single RTX 4090, which makes per-site fine-tuning genuinely cheap.

Two Gaze-LLE properties matter for you specifically:

1. **It has an in/out-of-frame head** (the `_inout` checkpoints, fine-tuned on
   VideoAttentionTarget). That is a ready-made, pretrained "is the gaze target even visible"
   signal — the closest off-the-shelf thing to your `NONE` requirement.
2. **The head box is a soft prompt, not a hard input.** The paper's ablation shows the model
   still predicts a valid target with no head prompt in single-person scenes. A bedside
   camera *is* a single-person scene, so you can degrade gracefully when head detection
   flickers.

Alternatives: [ViTGaze](https://github.com/hustvl/ViTGaze) (reuses ViT self-attention as the
human–scene interaction signal; state of the art among single-modality methods, +3.4% AUC
and +5.1% AP with 59% fewer parameters than multimodal peers) and
[Sharingan](https://arxiv.org/abs/2310.00816) (a point-regression variant doing multi-person
prediction in one forward pass). The geometrically grounded
[ChildPlay model](https://publications.idiap.ch/attachments/papers/2023/Tafasca_ICCV_2023.pdf)
explicitly reasons about the 3D field of view via depth, and is a good middle ground between
B and C.

**Advantages.** Best-in-class use of scene context, so it exploits the fact that a cup and a
phone *look* like plausible gaze targets. Strong pretrained weights, so it works reasonably
zero-shot. Robust to imprecise head boxes. Ships with an out-of-frame confidence head.

**Limitations.** Optimised for pixel-level target localisation, not for discriminating
between five nearby small objects — heatmap mass can straddle two adjacent items.
Benchmark AUC is measured over whole scenes and translates poorly into your decision metric.
Domain gap is real: all these models degrade on **GOO-Real**, and the Gaze-LLE authors
attribute that partly to the subject rarely facing the camera and partly to the annotation
scheme being "what the participant was told to look at" rather than "what an annotator
infers" — your setup is the *former* kind, which is the harder one for these models.
Larger and heavier than A or B.

**Real-time.** The vanilla ViT-B model is ~88.8M total parameters; ViT-L is ~302.9M. The
important practical development is [PINTO0309/gazelle-dinov3](https://github.com/PINTO0309/gazelle-dinov3),
which distils Gaze-LLE into DINOv3-ViT and HGNetV2-CNN backbones and publishes **ONNX
exports with TensorRT benchmarks**:

| Variant | Params | GazeFollow AUC | VAT in/out AP | Input |
|---|---|---|---|---|
| Atto (CNN) | 2.93 M | 0.9267 | 0.8749 | 320² |
| Femto (CNN) | 3.15 M | 0.9391 | 0.8779 | 416² |
| Pico (CNN) | 3.51 M | 0.9491 | 0.8861 | 640² |
| N (CNN) | 4.61 M | 0.9481 | 0.9012 | 640² |
| S (ViT) | 8.17 M | 0.9545 | 0.8945 | 640² |
| M (ViT) | 12.37 M | 0.9564 | 0.8953 | 640² |
| X (ViT) | 31.43 M | **0.9604** | **0.9118** | 640² |
| XL (teacher) | 88.50 M | 0.9593 | 0.9051 | 640² |
| *Gaze-LLE ViT-B (ref.)* | *88.80 M* | *0.9560* | *0.8970* | *448²* |

Pico at 3.51M parameters retains AUC 0.9491 — within ~0.7% of the 88.8M original. That makes
approach C deployable on an embedded device, which it otherwise would not be.

---

### D. End-to-end Gaze Object Prediction

Single networks that jointly detect objects and predict which one is attended, rather than
chaining a gaze model to a detector.

- [GaTector](https://arxiv.org/abs/2112.03549) — unified framework with a shared backbone.
- [TransGOP](https://arxiv.org/abs/2402.13578) — transformer-based; reported state of the art
  on GOO-Synth and GOO-Real across all three tracks (detection, gaze estimation, GOP).
  Code: [chenxi-Guo/TransGOP](https://github.com/chenxi-Guo/TransGOP).
- [Open-Vocabulary GOP (ACM MM 2026)](https://arxiv.org/abs/2607.18827) — introduces the
  **DiSG** benchmark with 86 in-the-wild categories, and a method combining text-driven
  object discovery with a gaze-guided selection module that picks the intended target from
  the candidates. This is architecturally the closest published match to your problem
  statement, and being open-vocabulary it would let a caregiver add "tissue box" by typing it.
- [GazeVLM](https://arxiv.org/abs/2511.06348) — a vision-language model doing person
  detection, gaze target detection and gaze object identification in one framework, fusing
  RGB with HHA-encoded depth under text prompts; introduces an object-level metric `AP_ob`
  and reports state of the art on GazeFollow and VideoAttentionTarget.

**Advantages.** Outputs the object label directly, which is your actual desired output.
Jointly optimised, so the detector and gaze branch co-adapt. Open-vocabulary variants make
the object set configurable at runtime without retraining.

**Limitations.** Trained and evaluated almost entirely on retail-shelf data (GOO,
RetailGaze), a domain very unlike a hospital bed. Heaviest option; VLM-based variants are
far from real-time on edge hardware. Wasteful here — it spends capacity re-detecting objects
every frame in a scene where objects barely move. Fewer mature, maintained implementations.

**Real-time.** TransGOP-class models are plausible on a desktop GPU; GazeVLM is not
real-time on embedded hardware today.

---

### E. Zero-shot VLM prompting

Ask a general vision-language model directly ("which object is the person looking at?").

**Advantages.** Zero implementation cost for a baseline. Handles arbitrary objects and can
explain its answer in text. Excellent for rapid feasibility checks and for auto-labelling
your pilot recordings.

**Limitations.** Current evidence says this is not yet reliable enough to act on. A 2026
benchmark, [Benchmarking Gaze Following and Social Gaze Prediction in VLMs](https://arxiv.org/html/2605.19859),
frames gaze following as requiring precise face understanding, 3D scene structure and
spatial grounding — the geometric-reasoning regime where VLMs are weakest. Also unbounded
latency, no calibrated confidence, and cloud inference is a non-starter for patient video.

**Real-time.** No. Use it offline as a labelling assistant and an upper-bound sanity check.

---

## 3. Comparison

| | A. Zone classification | B. Gaze ray + geometry | C. Heatmap + association | D. End-to-end GOP | E. VLM |
|---|---|---|---|---|---|
| Accuracy on *this* task | **Highest (if calibrated)** | Medium–high | Medium | Medium | Low |
| Needs your own data | **Yes (blocking)** | No | Optional | Yes | No |
| Interpretable | No | **Yes** | Partly | Partly | Nominally |
| Add a new object | Retrain | **Register position** | Add a box | Retrain (or text prompt) | Prompt |
| Native `NONE` support | **Yes (a class)** | Yes (angular margin) | Yes (in/out head) | Weak | Weak |
| Robust to layout change | No | **Yes** | Yes | Yes | Yes |
| Edge real-time | **Yes, easily** | Yes | Yes (distilled) | Marginal | No |
| Clinical explainability | Poor | **Good** | Fair | Fair | Poor |
| Engineering effort | Low model / high data | Medium | Low–medium | High | Very low |

---

## 4. Datasets

No public dataset exists for gaze-to-object in a clinical bedside setting, and none covers
post-stroke faces. **This is the central gap and you should plan to collect data.** What
exists is useful for pretraining and for baselining, not for validation.

| Dataset | Content | Use to you |
|---|---|---|
| [GazeFollow](https://arxiv.org/abs/2105.10793) (via GOP lineage) | ~large in-the-wild images, ~10 annotations/image, 2D gaze point | Pretraining backbone for approach C |
| [VideoAttentionTarget](https://arxiv.org/html/2003.02501v2) | Video clips, dynamic gaze, **in/out-of-frame labels** ([code](https://github.com/ejcgt/attention-target-detection)) | The only mainstream source of supervision for your `NONE` class |
| [GOO-Synth / GOO-Real](https://arxiv.org/abs/2105.10793) | Synthetic + real retail; head, gaze point, **gazed-object** labels; built for sim2real ([repo](https://github.com/upeee/GOO-GAZE2021)) | Closest task match; its sim2real design is the template for a synthetic bedside set |
| [Retail Gaze / RetailGaze_V2_seg](https://huggingface.co/datasets/Voxel51/retail_gaze) | 3,922 images, 12 camera angles, product-region segmentation | Multi-viewpoint robustness; camera-angle ablation |
| [ChildPlay](https://arxiv.org/html/2307.01630v1) | Children + adults, uncontrolled settings, rich gaze annotation | **Read the finding, not just the data** (below) |
| [DiSG](https://arxiv.org/abs/2607.18827) | 86 in-the-wild categories for open-vocabulary GOP | Baseline for approach D; long-tail evaluation |
| MPIIGaze / Gaze360 / ETH-XGaze | Face crops with 3D gaze angle labels | Pretraining approach B's gaze regressor |

**The most important dataset result for your project is from ChildPlay.** Tafasca et al.
found that looking-at-faces performance was much worse on children than adults, and that
fine-tuning on child-specific gaze annotations improved it substantially. The lesson
generalises directly: gaze models inherit the demographics of their training data, and a
population absent from that data (children there, stroke patients here) is systematically
underserved until you fine-tune on it. Expect out-of-the-box performance on your patients
to be meaningfully worse than any published benchmark number, and budget for fine-tuning.

Encouragingly, personalisation is cheap. [Few-Shot Adaptive Gaze Estimation](https://arxiv.org/abs/1905.01941)
reports adapting to a new person with as few as 3 calibration samples, reaching 3.18° on
GazeCapture (a 19% improvement over prior art). [Alfa](https://arxiv.org/html/2603.08445v1)
does cross-domain personalisation from a few *unlabelled* samples. Since you have a
cooperative patient in a fixed bed, a 60-second guided calibration ("please look at the cup…
now the phone…") is clinically realistic and is the highest-leverage thing in the entire
system.

---

## 5. The `NONE` class is the hard part

Detecting "not clearly looking at any object" is harder than the classification, and it is
where a naive system will fail in the clinic. A patient looks around constantly: at a
visitor, a TV, the ceiling, nowhere. If every glance at the cup triggers `WATER`, the
system is unusable — this is the **Midas touch problem**, named in gaze-interaction research
for interfaces that treat mere looking as commanding
([JEMR](https://www.mdpi.com/1995-8692/2/4/22/xml),
[Isomoto et al., ETRA 2022](https://www.iplab.cs.tsukuba.ac.jp/~isomoto/papers/isomoto_etra2022p.pdf)).

Four mechanisms, best used together:

1. **Make `NONE` an explicit class with substructure, not a rejection threshold.** Driver
   gaze-zone systems always include a "forward / road" zone rather than treating it as
   absence. Do the same: add `REST` (the patient's neutral head-and-eye posture) and
   `ELSEWHERE` as trained classes. Discriminative training on the negative class works far
   better than thresholding a five-way softmax.
2. **Dwell time.** Require the same label to hold for a sustained window before emitting.
   This is standard AAC practice and directly attacks Midas touch. Consider
   [variable dwell time](https://arxiv.org/abs/1704.06399) — shorter for high-prior items,
   longer for rare ones — and probabilistic dwell adjustment.
3. **Temporal evidence accumulation, not per-frame argmax.** Recall the 74.96% → 87.02%
   jump from single-frame 2D CNN to sequence-based 3D CNN in the driver study. Run a
   Bayesian filter or small temporal model over per-frame posteriors; abstain while the
   posterior is diffuse.
4. **Two-step confirmation.** On a candidate selection, speak or display "Water?" and require
   a confirmation — a sustained blink, or gaze at a dedicated YES marker. Two-step selection
   is the established fix for false activation and converts a false positive from a wrong
   action into a mild annoyance. **For a MEDICINE or CALLING_BELL action this is mandatory.**

Design your metric around this: not accuracy, but **per-class recall at a fixed
false-activation rate during idle periods** (e.g. ≤1 spurious selection per hour of the
patient just lying there looking around). An 85%-recall system with near-zero false
activations is clinically useful; a 97%-accuracy system that fires randomly is not.

---

## 6. Stroke-specific challenges (the largest risk, and least researched)

Every model above is trained on neurologically healthy faces. Post-stroke patients violate
those assumptions in ways that are individually predictable and collectively severe:

- **Gaze palsy.** Supranuclear and horizontal gaze palsies are common in acute stroke
  ([PMC7989724](https://pmc.ncbi.nlm.nih.gov/articles/PMC7989724/),
  [PMC9795706](https://pmc.ncbi.nlm.nih.gov/articles/PMC9795706/)). The patient may be
  physically unable to direct their eyes at an object they want. **Gaze direction and
  communicative intent can be decoupled** — the deepest problem here, and no amount of model
  accuracy fixes it. Per-patient calibration to the patient's *achievable* gaze range is the
  only real mitigation.
- **Visual field loss.** Hemianopia and quadrantanopia mean half the field may be invisible
  ([NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK562262/)), so objects must be
  placed inside the intact field. Patients with associated neglect may be *unaware* of the
  deficit and will not report it.
- **Non-stationarity.** Over half of hemianopsia cases after ischaemic stroke recover
  spontaneously within about a month. The patient's gaze behaviour is a moving target;
  calibration must be repeatable and periodically refreshed, not one-shot at admission.
- **Facial asymmetry, ptosis, incomplete eye closure.** These break face alignment,
  landmark detection and eye-crop-based gaze models, and they corrupt blink detection —
  which matters if you use blink as the confirmation channel. Asymmetry also means
  left-eye and right-eye estimates may disagree; treat that disagreement as a feature and a
  confidence signal rather than averaging it away.
- **Head posture.** Bed-bound patients are often reclined, tilted, or partly occluded by
  pillows and lines — an extreme head-pose regime that is underrepresented in training data
  and that triggers the self-occlusion and non-aligned-head-and-eye failure modes.
- **Fatigue and fluctuating alertness.** Dwell parameters that work in the morning may not
  in the evening; adaptive rather than fixed thresholds.

Clinical grounding worth reading: the
[ESO guideline on visual impairment in stroke](https://pmc.ncbi.nlm.nih.gov/articles/PMC12098360/),
and [PLoS One 2022 on characterising eye-gaze positions in people with severe motor
dysfunction](https://pmc.ncbi.nlm.nih.gov/articles/PMC9432701/), which develops scoring
metrics for exactly this population.

**Do not position this as diagnostic.** It is an assistive communication aid whose output
is always mediated by a caregiver confirming the request. That framing keeps it out of
regulated-medical-device territory and, more importantly, is the honest description of what
the accuracy will support.

---

## 7. Recommended architecture

A **calibrated hybrid of B and A, with C as the context prior** — chosen because it is
interpretable enough for clinicians to trust, cheap enough to run at the bedside, and
degrades gracefully.

### Setup phase (once per patient session, ~2 minutes)

1. Fix camera; capture intrinsics once per hardware unit.
2. Register the five objects. Run an open-vocabulary detector — [YOLO-World](https://arxiv.org/html/2401.17270v3)
   (35.4 AP on LVIS at 52 FPS on a V100) or OWLv2 — prompted with the object names, and let
   the caregiver confirm/correct the boxes in a simple UI. Recover 3D positions from
   [Depth Anything V2 metric-indoor](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Large-hf),
   or from hand-measured positions for the highest reliability.
3. **Guided calibration.** Prompt the patient to look at each object in turn, plus a rest
   pose. Collect ~10-20 seconds each. Use it to (i) personalise the gaze regressor
   ([few-shot adaptation](https://arxiv.org/abs/1905.01941)), (ii) fit the per-patient
   decision boundaries, and (iii) **measure the patient's achievable gaze range** and warn
   the caregiver if two objects are not separable for this patient.
4. **Co-design the layout.** You control object placement — use it. With ~10° of gaze
   uncertainty at 60 cm viewing distance you have ~10.5 cm of lateral error, so place
   objects ≥25-30 cm apart, or arrange five items over a ~120° arc for ~24° of angular
   separation each. Placing objects for maximum angular separation inside the intact visual
   field buys more accuracy than any model upgrade.

### Runtime, per frame (~30-60 ms budget)

```
frame
 ├─ face/head detection (SCRFD or YOLO-face)        ~3-5 ms
 ├─ head pose + landmarks (prior + quality gate)    ~3 ms
 ├─ personalised gaze regressor (L2CS-Net class)    ~10 ms   → pitch, yaw + uncertainty
 ├─ [optional] distilled Gaze-LLE Pico (3.51 M)     ~10 ms   → scene-context heatmap prior
 ├─ score each registered object: angular margin × heatmap mass
 ├─ include REST and ELSEWHERE as scored hypotheses
 └─ Bayesian filter over the last N frames
      └─ dwell satisfied AND margin above per-patient threshold?
           └─ two-step confirmation → emit WATER / FOOD / MEDICINE / PHONE / BELL
```

Objects are re-detected every few seconds, not every frame. All inference is local — no
patient video leaves the device.

### Hardware and latency

Jetson Orin Nano or equivalent, everything in ONNX/TensorRT. The key realisation is that
**your latency requirement is loose**: the dwell window (roughly 800-1500 ms) dominates
end-to-end response time, so 30-60 ms per frame is ample. What throughput buys you is not
responsiveness but *evidence* — at 20-30 FPS a 1.5 s dwell yields 30-45 independent
observations to filter over, which is what makes a low false-activation rate achievable.
For reference, a comparable landmark-based gaze HCI system reports 3.0° average angular
error and sub-70 ms end-to-end latency ([Appl. Sci. 16(11):5653](https://www.mdpi.com/2076-3417/16/11/5653)).

CPU-only fallback is viable with the Atto/Femto distilled variants (2.93M / 3.15M params) at
reduced accuracy.

---

## 8. Evaluation protocol

Two methodological points that are easy to get wrong and that will invalidate your results:

- **Split by session and by patient, never by frame.** Frames within one dwell are almost
  identical; random frame splits produce inflated accuracy that evaporates in deployment.
  Report cross-patient (leave-one-patient-out) numbers as the headline.
- **Measure during idle periods too.** Accuracy on trials where the patient *was* asked to
  look at something tells you nothing about false activations during the other 23 hours.
  A large fraction of your evaluation recording should be unprompted.

Metrics to report:

| Metric | Why |
|---|---|
| Per-class recall @ ≤1 false activation/hour idle | The clinically decisive number |
| `NONE` / idle specificity | Governs whether the system is tolerable to live with |
| Median and 95th-percentile time-to-selection | Usability; patients fatigue quickly |
| Confusion matrix over the 5 objects + NONE | Reveals which pairs need repositioning |
| Accuracy vs. head-pose deviation and vs. object angular separation | Tells you the operating envelope and drives layout guidance |
| Degradation over a session | Detects fatigue effects and calibration drift |

Baselines worth running for comparison: head-pose-only (to quantify how much the eyes
actually add for *your* patients), zero-shot Gaze-LLE `_inout` with nearest-object
association, and a zero-shot VLM.

---

## 9. Suggested order of work

1. **Zero-shot feasibility, on healthy volunteers, in a mock bed setup.** Gaze-LLE `_inout`
   + hand-registered object boxes. One afternoon. Tells you whether the geometry of your
   layout is even separable before you invest in data.
2. **Approach B end-to-end** with L2CS-Net and hand-measured object positions. Establishes
   the interpretable baseline and the confidence signal.
3. **Collect a pilot dataset.** Healthy volunteers first, then — with ethics approval — a
   small post-stroke cohort. Record unprompted idle time deliberately. This is the critical
   path and the long lead time; start the approvals early.
4. **Add per-patient calibration and the temporal filter.** Expect the largest single
   accuracy gain here, based on the few-shot and 2D-vs-3D-CNN evidence above.
5. **Then, if needed, train approach A** on the pooled data as a per-site specialist model,
   keeping B running in parallel as the interpretable cross-check and fallback.

## 10. Honest assessment of the risks

- The dominant risk is not model accuracy but **the decoupling of gaze from intent** in
  patients with gaze palsy or neglect. Some patients will not be servable by any
  gaze-based system, and the system should be able to *detect and declare* that at
  calibration rather than silently produce noise.
- Second is the **absence of any clinical training or validation data**. Every headline
  number cited in this document comes from a healthy, mostly upright, mostly
  camera-facing population. Treat them as upper bounds.
- Third is **false activation cost asymmetry**: a spurious `MEDICINE` is far worse than a
  spurious `WATER`. Per-class thresholds and mandatory confirmation for high-stakes labels,
  not one global threshold.

---

*Content from external sources was rephrased and summarised for compliance with licensing
restrictions; all claims are linked to their original sources inline.*


---

## 11. Decision record — approach locked

**Decision:** Approach **B (3D gaze direction from a single RGB camera)** is locked as the
architecture. This section supersedes the recommendation in §7.

**Rejected, with reasons:**

| Option | Verdict | Reason |
|---|---|---|
| A. Zone classification | Deferred | Requires labelled data from the exact setup, which does not exist yet. Revisit as a per-site specialist model once a pilot dataset exists. |
| C. Scene heatmap | Fallback only | 2D heatmap cannot disambiguate objects at different depths; trained on annotator-inferred labels rather than instructed-target labels. *(An earlier objection — that it constrains camera placement by needing patient and objects co-framed — no longer applies: the camera is confirmed to cover both. C is therefore retained at zero extra cost as a no-calibration fallback and optional cross-check.)* |
| D. End-to-end GOP | Rejected | Retail-domain training data, heaviest to run, and re-detects objects every frame in a near-static scene. |
| E. VLM | Rejected as system, retained as tool | Weak spatial reasoning, unbounded latency, cloud privacy problem. Keep for offline auto-labelling of pilot recordings. |

**Split within Approach B.** The upstream half is fixed; the decision layer is swappable.

- *Upstream (fixed):* face/head detection → pretrained gaze regressor → `(pitch, yaw)` +
  head pose + per-eye agreement, as a feature vector.
- *Downstream (primary):* a **small per-patient classifier** fitted on ~60 s of guided
  calibration, mapping those features directly to labels. This removes 3D object positions,
  monocular depth, and camera intrinsics from the error chain entirely.
- *Downstream (secondary):* explicit **geometric ray–object intersection**, retained for
  clinician-facing explanation and for the setup-time separability advisory (how far apart
  objects must be placed given this patient's measured gaze error).

**Consequences accepted:**

- Gaze-angle accuracy on post-stroke faces is now the single load-bearing dependency.
  Prefer regressors trained/evaluated on **wide head-pose** data (Gaze360-style) over
  narrow-pose data (MPIIGaze-style), because bed-bound patients are reclined and off-axis.
- Per-patient calibration is **mandatory, not optional**. The system cannot run uncalibrated
  except in the degraded Option C fallback mode.
- Calibration must be repeatable and periodically refreshed, since post-stroke visual
  deficits are non-stationary.

**Model selection constraint (small-data regime).** Calibration yields on the order of
10²–10³ frames per class, heavily temporally correlated. The decision layer must therefore be
a **low-variance classifier** (LDA, Gaussian mixture, k-NN, or a shallow gradient-boosted
tree) — *not* a neural network. Model capacity here is a liability, not an asset.

**Temporal layer.** Use an HMM with high self-transition probability over the per-frame
posteriors. This yields dwell behaviour, temporal smoothing, and principled abstention from a
single mechanism, rather than three independent hand-tuned thresholds.


### 11.1 Amendment — patient-independent operation required

**New requirement:** the system must work for **any patient** without per-patient setup,
given the same room, camera and object layout. This supersedes the "per-patient calibration
is mandatory" consequence recorded above.

**Reasoning.** Two distinct things were being conflated under "calibration":

1. **Per-site geometry** — where the objects sit relative to the camera and the patient's
   head. Fixed for the installation, so it is calibrated **once, by staff or volunteers**,
   and reused for every patient. This is fully compatible with the new requirement: the
   patient does nothing.
2. **Per-person anatomy** — the offset between optical and visual axis (kappa angle, roughly
   4-5° and person-specific), plus eyelid and asymmetry effects. This is the part that
   genuinely cannot be known in advance for a new patient.

Only (2) is actually dropped. It is recovered two ways:

- **Angular separation substitutes for calibration.** Object spacing and calibration are
  interchangeable ways of buying the same margin. Removing per-patient calibration means the
  layout must absorb the residual error instead.
- **Implicit calibration from confirmations.** The two-step confirmation already required for
  Midas-touch safety produces a *labelled sample* every time the patient confirms a
  selection. The system therefore starts patient-independent and personalises itself silently
  during normal use, with no explicit calibration session.

**Error budget.** Wide-pose gaze regressors carry roughly 10° error; uncorrected per-person
offset adds ~5°. At a 60 cm viewing distance 1° ≈ 1.05 cm laterally, so the combined budget
is ~11-15 cm of lateral uncertainty. Reliable separation needs object spacing of roughly
2-3× the error → **~30-45° of angular separation, i.e. ~30-45 cm apart at 60 cm.**

**Consequence — this is the load-bearing finding.** Five objects on a single small bedside
table **cannot** be separated patient-independently. The layout must either spread the five
objects over a wide arc (~120-150° total), or reduce the object count, or adopt
**hierarchical selection** (choose a left/right group first, then the item within it), which
trades interaction time for angular precision.

**Consequences for the decision layer.** With calibration pooled across many people at a
fixed site rather than fitted to one patient, training data grows and a low-variance
classifier is no longer mandatory. Validation must become **leave-one-person-out**;
within-person splits are now meaningless. Accuracy will be lower than the per-patient
calibrated ceiling — this is the accepted price of the requirement.

**Note on Option C.** Patient-independence is the one axis on which the rejected scene-heatmap
approach is inherently strong, since it needs no calibration at all. It is therefore promoted
from "fallback" to **cold-start path and cross-check** for a newly admitted patient, before
any implicit calibration has accumulated. The depth-ambiguity and
annotator-versus-intent objections still bar it from being the primary path.

**Note on Option A.** A fixed installation plus pooled multi-patient data is precisely the
regime in which direct classification becomes viable. The long-term endpoint of this system is
likely a **per-site Option A model trained on pooled patients**, with Option B as the
bootstrap that generates the data and remains the interpretable cross-check.

**Hard limit that no approach removes.** "Works for any patient" cannot include patients with
gaze palsy, severe neglect, or a gaze range too restricted to reach the objects. For those
patients gaze and intent are decoupled at the physiological level. The system must **detect
and declare** this at admission rather than emit confident noise.


## 12. Target design — objects vs. symbol cards

### 12.1 What each approach requires of the targets

| Requirement | Option B (gaze angles) | Option C (scene heatmap) |
|---|---|---|
| Target position known | Yes (angular, per site) | Implicitly, via detection |
| Target visible to camera | **No** | **Yes** |
| Target visually distinctive | **No** — B never looks at the target | **Yes** |
| Minimum apparent size | Irrelevant | **Yes** — see resolution note |
| Separation metric that matters | **Angular**, from the patient's eyes (~30-45°) | **2D image-space**, in the camera projection |
| Depth-separated targets | Resolvable | **Not resolvable** |

**Resolution note.** Gaze-LLE emits a 64×64 heatmap from a 448×448 input, so one heatmap cell
covers ~7×7 input pixels. A medicine strip occupying ~30×15 px spans only ~4×2 cells —
structurally too coarse to separate from an adjacent item. Option C therefore cannot support
small targets, independent of how well it is trained.

### 12.2 Decision: use fixed symbol cards, not the physical objects

Physical bedside objects are a poor target set: transparent bottles are hard to detect against
linen, pill strips are too small for the heatmap resolution, and objects get moved, emptied or
removed — invalidating registration. More fundamentally, several of the highest-priority
patient needs **are not objects at all**.

Adopt a mounted board of large, high-contrast, matte symbol cards (~A5) at fixed angular
positions. This simultaneously resolves detectability, apparent size, angular separation,
target stability, and — critically — makes the **site calibration standardised and therefore
reusable across rooms and patients**, which is what makes the patient-independence requirement
in §11.1 achievable in practice.

*Counterpoint retained:* patients with aphasia or cognitive impairment may respond more
instinctively to a real object than to a pictogram. A hybrid (real object for the 1-2 most
concrete needs, cards for abstract needs) is acceptable and should be an evaluated variable,
not assumed.

### 12.3 Revised target vocabulary

The original set (`WATER`, `FOOD`, `MEDICINE`, `PHONE`, `CALLING_BELL`) has three clinical
problems: **TOILET is absent** despite being among the most frequent and dignity-critical
needs of a bed-bound patient; **MEDICINE is the wrong abstraction** — medication is
staff-scheduled rather than patient-requested, and a false `MEDICINE` is the highest-risk
misfire, so the patient's actual intent is better captured as `PAIN`; and several critical
needs (pain, toilet, repositioning, temperature) have no physical object to look at.

**v1 (4 targets, maximising angular separation):** `WATER/DRINK`, `TOILET`, `PAIN`,
`HELP/NURSE`.

**v2 (add once separability is demonstrated):** `FOOD`, `REPOSITION`, `FAMILY/PHONE`,
`TOO_HOT/TOO_COLD`.

**Safety constraint.** Post-stroke **dysphagia** is common, so a `WATER` output must never be
interpreted as an instruction to give fluids. Every output is a *communication act* routed to a
caregiver who checks the patient's diet plan — never an action. This applies to the whole
vocabulary and is the reason the system stays outside regulated-device territory.

### 12.4 Fusing B and C rather than choosing

B and C fail differently: B degrades measurably (angular margin narrows, enabling principled
abstention) while C fails confidently. Running both and feeding them as independent evidence
into the same temporal filter is affordable (distilled Gaze-LLE is 3.51 M parameters), and
**disagreement between the two becomes the strongest available abstention signal** — the
property that matters most for a safety-critical AAC device.

Primary/secondary assignment hinges on one question: *can a one-time site calibration be
performed with staff or healthy volunteers?* If yes, B is primary. If no, C is primary and
depth confusions plus coarse resolution are accepted.
