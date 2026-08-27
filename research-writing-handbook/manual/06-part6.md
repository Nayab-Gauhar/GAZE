# PART VI — RESEARCH GAP

<div class="partintro">

Part VI is the pivot of this handbook. Everything in Parts III to V was preparation for it, and everything in Parts VII to X depends on it. Chapter 17 defines what a research gap is, what it is not, and gives a thirteen-type taxonomy. Chapter 18 provides a systematic procedure for deriving a gap from a literature matrix. Chapter 19 contrasts weak and strong gap statements and specifies how a gap must be evidenced.

The central claim of this part: **a research gap is not discovered by inspiration. It is computed from a documented literature matrix, stated with counts, and stress-tested by a hostile reader before it reaches a reviewer.**

</div>

<div class="pagebreak"></div>

# Chapter 17 — Understanding Research Gaps

## 17.1 Definition

**Definition.** A research gap is a specific, evidenced absence or inadequacy in the accessible literature, whose resolution would change what the field knows or can do.

Four components are obligatory. A statement missing any one of them is not yet a gap.

| Component | Question it answers | Example *[HYPOTHETICAL]* |
|---|---|---|
| **What is absent** | Precisely what is missing? | No leakage-free, multi-institution quantification of CXR classifier degradation |
| **Evidence of absence** | How do you know? | 11 of 15 surveyed studies use random row-level splits; 0 of 15 report worst-institution performance |
| **Why it matters** | Who is harmed by the absence? | Reported figures overstate deployable performance; a hospital cannot estimate the accuracy it would obtain |
| **What resolution enables** | What becomes possible? | A trustworthy degradation estimate, and a mitigation usable without privileged metadata |

The second component is the one that separates a defensible gap from an assertion, and it is the one most often missing. "Evidence of absence" does not mean proving a negative; it means demonstrating that you looked systematically and reporting what the search found.

## 17.2 What is not a gap

| Statement that is not a gap | Why not | How to rescue it |
|---|---|---|
| "Nobody has applied method X to dataset Y." | Absence of *activity*, not of *knowledge*. Doing something untried teaches nothing by itself | Identify which assumption of X is violated by Y, predict the consequence, measure it (§5.5) |
| "Accuracy can be improved." | True of every task, forever; unfalsifiable | Specify a threshold and why it matters: what decision changes at what level? |
| "The topic is new and trending." | Novelty of attention, not of knowledge | Find what is actually unresolved within the trend |
| "Existing methods have limitations." | Every method has limitations | Name the specific limitation, count how many studies share it, show what it costs |
| "No work exists in my country, language, or domain." | Geography is not a mechanism | Give a reason to expect different results here: what property differs? |
| "No one has combined A and B." | Combination is not knowledge | Predict *why* the combination should behave differently, and test the prediction |
| "Prior work is old; we use a newer model." | Recency is not a contribution | Ask what the newer model changes about the *conclusion*, not about the implementation |
| "There is limited research on this." | "Limited" is not a measurement | Count it. Report the count. Then say what the count implies |

Nearly every first draft contains at least one of these. The rescue is always the same shape: **add a mechanism and a measurement.**

## 17.3 The thirteen-type taxonomy

Knowing which *type* of gap you have is practically useful, because each type demands a different kind of evidence and each carries a different cost to address.

**Table 17.1 — Thirteen types of research gap**

| # | Type | Definition | Example *[HYPOTHETICAL unless cited]* | Evidence you need |
|---|---|---|---|---|
| 1 | **Knowledge** | A phenomenon is unexplained or unmeasured | Why does self-supervised pretraining help under distribution shift but not under label noise? | Prior work reports the effect but not its cause |
| 2 | **Methodological** | Existing methods rest on an assumption that fails in practice | All identified domain-generalisation methods require institutional labels; deployment strips them | The assumption, stated in each paper's setup |
| 3 | **Dataset / resource** | No suitable data exists for a population, language, modality, or annotation | No code-mixed paraphrase benchmark with graded obfuscation levels | A documented search of dataset registries returning nothing |
| 4 | **Performance** | The best known result is insufficient for the intended use | Worst-institution AUC of 0.83 against a clinically required 0.90 | A requirement derived from the application domain |
| 5 | **Application / translation** | A method works in the laboratory and is unstudied under deployment constraints | Test-time adaptation requires target batches; latency and memory unreported for edge hardware | Absence of cost reporting in prior work |
| 6 | **Population / domain** | Evidence exists for one group and is untested for another, **with reason to expect difference** | Models trained on adult frontal radiographs untested on paediatric populations, where anatomy differs systematically | A domain argument *plus* absence of studies |
| 7 | **Evaluation** | Metrics or protocols do not measure what matters | Imbalanced multi-label classification evaluated by accuracy; calibration unreported | A column tally of metrics across studies |
| 8 | **Scalability** | Behaviour at the target scale is unknown | A graph method validated to 10⁴ nodes; production graphs are 10⁸ | Complexity analysis plus absence of large-scale results |
| 9 | **Generalisation** | Results do not transfer across distributions | Chest-radiograph models can exploit institution-specific signal, so internal performance overstates external performance (Zech et al., 2018) | Direct re-evaluation under a leakage-free protocol |
| 10 | **Reproducibility** | Results cannot be independently obtained | Reported numbers not recoverable from released code under the described protocol | Your own documented reproduction attempt |
| 11 | **Computational efficiency** | Accuracy is achieved at unreported or unacceptable cost | A 0.02 AUC gain for four times the parameters and three times the latency, never reported | Cost measurements absent from prior work |
| 12 | **Explainability / trust** | Decisions are unexplained, or explanations are unvalidated | Saliency maps used as evidence of correctness without validation against expert annotation | Absence of explanation-validation studies |
| 13 | **Temporal** | Findings may not hold as the underlying distribution changes over time | A detector validated on 2019 data deployed against 2026 traffic patterns or 2026 malware | Evidence of drift plus absence of longitudinal evaluation |

### 17.3.1 Which gaps are achievable with limited resources

**This is a recommendation.** Gaps of types **7, 9, 10, and 11** — evaluation, generalisation, reproducibility, and efficiency — are usually the most achievable for a researcher without large compute, for three reasons:

1. They require **careful experimental design** rather than new theory or enormous training budgets.
2. Their evidence is largely **arithmetic**, which makes them difficult for a reviewer to dismiss.
3. They frequently **change practice**, which makes them well cited.

The honest counterweight: work of this kind must be executed impeccably. If you are criticising the rigour of others, your own rigour must be beyond reproach — equal tuning budgets, released code, adequate seeds, appropriate statistics, and scrupulously neutral language about other authors.

## 17.4 Gap types often combine

Real gaps are rarely of a single type, and saying so is a strength rather than a hedge. The running example combines:

- Type 9 (generalisation) — degradation across institutions;
- Type 7 (evaluation) — worst-site performance and calibration unreported;
- Type 2 (methodological) — all mitigations assume metadata that deployment removes.

A gap statement that names two or three types with evidence for each is more convincing than one claiming a single dramatic absence.

## Exercises

**Exercise 17.1** Write your current gap statement. Check it against every row of §17.2. If it matches any, rescue it by adding a mechanism and a measurement.

**Exercise 17.2** Classify your gap against Table 17.1. Expect two or three types. For each, write the specific evidence you hold.

**Exercise 17.3** Consider deliberately whether a type 7, 9, 10, or 11 framing of your topic would be more achievable with your resources than your current plan.

<div class="pagebreak"></div>

# Chapter 18 — How to Identify a Research Gap

## 18.1 The systematic procedure

Gaps are produced by a repeatable process, not by waiting for insight.

**Figure 18.1 — From fifteen papers to a defensible research gap**

```
  STEP 1 · ASSEMBLE          15 studies in the matrix, from a logged search
                             (Chapters 10, 15)
        │
        ▼
  STEP 2 · TALLY COLUMNS     Count every column. Write each count as a sentence.
                             • 11/15 random row-level splits on grouped data
                             • 12/15 report only accuracy or AUC
                             •  0/15 report worst-group performance
                             •  2/15 report calibration
                             •  0/15 run any statistical test
                             •  9/15 compare against ≤1 baseline
                             •  6/15 release no code
                             • 15/15 mitigations require domain labels
        │
        ▼
  STEP 3 · CLUSTER INTO      L1  Evaluation protocol leaks group identity   (11/15)
           LIMITATIONS       L2  Reported gains may lie within seed noise   (0/15 tests)
                             L3  Domain labels assumed available            (15/15)
                             L4  Decision-relevant quantities unreported    (0/15, 2/15)
        │
        ▼
  STEP 4 · UNRESOLVED        "The true cross-institutional degradation is unknown,
           PROBLEM            and no mitigation has been shown to work without
                              domain labels."
        │
        ▼
  STEP 5 · GAP STATEMENT     Absence + evidence + significance + what resolution
                             enables.  (Template in §19.4)
        │
        ▼
  STEP 6 · CONTRIBUTIONS     C1 ← answers L1, L2      C2 ← answers L3
           (1:1 mapping)     C3 ← answers L1, L4
```

Notice that **the study design fell out of the gap analysis**. This is the correct order. Most beginners design the method first and reverse-engineer a gap to justify it, which is why reviewers can smell it: the gap does not quite fit the method, and the contributions do not map onto the limitations of prior work.

## 18.2 The nine signals

Gaps announce themselves in nine recognisable places. Learn to read all nine.

| Signal | How to detect it | Gap types it typically yields |
|---|---|---|
| **Stated limitations** | Read every limitations and threats-to-validity section; tally recurring items | 2, 5, 6, 12 |
| **Future work** | Collect verbatim; a suggestion repeated by three or more papers is a field priority | any |
| **Contradictory results** | Two studies, same task, opposite conclusions → find the confound | 1, 7, 9 |
| **Missing datasets** | Search dataset registries; note absent languages, populations, modalities | 3, 6 |
| **Poor evaluation** | Tally the metrics column: accuracy on imbalanced data, no CI, no test | 7 |
| **Weak baselines** | Tally the baseline column: "compared with ERM only", or with a five-year-old method | 4, 7 |
| **Missing comparisons** | Method families that have never been compared *under one protocol* | 7, 9 |
| **Small samples, few seeds** | *n* below field norms; one to three seeds; a single split | 7, 10 |
| **Scope restrictions** | "We consider only English / adults / frontal views / synthetic data" | 6, 8, 9, 13 |

### 18.2.1 Mining limitations systematically

**Procedure.**

1. For each of ten to fifteen recent papers, open the limitations, threats-to-validity, discussion, and conclusion sections.
2. Copy each admitted weakness into a spreadsheet **verbatim**, with paper, section, and page.
3. Tag each with a category: `data`, `method`, `evaluation`, `scale`, `generality`, `efficiency`, `explainability`, `ethics`.
4. **Count the tags across papers.** A weakness admitted by six of fifteen studies is a field-level gap, not one author's excuse.
5. For each recurring weakness, ask the decisive question: *is it unsolved, or solved elsewhere and simply not applied here?*
   - **Unsolved** → potential novel contribution.
   - **Solved elsewhere** → potential transfer contribution. This is still publishable, but you must be honest in framing it, and you must explain why the transfer is non-obvious (§5.5).

Step 2 is not busywork. Those verbatim quotations, with page numbers, become the citations that justify the gap paragraph of your introduction (Chapter 32). Collecting them now saves reconstructing them later.

## 18.3 Reading "future work" correctly

Future-work sections are the most explicit, most freely given, and least used source of research directions in the literature.

Two cautions. First, a suggestion made once by one author is a hint; a suggestion made by five independent groups is a field priority and probably also a crowded space — check whether it has been done since. Second, authors sometimes propose future work they have already begun; forward-chain the paper (§10.8) to see whether the follow-up exists before investing.

## 18.4 Contradictions: the richest and least-used signal

When two studies on the same task reach opposite conclusions, the *explanation of the discrepancy* is a knowledge contribution — and one you can often produce with a controlled re-run rather than a new method.

**Procedure.**

1. Tabulate both studies side by side across every attribute in your matrix.
2. List every difference: dataset, split protocol, split unit, preprocessing, tuning budget, metric, seed count, model scale, evaluation code.
3. Form a hypothesis about which difference is the causal confound.
4. Design a single experiment that varies **only that factor**, holding everything else fixed.

This yields a clean, publishable study with a genuine knowledge claim, achievable in a semester, requiring no new theory. It is among the best first-paper designs available.

## 18.5 Worked derivation

**[HYPOTHETICAL]** Continuing the running example, with the tallies from Figure 18.1.

**Step 3 — limitations with counts and citations.**

| ID | Limitation | Count | Evidence source |
|---|---|---|---|
| L1 | Evaluation protocol permits group identity to leak between partitions | 11/15 | Matrix column F; mechanism documented by Zech et al. (2018) |
| L2 | Reported improvements are not distinguished from run-to-run variance | 15/15 report no test; 13/15 use ≤3 seeds | Matrix columns L, M |
| L3 | Mitigation methods require domain labels at training time | 15/15 of the mitigation subset | Each paper's setup section |
| L4 | Decision-relevant quantities (worst-group performance, calibration) unreported | 0/15 and 2/15 | Matrix column J |

**Step 4 — unresolved problem.** The magnitude of cross-institutional degradation is unknown under leakage-free protocols, and no mitigation has been demonstrated in the label-free regime that deployment actually imposes.

**Step 5 — gap statement.**

> "Across fifteen studies published between 2022 and 2026 and identified through a logged search of four databases, eleven evaluate chest-radiograph classifiers on random splits in which images from the same institution occur in both training and test partitions — a protocol shown to permit institution-specific confounding (Zech et al., 2018). Consequently the reported AUCs of 0.88 to 0.91 cannot be interpreted as cross-institutional performance, and the magnitude of degradation under leakage-free evaluation remains unquantified. Moreover, all eight mitigation methods we identified require institutional labels during training, whereas provenance metadata is routinely removed before data leaves an institution; and no study reports worst-institution performance or calibration, although these determine clinical usability. This study quantifies the degradation under institution-disjoint protocols with statistical validation, and evaluates a label-free mitigation on worst-institution AUC and calibration."

**Step 6 — contributions mapped one-to-one.**

| Contribution | Answers | Requires new theory? | Compute |
|---|---|---|---|
| C1 Leakage-free multi-institution re-evaluation of five published models, ten seeds, paired tests, confidence intervals | L1, L2 | No | Moderate |
| C2 A label-free adaptation method, with an ablation isolating the mechanism | L3 | Modest | Moderate |
| C3 Public release of institution-disjoint splits, code, and weights | L1, L4 | No | Negligible |

Two of the three contributions require no new theory and modest compute. This is what a resource-constrained but well-framed project looks like.

## 18.6 Common mistakes

| Mistake | Correction |
|---|---|
| Looking for a gap before reading | Read fifteen papers and build the matrix first |
| Looking for a gap in your head rather than in the tallies | Count the columns; the gap is usually audible when you read the tallies aloud |
| Finding the gap *after* choosing the method | Reverse the order (§18.1) |
| Treating one paper's limitation as a field gap | Count across papers; require a meaningful share |
| Ignoring contradictions | They are the richest signal (§18.4) |
| Not recording verbatim quotes with pages | You will need them as citations in your introduction |
| Choosing a gap you cannot address with your resources | Re-check the feasibility audit (§4.6) |
| Claiming a single dramatic gap | Two or three evidenced types are more convincing |

## Exercises

**Exercise 18.1** Complete Steps 1–6 of Figure 18.1 on your own matrix. Produce the tallies, the limitation table with counts, the unresolved problem, the gap statement, and the contribution mapping.

**Exercise 18.2** Mine limitations from fifteen papers using §18.2.1. Tag and count them. Report which weakness is most widely shared.

**Exercise 18.3** Find one contradiction in your set and complete the four-step procedure of §18.4. Assess whether the resulting experiment is within your resources.

**Exercise 18.4** For each contribution you propose, name the limitation it answers. Any contribution that answers none is unnecessary; any limitation with no contribution is an opportunity you are leaving unused.

<div class="pagebreak"></div>

# Chapter 19 — Strong versus Weak Research Gaps

## 19.1 Why this chapter exists

The difference between a publishable and an unpublishable paper is very often a single paragraph. Reviewers form a judgement about the gap early and read the remainder of the paper in that light. A gap stated with counts and citations produces a sympathetic reading; a gap stated as "existing methods have limitations" produces a sceptical one that the rest of the paper must then overcome.

## 19.2 Side-by-side comparison

**Table 19.1 — Weak and strong gap statements**

| ❌ Weak *[HYPOTHETICAL]* | Diagnosis | ✅ Strong *[HYPOTHETICAL]* |
|---|---|---|
| "Many researchers have worked on chest X-ray classification, but there is still room for improvement." | Vague; no absence identified; unfalsifiable; true of everything | "Across fifteen studies (2022–2026), eleven evaluate on random splits in which images from the same institution appear in both partitions; consequently the reported AUCs of 0.88–0.91 cannot be interpreted as cross-institutional performance, and the degradation under leakage-free protocols remains unquantified." |
| "Deep learning has not been applied to our hospital's dataset." | Local activity, not knowledge; no mechanism | "Our institution's imaging protocol differs from those represented in public benchmarks in exposure settings and device mix; since models are known to exploit acquisition artefacts (Zech et al., 2018), it is unknown whether published performance transfers to this acquisition regime." |
| "Existing methods have low accuracy." | Unquantified; low relative to what threshold? | "Reported worst-institution AUC does not exceed 0.83 in any study we identified, whereas triage support has been argued to require sensitivity above 0.90 at fixed specificity; the shortfall is therefore approximately 0.07 AUC and its cause is unexamined." |
| "No one has combined transformers with domain adaptation for radiographs." | Untried combination; no reason to expect anything | "Transformer attention aggregates global context, which we hypothesise increases sensitivity to institution-level acquisition signal relative to convolutional inductive bias; if so, transformers should degrade *more* under institution shift, which is testable and has not been tested." |
| "Research on explainability in medical imaging is limited." | "Limited" is not evidence | "Of fifteen studies, twelve present saliency maps as evidence of clinical validity, and none validates them against expert region annotation; the agreement between saliency and expert attention, and whether it predicts model correctness, is therefore unestablished." |
| "Prior work is old; we use a newer model." | Recency is not a contribution | "Prior comparisons predate architectures with global attention; whether the *conclusion* that invariance methods help survives the change in inductive bias is unknown, since no study evaluates both families under one protocol." |

The pattern is consistent. Strong statements are **longer**, contain **counts**, carry **citations**, name a **mechanism**, specify a **threshold**, and are **falsifiable**.

## 19.3 The three rescue operations

Almost every weak gap can be repaired by one of three moves.

**Rescue 1 — Add a mechanism.** Convert "X has not been applied to Y" into "assumption A of X is violated by property P of Y, so we predict effect E." Now there is a prediction that could fail.

**Rescue 2 — Add a count.** Convert "existing methods have limitations" into "*n* of *N* studies exhibit limitation L." Now the claim is evidenced and auditable.

**Rescue 3 — Add a consequence.** Convert "accuracy could be improved" into "performance is *x* against a required *y*, so decision D cannot currently be supported." Now significance is grounded in a decision rather than asserted with adjectives.

Most strong gap statements use all three.

## 19.4 The template

> "Across **[N]** studies identified through **[databases, search strings, date range]**, **[pattern, with counts]** holds. Consequently, **[specific quantity or mechanism]** remains **[unquantified / untested / unexplained]**, even though **[why it matters, and to whom]**. This study addresses that by **[action]**."

Every slot must be filled. If you cannot fill the first slot, you have not searched systematically; if you cannot fill the third, you have not identified an absence; if you cannot fill the fourth, you have not established significance.

## 19.5 How a gap must be evidenced

A gap is a claim about the literature, and like any claim it requires support. Four acceptable forms of evidence:

1. **Counts from a documented search.** The strongest form: "eleven of fifteen studies use protocol P". Requires the search log (§10.9) so a reviewer can audit it.
2. **Citations to authors' own admissions.** "Three of the studies we surveyed explicitly note this limitation [4], [9], [12]." Very strong, because the authors themselves concede it.
3. **A documented negative search.** "We searched four databases with the strings in Appendix A and identified no study that evaluates X under condition Y; the closest is [12], which evaluates X under Z." This is how absence is claimed responsibly.
4. **Your own measurement.** "In our reproduction, the reported result was not recoverable under the described protocol (§V-C)." Strongest of all for reproducibility gaps, but requires the work first.

**Not acceptable:** "to the best of our knowledge" with no search described; "few studies exist" with no count; an absence claim contradicted by a paper a reviewer finds in five minutes.

## 19.6 Stress-testing before submission

Before you commit, have a critical reader — supervisor, colleague, or reading group — attempt to break the gap with these six questions. This is the single highest-value review you can obtain, and it is free.

| Question | What a failure reveals |
|---|---|
| **Has this been done? Which paper is closest, and how exactly does yours differ?** | If you cannot name the closest paper, you have not searched enough |
| **How do you know the gap is real — which count supports it?** | If there is no count, the gap is an assertion |
| **Who benefits if you succeed, outside your institution?** | If nobody, significance is not established |
| **What is your riskiest assumption?** | If you cannot name one, you have not examined your own design |
| **Can you address it with your data, compute, and time?** | If not, the gap is real but not *yours* — narrow it |
| **What would a negative result look like, and would it be publishable?** | If not, this is advocacy rather than research (§5.3) |

Participants consistently want to skip this step. It is the step that prevents six months of work on an indefensible premise.

## 19.7 Common mistakes

| Mistake | Correction |
|---|---|
| "Room for improvement" as a gap | Apply all three rescues (§19.3) |
| A gap with no numbers | Count your matrix columns |
| "No work exists" without a documented search | Use the negative-search form (§19.5, item 3) |
| A gap requiring resources you lack | Narrow it, or reframe to type 7, 9, 10, or 11 (§17.3.1) |
| Gap and contributions that do not correspond | Map one-to-one (§18.5) |
| A gap found after the method was chosen | Reviewers detect retrofitting; reverse the order |
| Claiming a single gap type when two or three apply | Name them all, with evidence for each |
| Never stress-testing | Run §19.6 before writing anything else |

## 19.8 Verification checklist for Part VI

- [ ] My gap statement contains all four obligatory components (§17.1).
- [ ] It matches none of the eight non-gaps in §17.2.
- [ ] It is classified against the thirteen types, and I expect two or three.
- [ ] Every absence claim is supported by a count, an admission, a documented negative search, or my own measurement.
- [ ] I have written the tallies as sentences and they appear in the statement.
- [ ] I have collected verbatim limitation quotes with page numbers.
- [ ] I have examined every contradiction in my matrix.
- [ ] My contributions map one-to-one onto counted limitations.
- [ ] The gap is addressable with my actual data, compute, and time.
- [ ] A negative result would still be publishable, and I have written the sentence that would report it.
- [ ] A critical reader has attempted all six stress-test questions and the gap survived.

## Exercises

**Exercise 19.1** Rewrite your gap statement using the template in §19.4, filling every slot with specifics from your matrix.

**Exercise 19.2** Check it against every row of Table 19.1 and apply whichever of the three rescues it needs.

**Exercise 19.3** Identify which of the four evidence forms in §19.5 supports each absence claim you make. Any claim with no evidence form must be softened or removed.

**Exercise 19.4** Run the six stress-test questions with a partner. Record which question was hardest; that is where your project is weakest, and it is where a reviewer will begin.

<div class="pagebreak"></div>
