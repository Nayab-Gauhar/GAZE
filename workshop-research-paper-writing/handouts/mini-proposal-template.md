# Mini Research Proposal — Final Deliverable Template

**Integrity rules for this document**
- Every citation must be one **you have opened**. Every DOI must resolve at `doi.org`.
- Use `[TBD]` for any number you have not measured. **Never write a placeholder number.**
- Datasets must be real, with a stated licence and access route.
- Log where AI assisted and what you verified (§15).

---

## 1 · Title

| | Candidate | Notes |
|---|---|---|
| A | | |
| B | | |
| C | | |

**Selected:** ______________________________________________

- Contains searchable keywords of my field? ☐
- Names method + problem + domain? ☐
- 8–15 words, no dead words ("A Study of", "Novel", "Using", "Based on")? ☐
- Scholar test: pasting the title returns my intended peers? ☐

---

## 2 · Problem statement (3–5 sentences)

*What is the problem, who has it, and what is currently unsatisfactory. No literature review here.*

> ______________________________________________________________________

**4-part research-problem test**
☐ The answer is currently unknown in the literature
☐ It can be measured or proven
☐ A negative result would still be publishable
☐ It matters to someone outside my institution

---

## 3 · Research gap (4–6 sentences)

*Use the template. Include counts from your literature matrix.*

> "Across **[N]** studies identified by **[databases, strings, dates]**, **[pattern with counts]** holds. Consequently, **[quantity/mechanism]** remains **[unquantified/untested/unexplained]**, even though **[why it matters]**. This study addresses that by **[action]**."

**My gap:**

> ______________________________________________________________________

**Gap type(s):** ______________________  **Closest existing paper, and how mine differs:** ______________________

---

## 4 · Aim, objectives, hypotheses

**Aim (exactly one sentence):**
> To ______________________________________________________________________

**Objectives** — each "To + measurable verb + object + condition"; each must be markable done/not-done.

| | Objective | Measurable outcome | Maps to contribution |
|---|---|---|---|
| O1 | | | |
| O2 | | | |
| O3 | | | |
| O4 | | | |

**Research questions**

| | Question |
|---|---|
| RQ1 | |
| RQ2 | |
| RQ3 | |

**Hypotheses** — falsifiable, pre-specified, with the test named **before** seeing results.

| | H0 | H1 | Test | α | Multiple-comparison correction |
|---|---|---|---|---|---|
| H1 | | | | | |
| H2 | | | | | |

---

## 5 · Proposed methodology (≈1 page)

**Pipeline:**
`Data → Preprocessing → Feature extraction → Model → Training → Validation → Testing → Evaluation`

- Overview paragraph (5–7 sentences, one per block):
- Formal problem statement (notation, inputs, outputs, objective):
- The **novel component**, isolated:
- **Why it should work** (mechanism hypothesis — this sentence separates research from engineering):
- Extra cost relative to the baseline (params / FLOPs / latency):

**Attach:**
☐ System architecture diagram (vector: SVG/PDF; novel block highlighted; arrows labelled with what flows)
☐ Algorithm 1 pseudocode (10–15 lines; novel lines marked; complexity stated)
☐ Loss function / mathematical formulation with every symbol defined

---

## 6 · Datasets

| Dataset | Version | Size | Classes | Class balance | Split protocol | **Split unit** | Public? | Licence / DUA | Ethics needed? |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |

☐ Leakage statement drafted: *"All preprocessing statistics, resampling and feature selection are fitted on training folds only. Splits are ______-disjoint."*
☐ Licences permit my intended use and any redistribution of splits
☐ Ethics/IRB route identified (or explicit statement that approval is not required, and why)

---

## 7 · Baseline methods (minimum 4)

| Baseline | Category | Repository / source | Runs successfully? | Tuning budget (equal to mine?) |
|---|---|---|---|---|
| | trivial / majority | — | — | — |
| | strong classical | | ☐ | ☐ |
| | current SOTA | | ☐ | ☐ |
| | **mine minus its novelty** | — | ☐ | ☐ |
| | oracle / upper bound (optional but powerful) | | ☐ | ☐ |

☐ Identical splits, preprocessing and augmentation for all methods
☐ Identical hyperparameter search space size and trial budget, and I will **state** it

---

## 8 · Evaluation metrics

| Metric | Why this metric — tied to the decision the model supports | Primary or secondary |
|---|---|---|
| | | |
| | | |
| | | |
| Cost: params / FLOPs / latency / memory | Deployment claim requires it | secondary |

☐ Metric choice justified in one sentence in the paper (pre-empts a whole class of reviewer objection)
☐ Confusion matrix / error breakdown planned
☐ Subgroup (worst-group) reporting planned
☐ Calibration reported if probabilities inform decisions
☐ ≥5 seeds (10 preferred), mean ± CI, paired significance test named

---

## 9 · Expected contributions (calibrated — no "state of the art")

| | Contribution | Type | Maps to objective | Evidence that will support it |
|---|---|---|---|---|
| C1 | | | | |
| C2 | | | | |
| C3 | | | | |

**Traceability audit** — every row must be complete:

| Objective | Method | Results subsection | Contribution |
|---|---|---|---|
| O1 | | §V-A | C1 |
| O2 | | §V-B | C2 |
| O3 | | §V-C | C3 |

---

## 10 · Target journals

| | Journal | Publisher | Index | Quartile (source + category) | APC | Time to decision | Decision |
|---|---|---|---|---|---|---|---|
| Target | | | | | | | |
| Backup 1 | | | | | | | |
| Backup 2 | | | | | | | |

☐ Verification sequence completed for all three (`journal-selection-checklist.md`, Part A)
☐ Scope phrase quoted for the target
☐ ≥3 papers I cite are published in the target
☐ Accepted by my university's degree regulations
☐ Formatting for the target from the first draft

---

## 11 · Initial abstract (200–300 words, seven moves)

Label each sentence with its move number while drafting, then remove the labels.

| Move | | Present? |
|---|---|---|
| 1 | Background | ☐ |
| 2 | Problem / gap (with a number if possible) | ☐ |
| 3 | Objective / approach | ☐ |
| 4 | Method mechanism | ☐ |
| 5 | Data / experiment (datasets named, baselines named) | ☐ |
| 6 | Results (numbers with comparison point + variance, or `[TBD]`) | ☐ |
| 7 | Conclusion / implication with scope | ☐ |

> ______________________________________________________________________
> ______________________________________________________________________

**Word count:** ______  ☐ No citations ☐ No undefined acronyms ☐ No figure/section references ☐ Every number matches (or is `[TBD]`)

---

## 12 · Introduction outline (six paragraphs)

| ¶ | Job (≤6 words) | Key content | Citations to use |
|---|---|---|---|
| 1 | Background / stakes | | |
| 2 | Existing problem | | |
| 3 | Existing approaches (2–3 grouped families) | | |
| 4 | **Limitations → gap (the hinge)** | counts: | |
| 5 | Proposed approach + why it should work | | |
| 6 | Numbered contributions + roadmap | | |

☐ Reverse-outline test passed: no two paragraphs share a job; no job is missing
☐ ¶4 contains at least one count from my matrix
☐ ¶6 contributions match §9 above **and** the abstract

---

## 13 · Literature matrix

☐ Attached as a spreadsheet, ≥10 rows × 15 columns
☐ Split protocol recorded for every row
☐ My own critique in the Limitations_Mine column for every row
☐ Every cell verified against the PDF (including any AI pre-filled cells)
☐ Column tallies computed
☐ Five tally sentences written

---

## 14 · References (≥15, IEEE style)

☐ Numbered in order of first appearance
☐ Every in-text citation present in the list, and vice versa
☐ **Every DOI resolved at doi.org** and metadata checked against the publisher record
☐ Consistent author formats, journal abbreviations, capitalisation
☐ Preprints labelled as preprints; published versions used where they exist
☐ Retraction check done for load-bearing references
☐ Foundational works cited, not only the last four years
☐ **Every reference has actually been read**

---

## 15 · AI-assistance and declarations log

| Task | Tool used | What I verified, and how |
|---|---|---|
| | | |

**Draft declarations block**

| Declaration | Text |
|---|---|
| Author contributions (CRediT roles) | |
| Ethics approval | |
| Informed consent | |
| Conflict of interest | |
| Funding | |
| Data availability | |
| Code availability | |
| AI use | |
| Prior presentation / conference extension | |

---

## 16 · Risks and next 12 weeks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| | | | |

| Week | Action |
|---|---|
| 1 | Set 3 literature alerts; fix all Zotero metadata |
| 2 | Grow matrix to 25 rows; recompute tallies |
| 3 | Rewrite gap; stress-test with supervisor |
| 4 | Freeze objectives and hypotheses |
| 5–6 | Reproduce one baseline end-to-end; document discrepancies |
| 7–8 | Build pipeline; fix seeds, configs, logging |
| 9–10 | Full experiments: equal budgets, ≥5 seeds, ablations |
| 11 | Build all figures and tables first |
| 12 | Draft in writing order; similarity check; verify every DOI |
