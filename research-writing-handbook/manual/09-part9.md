# PART IX — EVALUATION AND RESULTS

<div class="partintro">

Part IX concerns measurement and its honest presentation. Chapter 27 treats evaluation metrics in depth — formula, meaning, interpretation, appropriate use, limitations, and worked example for each. Chapter 28 covers results presentation and the specific ways visualisations mislead. Chapter 29 draws the boundary between Results and Discussion, the most frequently violated structural convention in scientific writing.

The theme: **a metric is a claim about what matters.** Choosing accuracy for a rare-disease detector is not a technical shortcut but a substantive assertion that false negatives and false positives are equally costly — an assertion that is usually false and almost never defended.

</div>

<div class="pagebreak"></div>

# Chapter 27 — Evaluation Metrics

## 27.1 The principle of metric selection

**Definition.** An evaluation metric is a function mapping predictions and ground truth to a scalar summarising performance along one dimension.

**The principle.** Choose metrics from the **decision the model supports**, not from convention or convenience. Then justify the choice in one sentence in the paper. That sentence — *"because prevalence is 1.2%, we report average precision and recall at fixed specificity rather than accuracy"* — pre-empts an entire class of reviewer objection and takes ten seconds to write.

## 27.2 The confusion matrix and its family

Nearly all classification metrics derive from four counts.

**Figure 27.1 — The confusion matrix and the metrics derived from it**

```
                          PREDICTED
                    Positive      Negative
                 ┌────────────┬────────────┐
          Pos    │     TP     │     FN     │  → Recall = TP/(TP+FN)
  ACTUAL         │            │            │    (sensitivity, TPR)
          Neg    │     FP     │     TN     │  → Specificity = TN/(TN+FP)
                 └────────────┴────────────┘
                        │
                  Precision =
                  TP/(TP+FP)

  Accuracy         = (TP + TN) / (TP + TN + FP + FN)
  F1               = 2·Precision·Recall / (Precision + Recall)
  Balanced accuracy= (Recall + Specificity) / 2
  FPR              = FP / (FP + TN)  =  1 − Specificity
```

**Always report the confusion matrix itself.** A single scalar tells you how much error there is; the matrix tells you *which* errors occur, and that is what determines whether the model is usable.

## 27.3 Classification metrics in detail

**Table 27.1 — Classification metrics: use and misuse**

| Metric | Formula | Meaning | Use when | Do not use when | Worked example *[HYPOTHETICAL]* |
|---|---|---|---|---|---|
| **Accuracy** | `(TP+TN)/N` | Proportion correct | Balanced classes; symmetric error costs | **Imbalanced data** | 1,000 patients, 10 positive. Predict all negative → accuracy 99.0%, recall 0. Useless model, excellent accuracy |
| **Precision** | `TP/(TP+FP)` | Of flagged cases, how many are real | False positives are costly (referral, spam) | Alone — maximised by predicting almost nothing | Flag 5 cases, 4 correct → precision 0.80, but 6 of 10 cases missed |
| **Recall** (sensitivity, TPR) | `TP/(TP+FN)` | Of real cases, how many were found | Missing a case is costly (cancer, fraud, safety) | Alone — maximised by predicting everything positive | Flag all 1,000 → recall 1.00, precision 0.01 |
| **Specificity** (TNR) | `TN/(TN+FP)` | Of negatives, how many correctly cleared | Screening; always paired with sensitivity | Alone | Sensitivity 0.90 at specificity 0.95 is an interpretable operating point |
| **F1** | `2PR/(P+R)` | Harmonic mean of precision and recall | One number needed under imbalance | Error costs are asymmetric — use Fβ | P = 0.80, R = 0.40 → F1 = 0.53 (the harmonic mean punishes imbalance between them) |
| **Fβ** | `(1+β²)PR/(β²P+R)` | Weighted harmonic mean | β > 1 favours recall; β < 1 favours precision | Without justifying β | F2 = 0.44 for the same values — recall weighted more heavily |
| **Balanced accuracy** | `(TPR+TNR)/2` | Mean of per-class recall | Imbalance; interpretable to non-specialists | When per-class detail matters | The all-negative predictor scores 0.50, correctly exposing it |
| **MCC** | correlation of predicted and actual, from all four cells | Single number using the whole matrix | Imbalance; a stricter summary than F1 | When stakeholders cannot interpret it | The all-negative predictor scores 0 (Chicco and Jurman, 2020) |
| **Cohen's κ** | agreement corrected for chance | Agreement beyond chance | Inter-rater agreement; imbalanced classification | Across datasets with differing prevalence | κ = 0.81 indicates substantial annotator agreement |
| **ROC-AUC** | area under TPR vs FPR | Probability a random positive is ranked above a random negative | Threshold-free ranking quality; moderate imbalance | **Severe imbalance** — a large TN pool makes it look optimistic | AUC 0.90 can coexist with precision 0.10 at 1% prevalence |
| **PR-AUC / average precision** | area under precision vs recall | Ranking quality focused on the positive class | **Rare positives**: anomaly, rare disease, retrieval | Comparing across datasets with different prevalence — the baseline shifts | With 1% prevalence, a random ranker has PR-AUC ≈ 0.01 and ROC-AUC ≈ 0.50 |
| **Top-*k* accuracy** | correct if truth is in top *k* | Ranked-output tolerance | Many classes; ranked suggestions acceptable | Binary or decision-critical tasks | Top-5 accuracy 0.95 with top-1 0.72 |
| **Calibration: ECE, Brier** | binned gap between confidence and accuracy; mean squared probability error | Are the probabilities trustworthy? | Probabilities inform decisions or thresholds | — (under-reported; reporting it distinguishes your paper) | ECE 0.09 means predicted confidence is off by ~9 points on average (Guo et al., 2017) |

### 27.3.1 ROC versus precision–recall: the mechanism

This distinction is the most consequential in the chapter and is worth understanding mechanically rather than as a rule.

**Figure 27.2 — ROC versus precision–recall under class imbalance**

```
  Scenario: 10,000 samples, 100 positive (1% prevalence).
  A model flags 200 samples; 80 are true positives.

  TP = 80    FP = 120    FN = 20    TN = 9,780

  ROC axis:  FPR = FP/(FP+TN) = 120/9,900 = 0.012      ← barely moves!
             TPR = 80/100     = 0.80
             → looks excellent

  PR axis:   Precision = TP/(TP+FP) = 80/200 = 0.40    ← exposes the problem
             Recall    = 0.80
             → 60% of alerts are false alarms

  WHY: FPR has the huge TN pool in its denominator, so hundreds of false
  positives hardly register. Precision has only TP in its denominator
  alongside FP, so the same errors are fully visible.

  RULE: under severe imbalance, prefer PR-AUC / average precision.
  CAVEAT: the PR-AUC of a random ranker equals the positive prevalence,
  so PR-AUC is NOT comparable across datasets with different prevalence.
```

This behaviour is documented in the methodological literature; Saito and Rehmsmeier (2015) give a detailed treatment for imbalanced biological data.

### 27.3.2 Multi-class and multi-label reporting

For multi-class problems, report **per-class** precision, recall, and F1 alongside a **macro** average. Macro averaging weights every class equally and therefore exposes failure on rare classes; micro averaging weights by frequency and therefore conceals it. Reporting only a micro average on imbalanced data is a common way to hide the clinically or practically important failures.

For **multi-label** problems — where each instance may carry several labels — report per-label AUC and average precision plus the macro average. A single global accuracy over a multi-label problem is close to meaningless, because it is dominated by the prevalent labels.

## 27.4 Regression metrics

**Table 27.2 — Regression metrics: use and misuse**

| Metric | Formula | Meaning | Use when | Do not use when | Note |
|---|---|---|---|---|---|
| **MAE** | `mean(|y − ŷ|)` | Average absolute error, in target units | Robust, directly interpretable | You need to penalise large errors more | Optimises toward the conditional median |
| **MSE** | `mean((y − ŷ)²)` | Average squared error | Large errors matter disproportionately | Heavy outliers dominate | Units are squared, so hard to interpret |
| **RMSE** | `sqrt(MSE)` | Root mean squared error, in target units | Large errors matter; interpretable units wanted | Outlier-heavy data | Always ≥ MAE; the gap indicates error-variance spread |
| **R²** | `1 − SS_res/SS_tot` | Proportion of variance explained | Familiar; linear-model contexts | **Comparing across datasets with different target variance**; non-linear or heteroscedastic fits | Can be negative; is *not* "accuracy" |
| **MAPE** | `mean(|y−ŷ|/|y|)·100` | Mean absolute percentage error | Relative error; business reporting | Targets near or equal to **zero**; asymmetric penalty | Penalises over-prediction and under-prediction unequally |
| **MedAE / Huber** | median absolute error; hybrid loss | Outlier-robust error | Outlier-heavy data | — | Huber transitions from squared to absolute |
| **RMSLE** | RMSE of log1p values | Error on a multiplicative scale | Targets spanning orders of magnitude | Negative targets | Penalises under-prediction more |

**Two cautions.** R² is routinely misreported as though it were accuracy; it is not, it can be negative, and it is not comparable across datasets whose targets have different variance. And whichever metric you report, **plot residuals against predictions**: a good RMSE with structured residuals indicates a mis-specified model, and the scalar alone will never reveal it.

## 27.5 Object detection and segmentation

**Table 27.3 — Detection and segmentation metrics**

| Metric | Formula | Meaning | Notes and pitfalls |
|---|---|---|---|
| **IoU** (Jaccard) | `|A∩B| / |A∪B|` | Overlap between predicted and true region | The threshold that decides whether a detection counts as correct |
| **Precision / recall at IoU τ** | as §27.2, with correctness defined by IoU ≥ τ | Detection quality at one strictness level | **Always state τ** |
| **AP** | area under the precision–recall curve for one class | Single-class detection quality | Interpolation convention varies between benchmarks |
| **mAP** | mean AP over classes | Overall detection quality | `mAP@0.5` and `mAP@[.5:.95]` are different numbers — often by 15–20 points. Quoting one against the other is a real and common error |
| **AR** | average recall over IoU thresholds | Coverage | Report with a small/medium/large size breakdown where the benchmark provides it |
| **Dice** (F1 per pixel) | `2|A∩B| / (|A|+|B|)` | Overlap, weighted toward agreement | Standard in medical imaging; sensitive on small structures |
| **Dice ↔ IoU** | `Dice = 2·IoU/(1+IoU)` | Monotonic relation | Dice is always ≥ IoU for the same overlap; never compare one against the other |
| **mIoU** | mean IoU over classes | Semantic segmentation standard | Report per class as well as the mean |
| **Pixel accuracy** | correct pixels / total | Proportion of pixels correct | **Usually misleading** — background is often more than 95% of pixels |
| **Hausdorff distance / ASSD** | boundary distance measures | Boundary accuracy | Essential where shape or margin matters, e.g. surgical planning |

**Two rules.** `mAP` without a stated IoU threshold and non-maximum-suppression settings is not comparable to anything. And pixel accuracy on data with dominant background is a vanity metric; report per-class Dice or IoU plus a boundary metric when shape matters.

## 27.6 Metric selection by situation

**Table 27.4 — Metric selection by problem situation**

| Situation | Report these | Explicitly avoid |
|---|---|---|
| Binary, balanced | Accuracy, F1, ROC-AUC, confusion matrix | — |
| Binary, severe imbalance (<5% positive) | PR-AUC / AP, recall at fixed precision, F2, MCC, confusion matrix | Accuracy alone; ROC-AUC alone |
| Multi-class, imbalanced | Per-class P/R/F1, **macro** F1, confusion matrix, MCC | Micro average alone |
| Multi-label | Per-label AUC **and** AP, macro average | A single global accuracy |
| Screening / triage | Sensitivity at fixed specificity (or the converse), PR curve, calibration | A single operating point with no curve |
| Cost-sensitive | Expected cost, cost curves, decision-curve analysis | Symmetric metrics |
| Ranking / retrieval / recommendation | nDCG@k, MRR, MAP@k, Recall@k, coverage | Accuracy |
| Probabilistic forecasting | Brier score, ECE, reliability diagram, log loss | Hard-label accuracy alone |
| Text generation | Task-specific automatic metrics **plus human evaluation with inter-rater agreement** | Automatic overlap metrics alone as a quality claim |
| Deployment-constrained | The accuracy metric **plus** latency, memory, energy, parameters | Accuracy alone |
| **Any comparison claim** | Mean ± CI over ≥5 seeds **and** a paired statistical test | A single-run point estimate |

## 27.7 A note for non-computational disciplines

The logic transfers directly even though the instruments differ. Where this chapter says *metric*, read *measure*; the requirement that the measure match the decision and the data structure is identical. The corresponding apparatus includes reliability (internal consistency, intraclass correlation), agreement (Cohen's or Fleiss' kappa), validity (construct, content, criterion), effect sizes (standardised mean differences, variance-explained measures), and, for qualitative work, trustworthiness criteria and saturation. The failure modes are also analogous: using a measure because it is conventional rather than because it captures the construct, and reporting a point estimate without any indication of precision.

## 27.8 Common mistakes

| Mistake | Correction |
|---|---|
| Accuracy on imbalanced data | Use PR-AUC, macro F1, MCC; always show the confusion matrix |
| ROC-AUC alone under severe imbalance | Add PR-AUC; understand the mechanism (§27.3.1) |
| Comparing PR-AUC across datasets with different prevalence | Not comparable; the baseline differs |
| Reporting R² as accuracy | Report MAE and RMSE in target units alongside |
| MAPE with near-zero targets | Use MAE, MedAE, or a scaled alternative |
| `mAP` without IoU threshold and NMS settings | State both |
| Comparing Dice against IoU | Convert or report both |
| Pixel accuracy on background-dominated data | Per-class Dice or IoU plus a boundary metric |
| Micro average only on imbalanced multi-class | Add macro and per-class |
| Automatic generation metrics as a quality claim | Add human evaluation with agreement statistics |
| No calibration reported where probabilities drive decisions | Report ECE or Brier and a reliability diagram |
| Four decimal places from one seed | Mean ± CI over ≥5 seeds |
| No justification sentence for the metric choice | Add it; it costs one sentence |

## Exercises

**Exercise 27.1** Compute the §27.3.1 example by hand for your own class prevalence. If your positive class is below 5%, check whether your current headline metric conceals your error profile.

**Exercise 27.2** Write your metric set with a one-sentence justification per metric, tied to the decision the model supports.

**Exercise 27.3** For each metric, write the sentence a reviewer would use to attack it. Then decide whether to change the metric or defend it in the paper.

**Exercise 27.4** Identify the subgroup on which your model performs worst, and decide whether the paper will report it. (It should.)

<div class="pagebreak"></div>

# Chapter 28 — Results Presentation

## 28.1 Purpose and the reading order of a reviewer

A reviewer typically reads the abstract, then the figures and tables, then decides how sceptically to read the prose. Your floats are therefore not illustrations of the argument — for many readers they *are* the argument.

**Recommendation.** Before writing prose, list the figures and tables the paper needs. A typical empirical paper has six to eight:

```
  Fig. 1   System overview (novel component highlighted)
  Table I  Dataset statistics (size, classes, balance, split unit, licence)
  Table II Main comparison against baselines, with dispersion and significance
  Fig. 2   The key effect (e.g. degradation under protocol change)
  Table III Ablation study, one factor per row, with an oracle row
  Fig. 3   Error analysis or qualitative failure cases
  Table IV Cost: parameters, FLOPs, latency, memory
  Fig. 4   Sensitivity to the principal hyperparameter
```

If you cannot produce this list, you are not ready to write — you are still doing experiments. If the list contains no baseline comparison, no ablation, and no cost table, the paper will struggle regardless of how well it is written.

## 28.2 Choosing the right display

| Display | Use for | Avoid when |
|---|---|---|
| **Table** | Precise values; many conditions; anything readers will quote | Showing a trend — use a line plot |
| **Line plot** | A metric varying over a continuous variable (epochs, λ, sequence length) | Categories with no ordering |
| **Bar chart** | Comparing a few discrete categories | Many categories, or an implied continuum |
| **Box or violin plot** | Distributions across seeds or folds | Fewer than about five observations |
| **Scatter plot** | Relationships; trade-offs such as accuracy against latency | Heavy overplotting without transparency or binning |
| **Confusion matrix heat map** | Which errors occur | More than roughly 20 classes without aggregation |
| **ROC curve** | Threshold-free ranking, balanced data | Severe imbalance — add a PR curve |
| **Precision–recall curve** | Rare positives | Cross-dataset comparison at differing prevalence |
| **Reliability diagram** | Calibration | — |
| **Training curves** | Convergence behaviour; over-fitting evidence | As a substitute for test performance |
| **Critical-difference diagram** | Many methods across many datasets | Two methods only |

## 28.3 How visualisations mislead

Most misleading figures are produced without any intention to mislead. Knowing the failure modes is the defence.

**Figure 28.1 — Misleading and honest presentations of the same result**

```
  ❌ TRUNCATED AXIS                         ✅ FULL OR ANNOTATED AXIS
     0.86 ┤       ▇                            1.0 ┤
     0.85 ┤   ▇   ▇                                │   ▇▇▇  ▇▇▇  ▇▇▇
     0.84 ┤   ▇   ▇                            0.5 ┤   ▇▇▇  ▇▇▇  ▇▇▇
     0.83 ┤▇  ▇   ▇                                │   ▇▇▇  ▇▇▇  ▇▇▇
          └──A───B───C                          0.0 └───A────B────C
     "C is twice as good as A"                  0.831  0.848  0.862
     — the visual gap is an artifact            The real difference: 0.031
     of the axis, not the data.                 Now the reader judges it.

  OTHER FAILURE MODES
  ① No error bars → the reader cannot tell whether the difference is noise.
  ② Error bars whose definition is unstated (std? SEM? 95% CI?) — these
     differ by large factors and are not interchangeable.
  ③ Dual y-axes → any desired correlation can be manufactured by rescaling.
  ④ Cherry-picked subset of datasets or metrics shown in the figure.
  ⑤ Colour as the only channel → illegible to colourblind readers and in
     greyscale print.
  ⑥ 3-D bars and perspective → distort area and hide values.
  ⑦ Connecting unordered categories with a line → implies a trend.
  ⑧ Different y-scales across panels compared side by side.
  ⑨ Log axis unlabelled as such.
```

**The single most important rule: put dispersion on every mean.** A bar chart of means without error bars is uninterpretable, and a reader is entitled to assume the omission is convenient.

## 28.4 Table construction

| Rule | Detail |
|---|---|
| **Horizontal rules only** | Top, header, bottom. No vertical rules, no full grid |
| **Bold the best per column** | And state in the caption what bold denotes |
| **Uniform decimal places** | Two or three; aligned on the decimal point |
| **Include dispersion** | `0.822 ± 0.009`, with the definition given in the caption |
| **Mark significance** | A symbol with its meaning stated (`*p < 0.05`, Holm-corrected) |
| **Group rows meaningfully** | Trivial baselines → classical → prior state of the art → ours → oracle |
| **Include cost columns** | Parameters, FLOPs, latency in the main comparison table |
| **Delete unused columns** | If a column is never discussed, it is noise |
| **Never screenshot** | Typeset tables as tables |

## 28.5 Captions, numbering, and cross-referencing

- **Figure captions below the figure; table captions above the table** — the standard convention in IEEE and most engineering styles. **[VERIFY]** against your target journal's guide.
- **Captions must be self-contained.** A reader who reads only figures and captions should understand what is shown, on what data, and what to notice. Name the dispersion measure and the number of runs in the caption.
- **Number in order of first mention**, and mention every float in the text. An unreferenced float will be queried.
- Use the journal's abbreviation conventions consistently (for example "Fig. 3" mid-sentence, "Figure 3" at the start of a sentence; tables often numbered in roman numerals).
- **Place floats near their first mention.**

## 28.6 Common mistakes

| Mistake | Correction |
|---|---|
| Means with no error bars | Add dispersion to every mean |
| Dispersion measure unstated | Define it in the caption |
| Truncated axes exaggerating differences | Start at zero or annotate the truncation explicitly |
| Dual y-axes | Use two panels |
| Colour as the sole distinguishing channel | Add markers and line styles; use a colourblind-safe palette |
| Screenshots of plots or notebook output | Export vector graphics (PDF, SVG, EPS) |
| Unreadable font after scaling to column width | Set font sizes explicitly; check at final print size |
| Captions that merely name the figure | Make them self-contained and say what to notice |
| Tables with vertical rules and full grids | Booktabs style: horizontal rules only |
| A float never mentioned in the text | Reference it or remove it |
| Only favourable datasets plotted | Show all, or state clearly which are omitted and why |

## Exercises

**Exercise 28.1** Write your figure and table list before writing any prose. Check it contains a baseline comparison, an ablation, an error analysis, and a cost table.

**Exercise 28.2** Take one existing figure of yours and fix three things: font size, error bars with a stated definition, and vector export.

**Exercise 28.3** Read one of your captions aloud to a colleague and ask what they should notice. If they cannot say, rewrite the caption.

**Exercise 28.4** Audit your figures against all nine failure modes in §28.3.

<div class="pagebreak"></div>

# Chapter 29 — Results versus Discussion

## 29.1 The boundary

**Figure 29.1 — The boundary between Results and Discussion**

```
  ┌─ RESULTS ─────────────────────┐   ┌─ DISCUSSION ────────────────────┐
  │ Question: WHAT HAPPENED?      │   │ Question: WHY, AND SO WHAT?     │
  │                               │   │                                 │
  │ Contains                      │   │ Contains                        │
  │  • numbers, tables, figures   │   │  • mechanisms and explanations  │
  │  • statistical test outcomes  │   │  • comparison with literature   │
  │  • observed patterns          │   │  • practical implications       │
  │  • magnitudes and uncertainty │   │  • limitations and threats      │
  │                               │   │  • future directions            │
  │ MUST NOT contain              │   │ MUST NOT contain                │
  │  ✗ interpretation             │   │  ✗ new numbers                  │
  │  ✗ speculation                │   │  ✗ new experiments              │
  │  ✗ "this proves…"             │   │  ✗ new tables or figures        │
  │  ✗ comparison to other papers │   │                                 │
  │    beyond stating the number  │   │ Tense: present for established  │
  │                               │   │  meaning ("this suggests")       │
  │ Tense: past ("we observed")   │   │                                 │
  └───────────────────────────────┘   └─────────────────────────────────┘

  The two classic violations, both routinely flagged by reviewers:
   ① A Results section asserting "this proves our method is superior."
   ② A Discussion introducing a new table.
```

Some journals merge the two sections; check the template. When merged, the *functions* remain distinct even though the heading does not, and the discipline of separating observation from interpretation still applies.

## 29.2 Writing Results

**Structure.** One subsection per research question, in the order the questions were posed. This makes the traceability of Chapter 7 visible to the reader.

**The four-part narration pattern.** For each table or figure:

1. **Point** to the float.
2. State the **pattern**.
3. State the **magnitude**.
4. State the **uncertainty**.

**Table 29.1 — Results language versus Discussion language**

| Belongs in Results | Belongs in Discussion |
|---|---|
| "Macro AUC fell from 0.897 ± 0.004 to 0.781 ± 0.011." | "This suggests that reported performance reflects within-institution recognition rather than transfer." |
| "The difference was significant (paired Wilcoxon, p = 0.004)." | "The effect is consistent with institution-level confounding reported by Zech et al. (2018)." |
| "Gains on the smallest institution were not significant (p = 0.21)." | "The absence of an effect at the smallest site may reflect limited statistical power rather than a genuine boundary." |
| "Expected calibration error improved from 0.094 to 0.052." | "Improved calibration matters here because triage thresholds are set on predicted probabilities." |

**[HYPOTHETICAL] ❌ Weak Results.** *"Our model achieved 95% accuracy. Table 3 shows the results. From Table 3 it is clear that our model is better than the other models. The graph in Fig. 4 shows the comparison."*

Defects: no comparison point, no dispersion, no pattern, no magnitude; the reader must do all the work; and "it is clear that" is interpretation misplaced into Results — and is not evidence in any case.

**[HYPOTHETICAL] ✅ Strong Results.** *"Under institution-disjoint evaluation, macro AUC falls from 0.897 ± 0.004 to 0.781 ± 0.011 across the five architectures (Table II), a mean reduction of 0.116 (95% CI 0.104–0.128); the direction is consistent for every architecture and every seed. Degradation is largest for the transformer backbone (−0.142) and smallest for DenseNet-121 (−0.093). CLUSTER-DG raises worst-institution AUC from 0.781 ± 0.011 to 0.822 ± 0.009 (paired Wilcoxon signed-rank, p = 0.004, Cohen's d = 1.6), while in-domain AUC decreases by 0.008, which lies within seed variance. Expected calibration error improves from 0.094 to 0.052 (Fig. 3). On the smallest institution (n = 412) the improvement is not significant (p = 0.21)."*

The final sentence — an honestly reported null result — is the sentence that makes a reviewer trust the rest. Authors who report their own inconvenient findings are believed; authors whose every result is favourable are audited.

## 29.3 Writing Discussion

**The six-move paragraph pattern.** For each principal finding:

1. **Restate** the finding in one sentence, without numbers.
2. **Explain** the mechanism — why this happened.
3. **Reconcile** with prior literature, including work that disagrees.
4. **State the implication** — what someone should now do differently.
5. **State the limitation** on this specific finding.
6. **Point** to the next question.

**[HYPOTHETICAL] ❌ Weak Discussion.** *"Our proposed method achieved the best performance among all compared methods. This demonstrates the effectiveness and superiority of our approach. The results show that our method is suitable for real-world applications. In future we will extend the work to other datasets."*

Every sentence restates the result or asserts merit. No mechanism, no engagement with literature, no implication, no limitation. This paragraph could be attached to any paper on any topic.

**[HYPOTHETICAL] ✅ Strong Discussion.** *"Cross-institutional degradation is substantially larger than published within-institution figures imply, and most of it is recoverable without institutional metadata. The mechanism our ablation supports is that acquisition artefacts concentrate in low-order embedding statistics: clusters recovered from those statistics agree with true institutional labels for 78% of samples (§V-C), which is evidently sufficient to drive an invariance penalty. This is consistent with the confounding reported by Zech et al. (2018) and extends it by quantifying the gap under a leakage-free protocol. It also reconciles the apparent disagreement between [6] and [9] regarding calibration: both evaluated on random splits, where calibration is measured on the training distribution and therefore appears better than it is. The practical implication is that a hospital evaluating a published model should expect performance closer to the worst-site figure than to the reported mean, and that mitigation does not require the provenance metadata that privacy procedures remove. Two limitations bound this conclusion. First, our institutional partition is coarse: we treat each public dataset as one institution, whereas each aggregates several sites, so true site-level degradation may be larger. Second, the absence of a significant effect at the smallest institution leaves open whether the method helps where data are scarcest — the setting in which it would matter most. Resolving this requires multi-site data with genuine site labels for evaluation, which we identify as the next step."*

Note what it does: mechanism supported by a specific ablation number; reconciliation that *explains a contradiction in the literature*; a concrete implication for a named decision-maker; two specific limitations with their consequences; and a next question that follows from the limitation rather than being generic.

## 29.4 Interpreting rather than restating

The commonest Discussion failure is restatement. The test: if a sentence would still be true with all the numbers deleted and the method renamed, it is restatement.

| ❌ Restatement | ✅ Interpretation |
|---|---|
| "Our model achieved 95% accuracy, which is higher than the baselines." | "The gain concentrates entirely in the two most prevalent classes; on the three rarest classes our method is indistinguishable from the baseline, which suggests the improvement comes from better calibration on abundant data rather than from improved representation of rare findings." |
| "The ablation shows all components contribute." | "Removing the ramping schedule costs 0.014 AUC while removing the clustering branch costs 0.031, indicating that the branch — not the schedule — carries the contribution; the schedule appears to act as an optimisation aid rather than a source of invariance." |
| "Results demonstrate effectiveness." | "The effect size (d = 1.6) exceeds the seed-to-seed variation by roughly an order of magnitude, so the difference is unlikely to be an artefact of initialisation; however, it was measured under a single augmentation policy and may not persist under stronger augmentation." |

## 29.5 Reporting limitations well

Limitations are not a confession; they are a specification of where your claim stops being safe. A good limitation names the threat, its likely direction, and its consequence.

| ❌ Vague | ✅ Specific |
|---|---|
| "Our study has some limitations." | "We treat each public dataset as a single institution, though each aggregates multiple sites; this makes our estimate of site-level degradation conservative — true degradation is likely larger, not smaller." |
| "More datasets could be used." | "We evaluate on three datasets, all from high-resource settings with digital radiography; performance under computed radiography or portable acquisition is untested and we would expect it to be worse." |
| "The method could be improved." | "The clustering step assumes the number of latent groups is roughly known; we show sensitivity to K over 2–16 (Fig. 4), but performance degrades beyond K = 20, which bounds applicability to settings with a moderate number of sites." |

## 29.6 Common mistakes

| Mistake | Correction |
|---|---|
| Interpretation in Results | Move it to Discussion |
| New numbers or tables in Discussion | Move them to Results |
| Results as a table dump with no narration | Apply the four-part pattern (§29.2) |
| Discussion restating results | Apply the interpretation test (§29.4) |
| No engagement with contradicting literature | Address it explicitly; it strengthens the paper |
| Only favourable findings reported | Report null and adverse findings; it is what earns trust |
| Generic limitations | Name the threat, its direction, and its consequence |
| Generic future work | Derive it from your stated limitations |
| Causal language on non-causal designs | Match claim strength to design (§2.5) |

## 29.7 Verification checklist for Part IX

- [ ] Every metric is justified in one sentence by the decision it supports.
- [ ] Under imbalance I report PR-AUC or macro F1 or MCC, not accuracy alone.
- [ ] Confusion matrix or per-class breakdown is present.
- [ ] Calibration is reported where probabilities drive decisions.
- [ ] Detection metrics state the IoU threshold; segmentation reports per-class overlap plus a boundary metric where shape matters.
- [ ] Every mean carries dispersion, and the dispersion measure is defined.
- [ ] My float list includes baseline comparison, ablation, error analysis, and cost.
- [ ] No axis is truncated without explicit annotation; no dual y-axes.
- [ ] Figures are vector, colourblind-safe, and legible at print size.
- [ ] Results contains no interpretation; Discussion contains no new numbers.
- [ ] Each Results subsection corresponds to a research question.
- [ ] At least one inconvenient or null finding is reported.
- [ ] Every limitation names a threat, a direction, and a consequence.

## Exercises

**Exercise 29.1** Take your strongest table and narrate it in the four-part pattern: pointer, pattern, magnitude, uncertainty.

**Exercise 29.2** Write one Discussion paragraph using all six moves of §29.3.

**Exercise 29.3** Apply the restatement test to every sentence of your current Discussion. Delete or upgrade every sentence that survives with the numbers removed.

**Exercise 29.4** Write your three most important limitations in the specific form of §29.5, each naming a direction of bias.

<div class="pagebreak"></div>
