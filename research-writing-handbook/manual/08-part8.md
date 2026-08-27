# PART VIII — RESEARCH METHODOLOGY

<div class="partintro">

Part VIII covers the production of trustworthy evidence. Chapter 22 treats methodology as the logical bridge from objectives to conclusions. Chapters 23 and 24 address data — selection, licensing, quality, and the preprocessing decisions that silently determine your results. Chapter 25 covers model selection and its scientific justification. Chapter 26 specifies experimental design: splits, tuning, baselines, ablations, and reproducibility controls.

A single theme runs through all five chapters: **the credibility of your result is determined by decisions made before you run anything.** No amount of careful writing repairs an experiment in which the baseline was under-tuned or the split leaked.

</div>

<div class="pagebreak"></div>

# Chapter 22 — Designing the Methodology

## 22.1 What methodology is, and what it is not

**Definition.** The methodology is the defensible logical chain connecting your research questions to the evidence you will present.

It is emphatically **not** a list of software. "Methodology: Python, TensorFlow, Google Colab" describes an *environment*. A reviewer reading that sentence learns nothing about whether your conclusions follow from your procedure.

**Figure 22.1 — Methodology as the bridge from objectives to evidence**

```
  OBJECTIVES  ──────────────────────────────────────────────►  CONCLUSIONS
   (Chapter 7)                                                  (Chapter 37)
       │                                                              ▲
       │                    THE METHODOLOGY                           │
       │   ┌──────────────────────────────────────────────────┐       │
       └──►│ 1  DESIGN     What kind of study? What is        │───────┘
           │               manipulated, what is held fixed?    │
           │ 2  DATA       Which datasets, why those, what     │
           │               splits, what known biases?          │
           │ 3  PROCEDURE  Preprocessing, model, training,     │
           │               tuning protocol                     │
           │ 4  CONTROLS   Baselines, seeds, equal budgets,    │
           │               blinding where applicable            │
           │ 5  ANALYSIS   Metrics, statistical tests,         │
           │               error analysis                       │
           │ 6  THREATS    Validity limits and mitigations      │
           └──────────────────────────────────────────────────┘

  TEST OF ADEQUACY: for each objective, can you trace a path through all six
  layers to a specific number or figure in your results? If not, the design
  does not yet answer the objective.
```

## 22.2 The six layers, with the questions each must answer

| Layer | Questions it must answer | Where it appears in the paper |
|---|---|---|
| **Design** | Comparative, ablative, observational, or proof-based? What is the independent variable? What is held constant? | Methodology, opening paragraph |
| **Data** | Which datasets and why? What is the split unit? What biases are documented? | Dataset subsection; Table I |
| **Procedure** | Exactly what happens to an input, from raw file to prediction? | Methodology, main body; Algorithm 1 |
| **Controls** | Which baselines, tuned how? How many seeds? What is equalised? | Experimental setup |
| **Analysis** | Which metrics, why those, which statistical test, what effect size? | Experimental setup; Results |
| **Threats** | What could make this conclusion wrong, and what did you do about it? | Discussion; Threats to validity |

## 22.3 Procedure: designing a methodology from objectives

**Step 1 — Write each objective as a required comparison.** An objective such as *"To quantify degradation when random splits are replaced by institution-disjoint splits"* implies a comparison in which the *only* thing that changes is the split protocol. Everything else — architecture, preprocessing, tuning budget, seeds — must be held fixed. Naming the comparison first prevents the common error of designing an experiment in which several things differ at once, making the result uninterpretable.

**Step 2 — Identify the confounds the comparison must survive.** For the example above: different tuning effort between conditions, different numbers of training images after re-splitting, different class balance across institutions. Each confound needs an explicit control, and each control belongs in the paper.

**Step 3 — Specify the pipeline as a sequence of transformations.** Write it as a chain, then check that each arrow is fully specified:

```
  raw file → decode → filter (which records excluded, why) → resize/tokenise
  → normalise (statistics fitted on WHAT?) → augment (train only?) → model
  → output → threshold (chosen on WHAT?) → metric
```

Every arrow that you cannot describe in one sentence is a reproducibility hole and, frequently, a leakage risk.

**Step 4 — Choose the controls before the results exist.** Baselines, seed count, tuning budget, and statistical test are all design decisions, not reporting decisions. Choosing them after seeing outcomes is the mechanism of *p*-hacking (§3.4).

**Step 5 — Write the threats-to-validity list.** Do this *before* running experiments. It routinely reveals a design flaw while it is still cheap to fix.

## 22.4 System architecture, framework, and workflow

Three words are used loosely; distinguishing them helps you write clearly.

- A **system architecture** describes components and the data flowing between them. It answers *what is connected to what*.
- A **workflow** or **pipeline** describes an ordered sequence of operations. It answers *what happens in what order*.
- A **framework** — a word best used sparingly — implies a general structure into which different components can be substituted. Only use it if substitution is actually part of your contribution; otherwise name the thing precisely (a module, a loss, a protocol, a pipeline).

**Recommendation.** Present one overview figure early in the methodology (Figure 1 of the paper), with the novel component visually distinguished and identified as such in the caption. Reviewers form their understanding of your method from that figure. Chapter 38 covers how to draw it.

## 22.5 Design rationale: the sentences that separate research from engineering

For every non-obvious choice, the methodology should contain one sentence of the form:

> *"We use [choice] because [property of the problem] implies [expected consequence]."*

Compare:

> ❌ *"We add a clustering branch that assigns each sample to one of K groups."*
>
> ✅ *"We add a clustering branch over channel-wise embedding statistics, because acquisition artefacts are known to dominate low-order feature statistics; if that is so, clusters recovered from those statistics should approximate institutional identity closely enough to support an invariance penalty without any metadata. §V-C tests this by comparing inferred clusters against true site labels."*

The second version states a belief that could turn out to be false and names the experiment that checks it. That is the difference between describing a system and doing science, and it costs one sentence plus one experiment.

## 22.6 Common mistakes

| Mistake | Correction |
|---|---|
| Methodology as a tool list | Describe design, controls, and analysis — not the environment |
| A comparison in which several factors differ | Isolate one factor per comparison |
| No design rationale | Add one "because" sentence per non-obvious choice |
| Controls chosen after seeing results | Pre-specify baselines, seeds, budget, and test |
| Pipeline arrows that cannot be described in a sentence | Specify them; each is a reproducibility hole |
| "Framework" used to conceal what the contribution is | Name the artefact precisely |
| Threats to validity written last | Write them first; they reveal design flaws cheaply |

## Exercises

**Exercise 22.1** For each objective, write the comparison it requires and list what must be held constant.

**Exercise 22.2** Write your pipeline as a chain of arrows and mark every arrow you cannot yet describe in one sentence.

**Exercise 22.3** Write one design-rationale sentence for each non-obvious choice in your method, in the "because … implies …" form.

**Exercise 22.4** Write your threats-to-validity list now, before running experiments. Note any threat with no mitigation.

<div class="pagebreak"></div>

# Chapter 23 — Dataset Selection

## 23.1 Why this decision dominates your results

Dataset choice constrains everything downstream: what claims are possible, what baselines are comparable, which metrics are appropriate, and whether anyone can reproduce your work. It is also nearly irreversible — discovering in month six that your dataset cannot support your claim usually means restarting.

**Table 23.1 — Dataset selection criteria**

| Criterion | What to check | Why it matters |
|---|---|---|
| **Relevance** | Does it contain the phenomenon you study? | A dataset lacking the condition cannot test your claim |
| **Standard use** | Is it the benchmark your field uses? | Non-standard data makes your results incomparable |
| **Size** | Enough for the model class and the effect size? | Under-powered studies detect nothing reliably |
| **Label quality** | Who labelled it, how, with what agreement? | Label noise caps achievable performance and can invert conclusions |
| **Class distribution** | Imbalance ratio per class | Determines metric choice (Chapter 27) |
| **Grouping structure** | Multiple records per subject, site, author, session? | Determines the split unit — the most common validity failure |
| **Documentation** | Is there a datasheet or paper describing construction? | Undocumented data cannot be reasoned about |
| **Licence** | Research use, redistribution, derivatives, commercial terms | Determines what you may publish and release |
| **Access route** | Open download, registration, data-use agreement, application | Determines your timeline |
| **Ethics** | Consent basis; identifiability; approval needed? | Determines whether the study is permissible at all |
| **Known biases** | Documented confounds and artefacts | Prevents rediscovering a known artefact as a finding |

## 23.2 Public, private, and synthetic data

**Public datasets** are the default choice and should be your first option. They make results comparable, permit independent verification, and eliminate access risk. Their weakness is saturation — headline performance on a well-worn benchmark is usually near a ceiling, so a pure performance claim is hard. This is precisely why *evaluation* and *generalisation* contributions on public data are attractive (§17.3.1): the data are shared, so the contribution is the protocol rather than the access.

**Private or proprietary datasets** allow genuinely new questions and carry three costs that must be confronted honestly: nobody can verify your results; nobody can compare against them; and reviewers discount claims they cannot check. If you must use private data, mitigate: report descriptive statistics fully, release the code even when you cannot release the data, evaluate additionally on at least one public dataset, and state the limitation explicitly.

**Synthetic data** is legitimate for controlled study of a mechanism — you can vary one factor exactly, which real data rarely permits. Its threat is that conclusions may describe the generator rather than the world. The standard mitigation is to pair synthetic results with real-data validation, and to state which conclusions rest on which.

## 23.3 Data leakage: the failure that invalidates results silently

**Definition.** Leakage occurs when information from the evaluation partition influences training or model selection, so that measured performance overstates real performance.

Leakage is the most consequential technical error in applied machine learning because it is invisible: nothing crashes, and results *improve*.

**Figure 23.1 — Data leakage pathways**

```
  ① GROUP LEAKAGE — the most common
     Records sharing a group (patient, site, author, session, project, device)
     appear in both train and test. The model recognises the group, not the target.
     FIX: split by the group, not by the row.

  ② PREPROCESSING LEAKAGE
     Normalisation statistics, scalers, vocabularies, or feature selection
     fitted on all data before splitting.
     FIX: fit on training folds only; apply to validation and test.

  ③ RESAMPLING LEAKAGE
     Oversampling (e.g. synthetic minority generation) applied before splitting,
     so synthetic copies of test records appear in training.
     FIX: resample inside the training fold only, after the split.

  ④ TEMPORAL LEAKAGE
     Future records used to predict the past because the data were shuffled.
     FIX: split by time; train on earlier, test on later.

  ⑤ DUPLICATE LEAKAGE
     Exact or near-duplicate records straddling the split.
     FIX: deduplicate before splitting, including near-duplicates.

  ⑥ TARGET LEAKAGE
     A feature encodes the label (an identifier, a post-outcome measurement,
     a filename convention).
     FIX: audit features for post-hoc information.

  ⑦ SELECTION LEAKAGE (tuning on test)
     The test set consulted repeatedly during development.
     FIX: touch the test set once, at the end. Log every access.
```

Pathway ① deserves particular emphasis because it is both the most frequent and the most field-general. Zech et al. (2018) demonstrated the consequence concretely in medical imaging: models can key on institution-specific signal, so evaluation that mixes institutions across partitions measures something other than the transfer being claimed. The same structure occurs with multiple utterances per speaker, multiple commits per project, multiple pupils per classroom, and multiple readings per sensor.

**The declarative sentence reviewers look for.** Include it verbatim:

> *"All preprocessing statistics, resampling, and feature selection were fitted on training folds only. Splits are patient-disjoint and institution-disjoint: no patient and no institution appears in more than one partition."*

## 23.4 Licensing, ethics, and what you may publish

**Licensing.** Read the actual licence, not the summary on an aggregator. Distinguish: research-only versus commercial use; permission to redistribute the data; permission to publish derivatives such as split files, features, or trained weights; attribution requirements. **Recommendation:** if you cannot redistribute the data, you can almost always redistribute *split definitions* (lists of record identifiers), which is the single most valuable reproducibility artefact you can release.

**Ethics.** Human-subject data, patient data, and identifiable data generally require institutional review-board or ethics-committee involvement, and the requirement is determined by your institution and jurisdiction rather than by whether the data are already public. **[VERIFY] with your own committee.** Two points that beginners routinely miss: publicly available data are not automatically exempt from review, and web-scraped data may be subject to terms of service and data-protection law independently of any ethics approval.

**Declarations.** You will need statements on ethics approval, consent, data availability, and code availability at submission (§53.4). Draft them when you choose the dataset, not on submission day.

## 23.5 Common mistakes

| Mistake | Correction |
|---|---|
| Splitting by row when data are grouped | Split by group; state the unit explicitly |
| Fitting scalers or vocabularies before splitting | Fit on training folds only |
| Oversampling before splitting | Resample inside the training fold |
| Shuffling time series | Split temporally |
| Using a non-standard dataset without justification | Add the field-standard benchmark, even if unfavourable |
| Not reporting the imbalance ratio | Report it; it determines metric validity |
| Discovering the licence at submission | Read it in week one |
| Reporting accuracy on data with known artefacts as a finding | Check documented biases first |
| "Data available on request" | Deposit in a repository with a DOI, or state a specific, justified restriction |

## Exercises

**Exercise 23.1** Complete Table 23.1 for every dataset you intend to use, with specific answers.

**Exercise 23.2** Identify your grouping structure and state the split unit. If records share any group, a row-level random split is invalid.

**Exercise 23.3** Audit your pipeline against all seven leakage pathways in Figure 23.1. Write down which apply and what you did.

**Exercise 23.4** Draft your data-availability and ethics statements now.

<div class="pagebreak"></div>

# Chapter 24 — Data Preprocessing

## 24.1 Why preprocessing must be documented

Preprocessing decisions frequently affect results more than model choice, and they are the most under-reported part of most papers. Two consequences follow. First, undocumented preprocessing is the leading known cause of irreproducibility — when a reported number cannot be recovered from released code, a preprocessing difference is the most common explanation. Second, preprocessing is where leakage enters (§23.3).

**Table 24.1 — Preprocessing decisions and their documentation requirements**

| Operation | Decisions to record | Leakage risk | Common error |
|---|---|---|---|
| **Cleaning / filtering** | Exclusion criteria; resulting counts at each step | Low | Filtering on a property correlated with the label |
| **Missing values** | Mechanism assumed; imputation method; whether an indicator was added | **High** — imputation fitted on all data | Mean imputation computed over train and test together |
| **Normalisation / standardisation** | Which statistics, computed on which partition | **High** | Statistics computed on the full dataset |
| **Encoding** | Scheme; how unseen categories are handled | Medium | Vocabulary built from all data |
| **Resizing / resampling signals** | Target size; interpolation; aspect-ratio handling | Low | Unreported interpolation, which changes results measurably |
| **Tokenisation** | Tokeniser identity and version; vocabulary source | Medium | Vocabulary fitted including test text |
| **Augmentation** | Exact transforms, parameters, probabilities; **train only** | Medium | Augmentation applied at test time |
| **Class balancing** | Method; applied **after** splitting, inside training folds | **Very high** | Synthetic oversampling before the split |
| **Feature selection** | Criterion; fitted on training folds only | **Very high** | Selection using labels of the whole dataset |
| **Dimensionality reduction** | Method; number of components; fitted on train only | **High** | Projection fitted on all data |
| **Deduplication** | Exact or near-duplicate; threshold | Low | Skipped entirely |

The three rows marked *very high* or *high* account for most invalidated student results. The rule is uniform and simple: **anything that learns from data — a scaler, an imputer, a vocabulary, a selector, a projection, a resampler — is a model, and must be fitted on training data only.**

## 24.2 Documenting preprocessing: weak and strong

**[HYPOTHETICAL] ❌ Weak.** *"The images were preprocessed and resized. Data augmentation was applied to increase the dataset. The data was divided into training and testing sets."*

Unanswerable questions: resized to what, with what interpolation? Which augmentations, with what probabilities? Was augmentation applied to test data? What split ratio, and split by what unit?

**[HYPOTHETICAL] ✅ Strong.** *"Images are resized to 224 × 224 using bilinear interpolation with aspect ratio preserved by centre cropping. Intensities are normalised using channel statistics computed on the training partition only (μ = 0.503, σ = 0.291). Training augmentation comprises random resized crop (scale 0.8–1.0), horizontal flip (p = 0.5), and rotation (±10°); no augmentation is applied at validation or test time. Records are deduplicated by perceptual hash before splitting (412 near-duplicates removed). Splits are patient- and institution-disjoint in the ratio 70/10/20 by patient count. Class prevalence ranges from 1.2% to 38.5%, which motivates the per-class metrics reported in §V."*

The strong version is reproducible, states where statistics were fitted, confines augmentation to training, names the split unit, and connects the class distribution to the metric choice.

## 24.3 The five sentences every data subsection needs

1. **Provenance** — dataset name, version, size, source, licence.
2. **Filtering** — what was excluded and why, with resulting counts.
3. **Transformations** — exact operations and parameters, and **which partition any fitted statistics came from**.
4. **Split protocol** — ratios *and the unit of splitting*.
5. **Distribution** — class balance, and its consequence for metric choice.

## Exercises

**Exercise 24.1** Write the five sentences of §24.3 for your own data.

**Exercise 24.2** For every operation in your pipeline that *learns* anything from data, state which partition it was fitted on. Any answer other than "training only" is a defect.

**Exercise 24.3** Take the weak paragraph in §24.2 and rewrite it for your dataset at the strong version's level of specificity.

<div class="pagebreak"></div>

# Chapter 25 — Model Selection

## 25.1 Justifying model choice scientifically

The weakest sentence in applied papers is *"we use model M because it has achieved good results in recent literature."* That is an appeal to popularity. A scientific justification connects a property of the **problem** to a property of the **model**.

**Table 25.1 — Model families and the conditions that justify them**

| Family | Justified when | Inductive bias | Characteristic weakness |
|---|---|---|---|
| **Trivial / majority baseline** | Always, as a floor | None | — (its purpose is to bound the task's difficulty) |
| **Linear / logistic models** | Few samples; interpretability required; near-linear structure | Linearity, additivity | Cannot represent interactions |
| **Tree ensembles** (random forests, gradient boosting) | Tabular, heterogeneous features; moderate sample size | Axis-aligned partitions | Poor on raw high-dimensional signals |
| **Convolutional networks** | Signals with local structure and translation-equivariant patterns | Locality, weight sharing | Limited long-range context |
| **Recurrent networks (RNN, LSTM, GRU)** | Sequential data with order dependence; streaming | Sequential state, recency | Degradation on long dependencies; limited parallelism |
| **Transformers** | Long-range dependence matters; data are plentiful; pretraining available | Global attention; weak locality prior | Data- and compute-hungry; quadratic attention cost in sequence length |
| **Transfer learning / fine-tuning** | Target data are scarce and the source domain is related | Inherited from pretraining | Negative transfer under domain mismatch; pretraining data may overlap your test set |
| **Ensembles** | Variance reduction; competition settings | Averaging | Multiplied inference cost; obscures mechanism |
| **Hybrid architectures** | Two failure modes are complementary **and you can predict the interaction** | Combined | Frequently claimed, rarely justified (§20.4) |

## 25.2 Procedure for justifying a choice

1. **Name the property of your data** that dictates the requirement — long-range dependence, local texture, grouped structure, tabular heterogeneity, extreme scarcity.
2. **Name the model property** that addresses it.
3. **Name what you give up** — every inductive bias is a restriction, and stating the trade-off demonstrates understanding.
4. **Include a baseline from a different family**, so that the comparison tests your reasoning rather than assuming it.
5. **State the cost** in parameters, memory, and latency.

**[HYPOTHETICAL] Worked example.** *"Radiographic findings are characterised by localised texture at multiple scales, which motivates a convolutional backbone; we nonetheless include a vision transformer because global attention may capture the bilateral comparisons radiologists report using, and because it allows us to test whether stronger global context increases sensitivity to institution-level acquisition signal (§V-D). We additionally report a gradient-boosted baseline over handcrafted features as a non-deep reference point, since the literature we surveyed contains no such comparison."*

## 25.3 Why a strong classical baseline is not optional

**Recommendation, with an evidential basis.** Include a well-tuned classical baseline. Structured re-evaluation studies in several areas of machine learning have found that reported advantages of newer, more complex methods narrowed or disappeared when simpler baselines were tuned with comparable effort — reported for recommender systems by Dacrema et al. (2019), for language-model architectures by Melis et al. (2018), and for generative adversarial models by Lucic et al. (2018).

The practical consequence for you is twofold. If a reviewer suspects you avoided a strong simple baseline, your improvement claim is dead. And if the classical baseline *wins*, that is a genuine and publishable finding — not a failure.

## 25.4 Common mistakes

| Mistake | Correction |
|---|---|
| Justifying by popularity | Connect a data property to a model property |
| No baseline from a different family | Add one; it tests your reasoning |
| Omitting the trivial baseline | Include it; it bounds task difficulty |
| Omitting a tuned classical baseline | Include it (§25.3) |
| Claiming a hybrid without predicting the interaction | Apply §20.4 |
| Comparing models at different parameter counts | Match capacity, or report the mismatch prominently |
| Ignoring pretraining-data overlap with your test set | Check and disclose; it is a leakage pathway |
| Not reporting cost | Report parameters, FLOPs, latency, memory |

## Exercises

**Exercise 25.1** Justify your model in the four-part form of §25.2, including what you give up.

**Exercise 25.2** Identify a strong classical baseline for your task and commit to tuning it as hard as your own method.

**Exercise 25.3** If you use pretrained weights, check whether the pretraining corpus plausibly overlaps your evaluation data, and write a sentence disclosing what you found.

<div class="pagebreak"></div>

# Chapter 26 — Experimental Design

## 26.1 The seven design decisions

| Decision | Standard to meet |
|---|---|
| **Datasets** | Two or more with differing characteristics; include the field-standard benchmark |
| **Splits** | Grouped and, where relevant, temporal; fixed; identical across all methods; published |
| **Baselines** | Four categories (§26.5); tuned with equal effort |
| **Tuning** | Identical search space size and trial budget for every method — and stated |
| **Repetition** | Five seeds minimum, ten preferred; report mean with standard deviation or confidence interval |
| **Ablation** | One factor removed at a time, plus a cumulative build-up |
| **Cost** | Parameters, FLOPs, training time, inference latency, memory |

## 26.2 Training, validation, and testing

The three partitions have distinct and non-interchangeable roles:

- **Training** — parameters are fitted.
- **Validation** — hyperparameters, architecture variants, early-stopping points, and decision thresholds are selected.
- **Test** — the final estimate is computed, **once**.

**The cardinal rule.** Every additional look at the test set is a selection step, and selection on test invalidates the estimate. Keep a dated log of each time you evaluated on test and why (§3.5). Researchers who do this discover that they touch the test set far more often than they believed.

## 26.3 Splitting schemes

**Figure 26.1 — Splitting schemes and when each applies**

```
  Is your data grouped (multiple records per subject/site/author/session)?
  │
  ├─ NO ──── Is it time-dependent?
  │          ├─ NO ──── Is the dataset large?
  │          │          ├─ YES → fixed train/val/test (benchmark convention)
  │          │          └─ NO  → k-fold CV (k=5 or 10); stratified if imbalanced
  │          └─ YES → temporal split; rolling-origin evaluation. NEVER shuffle.
  │
  └─ YES ─── Split by the GROUP.
             ├─ Estimating in-domain performance → grouped k-fold
             ├─ Claiming cross-domain transfer   → leave-one-group-out
             │                                     (e.g. leave-one-site-out)
             └─ Small data + tuning required     → nested CV
                                                   (outer: estimation,
                                                    inner: hyperparameters)
```

| Scheme | Use when | Note |
|---|---|---|
| Fixed train/val/test | Large data; established benchmark convention | Report the split source; use the official split if one exists |
| *k*-fold CV | Small to medium data; variance estimates needed | Report per-fold results, not only the mean |
| **Stratified** *k*-fold | Class imbalance | Preserves class proportions in each fold |
| **Grouped** *k*-fold | Repeated measures per unit | Prevents group leakage (§23.3, pathway ①) |
| **Nested** CV | Tuning *and* unbiased estimation on small data | Expensive but correct; the honest choice for small datasets |
| Leave-one-group-out | Cross-domain generalisation claims | The design that actually supports a transfer claim |
| Temporal / rolling-origin | Any time-dependent data | Shuffling time series is a common invalid setup |
| Repeated CV with different seeds | Reporting variance honestly | Combine with the above |

## 26.4 Hyperparameter tuning and budget parity

**The fairness principle.** An improvement claim is only meaningful if every method received comparable optimisation effort. Otherwise you have measured your own tuning diligence.

**Procedure.**

1. Define one search space per method, of comparable dimensionality.
2. Fix a **trial budget** — the same number of trials for every method.
3. Use the same search strategy throughout (random search is a reasonable default and is easier to describe than manual tuning).
4. Select using the **validation** partition only.
5. Report the search space, the strategy, the budget, and the selected values.
6. Write the sentence: *"All methods received an identical budget of N trials over search spaces of comparable size, selected on validation data."*

That one sentence removes the most common reason reviewers distrust an improvement claim, and it costs nothing if you actually did it.

## 26.5 Baselines: four categories

**Table 26.1 — Baseline categories**

| Category | Purpose | Example |
|---|---|---|
| **Trivial** | Bounds the task's difficulty; exposes degenerate metrics | Majority class; random; predict-the-mean |
| **Strong classical** | Tests whether complexity is necessary at all | Gradient boosting on features; TF-IDF with a linear model |
| **Current state of the art** | Positions the contribution | The best published method, from official code where possible |
| **Your method minus its novelty** | Isolates the contribution, holding everything else constant | The full pipeline with the new component removed |

The fourth category is the one reviewers trust most, because it controls for every other difference. It is also the first row of your ablation table, so it costs nothing extra.

**On reusing published numbers.** Copying a baseline's number from its original paper is acceptable *only* if the dataset, split, and metric are provably identical. When they are not — which is usual — you must re-run the baseline. If you re-run and obtain a lower number than published, report both and say so plainly (§12.4).

## 26.6 Ablation studies

**Definition.** An ablation removes or replaces one component at a time to determine each component's contribution.

**Purpose.** Without ablation, you have shown *that* a pipeline works, not *which part* matters — so nobody, including you, knows what to reuse. An ablation is also the only experiment that tests a mechanistic claim (§1.5).

**Design rules.**

- **One factor per row.** Two simultaneous changes make the row uninterpretable.
- Report a **cumulative build-up** (baseline → +A → +A+B → full) *and* **leave-one-out** rows where they differ informatively.
- Include an **upper bound (oracle)** where one exists — for instance a version using privileged information you claim not to need. This converts "we improved by 0.04" into "we recovered 82% of the oracle's benefit without its requirements", a much stronger scientific statement.
- **Ablate the hyperparameters of your novel component** in a sensitivity analysis. If performance depends critically on a value you tuned, say so.
- **Ablate the data**: what happens at 10%, 25%, 50% of labels?
- If a component contributes approximately nothing, **report that and remove it**. Honest negative ablations increase credibility more than they cost — a paper in which every component contributes exactly as hoped reads as suspicious.

## 26.7 Sensitivity and error analysis

**Sensitivity analysis** varies one hyperparameter or condition across a range and plots the outcome. It answers *how fragile is this?* — a question practitioners care about far more than the peak number.

**Error analysis** examines *which* cases fail. It is the highest-value-per-hour activity in empirical research and the most frequently skipped.

**Procedure.** Inspect the confusion matrix for semantically sensible confusions; stratify errors by subgroup (site, device, demographic, input length, illumination) and report the **worst** subgroup, not only the mean; sample thirty to fifty errors manually and categorise their causes into a taxonomy with counts; correlate errors with input properties; and test for shortcut learning by masking the suspected shortcut and observing whether performance collapses.

Manually examining thirty failures teaches more about a model than a week of hyperparameter search, and the resulting taxonomy is often the most cited figure in the paper.

## 26.8 Statistical validation

| Situation | Appropriate test |
|---|---|
| Two models, same test set, per-item correctness | **McNemar's test** |
| Two models, paired scores across folds or seeds | Paired *t*-test (if normality is plausible) or **Wilcoxon signed-rank** |
| Two AUCs on the same sample | **DeLong's test** |
| More than two models across many datasets | **Friedman test** with a post-hoc procedure; critical-difference diagrams (Demšar, 2006) |
| Small data, tuning and estimation together | 5×2-fold cross-validated paired *t*-test (Dietterich, 1998) |
| Any metric, distribution-free interval | **Bootstrap** confidence interval (≥1,000 resamples) |
| Any comparison | Report an **effect size** alongside the *p*-value |

Three rules: pre-specify the test; report effect sizes because significance without magnitude is uninformative; and correct for multiple comparisons (Holm or an equivalent) when testing many model–dataset pairs.

McNemar's test deserves specific mention because it is the correct test for comparing two classifiers on a shared test set and is the one most often omitted from student papers.

## 26.9 Reproducibility controls

| Control | Concrete action |
|---|---|
| **Seeds** | Fix and record seeds for the language runtime, the numerical library, the framework, and the accelerator; report ≥5 runs with mean and dispersion. Never report a single best run |
| **Determinism** | Enable deterministic kernels where available; document residual nondeterminism |
| **Environment** | Export a dependency manifest; record framework, accelerator library, and driver versions; note the hardware |
| **Configuration over code edits** | One configuration file per experiment; never tune by editing source |
| **Data versioning** | Record dataset version, download date, and a checksum of your split files |
| **Release the splits** | The cheapest high-impact reproducibility artefact; often permissible even when the data are not redistributable |
| **Logging** | Track every run with an experiment-tracking tool or structured logs; keep run identifiers for the appendix |
| **Code release** | Public repository, tagged release, archival DOI, licence, and a README with exact commands |
| **Availability statement** | A data-and-code statement with a resolvable link |

**Red flags reviewers look for:** four-decimal accuracy from a single seed; "best of N runs"; no variance anywhere; hyperparameters "chosen empirically" with no search described; test-set numbers used for selection; and "code available on request".

## 26.10 Verification checklist for Part VIII

- [ ] Each objective traces through all six methodology layers to a specific result.
- [ ] Every non-obvious design choice has a "because" sentence.
- [ ] I have audited all seven leakage pathways and stated my controls.
- [ ] The split unit is the grouping unit of my data.
- [ ] Everything that learns from data is fitted on training folds only.
- [ ] All four baseline categories are present, including "mine minus its novelty".
- [ ] Every method received an identical, stated tuning budget.
- [ ] I run at least five seeds and report dispersion.
- [ ] My ablation changes one factor per row and includes an upper bound where possible.
- [ ] I have performed stratified and manual error analysis.
- [ ] The statistical test was pre-specified, with effect size and multiple-comparison correction.
- [ ] Cost is measured on stated hardware.
- [ ] Seeds, environment, configurations, and split files are recorded and releasable.
- [ ] The test set was touched once, and I have the log to show it.

## Exercises

**Exercise 26.1** Write your experimental protocol: datasets, split scheme and unit, baselines in all four categories, tuning budget, seed count, metrics, statistical test. One page.

**Exercise 26.2** Design your ablation table on paper, one factor per row, including an oracle row if one exists.

**Exercise 26.3** Compute your total run count as configurations × seeds × datasets, then multiply by three (§4.6.1). Compare with your resources.

**Exercise 26.4** Sample thirty errors from any model you have already trained and categorise their causes. Note how much you learn relative to the time spent.

<div class="pagebreak"></div>
