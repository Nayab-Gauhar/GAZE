# PART II — SELECTING A RESEARCH PROBLEM

<div class="partintro">

Part II covers the four decisions that determine whether a research project is completable and worth completing: the area you work in (Chapter 4), the problem you address within it (Chapter 5), the questions that make that problem answerable (Chapter 6), and the objectives that commit you to specific, checkable work (Chapter 7).

These decisions are cheap to make and expensive to unmake. A poorly chosen area wastes years; a poorly specified problem produces experiments that answer nothing; unmeasurable objectives produce a thesis that cannot be examined. The material here is deliberately procedural, because "choose a good topic" is advice that helps nobody.

</div>

<div class="pagebreak"></div>

# Chapter 4 — Selecting a Research Area

## 4.1 The problem with "follow your interest"

The standard advice is to work on what interests you. This is necessary and radically insufficient. Interest sustains you through year three; it does not tell you whether the work is possible, supervisable, or publishable. A research area must satisfy five constraints simultaneously, and the failure of any one of them is sufficient to end a project.

**Table 4.1 — Five constraints on the choice of a research area**

| Constraint | Question to answer honestly | Failure mode if ignored |
|---|---|---|
| **Personal endurance** | Can I read this literature for three to five years without resentment? | Abandonment in year two, after sunk cost |
| **Supervisory capability** | Can my supervisor critique my technical work here, not merely approve it? | Unsupervised drift; weak papers that pass internally and fail externally |
| **Resource availability** | Do I have the data, compute, subjects, licences, and ethics route? | Stalled experiments; a year lost to access negotiations |
| **Field momentum** | Is publication volume in this area rising, flat, or collapsing? | Working in a dead area, or arriving late at a saturated peak |
| **Career relevance** | Do job advertisements and funding calls name this area? | Employability mismatch at the end |

The second constraint is the one least often said aloud. If your supervisor cannot critique your work — because the area is outside their expertise, or because they supervise thirty students — you are not badly supervised so much as *unsupervised*, and you must construct a substitute critique network deliberately: a reading group, participation in peer review, correspondence with the authors of papers you read, and preprint feedback. This is achievable, but only if you recognise the need early.

## 4.2 Assessing field momentum

**Purpose.** To distinguish an emerging area (good entry point), a saturated area (high competition, fast obsolescence), and a declining area (easy novelty, few readers).

**Procedure.**

1. In Scopus or Web of Science, search your candidate area's core terms restricted to title, abstract, and keywords.
2. Use the platform's analysis view to plot **documents by year**. **[VERIFY]** The exact name of this feature changes; in Scopus it has been presented as "Analyze search results" and in Web of Science as "Analyze Results". Confirm on the platform.
3. Read the shape of the curve.

| Curve shape | Interpretation | Strategic implication |
|---|---|---|
| Rising steadily | Healthy, growing area | Good entry point; readers exist; questions remain open |
| Rising near-vertically | Hype phase | High visibility, brutal competition, results obsolete in 18 months |
| Flat and high | Mature, saturated | Novelty is hard; incremental gains are contested |
| Flat and low | Niche | Novelty is easy; few citers; harder to place in strong venues |
| Declining | Superseded | Establish *why* it declined before entering |

4. In the same analysis view, inspect **top source titles** (these are your candidate target journals, Chapter 51), **top authors** (these are your likely reviewers), and **top affiliations** (these are your competitors and potential collaborators).

That fifteen-minute exercise yields your venue list, your reviewer pool, and your competitive landscape simultaneously. It is among the highest-return activities in this handbook and is skipped by most beginners.

## 4.3 Narrowing: the funnel

**Figure 4.1 — The narrowing funnel: from research area to research objective**

```
LEVEL 0  DISCIPLINE          Computer Science
   │                          (hundreds of thousands of papers/year — meaningless as a topic)
   ▼
LEVEL 1  BROAD AREA          Machine learning for medical image analysis
   │                          (~10,000+ papers/year — still unreadable)
   ▼
LEVEL 2  SUB-AREA            Domain generalisation in chest radiograph classification
   │                          (a readable literature: roughly 100–300 papers)
   ▼
LEVEL 3  SPECIFIC PROBLEM    Published CXR classifiers are evaluated with random splits
   │                          that mix institutions across train and test, so reported
   │                          performance may not describe cross-hospital behaviour
   ▼
LEVEL 4  RESEARCH QUESTION   RQ1: How large is the performance drop under
   │                          institution-disjoint evaluation?
   │                         RQ2: Can it be mitigated without institutional metadata?
   ▼
LEVEL 5  OBJECTIVE           To re-evaluate five published architectures on three public
                             datasets under both random and institution-disjoint protocols,
                             over ten seeds, reporting macro AUC, worst-institution AUC,
                             and calibration error with 95% confidence intervals.
```

*[HYPOTHETICAL as a worked example, though grounded in the real finding of Zech et al. (2018) that CXR models can exploit institution-specific confounders.]*

### 4.3.1 The one-breath test

You have narrowed sufficiently when you can say this sentence without hesitation:

> *"I compare **[methods]** on **[datasets]** under **[condition]**, measured by **[metrics]**, to find out whether **[question]**."*

If you cannot fill all five slots with specifics, you are at least one level too broad. This test is more useful than any abstract discussion of scope because it fails loudly.

### 4.3.2 Narrowing operators

Apply these until the one-breath test passes. Each operator reduces scope along a different axis, and using two or three in combination is normal.

| Operator | Question | Example narrowing |
|---|---|---|
| **Population** | Which subjects, domains, or corpora? | All images → paediatric chest radiographs |
| **Task** | Which exact output? | "Understanding" → multi-label finding classification |
| **Condition** | Under what circumstance? | → under low-light and occlusion |
| **Constraint** | Subject to what limit? | → within 50 ms on an edge device |
| **Comparison** | Against what? | → versus four representative domain-generalisation methods |
| **Outcome** | Measured how? | → by worst-group AUC and calibration error |

### 4.3.3 Over-narrowing

The opposite error is rarer but real: a topic so specific that no one outside your laboratory can use the result. The diagnostic is that you cannot name anyone who would cite it.

The remedy is *not* to broaden the study. It is to raise the level of the **claim** while keeping the study specific. A study on one proprietary dataset with 200 images is weak. The same study, framed as "we characterise how detection performance degrades as annotation density falls below N examples per class, using X as a case", makes a transferable claim while performing the same experiments. The study is narrow; the knowledge is not.

## 4.4 Four routes into a topic

Different researchers arrive from different directions, and each route has a characteristic weakness worth knowing in advance.

**Technology-driven.** You are interested in a technique — diffusion models, graph neural networks, retrieval-augmented generation — and seek a place to apply it. *Characteristic weakness:* produces "apply X to Y" work with no reason why Y should be interesting for X. *Remedy:* identify a property of Y that violates an assumption of X, and measure what happens. That converts application into science (§5.5).

**Problem-driven.** You know a real difficulty — clinicians distrust model output; farmers cannot afford connectivity — and seek methods. *Characteristic weakness:* the problem may not be tractable, or may require data you cannot obtain. *Remedy:* run the feasibility audit (§4.6) before committing.

**Dataset-driven.** A dataset exists or you can build one. *Characteristic weakness:* dataset availability is not a research question; "we applied five models to this new dataset" is a technical report. *Remedy:* the dataset itself can be the contribution, if constructed and documented to publishable standards (§1.8.1, resource contribution), or ask what the data allows you to measure that was previously unmeasurable.

**Literature-driven.** You read carefully and find a contradiction, an admitted limitation, or an untested assumption. *Characteristic weakness:* slow to start; requires substantial reading before the topic appears. *Advantage:* this route produces the most defensible gaps, because the gap arrives already supported by citations. Part VI is built on it.

## 4.5 Finding emerging topics and unresolved problems

**Purpose.** To locate questions that are open, recognised as open, and not yet crowded.

### 4.5.1 Sources of emerging topics

| Source | What to look for | Cadence | Access |
|---|---|---|---|
| Preprint servers (arXiv and equivalents) | New listings in your categories; set keyword alerts | Weekly | Free |
| Semantic Scholar | Alerts, citation velocity, influential citations | Weekly | Free |
| Citation-graph tools (Connected Papers, Litmaps, ResearchRabbit) | Prominent nodes you have not read | Per topic | Free tiers |
| Scopus / Web of Science analysis views | Trend, top sources, top authors | Per topic | Subscription |
| **Journal special-issue calls** | Editors publicly declaring which gaps they want filled | Monthly | Free |
| Workshop titles at major conferences | The field's twelve-month agenda | Yearly | Free |
| Benchmark leaderboards | Metrics that have *stopped improving* | Per topic | Free |
| Funding-agency calls | What is considered strategically important | Per cycle | Free |

Two of these deserve emphasis because they are consistently underused.

**Special-issue calls for papers** are the most explicit statement of demand available anywhere. An editor writing a call is saying, in public, "we want papers on this and will handle them." That is a gap with a receptive gatekeeper and a deadline.

**Flattening leaderboard curves** are a research opportunity in either of two ways: progress is genuinely saturating, which is interesting, or the benchmark has ceased to measure what matters, which is more interesting.

### 4.5.2 Where unresolved problems are stated explicitly

Researchers routinely publish lists of open problems, and beginners routinely do not read them.

1. **Limitations sections** of recent papers.
2. **Future work** in conclusions.
3. **Open-challenge sections** of survey papers.
4. **Public peer review**, where available. Some venues publish reviews and author responses. **[VERIFY]** Availability varies by venue and year; OpenReview hosts public reviews for several major machine-learning conferences. Reading expert criticism of accepted *and rejected* papers teaches you the field's actual standards of evidence in the field's own words — and each stated weakness is a candidate gap that already carries an expert endorsement.
5. **Rebuttals**, where authors concede what they could not do.
6. **Reproducibility reports** and replication studies.
7. **Registered reports and pre-registrations**, which state predictions before results.

## 4.6 The feasibility audit

**Purpose.** To discover that a project is impossible *now*, in an afternoon, rather than in eight months.

**Procedure.** Complete every row with a specific answer. "We will find a dataset" is not an answer.

| Dimension | What to verify concretely | Red flag |
|---|---|---|
| **Data exists** | Named dataset, size, label type, access path | "We will collect our own" with no protocol, budget, or timeline |
| **Licence permits use** | Terms for research use, redistribution, derivative works | A data-use agreement requiring institutional signature you have not begun |
| **Ethics route** | Whether committee approval is needed; who applies; typical duration | Human or patient data with no identified approval route |
| **Compute** | GPU-hours for *your model × baselines × ablations × seeds × datasets* | An estimate that assumes one run per configuration |
| **Baselines runnable** | Official code located; does it execute on your machine? | No public implementation and no reimplementation plan |
| **Evaluation defined** | Metrics, splits, statistical test chosen in advance | "We will look at the accuracy" |
| **Skills** | Methods you must learn; who will teach you | A method central to the design that nobody available understands |
| **Time** | Backwards from a real deadline, with 40% slack | A plan with no slack for failure |

### 4.6.1 Compute arithmetic, done honestly

Beginners estimate compute as *one training run*. The real figure is a product:

```
  configurations   =  1 proposed method  +  4 baselines            =   5
  × seeds          =  × 10                                        =  50
  × datasets       =  × 3                                         = 150 runs
  × hours per run  =  × 2 GPU-hours                               = 300 GPU-hours

  plus hyperparameter search   (often 2–5× the above)
  plus the ablation study      (typically 5–15 further configurations)
  plus re-runs after a bug     (assume at least one full re-run)
  plus experiments reviewers demand in revision   (budget 20%)

  REALISTIC TOTAL:  roughly 3× your first estimate
```

Doing this arithmetic before committing is the single most effective protection against a stalled project. If the number exceeds your resources, you have three honest options: reduce the scope (fewer datasets, smaller models), change the question to one your resources can answer (evaluation and reproducibility questions are often far cheaper — §17.10), or secure more resources before starting.

### 4.6.2 A note on discovering infeasibility

If this audit shows your project is impossible, that is a *success*, and it should be treated as one. Discovering infeasibility in week one costs an afternoon; discovering it in month eight costs a year. Researchers who feel embarrassed by this outcome tend to press on, and pressing on is how projects consume a doctorate without producing a paper.

## 4.7 Common mistakes

| Mistake | Correction |
|---|---|
| Choosing a topic from titles rather than from reading | Read fifteen papers properly first (Part IV) |
| Confusing a domain ("AI in healthcare") with a problem | Apply the funnel to Level 3 and the one-breath test |
| Ignoring licences and ethics until submission | Audit them in week one (§4.6) |
| Ignoring baseline availability until the final month | Clone and run one baseline early (§4.6) |
| Entering a hype peak with no durable core | Balance one visible topic with one durable contribution |
| Assuming your supervisor's approval means the topic is sound | Approval is not critique; seek external criticism |
| Estimating compute as one run per configuration | Use the arithmetic in §4.6.1 |

## 4.8 Verification checklist

- [ ] My area passes all five constraints in Table 4.1, including supervisory capability.
- [ ] I have plotted documents-by-year and can describe the curve shape.
- [ ] I have listed the top five source titles and top five authors in my area.
- [ ] My topic passes the one-breath test with all five slots filled.
- [ ] I can name at least one real dataset, with its licence and access route.
- [ ] I have located at least one baseline implementation and confirmed it runs.
- [ ] I have completed the compute arithmetic and compared it with my actual resources.
- [ ] I have identified my single greatest risk and written one sentence on mitigation.

## Exercises

**Exercise 4.1 — The funnel.** Write your topic at all six levels of Figure 4.1. Most researchers discover they are working at Level 1 or 2 and believe they are at Level 3.

**Exercise 4.2 — Momentum.** Produce the documents-by-year curve for your area. Record the shape, the top five journals, and the top five authors.

**Exercise 4.3 — The feasibility audit.** Complete every row of §4.6 with specifics: dataset names with licences, baseline repository URLs you have actually opened, a GPU-hour figure from §4.6.1.

**Exercise 4.4 — Limitations harvest.** Take ten recent papers. Copy every sentence from their limitations and future-work sections into a spreadsheet, verbatim, with paper and page. You will use this in Chapter 18; it is also the fastest route to a topic.

<div class="pagebreak"></div>

# Chapter 5 — Identifying a Research Problem

## 5.1 Definition

**Definition.** A research problem is a specific, identified absence or inadequacy in current knowledge, whose resolution would change what the field knows or can do, and which is answerable by evidence you can obtain.

Note what this excludes. A research problem is not a *difficulty* (something being hard), not a *task* (something needing to be built), and not a *topic* (something being interesting). It is a specified gap between what is known and what needs to be known.

## 5.2 Research problem versus general problem

A general problem is a state of the world that is unsatisfactory. A research problem is a state of *knowledge* that is incomplete. The two are related but the conversion is not automatic, and doing it explicitly is the core skill of this chapter.

**Table 5.1 — General problems transformed into research problems**

| General problem | Why it is not yet a research problem | Research problem derived from it |
|---|---|---|
| Farmers lose crops to disease | A state of the world; no knowledge claim | *[HYPOTHETICAL]* Leaf-disease classifiers are trained on curated images with uniform backgrounds; their degradation under field illumination and occlusion is unquantified, and it is unknown whether few-shot adaptation recovers it within an edge-device inference budget |
| Our university needs plagiarism detection | A local procurement need | *[HYPOTHETICAL]* Sentence-embedding similarity detectors are validated on monolingual English corpora; their behaviour on code-mixed text is unmeasured, and tokeniser fragmentation is a plausible mechanism of failure |
| Hospitals want automated triage | An aspiration | Model performance reported within one institution may not transfer across institutions (Zech et al., 2018); the magnitude of that gap under leakage-free protocols, and whether it can be mitigated without institutional metadata, is not established |
| Large models are expensive | An observation | *[HYPOTHETICAL]* The accuracy–latency frontier for this task across four model scales on commodity edge hardware has not been characterised, so practitioners cannot select a model for a given latency budget |
| Students find our course difficult | An observation | *[HYPOTHETICAL]* It is unknown which specific misconception accounts for failure on this topic, and whether a targeted intervention addressing it improves outcomes relative to additional practice |

Observe the grammatical signature of the right-hand column. Each contains a *gap marker*: **unquantified**, **unmeasured**, **not established**, **has not been characterised**, **it is unknown which**. If your problem statement contains no such marker, it is probably not yet a research problem.

## 5.3 The four-part test

Apply all four. A statement that fails any one of them is not yet usable.

1. **Is the answer currently unknown in the accessible literature?** Not unknown to you — unknown to the field. Establishing this requires the documented search of Part III. If five papers already answer it, you have found a reading gap in yourself, which is useful but different.

2. **Can it be measured or proven?** Name the measurement or the proof strategy now. If you cannot, the problem is not yet operational.

3. **Would a negative result still be publishable?** This is the sharpest and least-known diagnostic. If the only reportable outcome is "my method wins", you have an advocacy exercise. If both outcomes teach the field something, you have science. Applied to the hospital example: if degradation turns out to be *small*, that is genuinely important news, because it would mean that the published literature can be trusted more than feared. Either way the study is worth doing.

4. **Does it matter to anyone outside your institution?** Name the population who would act differently if they knew the answer: practitioners, other researchers, tool builders, policy makers.

## 5.4 Anatomy of a problem statement

A problem statement is a short piece of formal writing — typically three to six sentences — that appears in your proposal, your introduction, and your funding applications. It has a fixed structure.

**Figure 5.1 — Anatomy of a problem statement**

```
 ┌─ CONTEXT ────────────────────────────────────────────────────────────┐
 │  What domain, why anyone should care. One or two sentences, concrete, │
 │  ideally with a number. No history of the discipline.                │
 └──────────────────────────────────────────────────────────────────────┘
 ┌─ CURRENT STATE ──────────────────────────────────────────────────────┐
 │  What is done now and what it achieves. Cited. Fair to prior work.   │
 └──────────────────────────────────────────────────────────────────────┘
 ┌─ THE INADEQUACY ─────────────────────────────────────────────────────┐
 │  What specifically is missing, wrong, unmeasured, or assumed. This    │
 │  is the pivot of the whole statement. Cite evidence for the claim.    │
 └──────────────────────────────────────────────────────────────────────┘
 ┌─ CONSEQUENCE ────────────────────────────────────────────────────────┐
 │  What cannot currently be done, decided, or trusted as a result.      │
 │  This is where significance lives — not in adjectives.                │
 └──────────────────────────────────────────────────────────────────────┘
 ┌─ SCOPE AND CONSTRAINTS ──────────────────────────────────────────────┐
 │  What you will and will not address. Stating limits early is a mark   │
 │  of competence, not weakness.                                        │
 └──────────────────────────────────────────────────────────────────────┘
```

### 5.4.1 Worked example

**[HYPOTHETICAL] ❌ Weak problem statement.** *"Deep learning has revolutionised medical imaging. Many researchers have proposed models for chest X-ray classification. However, there are still some challenges and limitations. There is a need for a more accurate and efficient model. This research proposes a novel framework to address these challenges."*

Diagnosis: the context is a cliché; "some challenges and limitations" identifies nothing; "a need for a more accurate model" is true of every task forever; no consequence is stated; there is no scope. Nothing here could be false.

**[HYPOTHETICAL, grounded in Zech et al. (2018)] ✅ Improved problem statement.**

> *"Chest radiography is among the most frequently performed diagnostic imaging examinations, and automated triage of abnormal studies has been proposed as a response to radiologist workload [context]. Convolutional and transformer-based classifiers report high discriminative performance on public benchmarks such as CheXpert and MIMIC-CXR [current state]. However, published evidence indicates that such models can learn institution-specific confounders rather than pathology (Zech et al., 2018), and in the studies we surveyed, evaluation is predominantly conducted on random splits in which radiographs from the same institution appear in both training and test partitions [the inadequacy]. Consequently, reported performance figures cannot be interpreted as estimates of cross-institutional performance, and a hospital considering deployment has no basis on which to estimate the accuracy it would actually obtain [consequence]. This study addresses the magnitude of that discrepancy and its mitigation in the setting where institutional metadata is unavailable at training time; it does not address prospective clinical validation or the effect on clinician decision-making [scope]."*

Each clause does one job, the inadequacy is supported by a real citation, the consequence names an affected decision-maker, and the scope pre-empts two obvious reviewer objections.

## 5.5 The mechanism requirement

This section contains the most transferable single technique in Part II.

A very large fraction of weak research problems have the form **"X has not been applied to Y."** This is an absence of *activity*, not an absence of *knowledge*, and it is not a research problem — because the fact that nobody has done something is not evidence that doing it would teach anyone anything.

The conversion is always the same. Ask: **which assumption of X is violated by Y, and what should happen as a result?**

| Weak: absence of activity | Strong: mechanism plus measurement |
|---|---|
| "Transformers have not been applied to language L." | "The subword tokenisers of pretrained transformers are fitted on corpora in which L is scarce; we predict that morphologically rich L suffers excess fragmentation, that fragmentation correlates with error, and we measure both across four language families." |
| "No one has used method M on our sensor data." | "M assumes stationarity; our sensor exhibits documented drift over deployment months. We measure the rate at which M degrades with drift magnitude and test one recalibration strategy." |
| "Nobody has combined A and B." | "A fails on long inputs, B fails on noisy inputs, and the two failure modes are hypothesised to be independent; if so, their combination should be robust to both, which is testable by crossing input length with noise level." |

The mechanism converts a combination into a *prediction*, and a prediction is something an experiment can refute. This is the difference between engineering novelty and scientific contribution.

## 5.6 Common mistakes

| Mistake | Correction |
|---|---|
| A problem statement with no gap marker | Insert *unquantified*, *unmeasured*, *not established*, or *it is unknown whether* — and then justify it |
| "There is a need for a better method" | Better by what measure, relative to what threshold, needed by whom? |
| Stating the inadequacy without evidence | Cite the papers whose limitations or protocols support your claim |
| Restating an engineering requirement | Apply the four-part test (§5.3) |
| "Apply X to Y" with no mechanism | Apply §5.5 |
| Omitting scope, hoping nobody notices | State exclusions explicitly; reviewers respect it |
| Choosing the problem to fit a method already chosen | Reverse the order; reviewers detect retrofitted problems easily |

## Exercises

**Exercise 5.1** Write your problem statement using the five blocks of Figure 5.1, one or two sentences per block. Mark which block is weakest.

**Exercise 5.2** Apply the four-part test. For test 3, write one sentence describing what a negative result would look like and why it would be worth publishing.

**Exercise 5.3** If your problem has the form "apply X to Y", rewrite it using §5.5: name the violated assumption, the predicted consequence, and the measurement.

**Exercise 5.4** Give your problem statement to someone outside your immediate group. Ask them to tell you, in their own words, what is currently unknown. If they cannot, the statement has failed regardless of how clear it seems to you.

<div class="pagebreak"></div>

# Chapter 6 — Research Questions

## 6.1 Definition and purpose

**Definition.** A research question is an interrogative statement that specifies exactly what the study will determine, in terms concrete enough that a reader can tell what evidence would answer it.

**Purpose.** The research question is the hinge of the whole project. It converts a problem (a statement about what is missing) into something that can be *answered*, and thereby determines the design, the data, the metrics, and the structure of the eventual paper. In a well-constructed paper, the results section has one subsection per research question, in order.

## 6.2 Properties of a good research question

| Property | Test |
|---|---|
| **Specific** | Every noun is concrete; no unspecified "various" or "different" |
| **Answerable** | You can describe the experiment or argument that would settle it |
| **Bounded** | It contains one relationship, not three |
| **Non-trivial** | The answer is not already obvious or already published |
| **Informative either way** | Both outcomes advance knowledge |
| **Appropriately scoped** | Answerable with your data, compute, and time |
| **Honest about type** | Descriptive, comparative, or causal — and phrased accordingly |

## 6.3 Question types and the designs they imply

**Table 6.1 — Question types and the study designs they imply**

| Type | Template | Example *[HYPOTHETICAL]* | Design implied |
|---|---|---|---|
| **Descriptive** | How much / how many / what is the distribution of…? | How large is the AUC reduction from random to institution-disjoint evaluation? | Measurement across strata; confidence intervals |
| **Comparative** | Does A differ from B with respect to M? | Does site-adversarial training outperform empirical risk minimisation on worst-institution AUC? | Controlled comparison; equal budgets; paired test |
| **Relational** | How does M vary with X? | How does detection accuracy vary with illumination level? | Stratified measurement; regression or trend analysis |
| **Causal / mechanistic** | Why does A produce B? Which component is responsible? | Which component of the proposed method accounts for the improvement? | Ablation; intervention; one factor at a time |
| **Conditional** | Under what conditions does A hold? | Under what degree of distribution shift does the gain persist? | Systematic variation of the condition until the effect vanishes |
| **Performance / feasibility** | Can the target be met within constraint C? | Can worst-institution AUC exceed 0.85 within a 50 ms inference budget? | Constrained evaluation with cost measurement |
| **Existence** | Does there exist an X such that…? | Is there a label-free procedure attaining most of the label-supervised benefit? | Constructive demonstration plus upper-bound comparison |
| **Synthesis** | What does the evidence collectively show? | What evaluation protocols are used across the literature, and how do they affect reported performance? | Systematic review with structured extraction |

Two practical notes. First, **ordering matters**: descriptive questions should precede comparative ones, which should precede mechanistic ones, because each supplies the context the next requires. Second, **causal phrasing carries obligations**. If your question asks *why*, your design must isolate the cause; observational data plus a *why* question is a validity failure that reviewers reliably catch.

## 6.4 Bad and good research questions

| ❌ Weak question | Diagnosis | ✅ Improved |
|---|---|---|
| Can deep learning be used for chest X-ray classification? | Already answered; answerable by yes | How much does classification performance degrade when random splits are replaced by institution-disjoint splits, across five published architectures? |
| Is our proposed model better? | Better than what, at what, under what conditions? | Does the proposed regulariser improve worst-institution AUC relative to the strongest of four baselines under an identical tuning budget? |
| What are the challenges in domain generalisation? | A literature-review prompt, not a question | Which of three documented failure modes accounts for the largest share of cross-institutional error in this task? |
| How can we improve accuracy? | Unbounded | Does inferring pseudo-domains by clustering embedding statistics recover a majority of the benefit obtained with true domain labels? |
| Does the model work well? | "Well" is undefined | Does the model attain sensitivity ≥ 0.90 at specificity 0.95 on each of three external institutions? |
| What is the effect of various hyperparameters on different datasets? | Two unspecified plurals; unbounded | How sensitive is worst-institution AUC to the invariance weight λ over the range 0.1–10 on three datasets? |

## 6.5 Frameworks for constructing questions

Several disciplines have formalised question construction. All are variations on "name your components explicitly", and any of them is better than none.

**PICO** (health sciences): **P**opulation, **I**ntervention, **C**omparison, **O**utcome. Widely used to frame systematic-review questions.

**PICOC** adds **C**ontext, which is useful in engineering and software research where setting dominates.

**A computational adaptation.** For machine-learning and data-science work, the following six slots map more directly onto what a paper must report:

| Slot | Content | Example *[HYPOTHETICAL]* |
|---|---|---|
| **D** — Data | Population, datasets, split unit | CheXpert, MIMIC-CXR, ChestX-ray14; split by institution |
| **M** — Method | The intervention | Clustering-based invariance regulariser |
| **B** — Baseline | The comparison | ERM, Mixup, CORAL, IRM, at equal tuning budget |
| **C** — Condition | The circumstance varied | Random versus institution-disjoint evaluation |
| **O** — Outcome | Metrics, with the decision they serve | Macro AUC, worst-institution AUC, expected calibration error |
| **T** — Threshold | What would count as a meaningful effect | ≥ 0.03 AUC, judged against seed variance |

Filling all six slots produces a research question, an experimental design, and the skeleton of your results tables simultaneously. The **T** slot is the one most often omitted and the most valuable: deciding in advance what size of effect would matter prevents the common outcome of celebrating a statistically detectable but practically irrelevant difference.

## 6.6 From problem to questions: worked conversion

Take the inadequacy identified in §5.4.1. Each clause of the gap converts mechanically into a question.

| Gap clause | Question |
|---|---|
| "…reported figures cannot be interpreted as cross-institutional performance" | **RQ1** (descriptive) How large is the difference between random-split and institution-disjoint performance across published architectures? |
| "…mitigation in the setting where institutional metadata is unavailable" | **RQ2** (comparative) Can a method that does not use institutional labels match methods that do? |
| "…a hospital has no basis to estimate accuracy it would obtain" | **RQ3** (conditional) Is worst-institution performance predictable from properties observable before deployment? |
| implied by any improvement claim | **RQ4** (mechanistic) Which component of the proposed method accounts for the observed improvement? |

Notice that four questions of four different types emerged from one problem statement, and that together they specify a complete study. This is the normal relationship: one problem, two to four questions, each answerable by a distinct experiment.

## 6.7 Common mistakes

| Mistake | Correction |
|---|---|
| Questions answerable by yes or no alone | Prefer *how much*, *under what conditions*, *which component* |
| Three relationships in one question | Split into separate numbered questions |
| Questions no experiment could settle | Specify the measurement, or discard the question |
| Causal phrasing on observational evidence | Change the phrasing or add an intervention |
| Questions written after the experiments | Reviewers detect this; pre-specify instead (§3.4) |
| No threshold for a meaningful effect | Fill the **T** slot before collecting data |
| Ten questions | Three or four; a paper cannot defend more |

## Exercises

**Exercise 6.1** Convert your problem statement into two to four research questions using the mechanical procedure of §6.6, and label each with its type from Table 6.1.

**Exercise 6.2** Fill the six DMBCOT slots (§6.5) for your principal question. Any slot you cannot fill is an unmade design decision.

**Exercise 6.3** For each question, write the single sentence that would appear in your results section if the answer were *no*. If any of those sentences would be unpublishable, revisit the question.

<div class="pagebreak"></div>

# Chapter 7 — Research Objectives

## 7.1 Five statements and how they differ

Beginners routinely conflate these five. Examiners and reviewers do not, and the distinctions are load-bearing.

**Figure 7.1 — Aim, objectives, questions, hypotheses, and contributions**

```
  AIM             ONE sentence. The overall purpose. Broad but bounded.
   │              "To establish how much X degrades and whether Y mitigates it."
   │
   ├─ QUESTIONS   2–4 interrogatives. What will be determined.
   │              "RQ1: How large is the degradation?"
   │
   ├─ OBJECTIVES  3–5 commitments to work. "To + measurable verb + object + condition."
   │              "O1: To re-evaluate five architectures under both protocols…"
   │
   ├─ HYPOTHESES  Falsifiable predictions with a named test.
   │              "H1: institution-disjoint AUC is lower (paired Wilcoxon, α=0.05)."
   │
   └─ CONTRIBUTIONS  2–4 noun phrases. What the field gains afterwards.
                  "C1: the first leakage-free multi-institution quantification of…"

  TRACEABILITY REQUIREMENT
  ┌───────────┬──────────┬──────────────────┬──────────────┐
  │ Objective │ Method   │ Results section  │ Contribution │
  ├───────────┼──────────┼──────────────────┼──────────────┤
  │ O1        │ §III-A   │ §V-A             │ C1           │
  │ O2        │ §III-B   │ §V-B             │ C2           │
  │ O3        │ §III-C   │ §V-C             │ C3           │
  └───────────┴──────────┴──────────────────┴──────────────┘
  Every row must be complete. An objective with no results section reads as an
  abandoned promise; a results section with no objective reads as an afterthought.
```

| Statement | Count | Grammatical form | Function |
|---|---|---|---|
| **Aim** | exactly 1 | "To + purpose" | Orientation; the destination |
| **Question** | 2–4 | Interrogative | What will be determined |
| **Objective** | 3–5 | "To + measurable verb + object + condition" | Commitment to specific work |
| **Hypothesis** | 1–4 | Declarative prediction, with test and α | What you expect, refutably |
| **Contribution** | 2–4 | Calibrated noun phrase | What the field retains |

## 7.2 Writing measurable objectives

**Procedure.**

1. Begin with **"To"** followed by a verb whose completion is *observable*.
2. Name the **object** — what exactly is acted upon.
3. Add the **condition or scope** — on what data, under what protocol, with what comparison.
4. Where possible, name the **outcome measure**.
5. Verify that an examiner could mark the objective *done* or *not done* without argument.

**Verbs that work:** quantify, measure, compare, characterise, derive, prove, construct, annotate, validate, determine, isolate, evaluate, establish.

**Verbs and phrases that fail:** study, analyse, investigate, explore, look into, understand, work on, develop a framework for, implement. These name activities with no completion criterion. (*Investigate* and *explore* are acceptable in genuinely exploratory studies — §2.5 — but then the objective must specify what will be produced.)

**Table 7.1 — Weak and strong research objectives**

| ❌ Weak objective | Why it fails | ✅ Strong objective |
|---|---|---|
| To study deep learning for medical imaging | No boundary, no completion criterion | To quantify the change in macro AUC and worst-institution AUC of five published architectures when random splits are replaced by institution-disjoint splits, across three public datasets and ten seeds |
| To implement a CNN model | An activity completable in a day; no knowledge | To determine whether label-free pseudo-domain inference recovers at least half of the worst-institution improvement achieved with true domain labels |
| To improve accuracy | Unquantified; no comparison point | To reduce worst-institution AUC degradation by at least 0.03 relative to empirical risk minimisation at equal parameter count and inference latency |
| To analyse various algorithms | "Various" is unspecified | To compare ERM, Mixup, CORAL, and IRM under an identical 50-trial tuning budget on identical splits |
| To develop a novel framework | Unfalsifiable; "framework" hides the claim | To construct and evaluate an adaptation module requiring no institutional metadata, assessed on worst-institution AUC, calibration error, and inference latency |
| To achieve 99% accuracy | Fixates on a number that may be meaningless or unattainable | To characterise the accuracy–latency trade-off across four model scales on a specified edge device |
| To explore the potential of transformers | No output specified | To determine which of three transformer variants attains the best worst-group performance under a fixed 12 GB memory budget |

## 7.3 Hypotheses

Not every discipline states hypotheses explicitly — much computational work does not — but **writing them anyway is a diagnostic**, because a hypothesis you cannot phrase is usually a hypothesis your experiment cannot test.

**Form.** State a null and an alternative, name the test, and fix the significance level *before* looking at results.

**[HYPOTHETICAL] Example.**

| | Statement |
|---|---|
| **H0** | Macro AUC does not differ between random-split and institution-disjoint evaluation. |
| **H1** | Macro AUC is lower under institution-disjoint evaluation. |
| **Test** | Paired Wilcoxon signed-rank across architecture × dataset pairs; α = 0.05; Holm correction across five architectures. |
| **Effect size** | Reported as the mean difference with a 95% bootstrap confidence interval. |
| **H2** | Label-free pseudo-domain inference improves worst-institution AUC by ≥ 0.03 over ERM. |

Three rules that prevent the most common statistical failures:

1. **Pre-specify the test.** Choosing a test after seeing which one gives significance is *p*-hacking (§3.4, §49).
2. **Report an effect size, not only a *p*-value.** With enough seeds, a difference of 0.001 becomes statistically detectable and remains practically worthless.
3. **Correct for multiple comparisons.** Testing five architectures × three datasets is fifteen comparisons; uncorrected, roughly one spurious "significant" result is expected by chance at α = 0.05.

## 7.4 Contributions

Contributions are covered fully in Chapter 21. Two points belong here because they constrain how objectives are written.

**Contributions must map one-to-one onto objectives.** If you have four objectives and two contributions, either two objectives are not producing knowledge, or you are under-claiming. If you have two objectives and five contributions, you are inflating.

**Contributions must be calibrated.** Compare:

> **[HYPOTHETICAL] ❌** "We propose a novel state-of-the-art framework that solves cross-domain generalisation."
>
> **[HYPOTHETICAL] ✅** "We provide the first leakage-free multi-institution quantification of degradation for five widely used architectures, with confidence intervals and paired tests; and a label-free adaptation module that recovers approximately 82% of the benefit obtained by methods using privileged institutional labels, at equal parameter count."

The second is longer, more specific, bounded, and — critically — much harder for a reviewer to refute.

## 7.5 Common mistakes

| Mistake | Correction |
|---|---|
| Objectives beginning "Study of…" or "Analysis of…" | Use an observable verb and a completion criterion |
| Objectives that are really methods | An objective states what will be *determined*; the method states *how* |
| Seven or eight objectives | Three to five; more cannot be defended in one paper |
| Objectives with no corresponding results section | Complete the traceability table (Figure 7.1) |
| Hypotheses written after seeing results | Pre-specify and date them |
| *p*-values without effect sizes | Report both, always |
| No multiple-comparison correction | Apply Holm or an equivalent when testing many pairs |
| Contributions that restate the method three times | Distinct, auditable contributions only |

## 7.6 Verification checklist for Part II

- [ ] My topic passes the one-breath test (§4.3.1).
- [ ] I have completed the feasibility audit with specifics (§4.6).
- [ ] My problem statement has all five blocks of Figure 5.1.
- [ ] My problem contains an explicit gap marker and passes the four-part test (§5.3).
- [ ] If my problem was "apply X to Y", I have added a mechanism (§5.5).
- [ ] I have two to four research questions, each typed (Table 6.1).
- [ ] I have filled all six DMBCOT slots, including the effect-size threshold (§6.5).
- [ ] Every objective starts with "To" plus an observable verb and can be marked done or not done.
- [ ] My hypotheses name a test and an α, and are dated before results.
- [ ] The traceability table in Figure 7.1 is complete, with no empty cells.

## Exercises

**Exercise 7.1** Write one aim, three to five objectives, and two to four contributions for your project. Check each objective against Table 7.1.

**Exercise 7.2** Complete the traceability table. Any empty cell is either missing work or an unnecessary claim.

**Exercise 7.3** Write H0 and H1 for your principal comparison, naming the test, α, and correction. Date the entry in your research journal.

**Exercise 7.4 — Examiner simulation.** Give your objectives to a colleague and ask them to mark each *done* or *not done* as though the work were finished. Any objective they cannot mark must be rewritten.

<div class="pagebreak"></div>
