# PART VII — NOVELTY AND CONTRIBUTION

<div class="partintro">

Part VII addresses the two questions a reviewer asks first and that authors answer worst: *what is new here?* and *what does the field gain?* Chapter 20 dissects novelty into nine recognisable kinds and confronts the most common misconception in applied research — that combining existing components constitutes novelty. Chapter 21 teaches contribution statements as a specific writing genre with its own rules.

The gap you established in Part VI says what is missing. Novelty and contribution say what you are adding. These are different statements and both must be written explicitly.

</div>

<div class="pagebreak"></div>

# Chapter 20 — Research Novelty

## 20.1 Definition

**Definition.** Novelty is the property of a contribution being new relative to the accessible published record — not new to the author, and not merely newly combined.

**Purpose.** Novelty is the price of entry to the permanent record. The record exists to accumulate knowledge; a paper that adds nothing new adds only volume. This is why "insufficient novelty" is the most common substantive rejection at selective venues, and why it is so often disputed: authors experience the *effort* of their work and assume it corresponds to novelty, while reviewers assess only the *increment*.

## 20.2 Novelty is a spectrum, not a binary

A great deal of unnecessary anxiety comes from treating novelty as an all-or-nothing property. It is better understood as degrees.

**Figure 20.1 — Degrees of novelty**

```
  LOW ─────────────────────────────────────────────────────────────► HIGH

  ┌─ REPLICATION ──────────────────────────────────────────────────────┐
  │ Same method, same data, independent execution.                     │
  │ Publishable when the original is influential and unverified.       │
  └────────────────────────────────────────────────────────────────────┘
  ┌─ INCREMENTAL IMPROVEMENT ──────────────────────────────────────────┐
  │ Established problem, established route, measurably better result.  │
  │ Publishable if the gain survives equal tuning, seeds, and tests.   │
  └────────────────────────────────────────────────────────────────────┘
  ┌─ SUBSTANTIVE CONTRIBUTION ─────────────────────────────────────────┐
  │ A new method, resource, evaluation protocol, or empirical finding. │
  │ The category into which most good published research falls.        │
  └────────────────────────────────────────────────────────────────────┘
  ┌─ REFRAMING ────────────────────────────────────────────────────────┐
  │ Shows the community was measuring, assuming, or asking wrongly.    │
  │ Rare; disproportionately cited.                                    │
  └────────────────────────────────────────────────────────────────────┘
  ┌─ PARADIGMATIC ─────────────────────────────────────────────────────┐
  │ Changes what the field considers the problem to be.                │
  │ A handful per decade per field. Not a reasonable PhD target.       │
  └────────────────────────────────────────────────────────────────────┘
```

**The practical point.** A doctorate does not require reframing or paradigm change. It requires a defensible substantive contribution — and the expectation that it must be revolutionary is a documented cause of paralysis and delay. Aim for *substantive*, execute it impeccably, and let the field decide whether it turns out to be more.

## 20.3 The nine kinds of novelty

Each kind carries a distinct evidential obligation. Knowing which you are claiming tells you what experiments you owe.

| # | Kind | You are claiming | Evidence obligation | Characteristic failure |
|---|---|---|---|---|
| 1 | **Algorithmic** | A new procedure for computing something | Correctness; complexity; comparison with the algorithm it replaces | Presenting a known algorithm under a new name |
| 2 | **Architectural** | A new arrangement of model components | Ablation isolating the new arrangement at matched parameter count | Concatenating two published blocks and calling it an architecture |
| 3 | **Dataset / resource** | New data, annotations, or a benchmark | Construction protocol, annotation agreement, quality audit, licence, baseline results | Releasing data with no documentation or baselines |
| 4 | **Application** | A method transferred to a genuinely different setting | A *mechanism* argument for why transfer is non-trivial, plus measurement of what changes | "Apply X to Y" with no mechanism (§5.5) |
| 5 | **Optimisation** | Better cost for equal quality, or better quality for equal cost | Cost measured honestly — parameters, FLOPs, latency, memory, energy — on stated hardware | Reporting accuracy gains while concealing added cost |
| 6 | **Evaluation** | A protocol or metric that measures what matters better | Demonstration that current evaluation is inadequate; validation that yours is better | Proposing a metric with no validation that it measures the construct |
| 7 | **Integration** | A combination whose behaviour is not predictable from its parts | A prediction about the interaction, and an experiment that could refute it | Combination without a prediction (§20.4) |
| 8 | **Theoretical** | A proof, bound, or formal characterisation | Correct derivation; assumptions stated; the bite of the assumptions acknowledged | A correct result whose assumptions exclude all practical cases |
| 9 | **Empirical** | A measured fact about the world or about existing methods | Careful measurement, controls, variance, replication across settings | Measurement without controls, presented as discovery |

Kinds 3, 5, 6, and 9 are systematically undervalued by early-career researchers and systematically valued by editors, because they change what practitioners do. They are also the kinds most achievable without large compute.

## 20.4 Why combination is not automatically novelty

This is the most important section in the chapter, because "we combine A and B" is the single most common weak novelty claim in applied machine learning.

Consider the claim: *"We propose a novel hybrid CNN–LSTM–Attention model."* A reviewer's internal response is: CNNs, LSTMs, and attention are each a decade or more old, and their combination has been published many times across many tasks. What is new?

The problem is not that combinations are worthless. It is that a combination, by itself, makes **no claim that could be false**. If you assemble three components and report a number, the reader learns that this assembly produces that number on that data — which is a fact about your run, not knowledge about the world.

**The conversion.** A combination becomes a contribution when you state a **prediction about the interaction** and test it.

| ❌ Combination as assembly | ✅ Combination as hypothesis |
|---|---|
| "We combine a CNN with an LSTM." | "Convolutional features capture local morphology but discard temporal ordering, while recurrent state captures ordering but degrades on long sequences. If the two failure modes are independent, the combination should be robust to both — which predicts that the gain over each component alone should be *largest* at intermediate sequence lengths and vanish at the extremes. We test this by crossing sequence length with noise level." |
| "We add attention to improve performance." | "If attention helps by suppressing background regions, then its benefit should scale with the proportion of background in the image, and masking the background should eliminate the benefit. We measure both." |
| "We use transfer learning with fine-tuning." | "Pretraining transfers low-level filters but not domain-specific texture statistics; we predict that freezing early layers preserves the benefit while freezing late layers destroys it, and we measure the crossover point." |

Notice what each rewrite adds: a **mechanism**, a **prediction that could be wrong**, and a **measurement that would detect it being wrong**. That is the difference between engineering assembly and scientific contribution, and it usually costs one extra experiment rather than a new idea.

## 20.5 Establishing novelty in writing

Novelty is not asserted; it is *positioned*. Three moves, in order.

**Move 1 — Name the closest prior work explicitly.** Reviewers trust authors who identify their nearest competitor. Concealing it looks either ignorant or evasive, and a specialist will find it regardless.

> ✅ *"The closest prior work is [12], which also infers latent groupings for invariance training. It differs from ours in requiring a known group count and in clustering on raw inputs rather than on embedding statistics; §V-D compares the two directly."*

**Move 2 — State the delta precisely.** One sentence naming exactly what is different — a component, an assumption relaxed, a condition tested, a quantity measured.

**Move 3 — Say why the delta matters.** A difference that changes nothing is not a contribution. Connect the delta to a consequence: something now possible, cheaper, more reliable, or newly known.

**On the phrase "to the best of our knowledge".** This is acceptable *only* when preceded by a documented search, and it is stronger when paired with the nearest-neighbour formulation of §19.5. "To the best of our knowledge, no prior study evaluates X under condition Y; the closest is [12], which evaluates X under Z" is defensible. The same phrase with nothing behind it is a liability.

## 20.6 Common mistakes

| Mistake | Why it fails | Correction |
|---|---|---|
| "Novel" as an adjective applied to your own work | Assertion, not evidence | Delete the word; demonstrate the delta instead |
| Combination without a prediction | Nothing could be false | Apply §20.4 |
| Claiming architectural novelty for a concatenation | Precedent will be found | Reclassify honestly — often it is an application or empirical contribution |
| Hiding the nearest prior work | Reviewers find it; credibility collapses | Name it and differentiate (§20.5) |
| Claiming novelty of *effort* | Reviewers assess increment, not labour | Identify what is *learned* |
| Claiming optimisation novelty without cost measurement | The claim is unverifiable | Measure parameters, FLOPs, latency, memory |
| "First work in this area" | Almost always falsifiable | Use the bounded, scoped form |
| Novelty claimed in the abstract but never isolated experimentally | Ablation absent | Every novelty claim needs an experiment that isolates it |

## 20.7 Verification checklist

- [ ] I can name which of the nine kinds of novelty I claim.
- [ ] I know the evidence obligation for that kind, and I have planned it.
- [ ] I can name the single closest prior work and state the delta in one sentence.
- [ ] If my contribution is a combination, I have stated a falsifiable prediction about the interaction.
- [ ] I have an experiment that isolates my novel component from everything inherited.
- [ ] If I claim efficiency, I measure cost on stated hardware.
- [ ] I have not used the word "novel" as a substitute for demonstrating novelty.
- [ ] Any absolute claim of priority is scoped and supported by a documented search.

## Exercises

**Exercise 20.1** Classify your contribution against the nine kinds in §20.3. If you cannot choose one, your novelty claim is not yet formed.

**Exercise 20.2** Name your closest prior work. Write the delta in one sentence, and the consequence of the delta in a second. If you cannot name a closest work, return to Part III.

**Exercise 20.3** If your work combines components, apply §20.4: write the mechanism, the prediction, and the experiment that could refute it.

**Exercise 20.4** For your claimed novelty, name the specific experiment that isolates it. If no such experiment exists in your plan, add it now — a reviewer will demand it.

<div class="pagebreak"></div>

# Chapter 21 — Research Contribution

## 21.1 Definition and purpose

**Definition.** A contribution is a transferable statement of what the field gains from your work, expressed so that its truth can be checked against your evidence.

**Purpose.** Contribution statements do heavy structural work in a paper. They appear as a numbered list at the end of the introduction, they determine the shape of the results section, they are what the conclusion restates, and they are what a reviewer scores. They are also what a hiring or promotion committee reads when they read only your abstract.

## 21.2 The five types, and what each requires

| Type | Statement form | Evidence required | Example *[HYPOTHETICAL]* |
|---|---|---|---|
| **Methodological** | A procedure others can adopt | Fair comparison; ablation; released code | "A site-clustering regulariser that requires no institutional metadata at training time" |
| **Dataset / resource** | Data or a benchmark others can use | Construction protocol; annotation agreement; licence; baselines | "A benchmark of 4,000 code-mixed paraphrase pairs at four graded obfuscation levels, with inter-annotator agreement of κ = 0.81" |
| **Experimental / empirical** | A measured fact about the world | Controls; variance; replication across settings | "The first leakage-free multi-institution quantification of degradation for five widely used architectures" |
| **Theoretical** | A formal result | Proof; stated assumptions | "A bound on the excess risk of invariance training under bounded group imbalance" |
| **Practical** | An artefact or protocol with demonstrated utility | Deployment evidence; cost measurement; user evidence where relevant | "An inference configuration attaining worst-site AUC above 0.85 within a 50 ms budget on commodity edge hardware" |

Most papers make two or three contributions of *different* types. A paper claiming four methodological contributions is usually claiming one and padding.

## 21.3 The anatomy of a contribution statement

A well-formed contribution has four elements. Missing any one produces a recognisable defect.

```
  [ARTEFACT OR FINDING]  +  [SCOPE]  +  [QUANTIFICATION]  +  [SIGNIFICANCE]

  "A label-free adaptation module    ← artefact
   for multi-institution chest        ← scope
   radiograph classification
   that recovers 0.041 ± 0.009        ← quantification (with uncertainty)
   worst-institution AUC over the
   strongest of four baselines at
   equal parameter count,
   thereby attaining most of the      ← significance
   benefit of methods requiring
   privileged site labels without
   using them."
```

| Missing element | Resulting defect |
|---|---|
| Artefact | Vague — the reader cannot tell what they are being given |
| Scope | Overclaim — invites a counterexample outside your conditions |
| Quantification | Unverifiable — "improves performance" cannot be checked |
| Significance | Uninterpretable — the reader cannot tell why the number matters |

## 21.4 Weak and strong contribution statements

**Table 21.1 — Weak and strong contribution statements**

| ❌ Weak *[HYPOTHETICAL]* | Diagnosis | ✅ Strong *[HYPOTHETICAL]* |
|---|---|---|
| "We propose a novel deep learning framework for image classification." | "Framework" conceals the artefact; "novel" is asserted; no scope, quantification, or significance | "We propose a clustering-based invariance regulariser that operates without domain labels, and show it recovers 82% of the worst-group improvement obtained by label-supervised adversarial training on three public datasets." |
| "Our method outperforms state-of-the-art methods." | Unbounded; unquantified; invites refutation | "Our method improves worst-institution AUC by 0.041 (95% CI 0.032–0.050) over the strongest of four baselines tuned under an identical 50-trial budget." |
| "We conduct extensive experiments." | Effort, not knowledge | "We report the first evaluation of these five architectures under institution-disjoint splits across three datasets with ten seeds and paired significance testing, establishing a mean degradation of 0.116 AUC (95% CI 0.104–0.128)." |
| "We provide a comprehensive survey of the field." | "Comprehensive" is unverifiable | "We synthesise 68 studies retrieved by a logged four-database protocol, and show that 44 of them evaluate on splits that permit group leakage, which reconciles the apparent contradiction between [refs]." |
| "We release our code." | An artefact, not yet a contribution | "We release institution-disjoint split definitions, training code, and trained weights, enabling protocol-consistent comparison — currently impossible because no two of the surveyed studies share a split definition." |
| "This work has significant practical implications." | Asserted significance | "Because worst-site rather than mean performance governs deployment risk, the 0.116 gap implies that a model reported at 0.90 AUC may present as 0.78 at an unseen institution — a difference that changes the triage threshold a hospital should adopt." |
| "We solve the domain shift problem." | Overclaim | "We reduce but do not eliminate cross-institution degradation; approximately 0.075 AUC of the observed 0.116 gap remains unaddressed, and we characterise where it concentrates." |

The pattern is consistent throughout this handbook: strong statements are longer, carry numbers with uncertainty, name their scope, and concede limits. **Calibration reads as competence.** Overclaiming invites a reviewer to hunt for the counterexample, and they will find one.

## 21.5 Writing the contribution list

**Procedure.**

1. Write one contribution per **objective** (Chapter 7). If an objective yields no contribution, either it is not producing knowledge or you are under-claiming.
2. Order them by **importance**, not chronology. The reader's attention is highest at the first item.
3. Give each a **label** — C1, C2, C3 — and use those labels consistently in the results section and the conclusion. This is a small formatting habit with a large effect on how coherent the paper reads.
4. Include the **artefact release** as a numbered contribution where you have one; it is genuinely valuable and reviewers credit it.
5. Verify each against the four-element anatomy of §21.3.
6. Verify that each maps to a **results subsection** that supplies its evidence.

**A worked list.** *[HYPOTHETICAL]*

> The contributions of this paper are:
>
> **(1)** the first leakage-free, multi-institution quantification of performance degradation for five widely used chest-radiograph architectures, with ten seeds, paired significance tests, and confidence intervals (§V-A);
>
> **(2)** CLUSTER-DG, an adaptation method that requires no institutional metadata and recovers 0.041 ± 0.009 worst-institution AUC over empirical risk minimisation at equal parameter count (§V-B);
>
> **(3)** an ablation isolating the contributions of cluster granularity, invariance weight, and augmentation, which shows that the ramping schedule accounts for approximately one third of the gain (§V-C);
>
> **(4)** a public release of institution-disjoint split definitions, code, and trained weights, enabling protocol-consistent comparison in future work (§VI).

Each item names an artefact or finding, bounds its scope, quantifies where quantification is possible, and points to the evidence.

## 21.6 Calibration: a short discipline

Three habits prevent nearly all overclaiming.

**Bound every superlative.** Not "the best", but "the best of the four methods we evaluated under this protocol". Not "the first", but "to our knowledge the first under condition Y; the closest prior work is [12]".

**Report what you did not do.** One sentence in the contribution list or the limitations paragraph — "we did not evaluate methods requiring paired multi-site supervision" — removes an entire category of objection, because the reviewer's observation is already yours.

**Prefer a smaller claim you can defend completely.** A tightly bounded finding is more citable than a grand one that a later paper narrows. In the long run, calibration is also self-interested: the reputational cost of an overturned claim is much larger than the benefit of a bolder abstract.

## 21.7 Common mistakes

| Mistake | Correction |
|---|---|
| Contributions that restate the method three times | Merge into one; find genuinely distinct gains |
| A contribution with no corresponding results subsection | Add the evidence or delete the claim |
| "Extensive experiments" as a contribution | Experiments are method; the *finding* is the contribution |
| Ordering contributions chronologically | Order by importance |
| Contribution list inconsistent with the abstract or conclusion | Make them substantively identical; reviewers check |
| Omitting artefact release from the list | Include it; it is a real contribution |
| Unbounded superlatives | Bound every one (§21.6) |
| No quantification anywhere in the list | Add numbers with uncertainty wherever available |

## 21.8 Verification checklist for Part VII

- [ ] Each contribution names its type from §21.2.
- [ ] Each has all four elements of §21.3: artefact, scope, quantification, significance.
- [ ] Each maps one-to-one onto an objective and to a results subsection.
- [ ] Contributions are labelled C1…Cn and those labels recur in results and conclusion.
- [ ] Every superlative is bounded by the conditions actually tested.
- [ ] At least one sentence states what the work does *not* address.
- [ ] The list in the introduction matches the abstract and the conclusion in substance.
- [ ] I have not used "novel", "extensive", or "comprehensive" as evidence.

## Exercises

**Exercise 21.1** Write two to four contribution statements for your work, each containing all four elements of §21.3.

**Exercise 21.2** For each, name the results subsection that will provide its evidence. Any contribution without one is currently unsupported.

**Exercise 21.3** Rewrite each contribution twice: once deliberately overclaimed, once deliberately under-claimed. Choose the version you could defend under hostile questioning, and note how close it is to the under-claimed one.

**Exercise 21.4** Write the one sentence stating what your work does not address. Keep it in the paper.

<div class="pagebreak"></div>
