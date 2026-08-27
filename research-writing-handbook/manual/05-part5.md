# PART V — LITERATURE REVIEW

<div class="partintro">

Part V converts extracted papers into an argument. Chapter 14 distinguishes synthesis from summary and demonstrates the difference on the same set of papers. Chapter 15 specifies the literature matrix — the single most useful artefact in this handbook — and shows how gaps are found by reading its *columns*. Chapter 16 covers the tools, with the verification each requires.

</div>

<div class="pagebreak"></div>

# Chapter 14 — Literature Review Writing

## 14.1 Definition

**Definition.** A literature review is an argument about a body of work that (a) organises it into a structure of your making, (b) evaluates the quality of its evidence, and (c) demonstrates that a specific gap exists.

All three clauses are required. An organised account with no evaluation is a catalogue. An evaluation with no organisation is a series of opinions. Either without a terminating gap leaves the reader asking why they read it.

## 14.2 Review versus summary

| | **Summary (paper-by-paper)** | **Review (synthesis)** |
|---|---|---|
| Unit of a paragraph | One paper | One idea, method family, or finding |
| Ordering principle | The order you happened to read them | Your taxonomy |
| Characteristic verbs | proposed, used, applied, achieved | converge on, diverge, in contrast, remains untested |
| Comparison | None | Explicit, along shared dimensions |
| Evaluation | None | Quality of evidence assessed with reasons |
| Ends with | The last paper | **The gap** |
| Citations per sentence | One | Frequently two to five, grouped |

**The diagnostic.** Look at your draft. If most paragraphs begin with an author's name, you have written a summary. Run this test tonight on whatever you have.

**Figure 14.1 — Paper-by-paper listing versus critical synthesis**

```
  SUMMARY (weak)                          SYNTHESIS (strong)

  ¶ Author A did X, got 0.90.             ¶ Two families exist. FAMILY 1
  ¶ Author B did Y, got 0.89.               increases capacity [A,B,C];
  ¶ Author C did Z, got 0.91.               reports 0.89–0.91 BUT all three
  ¶ Author D did W.                         evaluate on random splits, so
  ¶ Author E did V.                         these are in-distribution numbers.
                                          ¶ FAMILY 2 targets invariance
  Reader learns: five facts.                [D,E]; does evaluate across sites
  Reader cannot tell what is KNOWN,         BUT both require site labels and
  what is DISPUTED, or what is              report ≤3 seeds without tests.
  MISSING.                                ¶ ACROSS ALL FIVE: worst-site
                                            performance and calibration are
                                            never reported.
                                          ¶ THEREFORE the gap is ...

                                          Reader learns: the state of
                                          knowledge, and what is absent.
```

## 14.3 Five organising structures

| Structure | Organising principle | Use when | Risk |
|---|---|---|---|
| **Chronological** | Time; paradigm shifts | The field has genuine successive eras | Becomes a timeline with no argument |
| **Thematic** | Sub-problems or facets | Several distinct facets exist | Themes overlap; papers repeat |
| **Methodological** | Technique families | You will argue a *family* shares a weakness | Ignores differences in task and data |
| **Comparative** | Dimensions in a matrix | You have quantitative evidence across studies | Reads like a spreadsheet if not interpreted |
| **Critical / argumentative** | Your thesis about the field | You have deep mastery and a defensible position | Can appear biased; needs scrupulous fairness |

**Recommendation.** Strong reviews are usually **hybrid**: a thematic top level, methodological groups within each theme, a comparison table per theme, and a critical synthesis paragraph closing each theme — with the section's final paragraph stating the gap.

A reusable skeleton for a related-work section:

```
  2.1  Problem formulations, datasets, and evaluation conventions
  2.2  Method family A          (+ comparison table, + critique paragraph)
  2.3  Method family B          (+ comparison table, + critique paragraph)
  2.4  Evaluation practices in this area        ← usually omitted; high value
  2.5  Synthesis: what is settled, what is contested, what is untested
                                                 ► THE GAP
```

Subsection 2.4 deserves comment. Almost no student paper contains a subsection on the *evaluation practices* of prior work, and it is where evaluation gaps become visible. If your contribution is a re-evaluation, 2.4 is the paragraph that justifies your entire paper.

**A practical shortcut.** Open the two most recent surveys in your area and examine their section structure. A taxonomy already exists. You may adopt it with citation, or deliberately improve on it — and explaining why the existing taxonomy is inadequate is itself a contribution.

## 14.4 Worked contrast on the same five papers

**[HYPOTHETICAL] ❌ Weak — a summary chain**

> "Zhang et al. [11] used a CNN with attention for chest X-ray classification and achieved 0.90 AUC. Patel et al. [12] used DenseNet-121 and reported 0.89. Lee et al. [13] applied a vision transformer, achieving 0.91. Gupta et al. [14] used CORAL for domain adaptation. Rao et al. [15] used IRM and showed improvement in external validation."

Five faults: chronological accident as structure; numbers from different datasets and splits presented as if comparable; no assessment of quality; no shared dimension; no gap at the end.

**[HYPOTHETICAL] ✅ Strong — synthesis with a critical edge**

> "**Capacity-scaling approaches.** One line of work treats cross-institutional robustness as a byproduct of stronger representations, progressing from attention-augmented convolutional backbones [11], [12] to vision transformers [13]. These report 0.89–0.91 AUC; however, all three evaluate on random splits in which radiographs from the same institution occur in both partitions (Table I), so their figures describe in-distribution performance and cannot be read as evidence of transfer.
>
> **Invariance-based approaches.** A second line optimises explicitly for domain invariance through feature alignment [14] or invariant risk minimisation [15], and does evaluate across institutions, reporting external gains of three to six AUC points. Both, however, require institutional labels during training, and neither reports variance over more than three seeds; since seed-to-seed variation of one to two AUC points is documented for these architectures [12], it is unclear whether the reported margins exceed run-to-run noise.
>
> **Evaluation practice.** Across the fifteen studies surveyed, none reports worst-institution AUC and only two report calibration, although a triage system's usability is governed by its weakest site and by the reliability of its confidence estimates rather than by mean discriminative performance.
>
> **Synthesis and gap.** The field has therefore established that distribution shift matters, but not how large it is under leakage-free protocols, nor whether invariance is attainable without institutional metadata, nor what happens to worst-site performance and calibration. This paper addresses these three questions."

Note the machinery: it groups; it names a shared dimension (evaluation protocol); it states what is credible and what is not, *with a reason*; it groups citations; it identifies what is missing across *all* studies; and its final sentence is a gap statement. No sentence begins with an author's name.

## 14.5 The synthesis phrasebook

Non-native English writers frequently find this the most immediately useful page in the handbook.

**Agreement and convergence.** "Consistently across [3]–[7], …" · "There is broad agreement that …, although the reported effect size ranges from X to Y." · "Both lines converge on …"

**Contrast and contradiction.** "In contrast to [4], who report …, [8] find the opposite when …" · "This discrepancy is plausibly attributable to differing split protocols rather than to the methods themselves." · "Whereas earlier work assumed …, more recent evidence suggests …"

**Evaluating quality.** "…, although the comparison employs an untuned baseline." · "…; the reported gain of 0.4 points is smaller than the seed-to-seed variance reported in [9]." · "…, on a single dataset, which limits generality." · "…, though the tuning budget is not stated, so fairness cannot be assessed."

**Establishing absence — the gap moves.** "**X** remains unquantified under **[condition]**." · "Existing evaluations do not report **[quantity]**, although it determines **[consequence]**." · "This assumption is unlikely to hold in **[setting]**, yet remains untested." · "We found no study that evaluates X under Y; the closest is [12], which does Z but not Y."

**A warning about absolute claims.** Never write "no work exists" casually — a specialist reviewer will find a counterexample, and the credibility damage extends to your whole paper. The safer and *stronger* formulation is the last one above: it demonstrates that you searched, names the nearest prior work, and survives contact with an expert.

## 14.6 Common mistakes

| Mistake | Correction |
|---|---|
| Every paragraph begins with an author's name | Reorganise by idea, not by paper |
| Comparing numbers from different datasets and splits | State explicitly that they are not comparable; that statement is itself a finding |
| Listing without evaluating | Every group needs a critique sentence with a reason |
| No gap at the end of the section | The final paragraph must state the absence |
| "No work exists" | "We found no study that…; the closest is [x]" |
| Dismissing prior work rudely | Criticise the protocol, never the authors — they may be your reviewers |
| Omitting an evaluation-practices subsection | Add §2.4; it is where the cheapest defensible gaps live |
| Citing one paper per claim about the field | Claims about a field need grouped citations |

## Exercises

**Exercise 14.1** Take four rows of your extraction set and write one synthesis paragraph of 120–180 words that groups them, evaluates their evidence, and ends with an absence statement.

**Exercise 14.2** Have a colleague mark every sentence in that paragraph as *reports*, *groups*, *evaluates*, or *identifies absence*. Any sentence that only reports should be cut or upgraded.

**Exercise 14.3** Examine the section structure of the two most recent surveys in your area. Write down their taxonomy, then write one sentence on how yours will differ and why.

<div class="pagebreak"></div>

# Chapter 15 — The Literature Matrix

## 15.1 Purpose

The literature matrix is a table with one row per study and one column per attribute. Its purpose is to make patterns visible that no amount of reading prose can reveal, because **gaps are properties of columns, not of rows**.

This is the central mechanical insight of Part V. When you read papers one at a time, you see each study's contribution. When you tally a column across fifteen studies, you see what the *field* has and has not done. Research gaps are found by counting.

Build it in a spreadsheet, never in a word processor: you must be able to sort, filter, and count.

## 15.2 Fields

**Table 15.1 — Literature matrix fields and why each earns its place**

| Col | Field | Example | Why it earns its place |
|---|---|---|---|
| A | Citation key | `Zech2018Confounding` | Links matrix to reference manager and bibliography |
| B | Year | 2018 | Chronology; locating the frontier |
| C | Venue and indexing | *PLOS Medicine*; indexed | Weighting evidence quality; identifying target journals |
| D | Research problem | Cross-site confounding | Grouping into themes |
| E | **Dataset(s) and split protocol** | CheXpert; **random** split | **The most diagnostic column** — reveals leakage and incomparability |
| F | **Split unit** | image / patient / **institution** | Separated from E because it is the single highest-value cell |
| G | Method | DenseNet-121 + CORAL | Building your method taxonomy |
| H | Novel component | The invariance term only | Distinguishes real from claimed novelty |
| I | Baselines and count | ERM only (1) | Reveals weak-comparison papers |
| J | Metrics | Accuracy, AUC | Reveals evaluation gaps |
| K | Key results | 0.90 AUC in-domain | Comparable **only** within the same dataset and split |
| L | Seeds and variance | 1 seed, no CI | Reveals reliability gaps |
| M | Statistical test | none | Almost always empty — and that emptiness is a finding |
| N | Cost reported | no | Reveals efficiency gaps |
| O | Code available | yes / on request / no | Reproducibility; feasibility as a baseline |
| P | Strengths | Public code; three datasets | Fair credit; tells you what to emulate |
| Q | Limitations (theirs) | Frontal views only | Raw material for the gap |
| R | **Limitations (yours)** | Random split; 1 seed; no ablation | **Where gaps are actually produced** |
| S | Gap it leaves | Leakage-free re-evaluation absent | Aggregates into your gap |
| T | Future work (verbatim) | "extend to lateral views" | Author-endorsed directions |
| U | Relevance | baseline / context / discard | Prioritisation |
| V | Contradicts | P4 on calibration | Contradictions are the richest gap signal |

**A critical warning about column K.** Numbers across rows are usually **not comparable** — different datasets, splits, preprocessing, and metrics. The matrix's job is to *expose* incomparability, not to construct a leaderboard. Averaging column K across papers is a serious error that produces a meaningless number.

## 15.3 Reading the matrix by column

**Figure 15.1 — Reading a literature matrix by column rather than by row**

```
  READING BY ROW (what beginners do)
  ─────────────────────────────────────────────────────────────────
  P1: ResNet-50, CheXpert, random split, 0.89 AUC, no baseline
  P2: DenseNet, ChestX-ray14, random split, 0.90 AUC, 1 baseline
  P3: ViT, site-wise, 0.84 external, 1 baseline
  ...
  → You learn what each paper did. You find no gap.

  READING BY COLUMN (what produces gaps)
  ─────────────────────────────────────────────────────────────────
  Column F (split unit):     11/15 random at row level  ◄── FINDING
  Column I (baseline count):  9/15 have ≤1 baseline      ◄── FINDING
  Column J (metrics):        12/15 report only Acc/AUC   ◄── FINDING
  Column M (stat. test):      0/15 run any test          ◄── FINDING
  Column L (seeds):          13/15 report ≤3 seeds       ◄── FINDING
  Column N (cost):            2/15 report cost           ◄── FINDING
  Column O (code):            6/15 release none          ◄── FINDING
  → Six field-level gaps, obtained by counting. No inspiration required.
```

**Procedure for the tallies.** In your spreadsheet, add a block below the data using count formulas — for example, in a spreadsheet where column F holds the split unit and your data occupy rows 2 to 30:

```
  Total studies                  =COUNTA(A2:A30)
  Random row-level splits        =COUNTIF(F2:F30,"image")
  Grouped splits                 =COUNTA(F2:F30)-COUNTIF(F2:F30,"image")
  Studies with ≤1 baseline       =COUNTIF(I2:I30,"<=1")
  Studies reporting a test       =COUNTA(M2:M30)-COUNTIF(M2:M30,"none")
  Studies releasing code         =COUNTIF(O2:O30,"yes")
  Studies reporting metric X     =COUNTIF(J2:J30,"*ECE*")
```

Then write each tally as a sentence. **Those sentences are your gap paragraph** (Chapter 18) and, later, the evidence in your introduction's fourth paragraph (Chapter 32).

## 15.4 Worked extract

**[HYPOTHETICAL]** Papers P1–P10 are invented placeholders for teaching. They are not real works.

| Paper | Yr | Dataset + split | Split unit | Method | Baselines | Metrics | Key result | Seeds | Test | Limitation (mine) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 2022 | CheXpert, random | image | ResNet-50 | none | Acc, AUC | 0.89 AUC | 1 | none | Leakage; no comparison possible |
| P2 | 2022 | ChestX-ray14, random | image | DenseNet-121 | ResNet-50 | AUC | 0.90 AUC | 1 | none | Baseline untuned; no CI |
| P3 | 2023 | CheXpert→CXR14, site-wise | institution | ViT-B/16 | DenseNet | AUC | 0.84 external | 3 | none | One external set; no worst-site |
| P4 | 2023 | MIMIC-CXR, random | image | CNN + attention | 2 CNNs | Acc, F1 | 0.91 Acc | 1 | none | Accuracy on imbalanced multi-label |
| P5 | 2023 | CheXpert→CXR14 | institution | CORAL | ERM | AUC | +0.03 external | 3 | none | Requires site labels |
| P6 | 2024 | 3 sets, site-wise | institution | IRM | ERM, CORAL | AUC, ECE | +0.04 worst-site | 3 | none | No significance test |
| P7 | 2024 | 3 sets, site-wise | institution | Site-adversarial | 4 methods | AUC, worst-site, ECE | 0.78→0.83 | 3 | none | Site labels; no ablation on novelty |
| P8 | 2024 | Private, undisclosed | unstated | Ensemble | 1 CNN | Acc | 0.95 Acc | 1 | none | Not reproducible; discard as baseline |
| P9 | 2025 | CheXpert, random | image | Self-supervised | ERM | AUC | +0.02 | 5 | none | No external validation |
| P10 | 2025 | 2 sets, site-wise | institution | Test-time adaptation | ERM, CORAL | AUC | +0.03 | 3 | none | Latency unreported |

**Column tallies:** 5/10 random row-level splits · 4/10 ≤1 baseline · **0/10 any statistical test** · 2/10 report calibration · 3/10 report ≥5 seeds · 1/10 reports cost · 0/10 operate without site labels.

Seven candidate gaps, produced by counting. Note in particular that **0/10 ran a statistical test** — an empty column is often the most valuable finding in the matrix.

## 15.5 Common mistakes

| Mistake | Correction |
|---|---|
| Building the matrix in a word processor | Use a spreadsheet; you must sort, filter, and count |
| One column labelled "Notes" | Use specific fields; a notes column cannot be tallied |
| Averaging results across incomparable studies | Never; use the matrix to expose incomparability |
| Recording only the authors' limitations | Column R is mandatory |
| Omitting the split unit | It is the highest-value cell in the table |
| Stopping at five papers | Patterns are invisible below roughly ten |
| Never computing the tallies | The tallies *are* the point |
| Filling cells from automated extraction without checking | Verify every cell against the PDF |

## Exercises

**Exercise 15.1** Build a matrix of at least ten studies with columns A–V. Fill column F for every row.

**Exercise 15.2** Compute at least six column tallies and write each as a sentence with its count.

**Exercise 15.3** Identify every contradiction between studies (column V). Each is a candidate research question (§18.4).

**Exercise 15.4** For non-computational fields, adapt the columns: dataset → sample and population; method → intervention or analytical approach; baselines → comparison groups; metrics → measures with their validity and reliability evidence. The logic is unchanged.

<div class="pagebreak"></div>

# Chapter 16 — Literature Review Tools

## 16.1 Scope and a standing caution

**[VERIFY]** This chapter describes categories of tool and the workflows they support. Individual products change names, features, pricing, and availability frequently; some described here may have altered materially since writing. The *functional* classification is stable; the products are not. Verify current capability before relying on any of them, and prefer tools whose output you can export and audit.

**Table 16.1 — Literature tools: purpose, workflow, limitations, verification**

| Tool | Purpose | Core workflow | Limitations | Verification you owe |
|---|---|---|---|---|
| **Zotero** | Reference library, PDFs, notes, citations, BibTeX | Install with browser connector and word-processor plugin → save from publisher page → add by DOI → organise with collections and colour tags → child notes using the extraction template → export CSV or BibTeX | Free storage tier is limited; publisher metadata is frequently wrong | **Check every metadata field.** Missing pages, ALL-CAPS titles, and wrong venue names are common |
| **Mendeley** | Same role, Elsevier ecosystem | Web importer → import RIS/BibTeX from Scopus or ScienceDirect → annotate → cite in word processor | Fewer extensions than Zotero; account-bound | Same metadata verification |
| **EndNote** | Institutional standard in many groups | Groups; cite-while-you-write; journal output styles | Licence cost; style files can lag journal requirements | Check output against the journal's current guide |
| **Semantic Scholar** | Discovery, citation context, alerts, API | Search → follow influential citations → set alerts → use API for bulk screening | Metadata noise; automated summaries lossy | Never characterise findings from a summary |
| **Citation-graph tools** (Connected Papers, Litmaps, ResearchRabbit) | Sideways discovery; finding what your matrix is missing | Seed with three to five core papers → inspect prominent unread nodes → export | Coverage depends on the underlying graph; incomplete | Treat as discovery, not as evidence of completeness |
| **Elicit** | Structured extraction across many papers | Upload or search a corpus → request columns (population, method, outcome) → export table | Extraction errors; mis-attributed numbers | **Verify every cell against the PDF** |
| **Consensus** | Evidence-oriented search over papers | Ask a question → read per-paper claim summaries → open the papers | Summaries compress nuance and can invert conditionals | Read the primary source before citing |
| **NotebookLM** | Grounded question-answering over *your own* uploaded documents | Upload your PDF set → ask cross-document questions → follow citations back to your sources | Limited to what you upload; still capable of error | Verify quotations and numbers against originals |
| **Reference verification** (DOI resolver, Crossref) | Confirming a reference exists and is correct | Resolve every DOI; compare fields against the publisher record | Authority for existence, not for page numbers | Do this for **every** reference before submission |

## 16.2 A recommended concrete workflow

This is one workflow that works end to end; adapt freely.

1. **Search** in a curated index (Chapter 10). Export **RIS or BibTeX including abstracts and keywords**.
2. **Import** into Zotero. Create a collection per project.
3. **Fix metadata** on import — this is not optional; publisher exports contain errors that will surface as citation defects later.
4. **Triage** in Zotero with colour tags: red = core, yellow = context, grey = discard (§12.2).
5. **Extract** into child notes using the sixteen-field template (Chapter 13), one note per paper.
6. **Export** the collection to CSV; open in a spreadsheet; this seeds columns A–C, and partially E–J.
7. **Complete** the judgement columns (R, S, U, V) by hand. These cannot be automated.
8. **Tally** the columns (§15.3) and write the tally sentences.
9. **Chain** citations (§10.8) and use a citation-graph tool to check for prominent papers absent from your matrix.
10. **Maintain**: alerts feed new papers into the same pipeline monthly.
11. **Before submission**, resolve every DOI in your bibliography (§16.1, last row).

## 16.3 Where tool assistance is legitimate, and where it is not

| Task | Tool may | You must |
|---|---|---|
| Finding candidate papers | Suggest, rank, expand queries | Run and log the searches yourself |
| Screening | Pre-rank by relevance | Make every include/exclude decision |
| Extracting factual fields | Pre-fill datasets, metrics, baselines | Verify every cell against the PDF |
| Extracting results | Propose numbers | **Check each against the actual table** |
| Summarising for triage | Produce a gist | Read core papers properly |
| Comparing papers | Suggest dimensions | Judge which comparisons are valid |
| Identifying gaps | Suggest gap *types* to check | Supply the evidence from your own tallies |
| Producing citations | Format existing verified records | **Never** accept a reference you have not resolved |

The final row is absolute and is developed in §45.4 and §46.4: bibliographic details produced by a generative tool must be treated as unverified until resolved against the publisher record, because plausible-looking but non-existent references are a documented failure mode with severe consequences.

## 16.4 Verification checklist for Part V

- [ ] No paragraph of my review begins with an author's name.
- [ ] My review is organised by idea, with a stated taxonomy.
- [ ] Each group has a critique sentence giving a *reason*.
- [ ] I have a subsection on prior evaluation practice.
- [ ] The final paragraph states the gap.
- [ ] Absence claims are phrased as "we found no study that…", not "no work exists".
- [ ] My matrix has at least ten rows and includes the split unit for each.
- [ ] I have computed at least six column tallies and written them as sentences.
- [ ] Contradictions between studies are recorded.
- [ ] Every automated extraction has been verified against the source PDF.
- [ ] Every metadata field in my reference manager has been checked.

## Exercises

**Exercise 16.1** Set up the workflow in §16.2 end to end for ten papers. Time it. The second ten will take a third as long.

**Exercise 16.2** Have a tool extract four factual columns for three papers, then verify every cell. Record the error rate; it calibrates how much verification you owe in future.

**Exercise 16.3** Seed a citation-graph tool with your three core papers and list any prominent work absent from your matrix. Add them and re-tally.

<div class="pagebreak"></div>
