# PART I — UNDERSTANDING RESEARCH

<div class="partintro">

Part I establishes the conceptual foundation on which everything else in this handbook depends. Chapter 1 defines research and, more importantly, distinguishes it from the activities it is most often confused with — building systems and solving problems. Chapter 2 surveys the types of research and shows how the type is dictated by the question rather than chosen for convenience. Chapter 3 lays out the complete research lifecycle, stage by stage, with the decisions and failure modes attached to each.

Readers who are impatient to begin searching the literature may be tempted to skip to Part III. Resist this. The single most expensive error in research is not a badly executed experiment; it is a well-executed experiment that answers a question nobody was asking. Parts I and II exist to prevent that.

</div>

<div class="pagebreak"></div>

# Chapter 1 — What Is Research?

## 1.1 Definition

**Definition.** Research is a systematic, documented, and critically evaluated process of inquiry that produces knowledge which did not previously exist in the accessible record, in a form that others can independently verify.

Every clause in that sentence carries weight, and it is worth unpacking each before going further.

**Systematic.** The inquiry follows a procedure that was chosen in advance for reasons that can be stated. The opposite is not disorder but *opportunism* — trying things until something works and then reporting the thing that worked as though it had been the plan. The test of whether your process is systematic is not whether it felt organised but whether a competent stranger could repeat it from your description.

**Documented.** The procedure, the data, the analysis, and the reasoning are recorded in sufficient detail that they can be examined. Undocumented research is indistinguishable from assertion.

**Critically evaluated.** The researcher actively attempts to find reasons why the conclusion might be wrong — alternative explanations, confounds, limits of applicability — and reports what that attempt found. This is the hardest of the four and the one most often skipped, because it requires arguing against your own result.

**Produces knowledge that did not previously exist in the accessible record.** Two qualifications matter here. *Accessible* means published, indexed, and findable — knowledge that exists inside your own head, or inside your company, or in an unpublished thesis nobody can obtain, has not yet entered the record. *Did not previously exist* is a claim about the literature, not about your personal awareness; the fact that you did not know something is not evidence that the field did not know it. Establishing this claim is the entire purpose of Parts III to VI of this handbook.

**In a form that others can independently verify.** Verification is what separates research from expert opinion. A result that only you can obtain, because only you have the data or only you know the undocumented preprocessing step, is a claim rather than a finding.

## 1.2 The purpose of research

It is worth being concrete about *why* this activity is organised the way it is, because the conventions of research writing — which can appear arbitrary and bureaucratic to a newcomer — are almost all consequences of its purpose.

Research exists to build a **cumulative, correctable body of knowledge**. Cumulative means each contribution is designed to be built upon by strangers; correctable means each contribution is designed to be *checked*, and overturned if wrong. Nearly every convention that frustrates early-career researchers follows from these two requirements:

| Convention | Purpose it serves |
|---|---|
| Citing prior work | Makes the increment visible; locates your claim in the cumulative structure |
| Describing method in tedious detail | Enables independent verification and reuse |
| Comparing against baselines | Distinguishes your contribution from the difficulty of the task |
| Reporting limitations | Tells later researchers where the claim stops being safe |
| Peer review | Filters claims before they enter the record others will build on |
| Reporting variance and statistics | Allows a reader to judge whether the effect is real |
| Publishing negative and null results | Prevents the field repeating your dead end |

Once you see the conventions as engineering solutions to the problem of building shared, checkable knowledge, they stop being hoops to jump through. A reviewer who demands a missing baseline is not being obstructive; they are protecting the cumulative property. A reviewer who asks for confidence intervals is protecting the correctable property.

## 1.3 Research versus project development

This is the distinction that determines whether most early-career work becomes publishable, and it causes more confusion than any other topic in this handbook — particularly in computer science, where the two activities look almost identical from the outside and use the same tools.

**Table 1.1 — Research versus project development**

| Dimension | Project / development | Research |
|---|---|---|
| **Goal** | Deliver a working artefact | Produce verifiable new knowledge |
| **Success criterion** | It works, on time, to specification | A claim is novel, significant, and validated |
| **Question form** | "How do I build X?" | "Under what conditions does X hold, and why?" |
| **Comparison** | Against requirements | Against baselines and the state of the art |
| **Evaluation** | Testing, user acceptance | Controlled experiment, statistics, ablation |
| **Meaning of failure** | A defect to be fixed | A *finding* to be reported and explained |
| **Reuse of existing work** | Encouraged and sufficient | Necessary but insufficient — must be exceeded or examined |
| **Generalisation** | Usually irrelevant | Usually the whole point |
| **Primary output** | Software, report, demonstration | Paper, dataset, theorem, protocol |
| **Audience** | Users, client, institution | The field, indefinitely |

The relationship between the two is not opposition. Most computational research *contains* a development project. The project is the **instrument**; the knowledge claim is the **product**. A telescope is an engineering achievement; "Jupiter has moons" is the discovery. Papers are cited for discoveries, not for instruments — which is why a paper that reports only the instrument reads to a reviewer as a technical report that has been submitted to the wrong kind of venue.

### 1.3.1 The diagnostic question

Here is the fastest way to classify your own work. Ask:

> **If my system works exactly as intended, what will the field know that it did not know before?**

Three kinds of answer are possible.

- **A specific, transferable statement** — "that cross-institutional degradation in this task is approximately 0.12 AUC under leakage-free evaluation", or "that this class of method fails when the input distribution has property P". This is research.
- **"That my system works"** — this is development. It may be excellent, useful, fundable development. It is not yet a research contribution.
- **"I am not sure"** — this is the most common and most rescuable answer. It means you have an instrument and have not yet chosen a question. Chapters 4 and 5 exist for exactly this situation.

### 1.3.2 Worked rescue: three development projects turned into research

The following transformations are the single most useful skill in Part I. Notice that in each case the *engineering work barely changes* — what changes is what is measured, what it is compared against, and what is claimed.

**[HYPOTHETICAL] Example A.** *Development framing:* "Build a web system that detects plagiarism in student assignments for our department."

This is bounded by a local need, solvable by integrating existing tools, and successful when deployed. Generalisation is irrelevant. No baseline comparison is required.

*Research framing:* "Sentence-embedding plagiarism detectors are reported at high F₁ on English benchmarks. Their behaviour on **code-mixed** student text (for example Hindi–English) is unmeasured, and there is reason to expect degradation: the subword tokenisers used by these models are trained predominantly on monolingual corpora, so transliterated and code-switched text fragments into unfamiliar subword sequences. We quantify the degradation across four levels of obfuscation and test whether script normalisation recovers it."

What changed: a *mechanism hypothesis* (tokeniser fragmentation) was added, a *measurable outcome* was specified, and the claim became transferable to anyone working on multilingual text.

**[HYPOTHETICAL] Example B.** *Development framing:* "Apply YOLO to helmet detection for traffic enforcement."

*Research framing:* "Object detectors are typically benchmarked on datasets whose images are well-lit and lightly occluded. We characterise how detection performance on two-wheeler helmet compliance degrades across illumination and occlusion strata in naturalistic traffic imagery, and measure whether a lightweight image-enhancement front-end recovers performance within a fixed edge-inference latency budget."

What changed: the study now measures a *degradation curve* across conditions rather than a single accuracy number, and introduces a *constraint* (latency budget) that makes the trade-off scientifically interesting rather than merely engineering-adjacent.

**Example C, grounded in real literature.** *Development framing:* "Train a CNN to detect pneumonia on chest radiographs."

This has been done many times and is not a contribution. But the *real* published literature provides the rescue. Zech et al. (2018) showed that convolutional networks trained on chest radiographs can learn to exploit hospital-specific confounders — such as differences in equipment or department-level disease prevalence — with the consequence that performance measured within one institution substantially overstates performance at a new one. That observation converts a saturated engineering task into a live research area, because it implies that a large body of reported performance numbers may not describe what they appear to describe.

*Research framing built on it:* "We re-evaluate published architectures under institution-disjoint protocols and quantify the degradation, then test whether it can be mitigated without access to institutional metadata."

The general lesson: **an engineering task becomes a research question when you find a reason to doubt what the reported numbers mean.**

## 1.4 Research versus problem solving

Problem solving and research overlap but are not the same, and the difference is instructive.

Solving a problem means moving a specific situation from an undesired state to a desired one. It is complete when the situation is resolved. Research means producing a statement about a *class* of situations, and it is complete when the statement is established and its limits are known.

An engineer who fixes a memory leak has solved a problem. A researcher who characterises the class of allocation patterns under which this family of runtimes leaks, and demonstrates the boundary conditions, has produced knowledge. The first is worth doing and stops mattering when the software is retired. The second remains true afterwards.

This distinction has a practical consequence for how you frame work in a paper. Reviewers react badly to papers that read as case reports — "we had this problem, we did these things, it improved" — not because the work is worthless but because there is no statement whose generality can be assessed. The fix is to identify what class your specific case belongs to, and to say something about the class.

## 1.5 Scientific investigation and evidence-based research

**Scientific investigation** is the practice of subjecting a candidate explanation to a test that could have refuted it. The critical phrase is *could have refuted it*. A test that would produce the same outcome whether or not your explanation is correct provides no evidence, however elaborate it is.

This has a sharp practical implication for computational research. Suppose your hypothesis is that a new attention mechanism improves performance because it captures long-range dependencies. Running your model and observing higher accuracy does not test that hypothesis, because higher accuracy is also consistent with a dozen other explanations: more parameters, more effective regularisation, a longer training schedule, a luckier initialisation, or unequal hyperparameter tuning effort. To *test* the hypothesis you need a comparison in which only the mechanism differs — which is what an ablation study is for (§26.6), and why an ablation is not an optional extra but the core evidential instrument for a mechanistic claim.

**Evidence-based research** means that each claim in your paper is traceable to something specific: a measurement, a proof, a cited result, or a documented observation. In practice this means being able to answer, for any sentence in your paper, the question *how do you know that?* The three acceptable answers are:

1. **We measured it** — and here is the experiment, the variance, and the statistical test.
2. **It is established in the literature** — and here is the citation, which we have read.
3. **It is a definition or a logical consequence** — and here is the derivation.

A fourth answer — *it is generally believed* or *it is well known* — is acceptable only for genuine textbook material, and is a frequent hiding place for unexamined assumptions. If you find yourself writing "it is well known that", stop and check whether it is known at all.

## 1.6 Originality and novelty

These terms are used loosely in everyday speech and need to be separated.

**Originality** is a property of the *work*: it was produced by you, not copied. Originality is a baseline requirement and its absence is misconduct (Part XIV).

**Novelty** is a property of the *contribution relative to the literature*: the knowledge is new to the field. Novelty is what makes work publishable and its absence is not misconduct — it is simply redundancy.

The two are independent. A study can be entirely original and completely unnovel: you may have honestly and independently discovered something that four other groups published in 2021. This is an ordinary experience and the appropriate response is not embarrassment but reframing — usually by asking what your version does that theirs does not, or by reporting the independent replication as such, which is a genuine contribution in its own right.

Novelty is discussed in depth in Chapter 20. Two points belong here because they shape how you should think from the beginning:

**Novelty is not a binary.** It is a spectrum from *incremental* (a better result on an established problem by an established route) through *substantive* (a new method, a new resource, a new evaluation protocol) to *paradigmatic* (a reframing of what the problem is). Almost all published research, including almost all *good* published research, is in the first two categories. The expectation that a PhD must be paradigmatic is a major and unnecessary source of paralysis.

**Novelty is not the same as difficulty.** Work can be extremely laborious and add nothing, and it can be conceptually simple and change a field. Reviewers assess what is *learned*, not what was *endured*. This is counter-intuitive and worth internalising early, because a great deal of effort is routinely spent on work whose difficulty is not converting into knowledge.

## 1.7 Four properties of trustworthy findings

Four terms are used constantly in research writing and are frequently confused with one another. They are not interchangeable, and reviewers use them precisely.

**Table 1.2 — Validity, reliability, reproducibility, generalizability**

| Property | Question it answers | Threat if absent | Concrete example of failure |
|---|---|---|---|
| **Validity** | Are we measuring what we claim to measure? | The result is about something other than what you say | A model that appears to detect disease is detecting scanner artefacts |
| **Reliability** | Would repeating the measurement give a consistent answer? | The result is noise | Reported gain of 0.4 points where seed-to-seed variation is 1.5 points |
| **Reproducibility** | Can others obtain this result from your materials? | The result cannot be checked | Numbers unobtainable from the released code |
| **Generalizability** | Does the result hold beyond the studied sample? | The result is true but useless | Accuracy holds on one hospital's data and collapses elsewhere |

### 1.7.1 Validity, and the vocabulary of validity threats

Validity is subdivided in the methodological literature, and the vocabulary is worth knowing because reviewers use it.

- **Construct validity** — does your measurement correspond to the concept you claim? If you claim to measure "code readability" using cyclomatic complexity, a reviewer may reasonably dispute the construct.
- **Internal validity** — within your study, is the observed relationship attributable to the factor you manipulated, rather than to a confound? Unequal hyperparameter tuning between your method and the baseline is an internal validity threat. So is data leakage.
- **External validity** — does the result transfer to other populations, domains, and settings? Single-dataset studies are weak here by construction.
- **Conclusion validity** (sometimes *statistical conclusion validity*) — do your statistical procedures support the inference you draw? Reporting a gain without variance, or selecting the one comparison that reached significance, are threats here.

These four categories, which originate in the experimental design literature (Campbell and Stanley, 1963; Shadish, Cook and Campbell, 2002) and are widely applied in empirical software engineering (Wohlin et al., 2012), give you the standard structure for a "Threats to Validity" section — and, more usefully, a checklist to run against your own design *before* you collect data.

### 1.7.2 Reproducibility: terminology and why it matters

Terminology in this area is genuinely inconsistent across communities, which is worth knowing so you are not confused by conflicting definitions. A widely used convention distinguishes:

- **Repeatability** — the same team, the same setup, obtains the same result.
- **Reproducibility** — a *different* team, the same artefacts (code, data), obtains the same result.
- **Replicability** — a different team, *independently implemented*, obtains a consistent result.

Some communities swap the last two. When precision matters, state what you mean rather than relying on the label.

The practical importance is not philosophical. Large-scale surveys and structured re-evaluations across several fields have repeatedly found that a substantial fraction of published results are hard to obtain independently, and that apparent improvements sometimes disappear when comparisons are made under equal conditions. Baker (2016) reported survey evidence of widespread concern about reproducibility across scientific disciplines. In machine learning specifically, methodological critiques and re-evaluation studies — for example Sculley et al. (2018) on empirical rigour, Lipton and Steinhardt (2019) on failure modes of scholarship, Dacrema et al. (2019) on recommender-system baselines, Melis et al. (2018) on language-model baselines, and Lucic et al. (2018) on generative adversarial network comparisons — have documented cases in which reported gains narrowed or vanished once baselines were tuned with comparable effort.

Two conclusions follow, and they are among the most actionable in this handbook:

1. **Tune your baselines as hard as you tune your own method, and say so in the paper.** One sentence stating that all methods received an identical search budget removes the most common reason reviewers distrust an improvement claim.
2. **The reproducibility gap is a research opportunity.** A rigorous re-evaluation requires careful experimental work rather than new theory or large compute, which makes it achievable for a researcher with modest resources, and such studies are frequently well cited because they change practice. This is developed in §17.10.

### 1.7.3 Reliability in practice: the single-run problem

A very common defect in student work is reporting a single run to four decimal places. Stochastic training procedures produce a *distribution* of outcomes; a single sample from that distribution is not an estimate of the method's quality, and the difference between two single samples is not evidence of a difference between two methods.

The remedy is mechanical and cheap: run each configuration with at least five different random seeds — ten is better — and report the mean with a standard deviation or a confidence interval. `0.822 ± 0.009` is more informative than `0.8221`, and it is the form that allows a reader to judge whether your improvement of `0.014` means anything. Statistical testing is covered in §26.8 and §29.5.

## 1.8 What makes a contribution rather than an implementation

We can now state the distinction precisely. Consider three levels:

**Figure 1.1 — The relationship between activity, evidence, and contribution**

```
  ACTIVITY                 EVIDENCE                    CONTRIBUTION
  what you did             what you measured           what the field gains
  ─────────────            ─────────────────           ────────────────────
  "We trained a      →     "It reached 0.94      →     ??? nothing, if this
   DenseNet on              accuracy on the             number is already
   CheXpert."               official test split."       in the literature

  "We re-split       →     "Macro AUC falls        →   "Reported CXR
   three public             from 0.897 to 0.781        performance overstates
   datasets by              (95% CI 0.104–0.128         cross-hospital
   institution and          reduction) across five      behaviour by roughly
   re-evaluated five        architectures, over         0.12 AUC under
   published models."       10 seeds."                  leakage-free
                                                        evaluation."
```

*[HYPOTHETICAL — numbers illustrative]*

The activity in the second row is *less* technically demanding than in the first: no new architecture, no novel loss. Yet it produces a contribution, because it produces a statement about the world that other researchers must now take into account.

This is the mechanism by which researchers with limited computational resources produce influential work. You do not need to out-train a large laboratory. You need to ask a question whose answer changes what people should do.

### 1.8.1 The seven categories of contribution

It helps enormously to know explicitly which kind of contribution you are making, because each requires a different kind of evidence.

| Contribution type | What you claim | Evidence required |
|---|---|---|
| **New method** | A procedure that achieves something previously unachieved or achieves it better | Fair comparison, ablation isolating the novel component, statistics |
| **New theory or analysis** | A proof, bound, complexity result, or formal characterisation | Correct derivation; assumptions stated; ideally empirical corroboration |
| **New empirical knowledge** | A measured fact about the world or about existing methods | Careful measurement, controls, variance, replication across settings |
| **New resource** | A dataset, benchmark, corpus, or tool others will use | Construction protocol, quality assessment, annotation agreement, licence, baselines |
| **New evaluation** | A protocol or metric that measures something better | Demonstration that existing evaluation is inadequate; validation of the new one |
| **Synthesis** | An organised, critical account of a body of work | Reproducible search protocol, systematic screening, comparative analysis |
| **Reproduction or refutation** | An existing result does or does not hold | Faithful re-implementation, documented discrepancies, diagnosis of cause |

Most early-career researchers assume "new method" by reflex. In practice the strongest achievable first papers are frequently in the *new empirical knowledge*, *new resource*, *new evaluation*, and *reproduction* categories, because they are completable within a year, require modest compute, and are difficult for a reviewer to dispute when done rigorously.

## 1.9 Weak and strong research, weak and strong contributions

The following contrasts are deliberately concrete. All are hypothetical formulations constructed to illustrate the pattern.

### 1.9.1 Weak research

**[HYPOTHETICAL] ❌** *"We propose a novel hybrid CNN-LSTM framework for sentiment classification. Experiments on a benchmark dataset show that our model achieves 92.4% accuracy, outperforming existing state-of-the-art methods and demonstrating the effectiveness of the proposed approach."*

What is wrong, in order of severity:

1. **No question.** Nothing was unknown at the start; nothing is known at the end beyond one number.
2. **No mechanism.** Why should combining these components help? Without a stated reason, there is nothing to test and no explanation to transfer.
3. **"A benchmark dataset."** One dataset supports no generalisation claim, and it is not even named.
4. **"Existing state-of-the-art methods"** — unnamed, so the comparison is unauditable; and probably not tuned with equal effort.
5. **No variance, no statistical test.** 92.4% from how many runs?
6. **"Demonstrating the effectiveness"** — a conclusion restating the result, not interpreting it.
7. **Unfalsifiable framing.** There is no outcome of this study that would have been reported as informative other than "we won".

### 1.9.2 Strong research on the same topic

**[HYPOTHETICAL] ✅** *"Reported gains from recurrent components in sentiment classification are typically measured on datasets whose documents are short. We hypothesise that these gains are a function of document length and largely vanish once transformer context windows exceed typical document length. We test this by evaluating four architectures across five corpora stratified into four document-length bands, with an identical 50-trial tuning budget per architecture per band and ten seeds each. Recurrent components yield a mean improvement of 2.1 points macro-F₁ in the shortest band (95% CI 1.4–2.8) but no detectable improvement in the two longest bands (95% CI includes zero). This suggests that a portion of previously reported architectural gains is attributable to corpus composition rather than to modelling capacity."*

Why this is strong:

- It states a **hypothesis with a mechanism** (document length) that could have been refuted.
- The design **isolates the factor** by stratifying on it.
- **Fairness is controlled** and stated (equal tuning budget).
- **Uncertainty is quantified**, and a null result in two bands is *reported rather than hidden*.
- The conclusion is a **transferable statement about the literature**, not about the authors' model.
- The finding would have been publishable in either direction.

### 1.9.3 Weak and strong contribution statements

| **[HYPOTHETICAL] ❌ Weak** | Why it fails | **[HYPOTHETICAL] ✅ Strong** |
|---|---|---|
| "We propose a novel deep learning framework." | "Framework" conceals what the thing is; "novel" is asserted, not demonstrated | "We propose a site-clustering regulariser that requires no institutional metadata at training time." |
| "Our method outperforms state-of-the-art methods." | Unbounded, unquantified, invites a counterexample | "Our method improves worst-institution AUC by 0.041 (95% CI 0.032–0.050) over the strongest of four baselines under an identical tuning budget." |
| "We achieve high accuracy." | Relative to what threshold, on what data? | "We recover approximately 82% of the benefit obtained by methods that require privileged site labels, without using them." |
| "This is the first work in this area." | Almost always falsifiable by a specialist | "To our knowledge this is the first leakage-free multi-institution evaluation of these five architectures; the closest prior study [ref] evaluates two of them on a single external set." |
| "We solve the problem of domain shift." | Overclaim | "We reduce, but do not eliminate, cross-institution degradation; approximately 0.075 AUC of the observed 0.116 gap remains." |

Note the pattern: strong statements are **longer**, contain **numbers with uncertainty**, name their **scope**, and **concede** what they do not achieve. Calibrated claims are not weaker than bold ones — they are harder to attack, and reviewers read calibration as competence.

## 1.10 Common mistakes in conceptualising research

| Mistake | Why it happens | Correction |
|---|---|---|
| Treating the implementation as the contribution | Engineering training rewards working artefacts | Ask: what will the field *know*? |
| Choosing the method before the question | Methods are exciting; questions are hard | Derive the method from the gap (Part VI) |
| Assuming novelty requires a new architecture | Visibility of high-profile architecture papers | Review the seven contribution types (§1.8.1) |
| Equating effort with contribution | Effort is what the researcher experiences | Reviewers assess what is learned |
| Reporting only favourable outcomes | Fear that null results are failures | Design so that either outcome is informative |
| Believing a single run is a result | Deadline pressure; compute cost | Five seeds minimum; report variance |
| Using "it is well known that" | Convenient; avoids searching | Either cite it or measure it |
| Confusing "nobody has done this" with a gap | Superficially resembles novelty | Add a mechanism and a measurement (§19.3) |

## 1.11 Verification checklist for Chapter 1

Before proceeding, confirm that you can answer each of these about your own work.

- [ ] I can state, in one sentence, what the field will know if my study succeeds.
- [ ] That sentence is about a class of situations, not only about my system.
- [ ] I can name which of the seven contribution types (§1.8.1) I am attempting.
- [ ] I can name the evidence that contribution type requires.
- [ ] I can state a mechanism — a reason why my approach should work — that could turn out to be wrong.
- [ ] I have identified at least one outcome, other than "my method wins", that would be worth reporting.
- [ ] I can name the principal threat to internal validity in my planned design.
- [ ] I can name the principal threat to external validity.
- [ ] I know how many seeds or repetitions I will run, and how I will report variance.
- [ ] I have not used the words "novel", "framework", or "state of the art" in my own description without being able to justify each.

## Exercises

**Exercise 1.1 — Classification.** Write your current work in one sentence. Classify it as project development, research, or unclear. If project or unclear, complete this sentence: *"The field does not currently know whether ______, and this study would show it."*

**Exercise 1.2 — The mechanism test.** State why your approach should work, in the form *"Because [property of the problem], [property of the method] should produce [effect]."* If you cannot fill all three slots, you have an implementation plan and not yet a hypothesis.

**Exercise 1.3 — The falsifiability test.** Describe the result you expect. Then describe the opposite result. Write one sentence explaining why the opposite result would still be worth publishing. If you cannot, revisit §1.9.

**Exercise 1.4 — Contribution typing.** Identify which of the seven contribution types your work targets. Then list the specific evidence that type demands, and mark each item as *already planned* or *missing*. The missing items are your experimental to-do list.

**Exercise 1.5 — Critical reading.** Take any paper in your area. Identify (a) the activity, (b) the evidence, (c) the contribution, in the sense of Figure 1.1. If you cannot find (c), you have learned something important about the standards of the venue that published it.

<div class="pagebreak"></div>


# Chapter 2 — Types of Research

## 2.1 Why classification matters practically

Research typologies can feel like taxonomy for its own sake. They are not. The type of research you are conducting determines four concrete things:

1. **What counts as adequate evidence** — a proof, a controlled experiment, a saturated set of interviews, or a reproducible synthesis.
2. **What your validity threats are** — and therefore what a reviewer will attack.
3. **What reporting standard applies** — for example PRISMA for systematic reviews (Page et al., 2021), or the reporting conventions of your subfield.
4. **Where it can be published** — venues differ sharply in the types they accept.

Choosing a type by convenience, and then discovering that your evidence does not match your claim, is a common and expensive error. The type should be *derived from the question*.

## 2.2 By purpose: fundamental, applied, and translational

**Fundamental (basic) research** seeks to understand a phenomenon, without a specified application. *Why do heavily overparameterised networks generalise at all? What is the sample complexity of this learning problem?* Evidence is typically theoretical or carefully controlled empirical work. Success is explanatory power. The risk is irrelevance to practice; the reward is durability — foundational results remain citable for decades.

**Applied research** addresses a specified practical problem. *Can retinopathy be screened reliably using low-cost fundus cameras in primary care?* Evidence must include performance under realistic conditions. Success is usefulness. The risk is that the result is tied to a context that changes.

**Translational research** deliberately bridges the two: it takes a method established in idealised conditions and studies what happens when deployment constraints are imposed. Deployment constraints — latency, memory, privacy, missing metadata, distribution shift, human workflow — become the *independent variables* rather than nuisances. This is an under-occupied and highly productive space for early-career researchers, because the constraints are real, the questions are genuinely open, and the compute requirements are often modest.

## 2.3 By approach: experimental, theoretical, computational, observational

**Experimental research** manipulates one or more variables and measures the effect, holding others constant. Most machine-learning papers are experimental in form, though frequently weak in execution because the "holding others constant" requirement is not met (unequal tuning, different data pipelines, different training budgets).

**Theoretical research** derives consequences from stated assumptions: proofs, bounds, convergence guarantees, complexity results, impossibility results. Evidence is the correctness of the derivation. The characteristic failure is a result that is technically correct but whose assumptions exclude every case of practical interest — which is why strong theoretical papers state explicitly where their assumptions bite.

**Computational or simulation research** studies systems through models when direct experimentation is impractical. The characteristic threat is that conclusions describe the simulator rather than the world, which is why validation of the model against reality is essential.

**Observational or empirical research** measures what already exists without intervening: mining a hundred thousand public repositories, analysing published papers, characterising a corpus, measuring the behaviour of deployed systems. It cannot establish causation on its own, and the discipline of the field is to be careful with causal language. Its great advantage is scale.

## 2.4 By data type: quantitative, qualitative, mixed

**Quantitative research** measures, counts, and analyses numerically, aiming at generalisation. Its instruments are metrics, statistical tests, effect sizes, confidence intervals. Its blind spot is that it can only answer questions you thought to measure.

**Qualitative research** investigates meaning, mechanism, and experience: interviews, observation, document analysis, open-ended survey responses. It is not "soft" — rigorous qualitative work has explicit standards, including systematic coding, intercoder agreement, negative-case analysis, saturation, reflexivity, and audit trails. Reporting guidance such as COREQ and SRQR is used in several fields.

Its relevance to computational researchers is often underestimated. If your contribution concerns tools, explanations, interfaces, developer practice, or clinical adoption, then *how people actually interpret and use the system* is an empirical question that numbers alone cannot answer.

**Mixed-method research** integrates both deliberately — not merely running both, but designing so that one informs the other. A common and powerful pattern: a quantitative evaluation establishes that a model performs well, and a qualitative study establishes that intended users do not trust or cannot act on its output. The combination is a much stronger contribution than either half, and the tension between the two results is usually the most interesting thing in the paper.

## 2.5 By stage of knowledge: exploratory, descriptive, comparative, explanatory

This axis is about what is already known, and it governs how strongly you may phrase your conclusions.

| Stage | Question form | Typical design | Permissible claim strength |
|---|---|---|---|
| **Exploratory** | What is going on here? | Open-ended, small-scale, hypothesis-generating | Suggestive only; explicitly preliminary |
| **Descriptive** | What are the characteristics of X? | Measurement, characterisation, corpus analysis | Factual about the studied sample |
| **Comparative** | Does A differ from B, and by how much? | Controlled comparison with matched conditions | Difference, with effect size and uncertainty |
| **Explanatory / causal** | Why does A produce B? | Ablation, intervention, mediation analysis | Mechanism, if the design isolates it |

A very common reviewer objection is a mismatch between design and claim: an exploratory study whose abstract asserts a general causal mechanism. Matching the two is largely a matter of writing discipline, and Chapter 36 addresses it directly.

## 2.6 Review research: narrative reviews, systematic reviews, and surveys

Because reviews are often a researcher's first publication, they deserve specific treatment.

**Narrative review.** An expert account of a body of work, organised by the author's judgement. Strength: interpretation, taxonomy, agenda-setting. Weakness: selection is not reproducible, so a sceptical reader cannot tell whether inconvenient work was omitted. Usually written by established researchers, often by invitation.

**Systematic literature review (SLR).** A review conducted according to a pre-specified, reported protocol: databases searched, exact search strings, dates, inclusion and exclusion criteria, screening procedure, quality appraisal, and extraction fields. The defining property is that *another team could repeat it*. In medicine and increasingly elsewhere, PRISMA (Page et al., 2021) is the standard reporting framework; in software engineering, Kitchenham's guidelines (Kitchenham and Charters, 2007) are widely used.

**Systematic mapping study.** A lighter-weight relative of the SLR that characterises the shape of a field — what is studied, by whom, with what methods, in what venues — without appraising outcomes in depth. Useful when a field is too large or too heterogeneous for meta-analysis.

**Meta-analysis.** Statistical pooling of quantitative results across studies to estimate an overall effect. Requires comparable outcome measures, which in computational fields is often the binding obstacle: results measured on different datasets with different splits and different metrics generally cannot be pooled, and attempting it produces a meaningless average.

**Survey (in the computer-science sense).** A structured, tutorial-oriented account of methods in an area, usually with a taxonomy and comparison tables. Note the terminological collision: in social science a "survey" is a questionnaire study of human respondents, an entirely different thing. State which you mean.

### 2.6.1 Recommendation: the systematic review as a first paper

**This is a recommendation, not a fact.** For a researcher in their first or second year, a rigorous systematic review is often the highest-expected-value first publication, for four reasons:

1. It forces genuine mastery of the literature, which is required anyway.
2. Its by-products *are* the artefacts you need for your own empirical work — the literature matrix (Chapter 15) and the research gap (Part VI) fall out of it.
3. It requires no compute and no data access.
4. It remains citable for years.

The honest counterweight: it is more work than newcomers expect. Screening several hundred to a few thousand records is normal, and the protocol must be executed faithfully. It also does not demonstrate experimental skill, so it should not be your *only* output.

## 2.7 Choosing a type from your question

**Figure 2.1 — Choosing a research type from a research question**

```
  What does your question ask for?
  │
  ├─ "Is it true that…?" / "Does A differ from B?"
  │     → COMPARATIVE EXPERIMENTAL
  │       evidence: controlled comparison, equal budgets, seeds, statistics
  │
  ├─ "How much / how large / under what conditions?"
  │     → DESCRIPTIVE or COMPARATIVE EMPIRICAL
  │       evidence: measurement across strata, confidence intervals
  │
  ├─ "Why does it happen?"
  │     → EXPLANATORY (ablation / intervention / mediation)
  │       evidence: designs isolating one factor at a time
  │
  ├─ "Must it always be so?" / "What is the limit?"
  │     → THEORETICAL
  │       evidence: proof; assumptions stated and their bite acknowledged
  │
  ├─ "What do people do / think / experience?"
  │     → QUALITATIVE or MIXED
  │       evidence: systematic coding, agreement, saturation, reflexivity
  │
  ├─ "What is already known, and where does it disagree?"
  │     → SYSTEMATIC REVIEW
  │       evidence: reproducible protocol, screening funnel, appraisal
  │
  └─ "Does the published result hold?"
        → REPRODUCTION / REPLICATION
          evidence: faithful re-implementation, documented discrepancies
```

**Table 2.1 — Research types, questions they answer, and typical evidence**

| Type | Answers | Core evidence | Principal threat |
|---|---|---|---|
| Fundamental | Why does this phenomenon occur? | Theory plus controlled empirics | Practical irrelevance |
| Applied | Does this work for this purpose? | Realistic-condition evaluation | Context dependence |
| Translational | What happens under deployment constraints? | Constrained evaluation, cost measurement | Constraint chosen unrealistically |
| Experimental | Does the manipulation change the outcome? | Controlled comparison | Confounds; unequal effort |
| Theoretical | What follows from these assumptions? | Proof | Vacuous assumptions |
| Computational | How does the modelled system behave? | Simulation plus validation | Simulator ≠ world |
| Observational | What exists at scale? | Large-sample measurement | Causal overreach |
| Quantitative | How much? | Statistics | Measuring the wrong construct |
| Qualitative | What does it mean to participants? | Coded data, agreement, saturation | Researcher bias; unwarranted generalisation |
| Mixed | Both, integrated | Both, plus integration argument | Two studies stapled together |
| Systematic review | What is the state of evidence? | Reproducible protocol | Protocol not actually reproducible |
| Reproduction | Does the result hold? | Re-implementation, diagnosis | Unfair re-implementation |

## 2.8 Common mistakes

| Mistake | Correction |
|---|---|
| Calling a narrative review a "systematic review" without a protocol | Either follow a protocol and report it, or call it a review |
| Averaging accuracies across incomparable datasets as "meta-analysis" | Pool only genuinely comparable outcomes; otherwise present a structured comparison |
| Causal language ("improves", "causes", "leads to") on observational data | Use associational language, or add an intervention |
| Claiming generality from a single dataset | Add datasets, or bound the claim explicitly |
| Running a questionnaire and calling it qualitative | Open-text responses need systematic coding to count as qualitative analysis |
| Choosing the type from available skills rather than from the question | Derive the type from the question; acquire the method or change the question |

## Exercises

**Exercise 2.1** Write your research question. Trace it through Figure 2.1 and record the type it implies. Then list the evidence that type requires and mark what you currently have.

**Exercise 2.2** Identify the strongest validity threat for your type from Table 2.1, and write one sentence describing how your design will mitigate it.

**Exercise 2.3** If your question implies a type you have never used, decide now whether to acquire the method, collaborate, or reframe the question. Record the decision and the date.

<div class="pagebreak"></div>

# Chapter 3 — The Research Lifecycle

## 3.1 The lifecycle as a whole

The stages below are presented linearly because they must be described in some order. They are not executed linearly, and pretending otherwise is a source of real damage: researchers who believe the process is a pipeline treat every backward step as a failure, when in fact iteration is the normal mode of competent work.

**Figure 3.1 — The research lifecycle, with feedback paths**

```
 ┌───────────────────────── PHASE 1: FRAMING ──────────────────────────┐
 │  1  Research area                                                   │
 │  2  Research problem                                                │
 │  3  Research question(s)                                            │
 │  4  Literature search                                               │
 │  5  Paper reading and extraction                                    │
 │  6  Literature matrix                                               │
 │  7  Critical review / synthesis                                     │
 │  8  Research gap                                                    │
 │  9  Objectives, hypotheses, contributions                           │
 └─────────────────────────────────────────────────────────────────────┘
                                  │
 ┌───────────────────── PHASE 2: EVIDENCE ─────────────────────────────┐
 │ 10  Methodology design                                              │
 │ 11  Dataset selection and preparation                               │
 │ 12  Experimental design (baselines, splits, ablations, seeds)       │
 │ 13  Execution                                                       │
 │ 14  Evaluation and analysis                                         │
 │ 15  Results                                                         │
 │ 16  Discussion and interpretation                                   │
 └─────────────────────────────────────────────────────────────────────┘
                                  │
 ┌───────────────────── PHASE 3: COMMUNICATION ────────────────────────┐
 │ 17  Figures and tables                                             │
 │ 18  Manuscript writing                                             │
 │ 19  References                                                     │
 │ 20  Ethics and similarity check                                    │
 │ 21  Journal selection                                              │
 │ 22  Submission                                                     │
 │ 23  Peer review                                                    │
 │ 24  Revision and response                                          │
 │ 25  Publication, archiving, dissemination                          │
 └─────────────────────────────────────────────────────────────────────┘

 FEEDBACK PATHS THAT THE LINEAR DIAGRAM HIDES
  • Gap not defensible under scrutiny .............. return to stage 4
  • Objectives not measurable ...................... return to stage 8
  • Baselines unavailable or unrunnable ............ return to stage 9 or 12
  • Results contradict the hypothesis .............. return to stage 10
                                                     (NEVER to the data — see §3.4)
  • Reviewer identifies a missing comparison ....... return to stage 12
  • Scope mismatch at desk rejection ............... return to stage 21
  • Result already published while you worked ...... return to stage 8 and reframe
```

## 3.2 Stage-by-stage specification

**Table 3.1 — Lifecycle stages: inputs, outputs, decisions, mistakes, tools**

| # | Stage | Input | Output | Key decision | Characteristic mistake | Tools |
|---|---|---|---|---|---|---|
| 1 | Research area | Interest, supervisor capability, resources | A named sub-area with a readable literature | Breadth versus competition | Choosing a domain and calling it a topic | Scopus/WoS trend analysis, arXiv, conference programmes |
| 2 | Research problem | Sub-area | A statement of a specific unknown | Is the answer actually unknown? | Restating an engineering task | Recent papers' limitations sections |
| 3 | Research question | Problem | 1–3 answerable questions | Question type (Fig. 2.1) | Questions no experiment can settle | Chapter 6 frameworks |
| 4 | Literature search | Questions | A logged, reproducible record set | Databases, strings, inclusion window | One database, one spelling | Scopus, WoS, IEEE, ACM, Semantic Scholar |
| 5 | Reading and extraction | Record set | Filled extraction templates | Which papers deserve depth | Highlighting instead of extracting | Zotero, three-pass method |
| 6 | Literature matrix | Extractions | A sortable table of 10–25 studies | Which columns | A single "notes" column | Sheets/Excel, Zotero export |
| 7 | Critical synthesis | Matrix | Grouped, evaluated account | Organising principle | Paper-by-paper listing | Chapter 14 |
| 8 | Research gap | Synthesis | An evidenced gap statement | Which gap type | "Room for improvement" | Chapter 18 |
| 9 | Objectives | Gap | Aim, objectives, hypotheses, contributions | Measurability | Activity titles ("Study of…") | Chapter 7 |
| 10 | Methodology | Objectives | A reproducible design | Design that isolates the factor | Environment mistaken for methodology | Chapter 22 |
| 11 | Dataset | Methodology | Prepared, documented, licensed data | Split unit | Random splits on grouped data | Chapter 23 |
| 12 | Experimental design | Methodology, data | Protocol: baselines, splits, seeds, ablations | Tuning budget parity | Only comparing your own model | Chapter 26 |
| 13 | Execution | Protocol | Logged runs, artefacts | Configuration control | Tuning by editing source | MLflow, W&B, config files |
| 14 | Evaluation | Runs | Metrics, tests, error analysis | Metric choice | Accuracy on imbalanced data | Chapter 27 |
| 15 | Results | Analysis | Tables, figures, observations | What to report | Reporting only favourable findings | Chapters 28, 35 |
| 16 | Discussion | Results | Interpretation, limits | Mechanism versus speculation | Restating results | Chapters 29, 36 |
| 17 | Figures and tables | Results | Publication-quality floats | One message per figure | Screenshots; unreadable fonts | Chapters 38–39 |
| 18 | Writing | All above | Manuscript | Writing order | Introduction promising more than delivered | Chapters 30–37 |
| 19 | References | Reading | Verified, styled bibliography | Manager and style | Unopened or fabricated citations | Chapters 43–44 |
| 20 | Ethics and similarity | Manuscript | Clean report, declarations | Interpretation of matches | Chasing a percentage | Chapters 47–49 |
| 21 | Journal selection | Manuscript | Target plus two backups | Scope fit | Choosing after writing | Chapters 50–52 |
| 22 | Submission | Manuscript, letter | Submission record | Template compliance | Unproofed system PDF | Chapters 53–54 |
| 23 | Peer review | Submission | Reviews and decision | Nothing — you wait | Panicking at "major revision" | Chapter 55 |
| 24 | Revision | Reviews | Revised manuscript, response letter | Where to concede, where to argue | Undisclosed changes | Chapter 56 |
| 25 | Publication | Accepted paper | DOI, archive, dissemination | Where to deposit | Neglecting the proofs | Chapter 57 |

## 3.3 Where time actually goes

Beginners consistently misallocate effort, and the misallocation has a predictable shape.

**Figure 3.2 — Where time is actually spent versus where beginners expect to spend it**

```
                      EXPECTED              REALISTIC (first paper)
  Framing (1–9)       ███ 10%               ████████████ 30–35%
  Evidence (10–16)    ████████████████ 70%  ████████████████ 40–45%
  Communication       ██ 15%                ████████ 20–25%
   (17–22)
  Review (23–25)      █ 5%                  (mostly waiting: 3–12 months)
```

In calendar terms, a realistic first journal paper in a computational field spans roughly:

| Phase | Realistic duration | Note |
|---|---|---|
| Framing | 4–10 weeks | Almost always compressed, and this is the root cause of most later rejections |
| Evidence | 8–20 weeks | Budget three times your first estimate for compute; baselines and ablations dominate |
| Communication | 3–6 weeks | Underestimated; the abstract and response letter take longer than expected |
| Review to publication | 3–12 months | Largely outside your control |

The single most valuable planning insight in this chapter: **the framing phase is cheap in resources and decisive in outcome.** Four extra weeks spent establishing a defensible gap routinely saves six months of experiments that answer nothing.

## 3.4 One feedback path that is not permitted

Every backward arrow in Figure 3.1 is legitimate except one distinction that must be stated explicitly, because it is the point at which ordinary pressure turns into misconduct.

When results contradict your hypothesis, you may legitimately:

- Return to the **methodology** and ask whether the design actually tested the hypothesis;
- Discover and fix a genuine **bug**, then re-run everything, including the baselines;
- Add experiments that **probe why** the prediction failed;
- **Report the disconfirmation** and revise the hypothesis, clearly labelling the revision as post hoc;
- Conclude that the effect is absent, and publish that.

You may not:

- Adjust, exclude, or "clean" data until the hypothesis is supported;
- Try many analyses and report only the one that reached significance (*p*-hacking);
- Present a hypothesis formed after seeing the results as though it had been predicted (HARKing);
- Drop the datasets, seeds, or metrics on which the method lost, without disclosure;
- Report the best of many runs as the result.

The first list is science; the second is falsification or misrepresentation, discussed in Chapter 49. The boundary is not always obvious in the moment, which is why the practical safeguard is **pre-specification**: write down, before you look at test results, what you predict, what you will measure, which test you will use, and what would count as a disconfirmation. A dated entry in a research journal costs two minutes and settles the question later.

## 3.5 Recommended practice: the research journal

**This is a recommendation.** Keep a single dated, append-only log for each project, containing:

- Decisions and their reasons ("using site-wise splits because §Zech et al. suggests site confounding; decided 12 March")
- Search strings and the dates you ran them
- Pre-specified predictions and analysis plans
- Every time you evaluated on the test set, and why
- Discrepancies found when reproducing others' work
- Ideas deferred, with enough detail to resume

Three payoffs: your methods section is half-written; your response letters can cite what you did and when; and if your integrity is ever questioned, a contemporaneous record is the strongest evidence available. Plain text under version control, Obsidian, Notion, or a paper notebook all work — the tool matters far less than the habit.

## 3.6 Verification checklist for Part I

- [ ] I can state my contribution type and the evidence it requires (§1.8.1).
- [ ] I can state a falsifiable mechanism (§1.7, Exercise 1.2).
- [ ] I know my research type and its principal validity threat (Chapter 2).
- [ ] I know which lifecycle stage I am actually at (Table 3.1).
- [ ] I have written down what I predict, before seeing test results (§3.4).
- [ ] I have started a dated research journal (§3.5).
- [ ] I have allocated at least four weeks to framing before beginning experiments.

## Exercises

**Exercise 3.1** Locate yourself in Table 3.1. Write down the stage number, its required output, and whether you actually hold that output. If not, you have found your immediate task.

**Exercise 3.2** Draw your own version of Figure 3.1 for your project, and mark every backward arrow you have already traversed. Most researchers are surprised by how many there are — and reassured.

**Exercise 3.3** Write a pre-specification entry: your prediction, the measurement, the statistical test, the significance level, and what result would disconfirm you. Date it. Do not modify it later; add new entries instead.

**Exercise 3.4** Estimate your compute requirement as *configurations × seeds × datasets*, then multiply by three. Compare with the resources you actually have. If the result is infeasible, return to Chapter 4 now rather than in six months.

<div class="pagebreak"></div>
