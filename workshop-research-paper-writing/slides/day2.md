---
marp: true
theme: workshop
paginate: true
footer: 'Day 2 · Research Paper Writing and Research Tools: From Research Idea to Journal Publication'
---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _footer: '' -->

# DAY 2
## Research Paper Writing, AI Tools, References, Ethics and Journal Publication

**Sections 9 – 25**

<br>

<div class="flow">
S9  Anatomy       S14 Methodology     S19 References      S24 Reviewer response
S10 Title         S15 Experiments     S20 AI tools        S25 Full case study
S11 Abstract      S16 Metrics         S21 Ethics
S12 Introduction  S17 Results/Disc.   S22 Journal choice
S13 Related work  S18 Figures/Tables  S23 Submission
</div>

<div class="warn">

**Prerequisite for today:** your literature matrix and your gap statement from Day 1. Every writing exercise today uses **your** topic. If your matrix has fewer than 10 rows, fix that during the first break.

</div>

<!--
SPEAKER NOTES — Day 2 opening (5 min)
Recap Day 1 in three sentences: you documented a search, built a matrix, and computed a gap. Today you convert that into a manuscript and a submission plan.
Set expectations for the day's pace: Day 2 has 17 sections and is deliberately front-loaded with writing exercises (title, abstract, intro) because those are the sections that decide desk-rejection. The afternoon is about evidence quality (experiments, metrics, results) and the mechanics of publishing (references, ethics, journals, reviewers).
Ask two people to state their gap in one sentence. If either cannot, spend five minutes fixing it now — writing cannot repair a broken gap.
-->

---

<!-- _class: dense -->
# S9 · Anatomy of an IEEE-Style Research Paper

<div class="cols-3-2">
<div>

| # | Section | Function — the one question it answers | Typical length (12-pg paper) |
|---|---|---|---|
| 1 | **Title** | What is this about, in searchable terms? | 8–15 words |
| 2 | **Abstract** | Should I read this? | 150–300 words |
| 3 | **Keywords** | How will indexers and readers find it? | 4–8 terms |
| 4 | **Introduction** | Why does this matter and what is unknown? | 1–1.5 pages |
| 5 | **Related Work** | What is already known, and where does it fall short? | 1–2 pages |
| 6 | **Methodology** | Exactly what did you do? (reproducibly) | 2–4 pages |
| 7 | **Experimental Setup** | Under what conditions was it measured? | 0.5–1 page |
| 8 | **Results** | What was observed? | 1.5–3 pages |
| 9 | **Discussion** | What does it mean, and why? | 1–2 pages |
| 10 | **Conclusion** | What is now known? | 1 paragraph |
| 11 | **Future Work** | What next? (often inside Conclusion) | 2–4 sentences |
| 12 | **References** | On whose shoulders? | 30–60 (journal) |
| + | Acknowledgements, Declarations, Appendices, Supplementary | Funding, ethics, data/code availability | as required |

</div>
<div>

#### The hourglass shape
<div class="flow">
 ╲   Introduction: broad → narrow
  ╲
   ╲  Related work
    │
    │  Methodology  ← narrowest,
    │  Experiments     most precise
    │  Results
   ╱
  ╱   Discussion
 ╱    Conclusion: narrow → broad
</div>

<div class="demo">

**Section boundaries are contracts.**
Results = observations, no interpretation.
Discussion = interpretation, no new numbers.
Method = what you did, no justification of *importance*.
Introduction = importance, no implementation detail.

Violating these is the most common structural criticism in reviews.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (6 min)
Draw the hourglass on the board. Then state the contracts and give the two classic violations: (1) a Results section that says "this proves our method is superior" (interpretation in results), and (2) a Discussion that introduces a new table (new evidence in discussion). Reviewers flag both routinely.
Mention that variants exist: many journals merge Results and Discussion (check the template), Nature-family journals invert the order, and some CS venues place Related Work after Method. The functions never change even when the labels do — teach function, then obey the template.
-->

---

# S9 · Writing Order ≠ Reading Order

<div class="cols">
<div>

#### Write in this order
| Step | Section | Why here |
|---|---|---|
| 1 | **Figures + tables** | They *are* the paper; if the story is not in them, no prose will save it |
| 2 | **Methodology** | Easiest — you did it; write while details are fresh |
| 3 | **Experimental setup** | Mechanical; forces you to notice missing controls |
| 4 | **Results** | Describe the figures/tables you already made |
| 5 | **Discussion** | Interpret; here you discover what the paper is *about* |
| 6 | **Related work** | Now you know what to contrast against; use your Day 1 matrix |
| 7 | **Introduction** | Written last because it must promise exactly what you delivered |
| 8 | **Conclusion** | Compress the introduction's promise + results |
| 9 | **Abstract** | Compress the whole paper |
| 10 | **Title + keywords** | Compress the abstract |

</div>
<div>

<div class="good">

**Why "figures first" works:** a reviewer forms an opinion from the abstract and the figures before reading a full paragraph. If your Table 2 and Figure 3 alone do not make the contribution visible, restructure the experiments — not the prose.

</div>

#### The one-page skeleton to write before any prose
<div class="flow">
Fig 1  System overview
Tab 1  Dataset statistics
Tab 2  Main comparison vs baselines (± CI)
Fig 2  Degradation under protocol change
Tab 3  Ablation study
Fig 3  Error analysis / qualitative failures
Tab 4  Cost: params, FLOPs, latency
</div>

<div class="warn">

If you cannot list your figures and tables before writing, you are not ready to write — you are still doing experiments.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (5 min) + micro-exercise
Micro-exercise (8 min): every participant writes their own figure/table skeleton (5-7 items, titles only) for the paper their Day 1 gap implies. Ask three to read theirs out. Diagnose gaps: a skeleton with no baseline comparison table, no ablation, and no cost table will be rejected — better to learn that today than after six months of experiments.
Explain the psychology of writing the introduction last: introductions written first make promises the experiments never keep, and reviewers notice the mismatch between the claimed contribution and the delivered evidence.
-->

---

# S10 · Writing the Title

<div class="cols">
<div>

#### What a good title does
1. Contains the **searchable keywords** a reader would type
2. Names the **method**, the **problem**, and (often) the **domain/application**
3. Is **specific** — a competitor could not use the same title
4. Is **honest** — no claim the paper does not deliver
5. Is **readable** — 8–15 words, minimal nesting, no unexplained acronyms
6. Avoids dead words: *A Study of, Novel, Efficient (unmeasured), Towards (vague), Using, Based on, An Approach for*

#### Patterns that work
- `[Method] for [Problem] in [Domain]`
- `[Question form]: [scope]`
- `[Finding]: [evidence]` ← strong for empirical papers
- `[Resource name]: A [type] for [purpose]` ← datasets/benchmarks

</div>
<div>

| ❌ Weak | Problem | ✅ Improved |
|---|---|---|
| "A Study on Deep Learning for Medical Images" | No method, no problem, no domain; unsearchable | "Site-Wise Evaluation of Chest Radiograph Classifiers: Quantifying Cross-Hospital Degradation" |
| "A Novel Efficient Framework for Text Classification Using Machine Learning" | 4 dead words; "framework" hides the claim; no domain | "Morphology-Aware Subword Tokenisation for Extractive QA in Marathi and Kannada" |
| "Improved Accuracy in Plant Disease Detection" | Improved over what? Which crop? Which condition? | "Few-Shot Leaf-Disease Detection Under Field Illumination With ≤50 Labelled Images per Class" |
| "Deep Learning Based Plagiarism Detection System" | Engineering title; "System" signals project | "Script Normalisation Recovers Sentence-Embedding Plagiarism Detection on Code-Mixed Hindi–English Text" |
| "AI in Agriculture: A Review" | Scope unbounded for a review | "Edge-Deployable Crop-Disease Models (2020–2025): A Systematic Review of Accuracy–Latency Trade-offs" |

<div class="demo">

**Test:** paste your title into Google Scholar. If the top 10 results are *not* your intended peers, your keywords are wrong.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (5 min) + ACTIVITY 10.1
Explain why keywords in the title matter mechanically: indexing and search ranking weight title terms heavily, so a title without your field's search terms costs you citations for the paper's whole life.
Discuss the colon construction: it lets you have both a memorable claim and a precise scope. It is standard in strong venues.
ACTIVITY 10.1 (10 min): write 3 candidate titles for your own paper, apply the Scholar test to the best one, then have a partner pick the strongest and say why. Insist that at least one candidate uses the "[Finding]: [evidence]" pattern — it forces them to know what their finding is.
-->

---

# S11 · The Abstract — Seven Moves in 200–300 Words

| Move | Sentences | Content | Common failure |
|---|---|---|---|
| 1 **Background** | 1–2 | Why the problem matters. No textbook history | Three sentences on the history of AI |
| 2 **Problem / gap** | 1–2 | The specific unknown, ideally with a number | "However, there are some challenges" |
| 3 **Objective / approach** | 1 | What you did, named precisely | "We propose a novel framework" |
| 4 **Method detail** | 1–2 | The mechanism, enough to be identifiable | Marketing adjectives instead of mechanism |
| 5 **Data / experiment** | 1 | Datasets, scale, protocol, baselines | Datasets never named |
| 6 **Results** | 1–2 | **Numbers with the comparison point** and variance | "Results show effectiveness of our method" |
| 7 **Conclusion / implication** | 1 | What this now means; scope of the claim | Repeating the results verbatim |

<div class="cols">
<div>

#### Hard rules
- **No citations** (most venues), **no undefined acronyms**, **no figure/table/section references**
- **No claim absent from the paper**
- Numbers must **match** the results section exactly
- Written **last**; revised **most**
- Respect the word limit **exactly** — submission systems truncate

</div>
<div>

#### Structured abstracts
Many Elsevier/Springer/IEEE Access journals request explicit labels: **Background · Objective · Methods · Results · Conclusions**. Check the *Guide for Authors*; if labels are requested, use them verbatim.

<div class="demo">

**The 10-second test:** hide everything but your abstract. Can a stranger state your contribution and your headline number? If not, rewrite.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (5 min)
The abstract is the most-read and least-revised part of a student paper. Say plainly: editors desk-reject from the abstract, reviewers accept the invitation to review from the abstract, and readers decide from the abstract. It deserves 10% of total writing time.
Warn about the numbers-must-match rule with a real consequence: mismatched abstract/results numbers look like carelessness at best and manipulation at worst, and they are trivially caught by a careful reviewer.
-->

---

<!-- _class: dense -->
# S11 · Weak vs Improved Abstract

<div class="bad">

#### ❌ Weak (118 words — vague, unfalsifiable, no numbers)
"Deep learning has revolutionised medical image analysis in recent years. Many researchers have proposed various models for chest X-ray classification. However, there are still some challenges and room for improvement. In this paper, we propose a novel and efficient deep learning framework for chest X-ray classification. Our proposed model uses advanced techniques to extract better features. Experiments were conducted on a benchmark dataset and the results show that our proposed method outperforms existing state-of-the-art methods in terms of accuracy. The results demonstrate the effectiveness and superiority of the proposed approach. In future, we will extend our work to other medical imaging modalities."

**Diagnosis:** Move 2 is a cliché ("some challenges"); Moves 4–6 contain no mechanism, no dataset name, no number, no baseline; every claim is unverifiable. This abstract would be desk-rejected or, worse, ignored.

</div>

<div class="good">

#### ✅ Improved (247 words — same study, defensible)
"**[1 Background]** Deep learning models for chest radiograph (CXR) classification report areas under the ROC curve (AUC) of 0.88–0.91, and are increasingly proposed for triage support. **[2 Gap]** However, in a review of 15 studies published between 2022 and 2026, 11 evaluate on random splits in which images from the same institution appear in both training and test partitions, and none report worst-institution performance or calibration; the degradation incurred when models are deployed at an unseen hospital is therefore unquantified. **[3 Objective]** We re-evaluate five published architectures under leakage-free, site-wise protocols and ask whether site-label-free adaptation can mitigate the resulting degradation. **[4 Method]** We propose CLUSTER-DG, which replaces the site-supervised discriminator of adversarial domain generalisation with unsupervised clustering of image-embedding statistics, requiring no provenance metadata. **[5 Experiments]** Experiments use CheXpert, MIMIC-CXR and NIH ChestX-ray14 (712,000 images, 14 findings) with institution-disjoint splits, 10 random seeds, an identical 50-trial tuning budget for all methods, and four baselines (ERM, Mixup, CORAL, IRM). **[6 Results]** Replacing random with site-wise splits reduces macro AUC from 0.897 ± 0.004 to 0.781 ± 0.011 (mean ± 95% CI), a drop of 0.116. CLUSTER-DG recovers 0.041 ± 0.009 of worst-site AUC over ERM (paired Wilcoxon, p = 0.004) and reduces expected calibration error from 0.094 to 0.052, without site labels and at equal parameter count. **[7 Conclusion]** Reported CXR performance substantially overstates cross-hospital behaviour, and most of the recoverable gap can be closed without provenance metadata. Code, splits and trained weights are released."

</div>

<!--
SPEAKER NOTES — (8 min)
Read the weak abstract aloud, then ask: "What did they do? On what data? Better than what, by how much?" The room cannot answer. That is the lesson.
Then walk the improved version by labelled move. Point out five specific professional signals: (1) the gap has a count (11 of 15); (2) the method's mechanism is named in one clause; (3) the datasets and scale are explicit; (4) results carry variance AND a statistical test; (5) the last sentence states a scope-limited implication plus artefact release.
Note that the numbers here are illustrative for teaching. Tell participants explicitly: never invent numbers in a draft abstract, not even as placeholders you intend to replace - use "[TBD]" instead, because placeholder numbers have been known to survive into submitted manuscripts.
-->

---

# S11 · Abstract Checklist + Exercise

<div class="cols">
<div>

#### Checklist — tick every line before submission
- [ ] Within the journal's word limit (counted, not estimated)
- [ ] All seven moves present, in order
- [ ] Gap sentence contains a **specific unknown**, ideally quantified
- [ ] Method mechanism identifiable in one sentence
- [ ] Dataset(s) **named**, with scale
- [ ] Baselines named
- [ ] ≥2 result numbers **with comparison point and variance**
- [ ] Statistical test named if a comparison is claimed
- [ ] Every number matches the Results section
- [ ] No citations, no undefined acronyms, no "Fig. 3", no section refs
- [ ] No claim that the paper does not deliver
- [ ] Scope limitation or implication in the final sentence
- [ ] Keywords chosen from the journal's/IEEE thesaurus, not invented
- [ ] Read aloud once; no sentence longer than ~35 words

</div>
<div>

<span class="tag act">ACTIVITY 11.1 — 25 min</span>
**Write your abstract**

1. Write one sentence per move, in order — **7 sentences, nothing else**. (10 min)
2. Expand to 200–300 words. Where you do not yet have results, write the *shape* of the claim with `[TBD]` — never a fabricated number. (10 min)
3. Swap with a partner. The partner labels each sentence `1`–`7` and marks any move that is **missing** or **doubled**. (5 min)

<div class="warn">

**Ethics checkpoint:** an abstract for an unfinished study is a **plan**, not a claim. Mark placeholders clearly. Reporting results you have not obtained — even in a draft shared with a supervisor — is how fabrication starts.

</div>

<div class="good">

**Takeaway:** an abstract is seven decisions, not a paragraph. Make each decision explicitly and the paragraph writes itself.

</div>

</div>
</div>

<!--
SPEAKER NOTES — Activity facilitation (25 min)
The "7 sentences, nothing else" constraint is what makes this work. Do not let participants start with prose.
Circulate looking for the two most common defects: (a) Move 2 is a cliché rather than a specific unknown — send them back to their Day 1 tallies for a number; (b) Move 6 has no comparison point — "0.83 AUC" means nothing without "vs 0.78 for ERM".
Reinforce the ethics checkpoint verbally. This is the first of several places today where the workshop's integrity rule is applied concretely rather than preached.
-->

---

# S12 · The Introduction — Six-Paragraph Blueprint

<div class="cols-3-2">
<div>

| ¶ | Function | Contains | Length |
|---|---|---|---|
| **1** | **Background / stakes** | The domain problem and why it matters; 1–2 authoritative citations; a concrete number if possible | 4–6 lines |
| **2** | **Current state / existing problem** | What is being done now and what specifically is unsatisfactory | 5–8 lines |
| **3** | **Existing approaches** | The 2–3 families of prior solutions, grouped (not listed) | 6–10 lines |
| **4** | **Limitations → research gap** | The evidenced absence, with counts; the *pivot* of the paper | 6–10 lines |
| **5** | **Proposed approach** | What you do, the mechanism, and why it should work | 6–10 lines |
| **6** | **Contributions + roadmap** | 3–4 numbered contributions; one-line paper organisation | bulleted |

<div class="flow">
GENERAL ─► SPECIFIC ─► PROBLEM ─► GAP ─► SOLUTION ─► CONTRIBUTION
  ¶1         ¶2          ¶2/3      ¶4      ¶5           ¶6
</div>

</div>
<div>

#### Rules
- ¶4 is the **hinge**. Everything before it builds pressure; everything after releases it.
- Each paragraph should have **one job**; if you cannot name a paragraph's job, merge or delete it.
- Contributions in ¶6 must **match** the abstract, the results sections, and the conclusion **verbatim in substance**.
- Never introduce implementation detail (learning rates, library versions) in the introduction.
- The last sentence of ¶4 and the first of ¶5 should read as a single logical step.

<div class="demo">

**Reverse-outline test:** after drafting, write the job of each paragraph in the margin in ≤6 words. If two paragraphs have the same job, or a job is missing, the structure is broken — fix structure before sentences.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (5 min)
Emphasise the hinge. Weak introductions have no hinge: they drift from background to "in this paper we propose" without ever creating an unmet need, so the proposal answers no question.
Teach the reverse-outline test as a lifelong habit; it works on theses and grant proposals too.
Point out the consistency requirement across abstract / intro contributions / results / conclusion. Reviewers check this alignment, and misalignment reads as a paper assembled from parts.
-->

---

<!-- _class: dense -->
# S12 · A Complete Worked Introduction

<div class="small">

**[¶1 Background]** Chest radiography is the most frequently performed diagnostic imaging examination worldwide, and radiologist shortages have motivated automated triage of abnormal studies [1], [2]. Deep classifiers now report areas under the ROC curve (AUC) of 0.88–0.91 on public benchmarks such as CheXpert and MIMIC-CXR [3]–[5], a level often described as radiologist-comparable.

**[¶2 Existing problem]** These figures, however, are obtained almost exclusively within a single institutional distribution. Acquisition hardware, exposure protocols, patient demographics and post-processing pipelines differ substantially across hospitals, and models are known to exploit institution-specific artefacts — laterality markers, collimation borders, even scanner-specific noise — as shortcuts for prediction [6]. A model that is accurate on the distribution it was trained on may therefore be unsafe at the hospital that deploys it, which is precisely the setting that matters clinically.

**[¶3 Existing approaches]** Two families of work address this. The first increases representational capacity, moving from convolutional backbones [3] to vision transformers [5]; these report in-distribution gains of 1–3 AUC points but do not target transfer. The second explicitly optimises for invariance across domains, using feature-distribution alignment (CORAL [7]), invariant risk minimisation (IRM [8]), or adversarial site discriminators [9]; these report external gains of 3–6 AUC points.

**[¶4 Limitations → gap]** *(the hinge)* Both families rest on assumptions that our review of 15 studies published between 2022 and 2026 shows to be problematic. First, 11 of the 15 evaluate on random splits in which radiographs from the same institution — and frequently the same patient — occur in both training and test partitions, so the reported AUCs measure in-distribution performance rather than transfer. Second, all eight invariance methods we identified require **site labels at training time**, whereas provenance metadata is routinely stripped before data leaves a hospital for privacy reasons. Third, none of the 15 studies reports worst-institution AUC or calibration error, although these quantities, not the average, determine whether a triage system is deployable. The magnitude of cross-hospital degradation under leakage-free protocols is therefore unknown, and no mitigation has been demonstrated in the label-free regime that deployment actually imposes.

**[¶5 Proposed approach]** We address both parts of this gap. We first re-evaluate five published architectures under institution-disjoint splits on three public datasets, with 10 seeds and an identical tuning budget for every method, which isolates the effect of the evaluation protocol from the effect of the model. We then propose **CLUSTER-DG**, which replaces the site-supervised discriminator of adversarial domain generalisation with unsupervised clustering of channel-wise embedding statistics. The intuition is that acquisition artefacts dominate low-order feature statistics, so clusters recovered from those statistics approximate site identity closely enough to support an invariance penalty without any metadata.

**[¶6 Contributions]** Our contributions are: **(1)** the first leakage-free, multi-institution quantification of degradation for five widely used CXR architectures, with confidence intervals and paired significance tests; **(2)** CLUSTER-DG, a site-label-free adaptation method that recovers 0.041 ± 0.009 worst-site AUC over empirical risk minimisation at equal parameter count; **(3)** an ablation isolating the contribution of cluster granularity, invariance weight and augmentation; and **(4)** a public release of institution-disjoint splits, code and trained weights to make future comparisons protocol-consistent. Section II reviews related work, Section III describes the method, Sections IV–V present the setup and results, and Section VI discusses limitations.

</div>

<!--
SPEAKER NOTES — (10 min)
This is the single most reusable slide in Day 2. Walk it paragraph by paragraph and name the move each time.
Specific things to point out:
• ¶2 ends on stakes ("unsafe at the hospital that deploys it"), not on a technicality.
• ¶3 groups into two families with citation groups, not one-paper-per-sentence.
• ¶4 has THREE numbered evidence items with counts. This is where Day 1's matrix cashes out. Ask the room: "where did 11 of 15 come from?" Answer: column E tallies.
• ¶5 explains WHY the mechanism should work ("artefacts dominate low-order statistics"). Most student papers state what they built and never why it should work; reviewers read that omission as the absence of an idea.
• ¶6 numbered contributions, each auditable, one of which is an artefact release.
Then run ACTIVITY 12.1 (30 min): participants draft ¶4 and ¶6 for their own paper - the hinge and the contributions - because those two carry the paper. Partners check that ¶4 contains at least one count and that every ¶6 contribution maps to an objective from Day 1.
-->

---

# S12 · Introduction — Mistakes and Fixes

| ❌ Mistake | Why reviewers react badly | ✅ Fix |
|---|---|---|
| Textbook history ("AI began in 1956…") | Wastes the most valuable paragraph; signals inexperience | Start at the *specific* problem with a concrete number |
| Gap stated as "less work has been done" | Unverifiable; reads as an excuse | Count it: "11 of 15 studies…" |
| Contributions that restate the method 3 times | Padding; reviewers count real contributions | 3–4 distinct, auditable contributions |
| Introduction promising more than results deliver | Direct cause of major revision/reject | Write the introduction **after** results |
| Related work fully duplicated in the introduction | Redundancy; wastes page budget | ¶3 = 2–3 grouped families only; detail in Section II |
| Hyperparameters or code details in ¶5 | Wrong section | Mechanism and rationale only |
| No roadmap sentence | Minor, but editors notice | One sentence at the end of ¶6 |
| Citing only 2022–2026 work | Looks like you do not know the field's origins | Cite the origin *and* the frontier |
| First-person over-claim ("we solve the problem of…") | Invites hostile review | Bound the claim: "we quantify…", "we recover ~35% of…" |

<div class="good">

**Takeaway:** The introduction's job is to make your contribution *inevitable*. If a reader could finish ¶4 and predict ¶5, you have written it correctly.

</div>

<!--
SPEAKER NOTES — (4 min)
The "inevitable" test is the memorable line — say it twice. A good introduction makes the reader think of your solution before you present it; then your paper feels necessary rather than arbitrary.
On the citation-recency row: mention that citing only very recent work is a common LLM-assisted-writing artefact, and reviewers in mature fields notice immediately when the foundational papers are missing.
-->

---

# S13 · Related Work — Construction Mechanics

<div class="cols">
<div>

#### Procedure (from your Day 1 matrix, in 6 steps)
1. **Sort** the matrix by the Method column; look for natural families.
2. **Name** 2–4 families with substantive labels: *"capacity-scaling approaches"*, *"invariance-based approaches"*, *"test-time adaptation"* — not *"CNN-based"* / *"other methods"*.
3. **One subsection per family.** Inside each: what the family assumes → representative works (grouped citations) → what it achieves → **the shared weakness**.
4. **Insert a comparison table** with the columns your argument needs (usually: method, data, split protocol, baselines, metrics, key result, limitation).
5. **Add a subsection on evaluation practice** — this is where your evaluation gap becomes visible.
6. **Close with a synthesis paragraph** that states what is settled, what is contested, and what is untested → the gap, phrased identically to Introduction ¶4.

</div>
<div>

#### Citation mechanics
| Practice | Do |
|---|---|
| Grouping | `[3]–[5]` for a shared claim; individual cites only when the specific paper matters |
| Attribution of origin | Cite the paper that *introduced* the method, plus a recent user if needed |
| Density | Claims about the field need 2+ citations; a claim with one citation is an anecdote |
| Direct quotation | Rare in CS; if used, quote marks + citation + page |
| Secondary citation | Avoid "as cited in"; read the primary source |
| Self-citation | Only where genuinely relevant; excessive self-citation is flagged by editors |
| Adversarial cite | If a paper contradicts you, **cite and address it** — hiding it is worse |

<div class="warn">

Never cite a paper you have not opened, and never trust a reference produced by an AI tool without verifying it on the publisher's site. Fabricated citations are a fast route to a desk rejection and a damaged reputation.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (5 min)
Step 5 deserves emphasis: a subsection titled "Evaluation practices in prior work" is unusual in student papers and immediately signals rigour. It is also the paragraph that justifies the whole paper if your contribution is a re-evaluation.
Step 6's phrasing rule (same gap wording in intro and related work) is a coherence trick: repetition of a precise formulation reads as confidence, whereas two different phrasings of the same gap read as vagueness.
-->

---

<!-- _class: xdense -->
# S13 · Weak vs Strong Related Work + the Gap Paragraph

<div class="cols">
<div>

<div class="bad">

#### ❌ Weak (paper-by-paper, no dimension)
"Zhang et al. [11] proposed a CNN with attention and achieved 0.90 AUC on CheXpert. Patel et al. [12] used DenseNet-121 and reported 0.89. Lee et al. [13] applied a vision transformer, achieving 0.91. Gupta et al. [14] used CORAL for domain adaptation. Rao et al. [15] used IRM and showed improvement in external validation."

**Five faults:** (1) chronological accident as structure; (2) numbers from different datasets and splits presented as if comparable; (3) no evaluation of quality; (4) no shared dimension; (5) no gap at the end.

</div>

<div class="demo">

#### The comparison table that must accompany it
| Work | Split | Baselines | Metrics | Site labels |
|---|---|---|---|---|
| [11] | random | none | AUC | – |
| [12] | random | 1 | AUC | – |
| [13] | site-wise | 1 | AUC | – |
| [14] | site-wise | ERM | AUC | required |
| [15] | site-wise | ERM, CORAL | AUC, ECE | required |

*The table does the comparing; the prose does the judging.*

</div>

</div>
<div>

<div class="good">

#### ✅ Strong (grouped, evaluated, gap-terminating)
"**Capacity-scaling approaches.** One line of work treats cross-hospital robustness as a byproduct of better representations, progressing from attention-augmented convolutional backbones [11], [12] to vision transformers [13]. These report 0.89–0.91 AUC, but all three evaluate on random splits (Table I), so their numbers are in-distribution and cannot be read as evidence of transfer.

**Invariance-based approaches.** A second line optimises explicitly for domain invariance via feature alignment [14] or invariant risk minimisation [15], and does evaluate across institutions, reporting 3–6 point external gains. Both, however, require site labels during training, and neither reports variance over more than three seeds; since seed-to-seed variation of 1–2 AUC points is documented for these architectures [12], it is unclear whether the reported margins exceed run-to-run noise.

**Evaluation practice.** Across the 15 studies we surveyed, none reports worst-institution AUC and only two report calibration, although a triage system's usability is governed by its weakest site and by the reliability of its confidence estimates rather than by its mean AUC.

**Synthesis and gap.** The field has therefore established that distribution shift matters, but not how large it is under leakage-free protocols, nor whether invariance can be obtained without site metadata, nor what happens to worst-site performance and calibration. This paper addresses these three questions directly."

</div>

</div>
</div>

<!--
SPEAKER NOTES — (7 min) + ACTIVITY 13.1
Point out the division of labour between table and prose: the table carries facts, the prose carries judgement. Students often do the reverse - narrating facts in prose and never interpreting.
Note the phrase "cannot be read as evidence of transfer" - firm, specific, and about the protocol rather than the authors' competence. That is the professional register.
ACTIVITY 13.1 (25 min): participants write ONE family subsection (150-200 words) plus their comparison table from their own matrix, ending with an absence sentence. Partner check: does every sentence either group, evaluate, or identify absence? Any sentence that merely reports gets struck through.
-->


---

<!-- _class: dense -->
# S14 · Methodology — What Must Be Describable

<div class="cols-3-2">
<div>

<div class="flow">
DATA ──► PREPROCESSING ──► FEATURE EXTRACTION ──► MODEL
                                                    │
        EVALUATION ◄── TESTING ◄── VALIDATION ◄── TRAINING
</div>

| Component | Must state | Frequently omitted (→ reviewer question) |
|---|---|---|
| **Dataset** | Name, version, size, classes, distribution, licence, source | Class imbalance ratio; version/date |
| **Data collection** | Instrument, period, sampling, consent/IRB, annotation protocol, inter-annotator agreement | Who labelled it, and how disagreements were resolved |
| **Preprocessing** | Resize, normalisation (with statistics used), cleaning, deduplication, tokenisation | **Whether normalisation statistics came from train only** |
| **Feature extraction** | Handcrafted features or learned; input representation; dimensionality | Exact input size and channel handling |
| **Model architecture** | Layers, blocks, parameter count, pretrained weights + source | Parameter count; pretraining corpus |
| **Proposed algorithm** | Pseudocode, complexity, novel component isolated | Which part is new vs inherited |
| **Training** | Loss, optimiser, LR + schedule, batch size, epochs, early-stopping criterion, augmentation | Early-stopping signal (on validation, never test) |
| **Validation** | Split ratio or CV scheme, selection metric, tuning budget | Tuning budget per method |
| **Testing** | Held-out protocol, when the test set was touched | Number of test evaluations |
| **Hyperparameters** | Search space, search method, trials, final values | Search *budget* — the fairness variable |
| **Environment** | GPU/CPU, RAM, framework + version, seeds, wall-clock time | Seeds and versions |

</div>
<div>

#### The reproducibility standard
> *"Could a competent stranger, with the paper and the released code, obtain my numbers within noise?"*

If the answer needs an email from you, the methodology is incomplete.

<div class="warn">

**Leakage traps to declare explicitly**
- Normalisation/scaling fitted on the full dataset
- Oversampling (e.g. SMOTE) applied **before** splitting
- Data augmentation crossing the split boundary
- Multiple images of the same patient/user split across partitions
- Feature selection performed on all data
- Hyperparameters tuned on the test set
- Duplicated records between train and test

</div>

<div class="good">

State in one sentence: *"All preprocessing statistics, resampling and feature selection were fitted on training folds only."* Reviewers look for this sentence.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (7 min)
The leakage box is the highest-value content on this slide. SMOTE-before-split and scaler-fitted-on-all-data are pervasive in student papers and inflate results dramatically. Ask for a show of hands about who has done it; be kind, because almost everyone has.
The reproducibility standard is the sentence to remember. Contrast a methodology paragraph as a recipe (a stranger can cook it) with a methodology paragraph as a summary (only the author can).
Coaching note: the "tuning budget per method" row is the fairness lever that decides whether an improvement claim survives scrutiny.
-->

---

<!-- _class: dense -->
# S14 · Writing the Data and Preprocessing Subsections

<div class="cols">
<div>

<div class="bad">

#### ❌ Weak
"We used the CheXpert dataset. The images were preprocessed and resized. Data augmentation was applied to increase the dataset size. The data was divided into training and testing sets."

**Unanswerable questions:** which version? how many images? resized to what? which augmentations, with what probabilities? what split ratio, and split by *what unit*? Was augmentation applied to the test set?

</div>

<div class="good">

#### ✅ Strong
"We use CheXpert v1.0 (223,414 frontal and lateral radiographs from 65,240 patients, 14 findings with uncertainty labels) [3]. We retain frontal views only (191,027 images) and map uncertain labels to negative, following the convention of [3] to preserve comparability. Images are resized to 224 × 224 with bilinear interpolation and normalised using channel statistics computed **on the training partition only** (μ = 0.503, σ = 0.291). Training augmentation comprises random resized crop (scale 0.8–1.0), horizontal flip (p = 0.5) and rotation (±10°); no augmentation is applied at validation or test time. Splits are **patient-disjoint and institution-disjoint**: no patient and no institution appears in more than one partition (70/10/20 by patient count). Class prevalence ranges from 1.2% (pneumothorax) to 38.5% (support devices); we report per-class metrics because of this imbalance."

</div>

</div>
<div>

#### The five sentences every data subsection needs
1. **Provenance:** dataset name, version, size, source, licence.
2. **Filtering:** what you excluded and *why*, with resulting counts.
3. **Transformations:** exact operations, parameters, and **what statistics were fitted where**.
4. **Split protocol:** ratios *and the unit of splitting* (image / patient / site / user / time).
5. **Distribution:** class balance, and the consequence for your metric choice.

<div class="demo">

#### Dataset table (Table I in most papers)
| Dataset | Images | Patients | Sites | Classes | Split unit | Licence |
|---|---|---|---|---|---|---|
| CheXpert | 191,027 | 65,240 | 1 | 14 | patient | research use |
| MIMIC-CXR | 377,110 | 65,379 | 1 | 14 | patient | PhysioNet DUA |
| NIH CXR14 | 112,120 | 30,805 | 1 | 14 | patient | open |

*Numbers illustrative — verify against the dataset's own documentation before use.*

</div>

</div>
</div>

<!--
SPEAKER NOTES — (5 min)
Point 4 - the unit of splitting - is the sentence that separates careful papers from careless ones in any domain with grouped data: patients, users, sessions, schools, sensors, time periods. In NLP it is documents or authors; in SE it is projects; in education research it is classrooms.
Have participants take the weak paragraph and rewrite it for their own dataset in 6 minutes. Then ask two of them to state the unit of splitting in their study. If someone says "we split randomly by row" and their data is grouped, you have just prevented an invalid study.
-->

---

# S14 · Method, Algorithm, and Mathematical Formulation

<div class="cols">
<div>

#### Structure of a method section
1. **Overview paragraph** + Figure 1 (system architecture): the pipeline in 5–7 sentences, one per block.
2. **Formal problem statement**: notation, inputs, outputs, objective.
3. **Component subsections**, one per block, with the **novel component clearly isolated**.
4. **Algorithm box** (pseudocode) with complexity.
5. **Loss function** and how components combine.
6. **Design-rationale sentences**: *why* this choice, not just *what*.

#### Notation discipline
- Define **every** symbol at first use; keep a consistent convention (bold lowercase = vectors, bold uppercase = matrices, calligraphic = sets).
- Never reuse a symbol for two meanings.
- Match your **code variable names** to the paper's symbols — future-you and your reviewers will thank you.

</div>
<div>

#### Example formulation
Let $\mathcal{D}=\{(x_i,y_i,s_i)\}_{i=1}^{N}$ with image $x_i$, label $y_i$ and (unobserved) site $s_i$. With encoder $f_\theta$ and classifier $g_\phi$:

$$
\mathcal{L} = \underbrace{\frac{1}{N}\sum_i \ell_{\mathrm{BCE}}\big(g_\phi(f_\theta(x_i)),y_i\big)}_{\text{task loss}} \;-\; \lambda\,\underbrace{\mathcal{I}\big(f_\theta(x),\hat{c}(x)\big)}_{\text{invariance to inferred cluster}}
$$

where $\hat{c}(x)$ is the cluster assigned by k-means over channel-wise embedding statistics and $\lambda$ ramps $0\!\rightarrow\!1$ over the first 5 epochs.

#### Algorithm 1 · CLUSTER-DG (one epoch)
```
Input : batches B, encoder fθ, head gφ, K clusters, λ_t
1  for each batch b in B:
2      z ← fθ(b.x)                       # embeddings
3      μ,σ ← channel_stats(z)            # low-order stats
4      ĉ ← kmeans_assign(concat(μ,σ), K) # inferred site
5      L_task ← BCE(gφ(z), b.y)
6      L_inv  ← domain_confusion(z, ĉ)
7      L ← L_task − λ_t · L_inv
8      θ,φ ← Adam_step(∇L)
9  refit k-means centroids every E epochs
Output: θ, φ         # cost: O(NKd) per epoch over baseline
```

</div>
</div>

<!--
SPEAKER NOTES — (7 min)
Stress the "design-rationale sentences". Reviewers distinguish engineering from research precisely here: a paper that says "we add a clustering branch" is engineering; a paper that says "acquisition artefacts dominate low-order statistics, therefore clusters over those statistics should approximate site identity" is research, because it states a testable belief that the ablation then checks.
On pseudocode: keep it to 10-15 lines, name the novel lines (here 3-4-6), and report the extra complexity relative to the baseline. Reviewers ask "what does this cost?" every single time.
Tools to mention for typesetting: Overleaf with algorithm2e or algorithmicx, and mathpix/Detexify for symbol lookup.
-->

---

<!-- _class: dense -->
# S14 · Diagrams, Flowcharts and the Methodology Checklist

<div class="cols">
<div>

#### Making the figures <span class="tag tool">TOOLS</span>
| Tool | Best for | Notes |
|---|---|---|
| **draw.io / diagrams.net** | Architecture + flowcharts | Free; export **SVG/PDF** (vector) |
| **Inkscape** | Publication-grade vector editing | Free; full control |
| **PowerPoint / Keynote** | Fast block diagrams | Export as PDF, never as screenshot |
| **Mermaid / Graphviz** | Version-controlled diagrams from text | Great with Git; reproducible |
| **TikZ / PGFPlots** | LaTeX-native, perfect typography | Steep learning curve, best results |
| **Matplotlib / seaborn** | Result plots | Save as PDF/SVG; set font sizes explicitly |
| **NN-SVG, PlotNeuralNet** | Neural architecture drawings | Publication-quality CNN/transformer figures |

<div class="warn">

**Never** paste a screenshot of a diagram into a paper. Vector (PDF/SVG/EPS) only; raster only for photographs/heatmaps at ≥300 dpi.

</div>

</div>
<div>

#### Architecture-diagram rules
1. Left→right or top→bottom, one direction only.
2. Every arrow labelled with **what flows** (tensor shape, data type).
3. **Highlight the novel block** (colour or bold outline) and say so in the caption.
4. Include input and output shapes.
5. Font ≥ 8 pt **after** scaling to column width.
6. Greyscale-legible; never rely on colour alone.
7. The caption must be self-contained (a reader who reads only figures should understand it).

#### Methodology self-check
- [ ] A stranger could reimplement from this section alone
- [ ] Every symbol defined once, used consistently
- [ ] Novel component visibly isolated
- [ ] Complexity/cost stated relative to the baseline
- [ ] Leakage statement present
- [ ] Tuning budget stated and equal across methods
- [ ] Seeds, versions, hardware stated
- [ ] Code/data availability statement written

</div>
</div>

<!--
SPEAKER NOTES — (5 min) + ACTIVITY 14.1
ACTIVITY 14.1 (30 min): each participant (a) draws their system architecture in draw.io and exports SVG/PDF, (b) writes Algorithm 1 in 10-15 lines of pseudocode, (c) writes the data subsection using the five-sentence rule. Then swap laptops: the partner must attempt to explain the pipeline back from the diagram alone, without help. Every point of confusion is a defect to fix.
Live demo if time: draw.io -> a 5-block pipeline -> File > Export as > PDF (crop) -> insert in Overleaf. Two minutes, and it removes the excuse that good figures are hard.
-->

---

# S15 · Experimental Design

<div class="cols">
<div>

#### The seven design decisions
| Decision | Rule |
|---|---|
| **Datasets** | ≥2 (ideally 3) with different characteristics; justify each; include the standard benchmark of your field even if unfavourable |
| **Splits** | Grouped and, where relevant, temporal. Fixed, published, identical across methods |
| **Baselines** | (a) trivial/majority, (b) classical strong (e.g. gradient boosting, TF-IDF+SVM), (c) the current SOTA, (d) your method minus its novelty |
| **Tuning** | Identical search space size and trial budget for **every** method — state it |
| **Repetition** | ≥5 seeds (10 preferred), report mean ± std or 95% CI |
| **Ablation** | One component removed at a time, plus the cumulative build-up |
| **Cost** | Parameters, FLOPs, training time, inference latency, memory |

<div class="bad">

**Why "only my model" is insufficient:** without baselines you have measured the *task difficulty*, not your contribution. Without ablations you have shown *that* the whole pipeline works, not *which part* matters — so nobody, including you, knows what to reuse.

</div>

</div>
<div>

#### Splits, cross-validation and leakage
| Scheme | Use when |
|---|---|
| Fixed train/val/test | Large data; benchmark convention exists |
| *k*-fold CV (k=5,10) | Small/medium data; need variance estimates |
| **Stratified** *k*-fold | Class imbalance |
| **Grouped** *k*-fold | Repeated measures per patient/user/site |
| Nested CV | Tuning **and** unbiased estimation on small data |
| Leave-one-site-out | Cross-domain generalisation claims |
| Temporal / rolling-origin | Any time-dependent data — **never** shuffle time series |
| Repeated CV (different seeds) | Reporting variance honestly |

<div class="warn">

**The test set is touched once, at the end.** Every additional look is tuning, and tuning on test invalidates the estimate. Keep a decision log of when you evaluated on test and why.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (7 min)
Spell out baseline category (d): "your method minus its novelty" is the same thing as the first row of your ablation table, and it is the comparison a reviewer trusts most, because it holds everything else constant.
Give the classical-baseline warning with a concrete pattern: across several fields, well-tuned classical methods (gradient boosting on tabular data, TF-IDF+linear models on small text corpora, simple nearest-neighbour baselines for recommendation) have repeatedly matched or beaten deep models in re-evaluations. If a reviewer suspects you avoided the strong classical baseline, your claim is dead. Include it and, if it wins, that IS your finding.
Temporal splits: mention that shuffling time series is one of the most common invalid setups in applied forecasting papers.
-->

---

<!-- _class: dense -->
# S15 · Baselines and the Ablation Study

<div class="cols">
<div>

#### Ablation table anatomy
| Config | Cluster branch | λ ramp | Aug set | Worst-site AUC | Δ |
|---|---|---|---|---|---|
| ERM (baseline) | – | – | basic | 0.781 ± 0.011 | — |
| + augmentation | – | – | full | 0.794 ± 0.010 | +0.013 |
| + cluster branch (λ fixed) | ✔ | fixed | full | 0.808 ± 0.012 | +0.014 |
| **Full (CLUSTER-DG)** | ✔ | ramped | full | **0.822 ± 0.009** | +0.014 |
| Site-supervised (upper bound) | ✔ (true sites) | ramped | full | 0.831 ± 0.010 | +0.009 |

<div class="good">

**What makes this table strong:** cumulative build-up, one change per row, variance on every number, a Δ column that attributes gain to components, and an **upper bound** showing how much of the site-supervised benefit was recovered without labels (≈82%).

</div>

</div>
<div>

#### Ablation design rules
- **One factor per row.** Two simultaneous changes make the row uninterpretable.
- Include an **upper bound** (oracle) and a **lower bound** (trivial) where possible.
- Ablate **hyperparameters of the novel component** (here: K, λ) in a sensitivity plot — if performance depends critically on a value you tuned on test, say so.
- Ablate the **data** too: what happens with 10%, 25%, 50% of labels?
- If a component contributes ~0, **report it and remove it**. Honest negative ablations increase credibility more than they cost.

<div class="warn">

#### Fairness checklist before claiming a win
- [ ] Same splits, preprocessing, augmentation for all methods
- [ ] Equal tuning budget, stated
- [ ] Same seeds, ≥5, reported
- [ ] Baselines from official code where available, versions cited
- [ ] Cost reported (a win bought with 4× compute is a different claim)
- [ ] Statistical test named, paired, with effect size

</div>

</div>
</div>

<!--
SPEAKER NOTES — (6 min)
The "upper bound" row is the professional touch to sell hardest: it converts "we improved by 0.04" into "we recovered 82% of the benefit of privileged information without using it", which is a much more interesting scientific statement and is far harder to dismiss.
On honest negative ablations: reviewers reward them. A paper claiming every component contributes exactly as hoped looks suspicious; a paper reporting that one component gave +0.002 and was therefore dropped looks trustworthy.
-->

---

# S15 · Reproducibility Controls

<div class="cols">
<div>

#### Minimum viable reproducibility
| Control | Concrete action |
|---|---|
| **Seeds** | Fix and record seeds for Python, NumPy, framework, CUDA; report **≥5** and give mean ± std. Never report a single "best" run |
| **Determinism** | Enable deterministic kernels where available; document the residual nondeterminism |
| **Environment** | Export `requirements.txt` / `environment.yml`; record framework, CUDA and driver versions; note the GPU model |
| **Config over code edits** | One YAML/JSON per experiment; never tune by editing source |
| **Data versioning** | Record dataset version + download date + a checksum of your split files |
| **Split artefacts** | **Release the split files themselves** — the cheapest, highest-impact reproducibility action |
| **Logging** | Weights & Biases / MLflow / TensorBoard / CSV logs; keep run IDs in the paper's appendix |
| **Code release** | Public repo, tagged release, DOI via Zenodo, licence, README with exact commands |
| **Statement** | A "Data and Code Availability" statement with the URL/DOI |

</div>
<div>

<div class="good">

**Reporting variance is a claim about honesty.** `0.8221` from one run is less informative than `0.822 ± 0.009` from ten runs — and the second is what allows anyone (including a reviewer) to judge whether your +0.014 is real.

</div>

<div class="bad">

**Red flags reviewers actively look for**
- Accuracy to four decimals from a single seed
- "Best of N runs" reported as the result
- No variance anywhere in the paper
- Hyperparameters "empirically chosen" with no search description
- Test-set numbers used for model selection
- Code "available on request"

</div>

<div class="demo">

<span class="tag tool">TOOLS</span> **Zenodo** (code/data DOI) · **Docker/Apptainer** (environment) · **DVC** (data versioning) · **Papers with Code** (link paper→repo) · **ML Reproducibility Checklist** and the **ACM Artifact Review badging** criteria as self-audit templates.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (5 min)
"Available on request" is worth calling out explicitly: studies of data-sharing statements have repeatedly found that such requests often go unanswered, and many editors now treat the phrase as inadequate. Advise a repository link with a DOI instead.
Tell participants the release-your-splits tip is the single cheapest thing they can do to be cited: anyone who wants to compare against them must use their splits, which makes their paper the protocol reference.
-->

---

<!-- _class: dense -->
# S16 · Metrics — Classification

<div class="cols">
<div>

With TP, FP, TN, FN from the confusion matrix:

$$
\text{Precision}=\frac{TP}{TP+FP}\quad
\text{Recall (Sens.)}=\frac{TP}{TP+FN}
$$
$$
\text{Specificity}=\frac{TN}{TN+FP}\quad
F_1=\frac{2\,PR}{P+R}
$$
$$
\text{Bal. Acc.}=\tfrac{1}{2}\!\left(\text{Sens.}+\text{Spec.}\right)
$$

| Metric | Use when | Do **not** use when |
|---|---|---|
| **Accuracy** | Balanced classes, equal error costs | Imbalanced data — 99% "normal" gives 99% accuracy for a useless model |
| **Precision** | False positives are costly (spam, screening referral) | Alone — trivially maximised by predicting almost nothing |
| **Recall** | Missing a positive is costly (cancer, fraud, safety) | Alone — trivially maximised by predicting everything positive |
| **F1** | Single number needed under imbalance | Class costs are asymmetric; use Fβ (β>1 favours recall) |
| **Specificity** | Screening; paired with sensitivity | Alone |
| **MCC / Cohen's κ** | Imbalanced data; a stricter single number than F1 | When stakeholders cannot interpret it |

</div>
<div>

| Metric | Use when | Do **not** use when |
|---|---|---|
| **ROC-AUC** | Threshold-free ranking quality; roughly balanced or moderate imbalance | **Severe imbalance** — a large TN pool makes AUC look optimistic |
| **PR-AUC / AP** | Rare positive class (anomaly, rare disease, retrieval) | Comparing across datasets with different prevalence (the baseline shifts with prevalence) |
| **Confusion matrix** | **Always** — shows *which* errors occur | Never omit it |
| **Calibration: ECE / Brier / reliability diagram** | Probabilities inform decisions or downstream thresholds | — (under-reported; reporting it is a differentiator) |
| **Top-*k* accuracy** | Many classes, ranked output acceptable | Binary or decision-critical tasks |
| **Per-class + macro/micro/weighted** | Multi-class or multi-label | Reporting only micro-average, which hides rare-class failure |

<div class="warn">

**Multi-label (e.g. 14 CXR findings):** report **per-class AUC/AP plus macro average**. A single micro-averaged number is dominated by prevalent classes and hides failure on the rare, clinically important ones.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (7 min)
Do the arithmetic live: 1,000 patients, 10 positive. Predict "all negative" → 99% accuracy, recall 0. Then compute what ROC-AUC and PR-AUC would show for a mediocre ranker on the same data. This one calculation permanently fixes the metric-choice lesson.
Explain the ROC-vs-PR distinction mechanically: ROC's x-axis (FPR) has the large negative pool in the denominator, so many false positives barely move it; precision has FP in the denominator against TP only, so PR curves expose the same errors starkly. Under severe imbalance, prefer PR-AUC.
Mention that the PR-AUC baseline equals the positive prevalence, which is why PR-AUC is not comparable across datasets with different prevalence - a subtlety that catches many authors.
-->

---

<!-- _class: dense -->
# S16 · Metrics — Regression, Detection, Segmentation

<div class="cols3">
<div>

#### Regression
$$\text{MAE}=\tfrac{1}{n}\sum|y_i-\hat y_i|$$
$$\text{RMSE}=\sqrt{\tfrac{1}{n}\sum (y_i-\hat y_i)^2}$$
$$R^2=1-\frac{\sum (y_i-\hat y_i)^2}{\sum (y_i-\bar y)^2}$$

| Metric | Use | Avoid when |
|---|---|---|
| **MAE** | Robust, interpretable in target units | You need to penalise large errors |
| **MSE/RMSE** | Large errors matter; RMSE in target units | Heavy outliers dominate |
| **R²** | Variance explained; familiar to reviewers | Non-linear/heteroscedastic fits; comparing across datasets with different variance; can be negative |
| **MAPE** | Relative error, business reporting | Targets near or at **zero**; asymmetric penalty |
| **MedAE / Huber** | Outlier-heavy data | — |

*Always plot residuals vs predicted; a good RMSE with structured residuals means a mis-specified model.*

</div>
<div>

#### Object detection
$$\text{IoU}=\frac{|A\cap B|}{|A\cup B|}$$
- **IoU** decides whether a detection counts as correct (threshold, e.g. 0.5).
- **Precision/Recall** computed at that threshold.
- **AP** = area under the precision–recall curve for one class.
- **mAP** = mean AP over classes.
  - `mAP@0.5` (PASCAL VOC style)
  - `mAP@[.5:.95]` (COCO style, averaged over 10 IoU thresholds — stricter on localisation)
- Report **AR** and per-size breakdown (small/medium/large) where available.

<div class="warn">

Always state the **IoU threshold** and the **NMS settings**. `mAP` without them is not comparable to anything.

</div>

</div>
<div>

#### Segmentation
$$\text{Dice}=\frac{2|A\cap B|}{|A|+|B|}\qquad \text{Dice}=\frac{2\,\text{IoU}}{1+\text{IoU}}$$

| Metric | Notes |
|---|---|
| **Dice / F1** | Standard in medical imaging; sensitive to small structures |
| **IoU / Jaccard** | Stricter than Dice for the same overlap |
| **Pixel accuracy** | **Usually misleading** — background often >95% of pixels |
| **mIoU** | Semantic segmentation standard (per-class mean) |
| **Hausdorff / ASSD** | Boundary accuracy; essential for surgical/anatomical use |
| **Volumetric similarity** | 3D structures |

<div class="demo">

Report **per-class** Dice/IoU, not just the mean, and include a **boundary metric** when shape matters.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (7 min)
Three points to land:
1. R² is routinely misused. It is not "accuracy", it can be negative, and it is not comparable across datasets with different target variance. Recommend reporting MAE and RMSE in target units alongside it.
2. mAP is meaningless without the IoU threshold. Show that mAP@0.5 and mAP@[.5:.95] can differ by 15-20 points for the same model, so quoting one against the other's number is a real error seen in submissions.
3. Pixel accuracy on medical or aerial segmentation is a vanity metric because background dominates. Dice/IoU per class plus a boundary metric is the defensible set.
For non-CS participants, translate: reliability (Cronbach's alpha, ICC), agreement (Cohen's/Fleiss' kappa), validity (construct/content), and effect sizes (d, eta-squared) play the role that metrics play here - and the same principle holds: the measure must match the question and the data's structure.
-->

---

# S16 · Choosing Metrics — Decision Guide

| Situation | Report these | Explicitly avoid |
|---|---|---|
| Binary, balanced | Accuracy, F1, ROC-AUC, confusion matrix | — |
| Binary, **severe imbalance** (<5% positive) | PR-AUC/AP, recall at fixed precision, F2, MCC, confusion matrix | Accuracy alone; ROC-AUC alone |
| Multi-class, imbalanced | Per-class P/R/F1 + **macro** F1, confusion matrix, MCC | Micro-average alone |
| Multi-label | Per-label AUC **and** AP, macro average, subset accuracy if meaningful | A single global accuracy |
| Screening / triage | Sensitivity at fixed specificity (or vice versa), PR curve, calibration | A single operating point with no curve |
| Cost-sensitive | Expected cost, cost curves, decision-curve analysis | Symmetric metrics |
| Ranking / retrieval / recommendation | nDCG@k, MRR, MAP@k, Recall@k, coverage | Accuracy |
| Probabilistic forecasts | Brier score, ECE, reliability diagram, log loss | Hard-label accuracy only |
| Generation (text) | Task-specific automatic metrics **plus human evaluation** with inter-rater agreement | BLEU/ROUGE alone as a quality claim |
| Deployment-constrained | The accuracy metric **plus** latency, memory, energy, parameters | Accuracy alone |
| Any comparison claim | Mean ± CI over ≥5 seeds **and** a paired significance test | A single-run point estimate |

<div class="good">

**Rule:** choose metrics from the **decision** the model supports, then justify the choice in one sentence in the paper: *"Because pneumothorax prevalence is 1.2%, we report AP and recall at 95% specificity rather than accuracy."* That sentence pre-empts an entire class of reviewer objection.

</div>

<!--
SPEAKER NOTES — (5 min) + ACTIVITY 16.1
ACTIVITY 16.1 (15 min): each participant writes their metric set with a one-sentence justification per metric, tied to the decision their model supports. Partner challenge: "why not accuracy?" and "what does a reviewer see if this metric improves but the others do not?"
The justification sentence is the deliverable - it is a single sentence that saves a revision round.
-->

---

<!-- _class: dense -->
# S17 · Results vs Discussion

<div class="cols">
<div>

| | **Results** | **Discussion** |
|---|---|---|
| Answers | *What happened?* | *Why, and so what?* |
| Contains | Numbers, tables, figures, statistical tests, observations | Mechanisms, comparisons to literature, implications, limitations |
| Tense | Past ("achieved", "we observed") | Present for established meaning ("this suggests") |
| Forbidden | Interpretation, speculation, new claims | New numbers, new experiments, new tables |
| Failure mode | A table dump with no narration | Repeating results as if that were interpretation |

#### Results section structure
1. One paragraph per research question, in RQ order.
2. Point to the table/figure, then state the **pattern**, then the **magnitude**, then the **uncertainty**.
3. Report the inconvenient findings too — reviewers find them anyway, and finding them yourself is credibility.
4. No interpretation. None.

</div>
<div>

<div class="bad">

#### ❌ "Results" that report nothing
"Our model achieved 95% accuracy. Table 3 shows the results. From Table 3 it is clear that our model is better than the other models. The graph in Fig. 4 shows the comparison."

**Problems:** no comparison point, no variance, no pattern, no magnitude; the reader must do all the work; "it is clear that" is interpretation in the wrong section and is not evidence.

</div>

<div class="good">

#### ✅ Results that report
"Under site-wise evaluation, macro AUC falls from 0.897 ± 0.004 to 0.781 ± 0.011 across the five architectures (Table II), a mean reduction of 0.116 (95% CI 0.104–0.128); the drop is consistent in direction for every architecture and every seed. Degradation is largest for the transformer backbone (−0.142) and smallest for DenseNet-121 (−0.093). CLUSTER-DG raises worst-site AUC from 0.781 ± 0.011 to 0.822 ± 0.009 (paired Wilcoxon signed-rank, W = 3, p = 0.004, Cohen's d = 1.6) while in-domain AUC decreases by 0.008, which is within seed variance. Expected calibration error improves from 0.094 to 0.052 (Fig. 3). Gains on the smallest institution (n = 412) are not significant (p = 0.21)."

</div>

</div>
</div>

<!--
SPEAKER NOTES — (6 min)
Read both aloud. Then point at the last sentence of the strong version - the non-significant result on the small site - and say: "This sentence is why a reviewer will trust the whole paper." Authors who report their own null findings are believed; authors whose every result is favourable are audited.
Note the four-part narration pattern (pointer → pattern → magnitude → uncertainty) and have participants apply it to one of their own tables.
-->

---

<!-- _class: dense -->
# S17 · Statistical Significance and Error Analysis

<div class="cols">
<div>

#### Which test, when
| Situation | Test |
|---|---|
| Two models, same test set, per-item correctness | **McNemar's test** |
| Two models, paired scores across folds/seeds | Paired *t*-test (normality plausible) or **Wilcoxon signed-rank** |
| Two AUCs on the same sample | **DeLong's test** |
| >2 models across many datasets | **Friedman test** + Nemenyi/Holm post-hoc; critical-difference diagram |
| Small data, tuning + estimation | 5×2-fold CV paired *t*-test |
| Any metric, distribution-free interval | **Bootstrap** 95% CI (≥1,000 resamples) |
| Any comparison | Report an **effect size** (Cohen's d, rank-biserial, Δ with CI) |

<div class="bad">

**Statistical malpractice to avoid**
- Choosing the test after seeing results
- Reporting only the significant subset of comparisons
- No correction for many comparisons (Holm/Bonferroni/FDR)
- Treating p = 0.049 as proof and p = 0.051 as nothing
- Significance from n = 3 seeds
- "Significant improvement" with no test at all

</div>

</div>
<div>

#### Error analysis — what separates good papers
1. **Confusion matrix** → which class pairs are confused, and is the confusion semantically sensible?
2. **Stratify errors** by subgroup (site, age, sex, device, class prevalence, input length, illumination). Report the **worst** subgroup, not only the mean.
3. **Inspect failures qualitatively**: sample 20–50 errors and categorise causes; report the taxonomy with counts.
4. **Correlate errors with input properties** (image quality, sentence length, label noise).
5. **Check for shortcut learning**: does performance survive when the suspected shortcut is masked?
6. **Failure-case figure**: 4–6 illustrative errors with captions explaining the cause.

<div class="good">

**Discussion paragraph pattern**
(1) Restate the key finding in one sentence · (2) explain the mechanism · (3) reconcile with prior literature, including contradictions · (4) state practical implication · (5) state limitations honestly · (6) point to the next question.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (7 min)
McNemar's test deserves 60 seconds of explanation: it uses the counts of items where model A is right and B is wrong versus the reverse, which is exactly the paired structure of a shared test set - and it is the right test that student papers most often omit.
Error analysis step 3 is the highest-value habit: manually looking at 30 failures teaches more about a model than a week of hyperparameter search, and the resulting taxonomy is usually the most cited figure in the paper.
Shortcut learning example to give: masking the laterality marker or the image border and observing whether AUC collapses; in text, masking a spurious lexical cue. This is a cheap experiment that reviewers love.
-->

---

<!-- _class: dense -->
# S18 · Figures and Tables

<div class="cols">
<div>

#### Figure rules
1. **One message per figure.** If it needs two sentences to explain what to look at, split it.
2. **Vector format** (PDF/SVG/EPS); raster only for photos/heatmaps at ≥300 dpi.
3. Axis labels **with units**; readable at final printed size (≥8 pt after scaling).
4. **Error bars** on every mean, with the definition in the caption (std? SEM? 95% CI?).
5. **Colourblind-safe** palettes (viridis, ColorBrewer); distinguish also by marker/linestyle so it survives greyscale printing.
6. No 3-D bars, no gratuitous gradients, no chartjunk, no dual y-axes unless unavoidable.
7. Consistent style across all figures (same fonts, same palette, same sizing).
8. **Never** screenshot a plot or a table.

<div class="bad">

**Common figure defects:** unreadable 6 pt text; axes starting at a non-zero value to exaggerate a difference; missing legend; different colour meanings across figures; a 6-line plot where 3 lines overlap indistinguishably; a screenshot of a Jupyter output including the cell prompt.

</div>

</div>
<div>

#### Table rules
1. **Booktabs style**: horizontal rules only (top/mid/bottom); no vertical lines, no full grid.
2. **Bold the best** result per column; state in the caption what bold means.
3. Uniform decimal places (usually 2–3), aligned on the decimal point.
4. Include **variance**: `0.822 ± 0.009`, and define it.
5. Mark statistical significance with a symbol and explain it (`*p<0.05`).
6. Group rows: baselines → prior SOTA → ours → oracle/upper bound.
7. Report cost columns (params, FLOPs, latency) in the main comparison table.
8. Tables are **not** dumps: if a column is never discussed, delete it.

#### Captions, numbering, referencing
- **Figure captions below**, **table captions above** (IEEE convention).
- Captions are **self-contained**: what, on what data, what the reader should notice.
- Number in order of first mention; every float **must** be referenced in the text ("as shown in Fig. 3", "Table II reports…").
- IEEE: "Fig. 3" in text, "Figure 3" at the start of a sentence; "Table II" in roman numerals.
- Place floats near their first mention, at the top of a column.

</div>
</div>

<!--
SPEAKER NOTES — (6 min) + micro-exercise
Show one bad and one good version of the same plot if you can prepare them (matplotlib default vs. cleaned up: font sizes set, error bars added, colourblind palette, no top/right spines, tight_layout, saved as PDF). The visual difference is persuasive in a way that rules are not.
Micro-exercise (10 min): participants take one existing figure of theirs and fix three things: font size, error bars, and export format. Then read their caption aloud and ask the partner "what should I notice?" - if the partner cannot say, the caption fails.
Mention the ethics boundary here: adjusting brightness/contrast uniformly on a whole image is acceptable if disclosed; selectively editing regions, splicing lanes/panels, or duplicating image regions is image manipulation and is misconduct (S21).
-->


---

# S19 · Reference Management — Tools and Workflow <span class="tag">DEMO</span>

| Tool | Purpose | How to use | Example input → output | Limitations / verification |
|---|---|---|---|---|
| **Zotero** (free, open source) | Library, PDFs, notes, citations, BibTeX | Install + browser connector + Word/LibreOffice plugin → save from publisher page → *Add Item by Identifier* for DOI/ISBN/arXiv ID → organise in collections + colour tags → **Better BibTeX** plugin for stable citation keys and auto-exported `.bib` | Input: DOI `10.1109/TMI.2023.xxxxxxx` → Output: full record + PDF + `Author2023Title` key | Publisher metadata is frequently wrong (missing pages, ALL-CAPS titles, wrong venue). **Check every field.** Sync storage limited on the free tier |
| **Mendeley** (free, Elsevier) | Same role; Word plugin *Mendeley Cite*; Web Importer | Import RIS/BibTeX from Scopus/ScienceDirect → annotate PDFs → insert citations in Word | Scopus export → formatted IEEE reference list | Fewer plugins than Zotero; desktop feature changes over time |
| **EndNote** (paid) | Institutional standard in many labs | Groups, *Cite While You Write*, journal output styles | Import filters per database | Licence cost; heavier; style files can drift from journal requirements |
| **BibTeX / BibLaTeX** | The reference database behind LaTeX | Keep `refs.bib`; cite with `\cite{key}`; style via `\bibliographystyle{IEEEtran}` | `\cite{he2016resnet}` → `[7]` + entry | Garbage in, garbage out; braces needed to protect capitals: `{BERT}` |
| **Overleaf** | Collaborative LaTeX writing | New project from the **IEEEtran** template → upload `refs.bib` (or link Zotero via Better BibTeX/`\addbibresource`) → compile → track changes/history | `\cite{}` → numbered IEEE list | Free tier limits compile time and collaborators; **always keep a local Git mirror** |
| **DOI resolvers / Crossref** | Verify a reference exists and is correct | `doi.org/<DOI>`, `search.crossref.org`, `api.crossref.org/works/<DOI>` | DOI → authoritative metadata | The authority for *existence*; the publisher page is the authority for *page numbers* |

<div class="warn">

**Verification rule:** before submission, resolve **every** DOI in your `.bib` file and confirm authors, title, venue, year, volume, pages. This takes ~30 minutes for 50 references and prevents the single most avoidable reviewer complaint — and catches any fabricated or mismatched reference immediately.

</div>

<!--
SPEAKER NOTES — LIVE DEMO (12 min)
Demo in this order:
1. Zotero: save a paper from a publisher page with the connector; deliberately show a broken metadata field and fix it; add a DOI via Add Item by Identifier; show Better BibTeX auto-export to a .bib file.
2. Overleaf: open the IEEEtran template, upload the .bib, insert \cite{}, compile, show the numbered list forming in order of appearance.
3. Verification: pick a reference, paste the DOI into doi.org, and compare fields side by side. Do this once in front of the room so they have seen what "verify a reference" physically means.
Fallback: screenshots. State clearly which tools are free (Zotero, Overleaf free tier, Crossref) and which are paid (EndNote, Overleaf premium).
-->

---

<!-- _class: dense -->
# S19 · IEEE Citation Style and the Reference Audit

<div class="cols">
<div>

#### IEEE essentials
- **Numbered in order of first appearance**: `[1]`, `[2]`, … Reuse the same number on later mentions.
- Placement: **before** punctuation, after a space — "…as shown in [3]." Multiple: `[1], [3], [5]` or a range `[1]–[4]`.
- `[3]` is not a noun. Write "Smith *et al.* [3] showed…", not "In [3], they showed…" as the subject of every sentence.
- Journal article format:
  `[1] A. B. Author, C. D. Author, and E. F. Author, "Title of paper in sentence case," Abbrev. Journal Name, vol. 12, no. 3, pp. 45–58, Mar. 2024, doi: 10.xxxx/yyyyy.`
- Conference paper:
  `[2] G. H. Author, "Title," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Seattle, WA, USA, Jun. 2024, pp. 1234–1243.`
- Use **abbreviated** journal titles per the IEEE reference guide; be consistent.
- Preprint: label it — `arXiv:2401.01234, 2024`. Never present a preprint as a journal paper.
- 6+ authors: IEEE permits `et al.` — apply one rule throughout.

</div>
<div>

#### Pre-submission reference audit
- [ ] Every in-text citation appears in the list; every list entry is cited
- [ ] Numbering is sequential by first appearance (LaTeX handles this; **Word does not** unless you use a plugin)
- [ ] Every DOI resolves; metadata matches the publisher record
- [ ] Consistent author-name format, journal abbreviations, capitalisation
- [ ] No duplicate entries under different keys
- [ ] Preprints labelled; published versions preferred where they exist
- [ ] Retracted papers checked (Retraction Watch database / publisher notices) and **not** cited as valid evidence
- [ ] Foundational works cited, not only 2022–2026
- [ ] Every reference has actually been read
- [ ] Reference count appropriate for the venue (journal 30–60; letter 15–25)

<div class="bad">

**Citing a retracted paper** as supporting evidence is a serious and increasingly-checked error. Search each key reference for a retraction notice before submission.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (5 min)
The "[3] is not a noun" rule matters for readability and is a common non-native-writer pattern; show the rewrite once.
The retraction check is new to most participants. Tell them: check the publisher page for an "Expression of Concern" or "Retracted" banner, and search the Retraction Watch database for any paper that is load-bearing in their argument.
Warn Word users specifically: manual numbering breaks the moment a reference is inserted mid-draft. Use a citation plugin or LaTeX.
-->

---

# S20 · AI Tools for Research — The Landscape

| Tool | Type | Genuinely good at | Verification burden |
|---|---|---|---|
| **ChatGPT / Claude / Gemini** | General LLM assistants | Structuring sections, improving clarity and grammar, generating search-string variants, explaining unfamiliar methods, drafting code, building checklists, writing response-letter drafts, adversarial self-review ("attack my gap") | **High.** No reliable literature grounding by default; may state confident falsehoods; **must never be trusted for citations, numbers, or claims about what the literature says** |
| **Perplexity** | Search-grounded assistant | Quick orientation on an unfamiliar topic with visible sources | Medium-high. **Open every source** — the citation may exist but not support the sentence |
| **Elicit** | Literature-search + extraction over a paper corpus | Screening many papers; extracting structured columns (population, method, outcome) into a table | Medium. Extraction errors and mis-attributed numbers occur; verify each cell against the PDF |
| **Consensus** | Evidence-oriented search over papers | "What does the literature say about X?" with per-paper claim summaries | Medium. Summaries compress nuance; read the primary papers before citing |
| **NotebookLM** | Grounded assistant over **your uploaded** documents | Q&A across *your* PDF set with citations back to your own sources; comparison across your papers | Lower (it is grounded in your files) but still verify quotations and numbers against the original |
| **Semantic Scholar** | Academic search engine | TLDRs, citation intent, influential citations, alerts, free API | Low for metadata; TLDRs are lossy |
| **Research Rabbit / Connected Papers / Litmaps** | Citation-graph discovery | Finding what your matrix is missing | Low — but coverage is incomplete |
| **Grammarly / LanguageTool / Writefull** | Language | Grammar, register, academic phrasing | Low; check it has not altered technical meaning |
| **DeepL** | Translation | Drafting in L1 then translating | Medium; verify terminology |

<!--
SPEAKER NOTES — (6 min)
Frame the whole section with the division of labour from Day 1: AI may help you FIND, SORT, TRANSLATE, STRUCTURE and PRE-FILL. You must READ, VERIFY, COMPARE, JUDGE and CLAIM.
Call out NotebookLM as the safest of the general assistants for literature work, because it is grounded in documents the researcher supplies rather than in model memory - which structurally reduces (though does not eliminate) fabrication.
Note that tool capabilities and pricing change quickly; the classification by FUNCTION is what will still be valid in two years.
-->

---

<!-- _class: dense -->
# S20 · The Red Lines — What AI Must Never Be Trusted To Do

<div class="cols">
<div>

<div class="bad">

#### Never, without independent verification
| Task | Why it fails | What can go wrong |
|---|---|---|
| **Produce references** | Models generate plausible author/title/venue/DOI combinations that do not exist, or attach a real DOI to a wrong title | Fabricated citations in submitted papers → desk rejection, retraction, formal misconduct findings |
| **State what a paper found** | Summarises from patterns, not from the actual PDF | Misattributed claims and numbers |
| **Report experimental results** | It has run no experiment | **Data fabrication** — research misconduct |
| **Invent datasets or statistics** | Fluent invention | Unverifiable study |
| **Assert novelty** ("no work exists") | No comprehensive index; no reasoning about absence | Gap collapses at review |
| **Replace critical reading** | Cannot judge whether a baseline was tuned fairly | You lose the ability to defend your own paper |
| **Replace scientific reasoning** | Correlates text; does not test hypotheses | Unsupported claims |
| **Write text you submit unread** | You are the author and are accountable for every word | Integrity violation; viva failure |

</div>

</div>
<div>

#### The verification protocol — apply to every AI output
1. **Provenance:** for every factual claim, identify the primary source *yourself*.
2. **Open it:** resolve the DOI; read at least the abstract and the relevant table.
3. **Check the number:** compare against the actual table/figure, not the summary.
4. **Check the direction:** does the source actually support your sentence, or merely mention the topic?
5. **Re-express:** rewrite in your own words, with your own citation.
6. **Log it:** keep a note of what was AI-assisted, so you can answer honestly if asked.

#### Disclosure
- Major publishers and COPE guidance agree: **AI tools cannot be authors** (they cannot take responsibility or consent).
- Most journals now require **disclosure of substantive AI use** in a methods or acknowledgements statement — read your target journal's policy and follow it exactly.
- Many venues restrict AI use in **peer review** (confidentiality); do not paste a manuscript you are reviewing into a public AI tool.

<div class="good">

**Safe framing:** *"AI assistance was used for language editing and for drafting search-query variants. All literature identified was independently retrieved and verified by the authors; all results were produced by the authors' own experiments."* — accurate, and defensible.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (8 min) — the most important slide of Day 2 alongside S21
Do this live: ask an LLM for "five recent papers on site-wise evaluation of chest X-ray classifiers with DOIs", then attempt to resolve each DOI at doi.org in front of the room. Whatever happens is instructive: fabricated or mismatched entries make the point vividly, and correct entries let you demonstrate that verification is fast and non-negotiable either way.
Then state the professional consequence plainly: fabricated citations have led to retractions, sanctions, and — for students — failed vivas. The cost of the 30-minute DOI audit is trivial by comparison.
Emphasise the peer-review confidentiality point; early-career researchers who start reviewing often do not realise that pasting a manuscript into a public tool can breach confidentiality.
-->

---

<!-- _class: dense -->
# S20 · Effective Prompts by Research Task

<div class="cols">
<div>

#### Search-string generation <span class="tag tool">SAFE</span>
> "I study whether chest-X-ray classifiers generalise across hospitals. Produce three Scopus-syntax search strings of increasing precision using TITLE-ABS-KEY, with concept blocks for population, method, and distribution shift; include -ise/-ize variants, acronyms with expansions, and dataset names. Do **not** cite papers."
*Then run each string yourself and record the counts.*

#### Structuring <span class="tag tool">SAFE</span>
> "Here is my gap statement and my four contributions. Propose a section/subsection outline for an IEEE journal paper, with one sentence stating the job of each subsection. Flag any contribution that has no corresponding results subsection."

#### Language editing <span class="tag tool">SAFE</span>
> "Improve clarity and grammar of the paragraph below for an IEEE journal. Do not change technical content, do not add claims, do not remove hedging, and list every change you made and why."

#### Adversarial self-review <span class="tag tool">SAFE — highest value</span>
> "Act as a critical Reviewer 2 for an IEEE journal. Here are my abstract, method and results. List the ten strongest objections a reviewer could raise, ranked by severity, and the specific experiment or clarification that would neutralise each one."

</div>
<div>

#### Explanation / learning <span class="tag tool">SAFE</span>
> "Explain invariant risk minimisation to someone who knows empirical risk minimisation. State its assumptions, when it fails, and what to check in an implementation. I will verify against the original paper."

#### Code and analysis <span class="tag tool">SAFE with testing</span>
> "Write a PyTorch function computing expected calibration error with M equal-width bins, plus three unit tests including edge cases (all-correct, all-wrong, single bin). Explain the binning choice."
*Run the tests. Never trust unexecuted code.*

#### Response letters <span class="tag tool">SAFE</span>
> "Draft a polite, evidence-based response to this reviewer comment. Use the pattern: thank → restate the concern → what we changed → where (section/line) → evidence. Do not invent results; leave `[TBD]` where I must insert numbers."

<div class="bad">

#### Prompts you must not use
- "Give me 10 recent citations on X with DOIs" *(→ verify every one; better: use Scopus/Scholar)*
- "Write my related work section" *(→ you must know the literature)*
- "Make up plausible results / fill in the missing numbers"
- "Rewrite this so plagiarism software won't detect it"
- "Summarise this paper so I don't have to read it" *(for a **core** paper)*

</div>

</div>
</div>

<!--
SPEAKER NOTES — (7 min) + ACTIVITY 20.1
ACTIVITY 20.1 (20 min): every participant runs the "Reviewer 2" adversarial prompt on their own abstract and gap statement, then writes down the three objections they cannot currently answer. Those three become their next experiments. This is the single most useful AI application in the workshop and the one that most improves papers.
Explain why the last forbidden prompt is forbidden: rewriting to evade detection is intent to deceive. The legitimate action is to cite properly and express ideas in your own words - which reduces similarity as a side effect.
-->

---

# S20 · Manual vs AI-Assisted — The Division of Labour

| Research task | Do it **manually** (you are accountable) | AI may assist with | Verification you owe |
|---|---|---|---|
| Choosing the topic | Judgement of significance and feasibility | Brainstorming candidate framings | Feasibility audit with real datasets/repos |
| Literature search | Running strings on real databases; logging counts | Generating string variants, synonyms | Re-run every string yourself |
| Screening | Include/exclude decisions | Pre-ranking by relevance | Read title+abstract of every candidate |
| Reading core papers | All three passes | TLDR for triage only | Your own extraction template |
| Literature matrix | Judgement columns (limitations, gap, relevance) | Pre-filling factual columns (dataset, metrics, baselines) | Check every cell against the PDF |
| Finding the gap | The reasoning and the counting | Suggesting gap *types* to check | Evidence from your own tallies |
| Method design | All of it | Explaining alternatives; sanity-checking maths | Derive/verify yourself |
| Code | Design and correctness | Boilerplate, unit tests, refactoring, plotting | Run it; test it; read it |
| Experiments | All of it | Suggesting ablations you forgot | Your logs are the evidence |
| Results interpretation | All of it | Suggesting alternative explanations to test | Your data decides |
| Writing | Every claim, every citation | Structure, clarity, grammar, translation | Read and own every sentence |
| References | Verification of every entry | Formatting conversion | Resolve every DOI |
| Reviewer response | Substance and evidence | Tone and phrasing | You sign it |

<div class="good">

**One-line policy for your lab notebook:** *AI can accelerate everything reversible; you must personally own everything falsifiable.*

</div>

<!--
SPEAKER NOTES — (4 min)
This is the summary slide participants will photograph. Read the bottom line aloud.
If your institution has an AI-use policy, name it here and put its URL on the slide before delivering. If not, suggest that the group draft one for their lab - a genuinely useful outcome of the workshop.
-->

---

# S21 · Research Misconduct — The Taxonomy

| Category | What it is | Concrete example | Consequence |
|---|---|---|---|
| **Fabrication** | Inventing data or results | Reporting accuracy for an experiment never run; adding rows to a results table | Retraction; degree revocation; funding bans |
| **Falsification** | Manipulating data, images or analysis to misrepresent | Deleting outliers to reach significance; brightening only one panel; changing a number after a null result | Retraction; misconduct finding |
| **Plagiarism** | Using others' words, ideas, figures, code or data without attribution | Copying two paragraphs of related work; reusing a figure without permission and citation | Desk rejection; retraction; institutional action |
| **Self-plagiarism / text recycling** | Reusing your own published text without disclosure or citation | Copying your conference paper's method section verbatim into a journal version without citing it | Rejection; duplicate-publication finding |
| **Duplicate / redundant publication** | Publishing the same study twice | Submitting the same study to two journals; "salami slicing" one study into four thin papers | Retraction of the later paper |
| **Citation manipulation** | Distorting the citation record | Coercive self-citation; citation cartels; padding with irrelevant citations from one journal | Editorial sanctions; delisting of journals |
| **Authorship violations** | Credit not matching contribution | Gift/honorary authorship; ghost authorship; omitting a contributor; adding a name without consent | Disputes; correction; retraction |
| **Undisclosed AI use** | Substantive AI-generated content presented as your own where disclosure is required | Submitting AI-drafted discussion without disclosure or verification | Rejection; integrity investigation |
| **Ethical breaches** | Missing consent/approval, privacy violations, licence breaches | Using patient data without IRB approval; scraping data against terms of service | Legal liability; retraction |
| **p-hacking / HARKing** | Analytic choices made after seeing results, presented as pre-planned | Trying six tests, reporting the one with p<0.05; presenting a post-hoc hypothesis as a prediction | Irreproducible literature; increasingly detected |

<div class="warn">

Guidance and flowcharts: **COPE** (publicationethics.org) · **ICMJE** authorship criteria · **CRediT** contributor taxonomy · your institution's research-integrity policy.

</div>

<!--
SPEAKER NOTES — (7 min)
Deliver this without moralising; treat it as professional knowledge, like knowing tax law. Most misconduct by early-career researchers is committed out of ignorance or supervisor pressure, not malice.
Two items deserve extra time because participants routinely do not know they are problems: (1) text recycling from their own conference paper — the fix is to cite it and state what is new; (2) salami slicing — the test is whether each paper answers a distinct research question with its own contribution.
Mention the pressure case honestly: if a supervisor asks for a name to be added or for numbers to be "improved", the participant needs to know the institution's integrity office exists. Say it once, calmly.
-->

---

<!-- _class: dense -->
# S21 · Plagiarism in Practice

<div class="cols">
<div>

#### Types beyond copy-paste
| Type | Example |
|---|---|
| **Verbatim** | Sentences copied without quotation or citation |
| **Mosaic / patchwriting** | Synonym-swapping another's sentence while keeping its structure — **still plagiarism** even if similarity software scores it low |
| **Idea plagiarism** | Using someone's research design or gap framing without citation |
| **Image / figure** | Reusing a figure without permission **and** citation (copyright *and* attribution) |
| **Data plagiarism** | Reusing a dataset without citing it or honouring its licence |
| **Code plagiarism** | Copying code without honouring its licence and attribution |
| **Translation plagiarism** | Translating a paper from another language and presenting it as new |
| **Reference padding** | Citing works you never read to appear well-read |

</div>
<div>

#### The paraphrase test — worked
> **Source:** "Deep networks trained on single-institution radiographs frequently exploit acquisition artefacts as predictive shortcuts, which limits transfer to unseen hospitals."

<div class="bad">

**❌ Patchwriting (plagiarism):** "Deep networks trained on single-hospital X-rays often use acquisition artefacts as predictive shortcuts, limiting transfer to new hospitals [6]."
*Same structure, same clause order, synonym substitution. Citation present but the expression is still theirs.*

</div>

<div class="good">

**✅ Genuine paraphrase + synthesis:** "Shortcut learning is a documented failure mode in this setting: models can key on scanner-specific artefacts rather than pathology, so in-distribution accuracy overstates what transfers to a new site [6]. We test this directly by masking image borders (Section V-D)."
*Restructured, integrated into your own argument, cited, and connected to your own contribution.*

</div>

<div class="demo">

**Procedure that makes plagiarism structurally unlikely:** read → close the PDF → write from your extraction template in your own words → reopen only to check facts and numbers → cite.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (6 min)
The patchwriting example is essential — most participants believe that changing words plus adding a citation is sufficient. Show that the sentence architecture is itself the borrowed expression.
Teach the close-the-PDF procedure as a mechanical habit; it is far more effective than exhortation because it removes the source text from view at the moment of writing.
On figures: reusing a published figure requires permission (via RightsLink/publisher) plus a credit line, even with citation, unless the licence (e.g. CC-BY) permits reuse with attribution. Students routinely do not know this.
-->

---

<!-- _class: dense -->
# S21 · Similarity Tools — and Why the Percentage Is Not the Point

<div class="cols">
<div>

| Tool | Who uses it | What it does |
|---|---|---|
| **iThenticate** | Publishers/editors (Crossref Similarity Check) on submitted manuscripts | Matches against Crossref's publisher corpus + web |
| **Turnitin** | Universities on student work; Feedback Studio for teaching | Matches against student papers, publications, web |
| **Publisher screening** | Desk-check stage | Editors see a similarity report before reviewers are invited |

#### How to use them responsibly
1. Run your **own** check (via your institution) **before** submission.
2. Read the **report**, not the number: open every coloured match.
3. Ask of each match: is it (a) correctly quoted and cited, (b) unavoidable technical phrasing, (c) references/method boilerplate, or (d) **actual unattributed borrowing**?
4. Fix (d) by rewriting from your notes and citing — never by word-swapping.
5. Check the **self-match** to your own prior papers/thesis; disclose and cite legitimate overlap.
6. Keep the report; some journals ask for it.

</div>
<div>

<div class="bad">

#### Why "reduce the percentage" is the wrong goal
- **10% can be misconduct:** one uncited copied paragraph from one source is plagiarism regardless of the total.
- **25% can be clean:** long reference lists, standard method phrasing, dataset descriptions and correctly quoted definitions all inflate the number harmlessly.
- Similarity software detects **string overlap**, not dishonesty. It cannot see mosaic plagiarism, translated plagiarism, idea plagiarism, or fabricated data.
- Deliberately evading detection (synonym tools, character substitution, invisible text, paraphrasing tools used to disguise a source) is **intent to deceive** — worse than the original overlap.

</div>

<div class="good">

**The correct standard:** every idea, sentence, figure, dataset and line of code that is not yours is attributed, and every sentence in your paper is one you could defend as your own expression. Meet that standard and the percentage takes care of itself.

</div>

<div class="warn">

Note on **AI-detection tools**: their reliability is contested and false positives are documented, particularly for non-native English writers. Do not treat a detector score as proof, in either direction. Keep drafts and notes; a documented writing trail is your best evidence of authorship.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (6 min)
Give the two numbers deliberately: 10% can be misconduct, 25% can be clean. It reframes the whole conversation away from percentage-chasing, which is how most institutions unfortunately frame it.
If your institution enforces a threshold, acknowledge it honestly: "you must satisfy the institutional threshold AND the ethical standard; the threshold is a floor, not the goal."
On AI detectors, keep it factual and brief. The practical advice - keep drafts, keep notes, keep your Zotero history - is what protects an honest student accused wrongly.
-->

---

<!-- _class: dense -->
# S21 · Authorship, Declarations and Ethics Statements

<div class="cols">
<div>

#### Who is an author?
The widely used **ICMJE** criteria require **all four**:
1. Substantial contribution to conception/design **or** data acquisition/analysis/interpretation;
2. Drafting or critically revising the work;
3. Approval of the final version;
4. **Accountability** for the work's integrity.

Everyone else → **Acknowledgements** (with their permission).

| Bad practice | Why it is wrong |
|---|---|
| **Gift/honorary authorship** (head of department who did nothing) | Misrepresents accountability |
| **Ghost authorship** (real contributor omitted) | Denies credit; often hides conflicts |
| **Adding a name without consent** | Each author must approve |
| Selling/buying authorship (paper mills) | Fraud; leads to mass retractions |

<div class="good">

Use the **CRediT** taxonomy (conceptualisation, methodology, software, validation, formal analysis, investigation, resources, data curation, writing – original draft, writing – review & editing, visualisation, supervision, project administration, funding acquisition) and agree the author order **in writing, before writing starts.**

</div>

</div>
<div>

#### Declarations most journals now require
| Declaration | What to write |
|---|---|
| **Ethics approval** | Committee name, approval number, date — or an explicit statement that approval was not required and why |
| **Informed consent** | Obtained/waived; for identifiable images, consent to publish |
| **Conflict of interest** | Funding, employment, patents, advisory roles — or "The authors declare no competing interests" |
| **Funding** | Grant numbers and agencies |
| **Data availability** | Repository + DOI/accession, or a specific, justified reason for restriction (privacy, DUA) |
| **Code availability** | Repository URL + tagged release/DOI |
| **AI use** | Disclose substantive use per the journal's policy |
| **Author contributions** | CRediT statement |
| **Prior presentation** | "An earlier version appeared as [x]; this paper adds …" |

<div class="warn">

Write these **before** submission day. Missing declarations are a common cause of returned-before-review submissions.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (6 min) + ACTIVITY 21.1
ACTIVITY 21.1 (15 min): participants write their full declarations block for their own planned paper - author list with CRediT roles, ethics status, data and code availability, funding, conflicts, AI-use statement. Most discover at least one unresolved issue (no ethics approval route, a dataset they cannot legally redistribute, an unclear author order). Resolving these now is cheaper than at submission.
On author order: advise a written agreement at project start, including what happens if someone leaves. Authorship disputes are among the most common and most damaging conflicts in research groups, and they are almost entirely preventable.
-->

---

<!-- _class: dense -->
# S22 · Journal Selection — Criteria and Metrics

<div class="cols">
<div>

#### Selection criteria, in priority order
| # | Criterion | How to judge |
|---|---|---|
| 1 | **Scope fit** | Read the *Aims & Scope*; check that 3–5 papers *you cite* are from this journal. Scope mismatch is the #1 cause of desk rejection |
| 2 | **Indexing** | Scopus and/or Web of Science Core Collection (SCIE/SSCI/ESCI) — verify on the **official** lists |
| 3 | **Audience** | Are your intended readers/citers here? |
| 4 | **Article type fit** | Full paper vs letter vs short communication; page limits |
| 5 | **Quality tier** | JCR quartile (IF-based) / Scimago SJR quartile / CiteScore percentile |
| 6 | **Speed** | Journal-reported submission-to-first-decision and to-publication times |
| 7 | **Cost** | APC; waivers; whether your institution has a read-and-publish agreement |
| 8 | **Legitimacy** | See the next slide |
| 9 | **Special issues** | An open CFP matching your topic = a receptive editor and a clear timeline |
| 10 | **Your regulations** | Does your university accept this venue for your degree? |

</div>
<div>

#### Metrics — what they actually mean
| Metric | Source | Definition (in brief) | Caveat |
|---|---|---|---|
| **Impact Factor (JIF)** | Clarivate **JCR** (WoS) | Citations in year *Y* to items from *Y−1*, *Y−2*, divided by those items | Only for indexed journals; discipline-dependent; **not** a measure of your paper |
| **JIF quartile (Q1–Q4)** | JCR, **per category** | Rank of the journal within its subject category | A journal can be Q1 in one category and Q2 in another — always state the category |
| **CiteScore** | **Scopus** | Citations over a 4-year window per document | Different window and corpus from JIF; **not interchangeable** |
| **SJR** | **Scimago** (free) | Prestige-weighted citations (source-normalised) | Free proxy for tiering when you lack JCR access |
| **SNIP** | Scopus | Field-normalised citation impact | Enables cross-field comparison |
| **h5-index** | Google Scholar Metrics | Journal-level h-index over 5 years | Includes non-indexed venues |
| **Acceptance rate** | Journal/publisher page, if published | Fraction accepted | Often unpublished; treat third-party figures sceptically |

<div class="bad">

**"SCI journal" is loose usage.** The current index is **SCIE** (Science Citation Index Expanded) within the WoS Core Collection. Verify the exact index on Clarivate's **Master Journal List** — a claim of "SCI indexed" on a journal's own website is not evidence.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (7 min)
Hammer criterion 1. Read the scope statement aloud from a real journal page and show how to test fit using their own reference list — if none of the papers they cite appear in the journal, it is probably the wrong journal.
Clarify the IF vs CiteScore confusion explicitly, since participants often quote them interchangeably: different databases, different windows, different corpora. Quartiles must always be reported with the source and the category.
Say plainly that JIF describes a journal, not a paper. Hiring and evaluation committees increasingly know this (DORA), and a strong paper in a Q2 specialist journal often outperforms a weak paper in a Q1 generalist one.
-->

---

<!-- _class: dense -->
# S22 · Verifying a Journal and Spotting Predatory Venues <span class="tag">DEMO</span>

<div class="cols">
<div>

#### The verification sequence (10 minutes, always)
1. **Publisher site** — find the journal from the publisher's own domain (IEEE, Springer, Elsevier, ACM, Wiley, MDPI, Taylor & Francis…). Never from an email link.
2. **Clarivate Master Journal List** (`mjl.clarivate.com`) — search the exact title; note which index (SCIE/SSCI/ESCI) and check for coverage changes.
3. **Scopus Sources** (`scopus.com/sources` or the Scopus Source List file) — confirm active coverage and CiteScore; check whether coverage was **discontinued**.
4. **Scimago** (`scimagojr.com`) — quartile, SJR, subject category, trend.
5. **DOAJ** (`doaj.org`) — for open-access journals, confirms editorial standards and transparent APCs.
6. **ISSN Portal** (`portal.issn.org`) — confirm the ISSN belongs to *this* journal (catches hijacked clones).
7. **COPE membership** (`publicationethics.org`) — signals ethical governance.
8. **Editorial board** — pick three members and verify them on their institutional pages.
9. **Recent issues** — read two papers. Is the science and the English of a standard you want to be judged by?
10. **Retraction Watch hijacked-journal checker** — for suspiciously familiar titles.

</div>
<div>

<div class="bad">

#### Predatory / low-integrity red flags
- Unsolicited flattering email inviting a submission ("your esteemed research…")
- Promises of **publication in 3–7 days** or "guaranteed acceptance"
- Claims of a fake metric: "Global Impact Factor", "Universal Impact Factor", "Journal Impact Score" from an unknown body
- Claims "Scopus indexed" that fail step 3
- Impossibly broad scope ("Engineering, Medicine, Management and Social Sciences")
- APC disclosed only **after** acceptance, or payment to a personal account
- Editorial board with no affiliations, or members who did not consent
- Cloned website of a real journal (**hijacked journal**) at a slightly different URL
- No DOIs; no archiving policy; contact is a Gmail address
- Grammatical errors on the journal's own homepage

</div>

<div class="good">

**Think. Check. Submit.** (`thinkchecksubmit.org`) is the standard community checklist. Prefer positive verification (present in Scopus/WoS/DOAJ) over blacklists — informal "predatory lists" are incomplete and contested.

</div>

</div>
</div>

<!--
SPEAKER NOTES — LIVE DEMO (10 min)
Demo the sequence on one legitimate journal in the participants' field, narrating each check. Then, if you have one, show a real spam solicitation email from your own inbox (redact identifiers) and run the same checks until it fails.
Say plainly what is at stake: publishing in a predatory venue can render the work uncitable, may be rejected by the university for degree requirements, cannot usually be withdrawn and republished (the paper is now "published"), and the APC is unrecoverable. This has ended real students' timelines.
Advise: never respond to solicitation emails; choose journals by starting from your own reference list.
-->

---

<!-- _class: dense -->
# S22 · Journal Selection Checklist <span class="tag tool">HANDOUT</span>

<div class="cols">
<div>

#### Score your 3 candidate journals
| Item | J1 | J2 | J3 |
|---|---|---|---|
| Scope explicitly covers my topic (quote the phrase) | | | |
| ≥3 papers I cite are published here | | | |
| Indexed: Scopus ✔ / WoS index (SCIE/SSCI/ESCI) | | | |
| Quartile + **category + source** (JCR / Scimago) | | | |
| CiteScore / IF (with year) | | | |
| Article type + page/word limit fits my paper | | | |
| Reported time to first decision | | | |
| APC amount; waiver/institutional agreement | | | |
| Open access model: gold / hybrid / subscription | | | |
| DOAJ listed (if OA) | | | |
| COPE member / verifiable editorial board | | | |
| Accepted by my university's regulations | | | |
| Template available (LaTeX/Word) | | | |
| Special issue open + deadline | | | |
| **Decision: target / backup / reject** | | | |

</div>
<div>

#### Strategy
- Choose **one target and two backups** *before* writing, and format for the target from the start.
- Aim one tier above your honest self-assessment for the target; use the backups without ego if rejected.
- **Never** submit to two journals simultaneously — it is duplicate submission and can be treated as misconduct.
- If rejected, **use the reviews** before resubmitting elsewhere; a rejection with substantive reviews is free consultancy.
- Check whether the journal offers **transfer** to a sister journal — often faster than a fresh submission.

<div class="demo">

#### Open access, plainly
| Model | You pay | Reader pays |
|---|---|---|
| **Subscription** | usually nothing (page/colour charges possible) | yes |
| **Gold OA** | APC | no |
| **Hybrid** | optional APC for OA | yes, unless you pay |
| **Diamond/Platinum** | nothing | nothing |
| **Green** | nothing (self-archive the accepted version, per policy + embargo) | varies |

Check your funder's mandate and your institution's read-and-publish agreements before paying an APC yourself.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (5 min) + ACTIVITY 22.1
ACTIVITY 22.1 (20 min): each participant completes this table for three real candidate journals, using the verification sequence for each. Deliverable: a target and two backups, with quartile, source, category, APC and decision timeline recorded.
Mention green OA and self-archiving as the free route to visibility for those who cannot pay an APC, and note that many journals allow the accepted manuscript to be deposited in an institutional repository after an embargo. Check the specific policy (e.g. via the journal's page or Sherpa Romeo).
-->

---

<!-- _class: xdense -->
# S23 · Manuscript Submission

<div class="cols">
<div>

<div class="flow">
FINAL MANUSCRIPT
   ↓  format to the journal template
FORMATTING & COMPLIANCE CHECK
   ↓  write cover letter + declarations
COVER LETTER + SUPPLEMENTARY MATERIAL
   ↓  create account, upload, proof the PDF
SUBMISSION SYSTEM (ScholarOne / Editorial
   Manager / IEEE Author Portal / OJS)
   ↓
EDITOR TRIAGE  ──► desk reject (scope/format/
   ↓                 similarity/English)
REVIEWER ASSIGNMENT (weeks)
   ↓
PEER REVIEW  ──► DECISION
   ↓
REVISION + RESPONSE LETTER  ──► RE-REVIEW
   ↓
ACCEPT → PROOFS → EARLY ACCESS → ISSUE → DOI
</div>

</div>
<div>

#### Cover letter template (≈250 words)
> Dear Prof. **[Editor name]**,
>
> We submit our manuscript, *"**[title]**"*, for consideration as a **[Regular Paper]** in **[Journal]**.
>
> **[Problem + gap, 2 sentences.]** Across 15 studies published between 2022 and 2026, chest-radiograph classifiers are evaluated predominantly on random splits that leak institutional identity, and worst-institution performance is not reported.
>
> **[What you did + headline result, 3 sentences.]** We re-evaluate five published architectures under institution-disjoint protocols on three public datasets and show a mean AUC reduction of 0.116 (95% CI 0.104–0.128). We then introduce CLUSTER-DG, which recovers 0.041 ± 0.009 worst-site AUC without site metadata.
>
> **[Fit, 1–2 sentences.]** This work fits **[Journal]**'s scope in **[quote the scope phrase]** and extends work published in your journal [refs].
>
> **[Declarations.]** The manuscript is original, is not under consideration elsewhere, and all authors approve the submission. An earlier version was presented at **[conference]**; this submission adds **[X% new material: what]**. We declare no competing interests. Code, splits and weights are available at **[DOI]**.
>
> **[Optional]** Suggested reviewers: **[names + affiliations + emails + why]**. We request exclusion of **[name]** because **[reason]**.
>
> Sincerely, **[Corresponding author, affiliation, ORCID, email]**

</div>
</div>

<!--
SPEAKER NOTES — (6 min)
The cover letter is read by the editor, who decides whether to invite reviewers at all. It must answer three questions in 30 seconds: is this in scope, is it new, is it sound enough to spend reviewers' time on.
Point out the conference-extension disclosure line — this is where you pre-empt a duplicate-publication concern rather than hoping nobody notices.
Suggested reviewers: legitimate and often requested. Suggest people you cite who are not collaborators, from different institutions and countries. Exclusion requests are also legitimate if justified professionally (direct competitor, prior dispute) — keep the reason factual.
-->

---

<!-- _class: dense -->
# S23 · Pre-Submission Compliance Checklist

<div class="cols">
<div>

#### Manuscript
- [ ] Journal **template** used (LaTeX class or Word template), correct column format
- [ ] Within **page/word limit**; figure and table counts within limits
- [ ] Title, abstract, keywords finalised (keywords from the journal/IEEE thesaurus)
- [ ] All sections present; declarations block complete
- [ ] Figures: vector, ≥300 dpi rasters, fonts embedded, greyscale-legible, all referenced in text
- [ ] Tables: captions above, all referenced, units stated
- [ ] Equations numbered; all symbols defined
- [ ] References in journal style, sequential, every DOI resolved
- [ ] Anonymised version prepared if the journal is **double-blind** (no author names, no "our previous work [7]" phrasing, anonymised repo link)
- [ ] Language checked (and professionally edited if needed)
- [ ] Similarity check run and reviewed **match by match**

</div>
<div>

#### Files and system
- [ ] Main PDF **generated by the system**, then proof-read page by page
- [ ] Source files (`.tex` + `.bib` + figures, or `.docx`)
- [ ] Supplementary material (appendices, extra results, demo video)
- [ ] Highlighted/clean versions if requested
- [ ] Graphical abstract / highlights if required
- [ ] Cover letter
- [ ] Ethics approval document if required
- [ ] Data and code availability statements with **live** links (test them in a private window)
- [ ] All authors' names, affiliations, emails and **ORCIDs** entered correctly
- [ ] Corresponding author's email is one that will be monitored for months
- [ ] Funding information entered in the system's fields (not only in the text)
- [ ] Everything archived locally in a dated folder, plus the submission ID

<div class="warn">

**Proof-read the system-generated PDF.** Figures degrade, symbols vanish, and merged files reorder. This is the file reviewers actually see.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (5 min)
Tell participants that most desk rejections in their control come from this list: wrong template, over length, missing declarations, unresolvable data links, or an anonymity breach in a double-blind submission.
The anonymity point deserves a sentence: in double-blind venues, a GitHub link containing your username, or "in our previous work [7]" where [7] is obviously yours, breaks anonymity and can cause rejection. Use an anonymised repository.
Advise budgeting a full day for submission mechanics. Participants consistently underestimate it and rush, which is when errors enter.
-->

---

<!-- _class: dense -->
# S24 · Responding to Reviewers

<div class="cols">
<div>

#### Principles
1. **Every** comment gets a response — even "no comment" ones ("We thank the reviewer for this positive assessment.").
2. **Thank → restate → act → locate → evidence.**
3. **Locate precisely:** "revised text on p. 7, lines 312–319; new Table IV."
4. Quote your **new text verbatim** in the letter so reviewers need not hunt.
5. Be **courteous and unemotional**, always. Reviewers volunteered their time; editors read the tone.
6. Answer the **question behind the comment** — a confused reviewer usually indicates unclear writing, which is your defect to fix.
7. If two reviewers conflict, say so explicitly and explain your resolution; let the editor arbitrate.
8. Never make undisclosed changes; never remove content silently.
9. Meet the deadline, or request an extension **before** it passes.
10. Use a **two-column or table format**; highlight changes in the manuscript (colour or a "revision-marked" file).

</div>
<div>

#### Sample response table
| # | Reviewer comment | Response | Change + location |
|---|---|---|---|
| R1.1 | "Only three seeds are used; the claimed gain may be noise." | We agree. We reran all methods with **10 seeds** and added paired Wilcoxon tests with bootstrap CIs. The gain remains significant (p = 0.004). | Table II updated; new §V-B *Statistical validation*; p. 8, ll. 355–372 |
| R1.2 | "The comparison to CORAL is unfair — no tuning details." | We have equalised the budget: every method received the same 50-trial random search over an identical space, now specified. | New Table VII (search spaces); §IV-C; p. 6, ll. 240–258 |
| R2.1 | "The novelty over [9] is unclear." | [9] requires site labels; our method infers clusters from embedding statistics and needs no metadata. We now contrast them explicitly and add [9] as an upper bound. | §II-C rewritten; Table V adds "site-supervised (oracle)"; p. 4, ll. 150–163 |
| R2.2 | "Add experiments on a fourth dataset." | We were unable to obtain a fourth institution-disjoint public dataset with the required labels within the revision period (see §VI-B). To address the underlying concern about generality, we added **leave-one-site-out** evaluation over the three existing datasets, which yields five held-out site configurations. | New §V-E; Fig. 5; limitation stated p. 11, ll. 502–511 |

</div>
</div>

<!--
SPEAKER NOTES — (7 min)
Point at R2.2 as the model for a request you cannot fulfil: do not refuse, and do not pretend. Name the constraint, then satisfy the underlying concern by an alternative experiment, and state the residual limitation in the paper. Editors accept this routinely.
Note that R1.1's response strengthened the paper. Reframe reviews as free expert consultancy: the reviewer spent hours finding the weakness that would have discredited the work after publication.
Practical tip: build the response table as you make each change, not afterwards; reconstructing line numbers at the end wastes hours.
-->

---

<!-- _class: dense -->
# S24 · Disagreeing Professionally, and Tracking Revisions

<div class="cols">
<div>

#### How to disagree — the four-step pattern
1. **Acknowledge** the concern as legitimate: *"We appreciate this concern and have considered it carefully."*
2. **State your position** plainly: *"We respectfully retain the original choice, for the following reasons."*
3. **Give evidence**, not opinion: a citation, a new experiment, a definition, or a computation.
4. **Concede something**: add a clarification, a limitation sentence, or a supplementary analysis, so the reviewer's concern is visibly served even where you disagree.

> **Example.** "R2 suggests accuracy should be reported as the primary metric. Because pneumothorax prevalence is 1.2%, accuracy is dominated by the negative class: a constant-negative predictor attains 98.8% accuracy with zero recall. We therefore retain AP and recall at fixed specificity as primary, and we have **added accuracy to Table II for completeness** and explained this choice in §IV-D (p. 6, ll. 268–274)."

<div class="bad">

Never write: "The reviewer clearly did not read the paper." / "This comment is wrong." / "As already stated in the paper…" (even when true — instead: "We apologise that this was unclear; we have expanded §III-B.")

</div>

</div>
<div>

#### Tracking revisions mechanically
| Artefact | Purpose |
|---|---|
| **Response letter** (table format) | Point-by-point, with quoted new text and locations |
| **Marked-up manuscript** | Changes highlighted (LaTeX `\hl{}`/latexdiff, or Word track changes) |
| **Clean manuscript** | For typesetting and re-review |
| **Change log** | Your own private list of every edit, keyed to comment IDs |
| **Version control** | Git tags: `v1-submitted`, `v2-r1-response`, `v3-accepted` |
| **`latexdiff`** | Generates a difference PDF automatically from two `.tex` versions |

#### Decision decoding
| Decision | What it means | What to do |
|---|---|---|
| **Minor revision** | Likely acceptance | Respond fully; do not add scope |
| **Major revision** | Genuine interest; substantial work needed | Do the experiments; this is a success |
| **Reject & resubmit** | Sometimes a major revision with a reset clock | Treat as major revision; keep the reviewers' goodwill |
| **Reject** | Wrong venue, or fundamental flaw | Fix what the reviews exposed, then choose the next venue deliberately |

</div>
</div>

<!--
SPEAKER NOTES — (6 min) + ACTIVITY 24.1
ACTIVITY 24.1 (20 min): give every participant the same three synthetic reviewer comments (one easy, one requiring a new experiment, one you should push back on) and have them write the response table. Then compare two participants' responses to the push-back comment and discuss register. Handout: reviewer-response-template.md.
Explain "reject and resubmit" carefully — students often read it as a rejection and give up, when it frequently signals that the editor wants the paper after substantial work.
Say the emotional part once: a harsh review is about the manuscript. Wait 48 hours before writing the response letter. Never send a reply written on the day the reviews arrive.
-->

---

<!-- _class: dense -->
# S25 · Complete Case Study (1/2) — Idea to Results

<div class="cols">
<div>

| Stage | What was actually done | Time |
|---|---|---|
| **1 Idea** | Interest in medical imaging + reading a deployment failure report. Initial framing: "improve CXR classification" — **too broad** | wk 1 |
| **2 Narrowing** | Funnel → *domain generalisation in CXR*; one-breath test satisfied: 5 models, 3 datasets, site-wise splits, AUC/worst-site/ECE | wk 1–2 |
| **3 Search** | Scopus + WoS + IEEE + ACM + Semantic Scholar + arXiv; 6 strings logged with dates; **412 records → 118 title/abstract → 34 full text → 15 in matrix** | wk 2–3 |
| **4 Reading** | Pass 1 on 118; Pass 2 on 34 with the extraction template; Pass 3 on 4 (ran their code) | wk 3–6 |
| **5 Matrix** | 15 rows × 15 columns in Sheets, sourced from Zotero export; every cell verified against the PDF | wk 5–6 |
| **6 Gap** | Tallies: 11/15 random splits · 0/15 worst-site · 0/15 significance tests · 15/15 need site labels → **two-part gap** (unquantified degradation; no label-free mitigation) | wk 6 |
| **7 Objectives** | Aim + O1–O4 + H1–H3 with named tests; traceability table built | wk 6–7 |
| **8 Feasibility** | 3 public datasets (licences checked; PhysioNet DUA signed) · 4 baseline repos verified runnable · ≈480 GPU-hours estimated on one A100 | wk 7 |
| **9 Method** | CLUSTER-DG designed with an explicit mechanism hypothesis (artefacts dominate low-order statistics) | wk 8–9 |
| **10 Experiments** | 5 architectures × 2 protocols × 10 seeds; 4 baselines at equal 50-trial budget; ablation over K, λ, augmentation; leave-one-site-out; cost measured | wk 9–18 |
| **11 Results** | Degradation 0.116 (CI 0.104–0.128); CLUSTER-DG +0.041 worst-site (p = 0.004), ECE 0.094 → 0.052; **82% of the oracle recovered**; no significant gain on the smallest site — reported | wk 18–20 |

</div>
<div>

<div class="good">

#### What made this work publishable
- The **gap came from counting**, not from a hunch
- The **evaluation protocol itself** was part of the contribution
- **Equal tuning budgets** removed the standard reviewer objection
- **10 seeds + paired tests + CIs** made the margin defensible
- An **oracle upper bound** turned "+0.041" into "recovered 82% of privileged-information benefit"
- A **negative sub-result** (smallest site) was reported, which bought credibility
- **Artefacts released** (splits, code, weights) made it the protocol reference for later work

</div>

<div class="warn">

#### Where it nearly failed
- Week 4: the original plan needed a fourth private dataset — no data-use route. **Reframed** to three public datasets with leave-one-site-out.
- Week 12: baseline #3's official code would not reproduce its paper's number. Documented the discrepancy, contacted the authors, reported both numbers in a footnote.
- Week 16: 3 seeds showed a gain that vanished at 10 seeds for one architecture. **Reported it** rather than dropping that architecture.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (7 min)
Walk the timeline and dwell on the "nearly failed" box. Participants need to see that a successful paper contains three moments where an honest researcher lost something they wanted, handled it transparently, and ended up with a stronger paper.
The week-16 item is the ethical heart of the case study: the temptation to keep 3 seeds and the decision not to. Ask the room what the alternative would have been and what would have happened when someone tried to reproduce it.
-->

---

<!-- _class: xdense -->
# S25 · Complete Case Study (2/2) — Writing to Publication

<div class="cols">
<div>

| Stage | What was actually done | Time |
|---|---|---|
| **12 Figure/table skeleton** | 7 floats listed before any prose was written | wk 20 |
| **13 Writing order** | Method → setup → results → discussion → related work (from the matrix) → introduction → conclusion → abstract → title | wk 20–23 |
| **14 References** | 52 entries in Zotero → Better BibTeX → Overleaf `IEEEtran`; **every DOI resolved**; 2 retraction checks; 1 preprint replaced with its published version | wk 23 |
| **15 Similarity check** | iThenticate via the institution: 19% total. Report opened match by match: 11% references + standard method phrasing, 6% correctly quoted definitions, **2% patchwritten related-work sentences → rewritten** | wk 23 |
| **16 Ethics/declarations** | Public de-identified datasets (no IEC approval needed, stated explicitly); DUA compliance noted; CRediT statement; AI-use statement (language editing only); data/code DOIs minted on Zenodo | wk 23 |
| **17 Journal selection** | Target Q1 (scope quoted; 5 cited papers from it; SCIE-verified on MJL; APC covered by institutional agreement); two backups scored on the checklist | wk 24 |
| **18 Submission** | Template compliance, system PDF proofed, cover letter, 3 suggested reviewers, supplementary appendix | wk 24 |
| **19 First decision** | **Major revision**, 3 reviewers, 21 comments, 11 weeks | wk 35 |
| **20 Revision** | 10→10 seeds retained, 2 new experiments (leave-one-site-out extension, latency table), 1 reasoned disagreement (accuracy as primary metric), response table with quoted text and line numbers | wk 35–41 |
| **21 Second round** | **Minor revision** (4 comments) → accepted | wk 47–52 |
| **22 Production** | Proofs corrected (2 figure-caption errors, 1 wrong reference year caught); early access; DOI; Zenodo release linked | wk 53–56 |

</div>
<div>

#### Total: ~13 months from idea to early access

<div class="demo">

#### The reusable order of operations
<div class="flow">
1  Narrow until you can name
   datasets + baselines + metrics
2  Search reproducibly; log everything
3  Triage → extract → matrix
4  COUNT columns → gap
5  Gap → RQ → objectives → hypotheses
6  Feasibility audit BEFORE experiments
7  Baselines + ablations + seeds + stats
8  Floats first, prose second
9  Verify every reference
10 Similarity report: read matches
11 Declarations before submission day
12 Verify the journal on official lists
13 Respond to every comment, with locations
14 Proof-read the proofs
</div>

</div>

<div class="good">

**Notice what is absent:** no step where anything was invented, no step where an AI wrote submitted text unverified, and no step where an inconvenient result was hidden.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (7 min)
Give the honest timeline: 13 months, of which 6 were waiting. Participants planning "a paper this semester" need this calibration, and it argues for starting the search and matrix immediately rather than after the experiments.
Highlight step 15: 19% similarity, of which only 2% was a real problem — and that 2% was fixed by rewriting, not by word-swapping. This closes the loop with S21.
Close by reading the "notice what is absent" box aloud. It is the workshop's ethical summary.
-->

---

<!-- _class: dense -->
# Final Hands-On Activity — Mini Research Proposal

<div class="cols">
<div>

#### Deliverable: 14 components (`handouts/mini-proposal-template.md`)
| # | Component | Length |
|---|---|---|
| 1 | **Title** (3 candidates, best marked) | 1 line |
| 2 | **Problem statement** | 3–5 sentences |
| 3 | **Research gap** (template + counts + gap type) | 4–6 sentences |
| 4 | **Objectives** O1–O4 (+ aim, hypotheses with tests/α) | bulleted |
| 5 | **Proposed methodology** (+ architecture diagram, pseudocode) | 1 page |
| 6 | **Dataset(s)** (name, size, licence, split unit) | table |
| 7 | **Baseline methods** (4+, with repo links) | table |
| 8 | **Evaluation metrics** (+ 1-sentence justification each) | table |
| 9 | **Expected contributions** C1–C3 (calibrated) | bulleted |
| 10 | **Target journals** (1 target + 2 backups, checklist scored) | table |
| 11 | **Initial abstract** (7 moves, 200–300 words, `[TBD]` for unknowns) | paragraph |
| 12 | **Introduction outline** (6 paragraphs, job of each in ≤6 words) | bulleted |
| 13 | **Literature matrix** (≥10 rows × 15 columns) | spreadsheet |
| 14 | **References** (≥15, IEEE style, every DOI resolved) | list |

</div>
<div>

#### Timing (100 min)
| Min | Task |
|---|---|
| 0–10 | Assemble Day 1 artefacts (items 3, 4, 13) |
| 10–25 | Title candidates + problem statement (1, 2) |
| 25–50 | Methodology + diagram + pseudocode (5) |
| 50–65 | Datasets, baselines, metrics with justifications (6–8) |
| 65–75 | Contributions + journal checklist (9, 10) |
| 75–90 | Abstract (11) + introduction outline (12) |
| 90–100 | Reference audit: resolve every DOI (14) |

<div class="warn">

#### Integrity rules for this deliverable
- Every citation must be one **you opened**; every DOI must resolve.
- Use `[TBD]` for any number you have not measured. **No placeholder numbers.**
- Note where AI assisted, and what you verified.
- Datasets must be real, with a stated licence and access route.

</div>

</div>
</div>

<!--
SPEAKER NOTES — Final activity facilitation (100 min)
Circulate with a single question per participant, chosen from: "Which contribution has no objective?" / "Which metric has no justification?" / "Which reference have you not opened?" / "What is your killer risk?"
At minute 90, enforce the reference audit even if other sections are incomplete — resolving DOIs is the habit most likely to be abandoned, and doing it once under supervision makes it stick.
Collect the deliverables. If this is a credit-bearing workshop, mark against the rubric on the next slide; if not, ask participants to send the proposal to their supervisor within 48 hours while it is still warm.
-->

---

# Rubric, 12-Week Plan, and Close

<div class="cols">
<div>

#### Rubric (30 points)
| Criterion | Pts |
|---|---|
| Title specific + searchable; problem statement precise | 3 |
| Gap: evidenced with counts, correctly typed | 4 |
| Objectives measurable; traceable to contributions | 3 |
| Methodology reproducible; diagram + pseudocode present | 4 |
| Datasets real, licensed; split unit stated | 2 |
| ≥4 baselines incl. classical + "ours minus novelty" | 3 |
| Metrics justified by the decision they support | 3 |
| Abstract: 7 moves, numbers or honest `[TBD]` | 3 |
| Journals verified on official indexes; checklist scored | 2 |
| Matrix ≥10×15, cells verified | 2 |
| References IEEE-consistent; **all DOIs resolve** | 1 |

</div>
<div>

#### Your next 12 weeks
| Wk | Action |
|---|---|
| 1 | Set 3 alerts (Scopus/Scholar/Semantic Scholar); fix all Zotero metadata |
| 2 | Grow the matrix to 25 rows; recompute tallies |
| 3 | Rewrite the gap; **stress-test it with your supervisor** |
| 4 | Freeze objectives + hypotheses (with tests and α) |
| 5–6 | Reproduce **one** baseline end-to-end; document discrepancies |
| 7–8 | Build the pipeline; fix seeds, configs, logging from day one |
| 9–10 | Full experiments: baselines at equal budget, ≥5 seeds, ablations |
| 11 | Floats first: build all 7 figures/tables |
| 12 | Draft in writing order; run the similarity check; verify every DOI |

<div class="good">

#### Closing takeaway
Publication is a **process with checkpoints**, not a talent. The checkpoints are: a **narrow question**, a **documented search**, a **counted gap**, **measurable objectives**, **fair experiments**, **honest reporting**, **verified references**, and a **deliberately chosen venue**. Miss none of them, invent nothing, and the paper will find its journal.

</div>

</div>
</div>

<!--
SPEAKER NOTES — Closing (10 min)
Return to the Learning Outcomes slide from Day 1 and ask participants to self-rate 1-12. Whatever they rate lowest is what they should work on first; tell them that explicitly.
Ask each participant to say one sentence: "In the next seven days I will ___." Public commitment to a small, dated action massively increases follow-through. Write them down and email the list to the group.
Final message, in your own words: rejection is a normal, non-fatal, informative event; integrity is the only non-negotiable; and the artefacts they are holding — a matrix, a counted gap, a proposal — are the same artefacts every published researcher builds, only usually less deliberately.
Point them to the handouts folder and the facilitator guide so they can run this workshop for their own juniors.
-->
