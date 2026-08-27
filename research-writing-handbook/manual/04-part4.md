# PART IV — RESEARCH PAPER READING

<div class="partintro">

Part IV addresses a skill that is almost never taught explicitly and that determines how fast a researcher can develop: reading papers efficiently and critically. Chapter 11 dissects the anatomy of a paper and specifies what to extract from each section. Chapter 12 gives a three-pass reading method with time budgets. Chapter 13 provides a sixteen-field extraction framework that converts reading into structured data you can analyse.

The governing insight is that efficient reading is not *faster* reading. It is **selective depth**: triaging everything, comprehending a core set, and reconstructing only the few papers your contribution actually stands on.

</div>

<div class="pagebreak"></div>

# Chapter 11 — Anatomy of a Research Paper

## 11.1 Why structure knowledge helps you read

A research paper is a highly conventional document. Once you know what each section is *for*, you know where to look for what you need and — just as important — you can detect when something that should be present is missing. An absent ablation, an unstated split protocol, or an unreported variance is invisible if you read linearly and obvious if you read structurally.

## 11.2 Section by section

**Table 11.1 — What to extract from each section of a paper**

| Section | Its function | What you should extract | Warning signs |
|---|---|---|---|
| **Title** | Identify and index the work | Method, problem, domain; whether it claims a finding or an artefact | Vague or buzzword-laden; claims not supported later |
| **Abstract** | Let a reader decide whether to read on | Problem, gap, method, data, headline result | No numbers; no dataset named; "results show effectiveness" |
| **Keywords** | Indexing and discovery | Controlled vocabulary for your own synonym table (§10.2) | Keywords absent from the paper's own content |
| **Introduction** | Establish importance and the gap | The claimed gap; the contribution list; the framing you may need to challenge | No gap paragraph; contributions that restate the method |
| **Related work** | Position the contribution | Their taxonomy of the field; who they consider competitors; **who they omit** | Paper-by-paper list; obvious competitor missing |
| **Methodology** | Enable reproduction | Architecture, algorithm, loss, the *novel component* isolated from the inherited parts | Cannot tell what is new; no rationale for design choices |
| **Dataset** | Define the evidence base | Names, versions, sizes, class balance, licence, **split protocol and split unit** | Unnamed or private data; split unit unstated |
| **Experimental setup** | Establish comparability | Baselines, tuning budget, seeds, hardware, framework versions | No seed count; no tuning budget; baselines from a paper rather than re-run |
| **Results** | Report observations | Numbers *with their comparison point*, variance, statistical tests | Single-run values; only favourable datasets reported |
| **Discussion** | Interpret | Mechanism offered; reconciliation with prior work; admitted limits | Results restated as interpretation; no limitations |
| **Conclusion** | State what is now known | The claim as the authors would defend it | New claims not supported by the results |
| **References** | Credit and traceability | Origin papers you must also read; the field's canon | Very recent only; single-group clustering; canon missing |
| **Appendices / supplementary** | Detail that would obstruct the main text | The honest details — full hyperparameters, extra datasets, failure cases | Material that contradicts the main text's emphasis |
| **Declarations** | Ethics, funding, data and code availability | Whether you can obtain the artefacts | "Available on request"; no ethics statement where required |

## 11.3 Where the important information actually hides

Three practical observations that experienced readers rely on:

**The tables tell you what was really compared.** An introduction tells you what the authors want you to believe was compared; the tables tell you what was. Read the tables before the prose.

**The appendix tells you what was really done.** Page limits push inconvenient detail into supplementary material: the full hyperparameter grid, the datasets where the method did less well, the sensitivity analysis. Read it for any paper you intend to use as a baseline.

**The limitations section is a gift.** Authors are required to admit weaknesses and generally do so honestly. Those admissions, aggregated across many papers, are the raw material of your research gap (Chapter 18).

## Exercises

**Exercise 11.1** Take a paper in your area and, for each row of Table 11.1, write down what you extracted and any warning signs you found. Papers with three or more warning signs should not be used as baselines without a deep read.

**Exercise 11.2** Find a paper whose abstract number does not appear in the same form in the results tables. This takes less searching than you would hope, and it permanently changes how you read abstracts.

<div class="pagebreak"></div>

# Chapter 12 — How to Read a Research Paper

## 12.1 The three-pass method

The approach below is an adaptation of the widely used three-pass method described by Keshav (2007), extended with an extraction framework for empirical computational work. Keshav's original two-page article is worth reading directly; it takes ten minutes.

**Figure 12.1 — The three-pass reading method**

```
  ┌─ PASS 1 · TRIAGE ─────────────────────────── 5–10 min · 100% of papers ─┐
  │  Read: title, venue, abstract, all figures and tables with captions,     │
  │        section headings, conclusion, skim references                     │
  │  Decide: DISCARD / CITE-ONLY / READ FULLY                               │
  │  Output: one line in your triage sheet                                  │
  └─────────────────────────────────────────────────────────────────────────┘
                     │  (roughly 10–20% survive)
  ┌─ PASS 2 · COMPREHENSION ─────────────────── 45–60 min · core set ───────┐
  │  Read: everything except heavy derivations; all tables carefully         │
  │  Do:   redraw their pipeline yourself; interrogate every table          │
  │  Output: a filled 16-field extraction template (Chapter 13)             │
  └─────────────────────────────────────────────────────────────────────────┘
                     │  (roughly 3–6 papers per project)
  ┌─ PASS 3 · RECONSTRUCTION ────────────────── 2–5 h+ · baselines only ────┐
  │  Read: everything, including proofs, appendices, and THE CODE            │
  │  Do:   re-derive equations; clone and run; reconcile code with paper     │
  │  Output: a trustworthy baseline number; a list of hidden assumptions     │
  └─────────────────────────────────────────────────────────────────────────┘
```

**Table 12.1 — Reading passes: time, coverage, and output**

| | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|
| Time | 5–10 min | 45–60 min | 2–5 h or more |
| Share of your set | 100% | 10–20% | 2–5% |
| Governing question | Is this relevant to *my* question? | Do I believe the claim? | Can I build on, extend, or break this? |
| Output | Triage line | Extraction template + matrix row | Reimplementation; assumption list; new research ideas |

**The arithmetic that justifies this.** Reading two hundred papers at forty-five minutes each is 150 hours. Triaging two hundred at seven minutes (23 hours), comprehending twenty-five at fifty minutes (21 hours), and deeply reading four (20 hours) is about 64 hours for *better* coverage, because you spend your depth where it matters. Efficiency here is not laziness; it is what makes a literature review finishable.

## 12.2 Pass 1: triage

**Read in this order — and note that it is deliberately not the printed order:**

1. **Title, venue, year.** Is it peer reviewed? Which community? Does the venue suggest a standard of evidence?
2. **Abstract.** Problem, method, headline claim.
3. **Figure 1** (usually the architecture or overview). The idea in one image.
4. **All tables.** What was compared, on what data, against what.
5. **Section headings.** The shape of the argument.
6. **Conclusion and limitations.** Their own account of what they did not achieve.
7. **Skim references.** Do you recognise the canon? Is anything conspicuously absent?

Reading figures and tables *before* the introduction is the key move: it protects you from adopting the authors' framing before you have assessed their evidence.

**Record five items:** problem; method in eight words or fewer; datasets; headline metric; relevance verdict.

**Discard signals.** Different task with no transferable mechanism; no baseline comparison at all; no named dataset and no access route; venue you cannot verify (Chapter 52); results implausible without explanation; superseded by a later version you already hold.

**Cite-only signals.** Provides a definition, statistic, or dataset you need; is the origin of a method you use; **contradicts another paper you are keeping** — flag contradictions explicitly, because they are the richest source of research gaps (§18.4).

## 12.3 Pass 2: comprehension

**Procedure.**

1. Re-read the abstract and write **their claim in your own words**. If you cannot, note it — that may be their writing failure rather than your comprehension failure, but you must resolve it either way.
2. **Redraw their pipeline as a block diagram yourself, without copying theirs.** This is the highest-value single habit in this chapter. Drawing forces you to make explicit what their prose left vague, and where you cannot draw, you have found either a gap in your understanding or an under-specified method. Both are useful.
3. Extract the experimental setup: datasets, splits and split unit, baselines, metrics, hyperparameters, tuning budget, seeds, hardware.
4. For **each table**, ask four questions:
   - What exactly is the comparison?
   - Was the baseline tuned with effort comparable to the proposed method?
   - Is the reported gain larger than the run-to-run variance?
   - Are *all* datasets and metrics reported, or only the favourable ones?
5. Mark unfamiliar terms and citations, and build a follow-up reading queue rather than breaking flow.
6. Fill the extraction template (Chapter 13).

**Critical-reading questions that expose weak work.**

| Target | Question |
|---|---|
| Novelty | Which *exact* component is new? Which prior paper is closest, and how does this differ? |
| Fairness | Same data, splits, preprocessing, and tuning budget for every method? |
| Leakage | Any subject, site, or user appearing in both training and test? Any tuning on the test set? |
| Variance | Multiple seeds? Standard deviations? Confidence intervals? Any statistical test? |
| Selectivity | Are the omitted datasets or metrics the inconvenient ones? |
| Cost | Are parameters, FLOPs, latency, and memory reported? |
| Reproducibility | Are code and weights available, and do they match the paper? |
| Explanation | Do the authors explain *why* it works, or only *that* it wins? |

The selectivity question requires care. Treat it as a hypothesis to check — compare the datasets named in the abstract with those in the appendix, and check whether the headline metric is used consistently throughout — not as an accusation to make.

## 12.4 Pass 3: reconstruction

**When to invest this much.** The paper is your principal baseline; you intend to extend its method; you suspect the result is overstated; or it is the theoretical foundation of your own contribution.

**What you actually do.**

1. Re-derive the key equations; check dimensions and assumptions.
2. Reconcile the notation in the paper with the variable names in the code. They frequently disagree, and the disagreement is informative.
3. Clone the repository. Run it **as published**, then on **your** data.
4. Record every discrepancy: undocumented preprocessing, hyperparameters in code differing from those in the paper, a metric implemented non-standardly, a different data split than described.
5. Read supplementary material and appendices in full.
6. Read public reviews and author responses if the venue provides them.
7. Email the authors with one specific, respectful question. Response rates are higher than early-career researchers expect.

**What this produces:** a baseline number you can defend to a reviewer; a list of hidden assumptions, each of which is a candidate research gap; and sometimes a reproducibility finding, which is itself publishable (§17.10).

**On reporting reproduction failures.** Write about the *method and protocol*, never about the authors' competence or honesty. A sentence naming a number, a protocol, a seed count, and a configuration is unanswerable:

> ✅ *"Using the released implementation with the described protocol, we obtained 0.86 ± 0.01 macro AUC over five seeds, compared with the reported 0.91. We were unable to identify the source of the discrepancy; the released configuration differs from the paper's description in the augmentation pipeline (Appendix C)."*

The most common causes of irreproducibility are undocumented preprocessing, different splits, unequal tuning budgets, and non-standard metric implementations — not misconduct. Documenting *which* one it was is a contribution.

## 12.5 Common mistakes

| Mistake | Correction |
|---|---|
| Reading linearly from page one on first contact | Triage first (§12.2) |
| Highlighting instead of extracting | Fill fields; highlighting produces no reusable data |
| Believing the abstract's number without checking the table | Always verify against the table |
| Recording only the authors' stated limitations | Add your own independent critique (§13.4) |
| Never checking whether a paper was later refuted | Forward-chain every core paper (§10.8) |
| Letting an automated summary replace reading a core paper | Summaries are for triage only |
| Not recording the citation key at extraction time | You will lose hours reconstructing provenance |

## Exercises

**Exercise 12.1** Triage five papers with a visible seven-minute timer. Write the five-item record for each. Most people are surprised how much is decidable in seven minutes.

**Exercise 12.2** Pass-2 one paper fully. Redraw its pipeline without looking at their figure, then compare. Note every place your drawing was uncertain.

**Exercise 12.3** For that paper, answer all eight critical-reading questions in §12.3. Then decide whether you would trust it as a baseline.

**Exercise 12.4** Choose your most important paper, clone its code, and attempt to reproduce one reported number. Whatever happens, you will learn more in three hours than from a week of reading abstracts.

<div class="pagebreak"></div>

# Chapter 13 — Research Paper Extraction

## 13.1 Purpose

Reading produces understanding; extraction produces **data**. The distinction matters because research gaps are found by *comparing across* papers (Chapter 18), and comparison requires structured fields, not prose notes. One filled template becomes one row of your literature matrix (Chapter 15) and, later, the raw material for your related-work section (Chapter 33).

Complete one during Pass 2. Save it as `<CitationKey>.md` — for example `Zech2018Confounding.md` — in one folder.

## 13.2 The sixteen-field framework

**Table 13.1 — The sixteen-field extraction framework**

| # | Field | What to capture | Why it matters later |
|---|---|---|---|
| 1 | **Citation key, venue, year, indexing** | Full citation; DOI verified; venue type | Provenance; weighting evidence quality |
| 2 | **Research problem** | The unknown they address, **in your own words** | Grouping papers into themes |
| 3 | **Motivation** | Why it matters — application or theory | Your own introduction's ¶1 |
| 4 | **Stated objective** | Their explicit aim or research question | Detecting mismatch between aim and evidence |
| 5 | **Claimed gap** | What they say prior work lacked, and whether they evidence it | Shows how gaps are argued in your field |
| 6 | **Dataset(s)** | Names, versions, sizes, classes, balance, licence, **split protocol and split unit** | **The most diagnostic field** — reveals leakage and incomparability |
| 7 | **Preprocessing** | Resizing, normalisation and where statistics were fitted, augmentation, resampling and whether before or after splitting | Leakage detection; reproduction |
| 8 | **Proposed method** | Architecture or algorithm; the *novel component* isolated; the stated mechanism | Building your method taxonomy |
| 9 | **Baselines** | What they compared against; whether tuned equally; number of baselines | Reveals weak-comparison papers |
| 10 | **Evaluation metrics** | Which, and whether appropriate to the problem | Reveals evaluation gaps |
| 11 | **Experimental setup** | Seeds, variance reporting, statistical test, cross-validation, optimiser, schedule, hardware, versions, tuning budget | Judging reliability |
| 12 | **Key results** | Two or three numbers, **each with its comparison point**, taken from the tables not the abstract | Your comparison tables |
| 13 | **Limitations — theirs** | Verbatim quotes with section and page | Citations for your gap paragraph |
| 14 | **Limitations — yours** | Your independent critique | **The field that produces research gaps** |
| 15 | **Future work** | Their suggestions, verbatim | Author-endorsed research directions |
| 16 | **Relevance and links** | Core / context / discard; which paper this contradicts; possible extension for you | Prioritisation; contradiction mining |

## 13.3 Field 6 in detail: why the split protocol matters most

If you extract only one thing carefully, extract the **split unit**.

Data are frequently *grouped*: many images per patient, many commits per project, many utterances per speaker, many readings per sensor, many pupils per classroom. When such data are split randomly *by row*, records from the same group appear in both training and test partitions. The model can then succeed by recognising the group rather than by learning the target relationship, and the reported performance describes within-group recognition rather than the generalisation the paper claims.

This is not a hypothetical concern. Zech et al. (2018) demonstrated that chest-radiograph classifiers can exploit institution-specific signal, with the consequence that internal performance overstates external performance.

So field 6 must record not only "70/15/15" but **the unit**: split by image, by patient, by institution, by author, by project, by time period. When you later tally this field across fifteen papers and find that most used random row-level splits on grouped data, you have discovered a field-level methodological gap that a reviewer cannot dismiss — because the evidence is arithmetic.

## 13.4 Field 14 in detail: your own critique is mandatory

A template containing only the authors' self-assessment reproduces their framing. That is summarising, not reviewing. Field 14 must contain *your* independent assessment, organised under headings:

- **Fairness of comparison** — equal tuning? official implementations? same preprocessing?
- **Statistical validity** — seeds, variance, tests, corrections?
- **Evaluation protocol** — appropriate metrics? leakage? split unit?
- **Generality** — how many datasets, populations, domains? What is excluded?
- **Cost and deployability** — reported at all?
- **Reproducibility** — code, weights, configurations, splits available?
- **Explanation** — is a mechanism offered and tested, or only a result reported?
- **Selectivity** — is anything conspicuously unreported?

## 13.5 Worked extraction

**[HYPOTHETICAL]** The following is an extraction of an invented paper, constructed for teaching. It is not a real work and must not be cited.

> **Paper P7** — "Site-Adversarial Training for Cross-Hospital Chest Radiograph Classification", hypothetical journal, 2024.

| Field | Content |
|---|---|
| 2 Problem | CXR classifiers lose performance at unseen hospitals; the magnitude under leakage-free protocols is unquantified |
| 3 Motivation | Deployment across institutions with differing equipment and protocols |
| 4 Objective | Reduce cross-site AUC loss without harming in-domain AUC |
| 5 Claimed gap | Prior domain-generalisation work evaluates on random splits that leak site identity |
| 6 Datasets | CheXpert (train); ChestX-ray14 and MIMIC-CXR (external); **institution-disjoint** splits |
| 7 Preprocessing | 224×224, histogram equalisation, random crop and flip; normalisation statistics from training partition only; no lung segmentation |
| 8 Method | DenseNet-121 with a gradient-reversal site-discriminator branch; invariance weight ramped over five epochs. Novel component: the ramping schedule. Mechanism claimed: site-invariant features transfer better |
| 9 Baselines | ERM, IRM, CORAL, Mixup — four, from official implementations |
| 10 Metrics | Macro AUC, worst-site AUC, expected calibration error |
| 11 Setup | **3 seeds**; Adam 1e-4; 30 epochs; single GPU; code released; tuning budget not stated |
| 12 Key results | Worst-site AUC 0.78 → 0.83; in-domain AUC 0.89 → 0.88; ECE 0.09 → 0.05 |
| 13 Limitations (theirs) | "Restricted to frontal adult radiographs; site labels are assumed known at training time." (§VI, p. 11) |
| 14 **Limitations (mine)** | Only three seeds and **no statistical test**, so the 0.05 worst-site gain may lie within run-to-run variance. **Tuning budget unstated**, so fairness cannot be assessed. **Requires site labels**, which are typically stripped before data leaves an institution — this is the binding practical constraint. No subgroup analysis by age, sex, or device, so worst-*site* may conceal worst-*group*. No cost reporting. **No ablation on the ramping schedule**, which is the claimed novelty — so the paper does not establish that its own contribution is responsible for the gain. |
| 15 Future work | Extend to lateral views and paediatric populations |
| 16 Relevance | **Core** — principal baseline. Contradicts P4 on whether calibration improves. Extension: can pseudo-domains inferred *without* site labels recover most of this gain, and does the effect survive ten seeds with a paired test? |

**Observe what field 14 produced.** Three candidate research directions emerged from critically reading one paper: a label-free variant (methodological gap), a statistical re-evaluation (evaluation and reliability gap), and a subgroup analysis (evaluation and fairness gap). None required an original idea from nothing; all came from asking *how do you know?* systematically.

## 13.6 Tool assistance and its limits

Software can pre-populate parts of this template, and doing so is legitimate and efficient — with a firm boundary.

| Field | May be pre-filled by a tool | Must be yours |
|---|---|---|
| 1, 6, 7, 9, 10, 11 | ✅ Factual fields, then verified cell by cell against the PDF | |
| 12 Key results | ⚠️ Extracted numbers **must** be checked against the actual table — this is where automated extraction most often errs, by attributing a number to the wrong condition | |
| 2, 4, 5 | | Your restatement of their problem and gap |
| 13 | | Verbatim quotes you located |
| **14, 16** | | **Your critique and your judgement — never delegable** |

The rule for the whole handbook, stated once and applied throughout: **tools may help you find, sort, translate, and pre-fill; you must read, verify, compare, judge, and claim.** Chapter 45 develops this.

## 13.7 Verification checklist for Part IV

- [ ] I triage every paper before reading it fully.
- [ ] My core set has a filled sixteen-field template each.
- [ ] Field 6 records the split **unit**, not only the ratio, for every paper.
- [ ] Field 12 numbers were taken from tables, not abstracts.
- [ ] Field 14 contains my own critique for every paper, under the eight headings.
- [ ] I have flagged every contradiction between papers in field 16.
- [ ] Every automated extraction has been verified against the PDF.
- [ ] I have deep-read and attempted to run at least one baseline.
- [ ] Citation keys were recorded at extraction time.

## Exercises

**Exercise 13.1** Complete the full sixteen-field template for three papers. Time yourself; the third will take half as long as the first.

**Exercise 13.2** For each, write field 14 under all eight headings. Then list every candidate research direction that fell out. Expect two to four per paper.

**Exercise 13.3** Tally the split unit across your extractions so far. If most are row-level random splits on grouped data, you have found a gap — proceed to Chapter 18.

**Exercise 13.4** Take one paper, have a tool extract fields 6, 9, 10, and 12, then verify every cell against the PDF. Record how many were wrong. Whatever the answer, you now know the verification is necessary.

<div class="pagebreak"></div>
