# Paper Extraction Template

Fill **one copy per paper** during Pass 2 (comprehension reading, 45–60 min). One filled template = one row of your literature matrix = the raw material for your Related Work section.

Save as `<CitationKey>.md` in a single folder, e.g. `Wang2023DenseCXR.md`.

---

## 0 · Identification

| Field | Value |
|---|---|
| Citation key | |
| Full citation (IEEE style) | |
| DOI (verified at doi.org? ☐) | |
| Venue | |
| Venue type | ☐ journal ☐ conference ☐ preprint ☐ workshop ☐ thesis |
| Indexed in | ☐ SCIE ☐ SSCI ☐ ESCI ☐ Scopus ☐ neither ☐ unknown |
| Year | |
| Citations (count / source / date checked) | |
| Code available? | ☐ yes (URL: ) ☐ on request ☐ no |
| Data available? | ☐ public ☐ restricted (DUA) ☐ private ☐ not stated |
| Reading passes done | ☐ Pass 1 ☐ Pass 2 ☐ Pass 3 |

---

## 1 · Research problem
*The unknown they address — in **your** words, not their abstract's words.*

## 2 · Motivation
*Why it matters. Application driver, theoretical puzzle, or both.*

## 3 · Stated objective / research question
*Quote or closely paraphrase their explicit aim.*

## 4 · Claimed research gap
*What they say prior work lacked. Note whether they give evidence for the claim or merely assert it.*

## 5 · Dataset(s)

| Dataset | Version | Size | Classes / labels | Split protocol | Split **unit** | Public? | Licence |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

- Class balance / imbalance ratio:
- Any leakage risk you can detect (unit of splitting vs grouped data):

## 6 · Preprocessing
*Resizing, normalisation (and **where the statistics were fitted**), cleaning, deduplication, tokenisation, augmentation, resampling (and whether **before or after** the split).*

## 7 · Proposed method

- One-sentence description:
- The component that is genuinely **new** (isolate it):
- What is inherited from prior work (and from which paper):
- Stated mechanism / reason it should work:
- Complexity or cost relative to the baseline:

## 8 · Baselines

| Baseline | From official code? | Tuned equally? | Notes |
|---|---|---|---|
| | | | |

- Number of baselines: ____
- Is a trivial/majority baseline included? ☐
- Is a strong classical baseline included? ☐
- Is "their method minus its novelty" included? ☐

## 9 · Evaluation metrics

| Metric | Appropriate for this problem? | Why / why not |
|---|---|---|
| | | |

- Metrics that should have been reported but were not:

## 10 · Experimental setup

| Item | Value |
|---|---|
| Seeds / repetitions | |
| Variance reported (std / CI / none) | |
| Statistical test used | |
| Cross-validation scheme | |
| Optimiser, LR, schedule, batch size, epochs | |
| Early-stopping signal (validation or test?) | |
| Hyperparameter search: space, method, **budget** | |
| Hardware | |
| Framework + versions | |
| Cost reported (params / FLOPs / latency / memory / train time) | |

## 11 · Key results
*2–3 numbers, each **with its comparison point**. Copy from the table, not the abstract, then check that the abstract agrees.*

| Claim | Number | Compared against | Table/Fig. | Variance | Significant? |
|---|---|---|---|---|---|
| | | | | | |

- Do abstract numbers match the results tables? ☐ yes ☐ no (note the discrepancy)
- Are all datasets/metrics mentioned in the setup also reported in the results? ☐ yes ☐ no

## 12 · Limitations — **theirs**
*Quote verbatim, with section and page. These quotes become citations in your gap paragraph.*

> "…" (§__, p. __)

## 13 · Limitations — **yours** (independent critique)
*Mandatory. A template with only the authors' self-assessment reproduces their framing.*

- Fairness of comparison:
- Statistical validity:
- Evaluation protocol / leakage:
- Generality (populations, domains, scale):
- Cost and deployability:
- Reproducibility:
- Explanation (do they show *why* it works?):
- Anything selectively reported:

## 14 · Future work + opportunity for me

- Their stated future work (verbatim):
- **My one-line opportunity:**
- Candidate gap type(s): ☐ knowledge ☐ methodological ☐ dataset ☐ performance ☐ application ☐ population/domain ☐ evaluation ☐ scalability ☐ generalisation ☐ reproducibility ☐ efficiency ☐ explainability

---

## 15 · Relevance decision

☐ **Core** — will be a baseline or a direct comparison
☐ **Context** — cite only, for definitions/statistics/background
☐ **Discard** — reason: ____________________

**Contradicts which other paper in my set?** ____________ *(contradictions are the richest gap signal — flag them)*

---

## AI-assistance log (for your own honesty trail)

| Field pre-filled by a tool | Tool | Verified against the PDF? | Corrections I made |
|---|---|---|---|
| | | ☐ | |

> Fields 1, 4, 13 and 14 must be **yours**. Field 11 must always be checked against the actual table.
