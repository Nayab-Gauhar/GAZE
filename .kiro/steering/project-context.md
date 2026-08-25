# Project context — multimodal assistive communication for post-stroke patients

**Purpose: research prototype.** Not a clinical deployment. Optimise for
publishable rigour — proper baselines, honest evaluation, reproducibility — not
for regulatory readiness.

## System architecture

```
                POST-STROKE PATIENT
                        │
               ┌────────┴────────┐
               ▼                 ▼
             CAMERA          MICROPHONE
               │                 │
               ▼                 ▼
         Vision Model       Speech Model
               │                 │
               ▼                 ▼
         Visual Target       Speech Meaning
               │                 │
               └────────┬────────┘
                        ▼
                  Fusion Layer
                        │
                        ▼
             Communication Intent
                        │
                        ▼
                   Caregiver
```

## The central design principle

**Vision and speech occupy different label spaces and must not be forced to agree.**

- **Vision** answers: *which physical object or target is the patient looking at?*
- **Speech** answers: *what is the patient saying, requesting, or experiencing?*

Do **not** assume vision should predict every speech class. Do **not** assume
intent can be read from gaze alone — gaze yields *attention*, and intent is only
recovered after fusion, dwell, and caregiver confirmation.

Fusion therefore needs a **compatibility mapping** between two different label
sets, not an argmax-agreement check.

```
Vision → WATER      Speech → THANNI        Final → Wants water
Vision → MEDICINE   Speech → MARUNDHU      Final → Wants medicine
Vision → FAN        Speech → FAN_PODU      Final → Turn on fan
Vision → BODY/ARM   Speech → VALIKUDHU     Final → Pain in arm
```

## Vision targets (current priority)

`WATER`, `MEDICINE`, `FOOD`, `PHONE`, `CALLING_BELL`, `TISSUE`, `NONE/UNCERTAIN`

The worked examples also imply two target families beyond that list, which the
vision component will need if those fusion cases are to work:

- **Appliances:** `FAN`, `TV`
- **Own body parts:** `BODY/ARM` etc., for pain localisation. Note this is a
  *different CV problem* from detecting objects on a table — the patient looks at
  their own body, so body parts must NOT be blocklisted as targets in that mode.

## Speech targets

Tamil, limited vocabulary, **dysarthric** speech (expect severe data scarcity):

`THANNI` (water), `SAAPADU` (food), `MARUNDHU` (medicine), `THAAGAM` (thirsty),
`PASIKKUDHU` (hungry), `VALIKUDHU` (pain), `THOOKKAM` (sleepy),
`REST_EDUKKANUM` (need rest), `PADUKKANUM` (need to lie down), `HELP`,
`FAN_PODU` (turn on fan), `TV_PODU` (turn on TV), `PAKKATHULA_VAA` (come near),
`NIRUTHUNGA` (stop), `NONE/UNKNOWN`

**Speech-only classes** — no meaningful visual target, must come from audio:
`THAAGAM`, `PASIKKUDHU`, `THOOKKAM`, `VALIKUDHU`, `DIZZINESS`,
`BREATHING_DIFFICULTY`

## Current scope

Vision component first: compare approaches, collect a dataset, evaluate properly.
Speech and fusion come later.

## Implications for how to help

- Prefer evaluation rigour over feature count. Leave-one-subject-out splits,
  confusion matrices, per-class metrics, honest baselines.
- Never split by frame — frames within one dwell are near-identical and inflate
  results. Split by subject and session.
- Measure idle/unprompted periods too, or false-activation rates are unknown.
- Keep clinical-safety notes as *paper limitations*, not blocking requirements.
- Flag conflicts between the stated target list and measured system capability
  rather than quietly accommodating them.
