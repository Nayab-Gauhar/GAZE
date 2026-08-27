# APPENDICES

<div class="partintro">

Sixteen reusable templates. These are intended to be copied into your own working documents and filled. Each names the chapter that explains it, so you can return to the reasoning when a field is unclear.

A machine-readable version of the literature matrix (Appendix 4) as a spreadsheet is more useful than a printed one; build it in a spreadsheet application so you can sort, filter, and count (§15.3).

</div>

<div class="pagebreak"></div>

## Appendix 1 — Research Problem Template
*(Chapter 5)*

| Block | Your text |
|---|---|
| **Context** — domain and why anyone should care; one or two sentences, with a concrete number | |
| **Current state** — what is done now and what it achieves; cited | |
| **The inadequacy** — what specifically is missing, wrong, unmeasured, or assumed; **cite the evidence** | |
| **Consequence** — what cannot currently be done, decided, or trusted | |
| **Scope** — what you will and will not address | |

**Gap marker present?** ☐ unquantified ☐ unmeasured ☐ not established ☐ unexplained ☐ it is unknown whether

**Four-part test (§5.3)**

| # | Test | Pass? | Evidence |
|---|---|---|---|
| 1 | The answer is currently unknown in the accessible literature | ☐ | |
| 2 | It can be measured or proven | ☐ | |
| 3 | A negative result would still be publishable | ☐ | |
| 4 | It matters to someone outside my institution | ☐ | |

**If my problem has the form "apply X to Y" (§5.5):**
Assumption of X violated by Y: ____________
Predicted consequence: ____________
Measurement that would detect it: ____________

<div class="pagebreak"></div>

## Appendix 2 — Research Question Template
*(Chapter 6)*

| | Question | Type (Table 6.1) |
|---|---|---|
| RQ1 | | |
| RQ2 | | |
| RQ3 | | |

**DMBCOT slots for the principal question (§6.5)**

| Slot | Content |
|---|---|
| **D** — Data: population, datasets, split unit | |
| **M** — Method: the intervention | |
| **B** — Baseline: the comparison, and its tuning budget | |
| **C** — Condition: the circumstance varied | |
| **O** — Outcome: metrics, and the decision each serves | |
| **T** — Threshold: what size of effect would matter, and why | |

**Quality check** — for each question:
☐ One relationship only ☐ Answerable by an experiment I can run ☐ Not answerable by yes/no alone ☐ Informative whichever way it resolves ☐ Claim type matches the design

**The negative-result sentence** — write the sentence that would appear in your results if the answer were *no*: ____________

<div class="pagebreak"></div>

## Appendix 3 — Research Objective Template
*(Chapter 7)*

**Aim** (exactly one sentence, "To + purpose"): ____________

| | Objective ("To + measurable verb + object + condition") | Measurable outcome | Maps to contribution |
|---|---|---|---|
| O1 | | | |
| O2 | | | |
| O3 | | | |
| O4 | | | |

**Verb check.** Acceptable: quantify, measure, compare, characterise, derive, prove, construct, annotate, validate, determine, isolate, establish. **Reject:** study, analyse, investigate, explore, understand, work on, develop a framework for, implement.

**Hypotheses (§7.3)**

| | H0 | H1 | Test | α | Correction | Effect size reported as |
|---|---|---|---|---|---|---|
| H1 | | | | | | |
| H2 | | | | | | |

Date pre-specified: ____________  *(before any test-set evaluation)*

**Traceability table (Figure 7.1)** — no cell may be empty

| Objective | Method section | Results section | Contribution |
|---|---|---|---|
| O1 | | | C1 |
| O2 | | | C2 |
| O3 | | | C3 |

**Examiner simulation:** could a colleague mark each objective *done* or *not done* without argument? ☐

<div class="pagebreak"></div>

## Appendix 4 — Literature Matrix
*(Chapter 15 — build this in a spreadsheet)*

**Columns**

| Col | Field | Col | Field |
|---|---|---|---|
| A | Citation key | L | Seeds and variance reported |
| B | Year | M | Statistical test |
| C | Venue and indexing | N | Cost reported |
| D | Research problem | O | Code available |
| E | Dataset(s) and split protocol | P | Strengths |
| F | **Split unit** | Q | Limitations (theirs) |
| G | Method | R | **Limitations (mine)** |
| H | Novel component | S | Gap it leaves |
| I | Baselines and count | T | Future work (verbatim) |
| J | Metrics | U | Relevance: core / context / discard |
| K | Key results | V | Contradicts which paper |

**Tally block** (§15.3) — adapt ranges to your sheet

| Tally | Formula |
|---|---|
| Total studies | `=COUNTA(A2:A30)` |
| Row-level random splits | `=COUNTIF(F2:F30,"image")` |
| Studies with ≤1 baseline | `=COUNTIF(I2:I30,"<=1")` |
| Studies running any test | `=COUNTA(M2:M30)-COUNTIF(M2:M30,"none")` |
| Studies releasing code | `=COUNTIF(O2:O30,"yes")` |
| Studies reporting metric X | `=COUNTIF(J2:J30,"*X*")` |

**Five tally sentences**

1. Of ___ studies, ___ use ____________
2. Of ___ studies, ___ report ____________
3. ___ of ___ compare against ____________
4. No study (0 of ___) reports ____________
5. All ___ studies assume ____________

> **Warning.** Column K is comparable only within identical dataset and split. Never average results across studies.

<div class="pagebreak"></div>

## Appendix 5 — Paper Reading Sheet
*(Chapter 13 — one per paper; save as `<CitationKey>.md`)*

| # | Field | Content |
|---|---|---|
| 1 | Citation key, venue, year, indexing; **DOI verified ☐** | |
| 2 | Research problem, in **my** words | |
| 3 | Motivation | |
| 4 | Stated objective or research question | |
| 5 | Claimed gap, and whether evidenced | |
| 6 | Dataset(s): names, versions, sizes, classes, balance, licence, **split protocol and split unit** | |
| 7 | Preprocessing; **where fitted statistics came from**; resampling before or after split | |
| 8 | Proposed method; the **novel component isolated**; stated mechanism | |
| 9 | Baselines; count; tuned equally? | |
| 10 | Metrics; appropriate to the problem? | |
| 11 | Setup: seeds, variance, test, CV, optimiser, hardware, versions, **tuning budget** | |
| 12 | Key results — from **tables**, each with its comparison point | |
| 13 | Limitations — **theirs**, verbatim with section and page | |
| 14 | Limitations — **mine** (mandatory; see headings below) | |
| 15 | Future work, verbatim | |
| 16 | Relevance: core / context / discard · contradicts ___ · possible extension for me | |

**Field 14 headings (§13.4):** fairness of comparison · statistical validity · evaluation protocol and leakage · generality · cost and deployability · reproducibility · explanation offered · anything selectively unreported

**Reading passes completed:** ☐ Pass 1 ☐ Pass 2 ☐ Pass 3

**Tool-assistance log:** fields pre-filled by a tool ____________ · verified against the PDF ☐ · corrections made ____________

<div class="pagebreak"></div>

## Appendix 6 — Research Gap Analysis Sheet
*(Chapters 17–19)*

**Step 1 — tallies:** see Appendix 4.

**Step 2 — limitations with counts and citations**

| ID | Limitation | Count (n of N) | Supporting papers | Evidence source |
|---|---|---|---|---|
| L1 | | | | |
| L2 | | | | |
| L3 | | | | |
| L4 | | | | |
| L5 | | | | |

**Step 3 — unresolved problem** (one sentence): ____________

**Step 4 — gap statement** (§19.4 template)

> "Across **[N]** studies identified through **[databases, strings, date range]**, **[pattern with counts]** holds. Consequently, **[specific quantity or mechanism]** remains **[unquantified / untested / unexplained]**, even though **[why it matters, and to whom]**. This study addresses that by **[action]**."

**Gap types (Table 17.1)** — tick all that genuinely apply, expect two or three:
☐ 1 Knowledge ☐ 2 Methodological ☐ 3 Dataset ☐ 4 Performance ☐ 5 Application ☐ 6 Population/domain ☐ 7 Evaluation ☐ 8 Scalability ☐ 9 Generalisation ☐ 10 Reproducibility ☐ 11 Efficiency ☐ 12 Explainability ☐ 13 Temporal

**Weak-gap self-check** — my statement is **none** of these (§17.2):
☐ "room for improvement" ☐ "nobody has applied X to Y" ☐ "accuracy is low" ☐ "no one has combined A and B" ☐ "topic is trending" ☐ "no work in my country/language" ☐ "prior work is old" ☐ "limited research exists" ☐ contains no numbers

**Evidence form for each absence claim (§19.5):** ☐ count from a documented search ☐ authors' own admissions ☐ documented negative search ☐ my own measurement

**Step 5 — stress test (§19.6)** — a critical reader must ask all six

| Question | My answer | Survived |
|---|---|---|
| Has this been done? Which paper is closest, and how does mine differ? | | ☐ |
| How do you know the gap is real — which count supports it? | | ☐ |
| Who benefits, outside my institution? | | ☐ |
| What is my riskiest assumption? | | ☐ |
| Can I do this with my data, compute, and time? | | ☐ |
| What would a negative result look like — and would it be publishable? | | ☐ |

<div class="pagebreak"></div>

## Appendix 7 — Research Contribution Template
*(Chapter 21)*

| | Contribution | Type | Answers which limitation | Results section supplying evidence |
|---|---|---|---|---|
| C1 | | | | |
| C2 | | | | |
| C3 | | | | |
| C4 | | | | |

**Types:** methodological · dataset/resource · experimental/empirical · theoretical · practical

**Four-element check for each (§21.3)**

| | Artefact or finding | Scope | Quantification (with uncertainty) | Significance |
|---|---|---|---|---|
| C1 | ☐ | ☐ | ☐ | ☐ |
| C2 | ☐ | ☐ | ☐ | ☐ |
| C3 | ☐ | ☐ | ☐ | ☐ |

**Novelty positioning (§20.5)**
Novelty kind (of nine): ____________
Closest prior work: ____________
The delta, in one sentence: ____________
Why the delta matters: ____________
Experiment that isolates my novel component: ____________

**Calibration (§21.6)**
☐ Every superlative is bounded by conditions actually tested
☐ One sentence states what the work does **not** address: ____________

<div class="pagebreak"></div>

## Appendix 8 — Methodology Template
*(Chapter 22, Chapter 34)*

**Six layers (§22.2)**

| Layer | Content |
|---|---|
| **Design** — study type; independent variable; what is held constant | |
| **Data** — datasets, why these, split unit, documented biases | |
| **Procedure** — preprocessing, model, training, tuning protocol | |
| **Controls** — baselines, seeds, equal budgets | |
| **Analysis** — metrics, statistical test, error analysis | |
| **Threats** — validity limits and mitigations | |

**Pipeline as a chain** — every arrow must be describable in one sentence

`raw → ______ → ______ → ______ → ______ → ______ → output → metric`

Arrows I cannot yet specify: ____________

**Design-rationale sentences (§22.5)** — one per non-obvious choice, in the form
*"We use [choice] because [property of the problem] implies [expected consequence]."*

1. ____________
2. ____________
3. ____________

**Two mandatory sentences (§34.2)**

> Leakage: *"All preprocessing statistics, resampling, and feature selection were fitted on training folds only. Splits are ______-disjoint."*
>
> Fairness: *"All methods received an identical budget of ___ trials over search spaces of comparable size, selected on validation data."*

**Attachments:** ☐ architecture diagram, vector, novel block highlighted ☐ Algorithm 1, 10–20 lines, novel lines marked, cost stated ☐ formal problem statement with every symbol defined

<div class="pagebreak"></div>

## Appendix 9 — Experimental Design Template
*(Chapter 26)*

| Element | Specification |
|---|---|
| Datasets (≥2, including the field-standard benchmark) | |
| Split scheme and **unit** | |
| Protocol comparison (what varies, what is fixed) | |
| Tuning: search space, strategy, **trial budget per method** | |
| Seeds (≥5, 10 preferred) | |
| Metrics, primary and secondary | |
| Statistical test, α, correction, effect size | |
| Cost measured (params, FLOPs, latency, memory) and hardware | |
| Test-set access policy and log location | |

**Baselines (§26.5)**

| Category | Specific baseline | Source / repository | Runs? | Equal budget? |
|---|---|---|---|---|
| Trivial | | — | — | — |
| Strong classical | | | ☐ | ☐ |
| Current state of the art | | | ☐ | ☐ |
| **Mine minus its novelty** | | — | ☐ | ☐ |
| Oracle / upper bound | | | ☐ | ☐ |

**Leakage audit (§23.3)** — record the control for each pathway

☐ ① group ☐ ② preprocessing ☐ ③ resampling ☐ ④ temporal ☐ ⑤ duplicate ☐ ⑥ target ☐ ⑦ tuning on test

**Ablation plan (§26.6)** — one factor per row

| Configuration | Component A | Component B | Component C | Metric | Δ |
|---|---|---|---|---|---|
| Baseline | – | – | – | | — |
| +A | ✔ | – | – | | |
| +A+B | ✔ | ✔ | – | | |
| Full | ✔ | ✔ | ✔ | | |
| Oracle | | | | | |

**Compute arithmetic (§4.6.1):** configs ___ × seeds ___ × datasets ___ = ___ runs × ___ h = ___ GPU-h × 3 = **___ GPU-h**

<div class="pagebreak"></div>

## Appendix 10 — Results Table Template
*(Chapters 28, 39)*

**Main comparison table**

| Method | Dataset 1 | Dataset 2 | Dataset 3 | Worst-group | Params | Latency |
|---|---|---|---|---|---|---|
| Trivial baseline | | | | | — | — |
| Strong classical | | | | | | |
| Prior SOTA [ref] | | | | | | |
| **Ours** | | | | | | |
| Oracle | | | | | | |

**Caption must state:** what the dispersion measure is (std, SEM, or CI) · the number of runs · what bold denotes · the meaning of any significance marker

**Float list before writing (§28.1)**

| | Float | Purpose | Done |
|---|---|---|---|
| Fig. 1 | System overview, novel block highlighted | | ☐ |
| Table I | Dataset statistics incl. split unit and licence | | ☐ |
| Table II | Main comparison with dispersion and significance | | ☐ |
| Fig. 2 | The key effect | | ☐ |
| Table III | Ablation, one factor per row, with oracle | | ☐ |
| Fig. 3 | Error analysis or qualitative failures | | ☐ |
| Table IV | Cost: params, FLOPs, latency, memory | | ☐ |
| Fig. 4 | Sensitivity to the principal hyperparameter | | ☐ |

**Figure audit (§28.3):** ☐ dispersion on every mean ☐ no truncated axis without annotation ☐ no dual y-axes ☐ colourblind-safe and greyscale-legible ☐ vector export ☐ ≥8 pt after scaling ☐ self-contained caption ☐ every float referenced in text

<div class="pagebreak"></div>

## Appendix 11 — Journal Selection Checklist
*(Chapters 51–52)*

**Verification sequence — never start from an email**

| # | Check | Source | J1 | J2 | J3 |
|---|---|---|---|---|---|
| 1 | Journal found on the publisher's own domain | publisher site | ☐ | ☐ | ☐ |
| 2 | Web of Science Core Collection; **which index** | Master Journal List | ☐ | ☐ | ☐ |
| 3 | **Active** Scopus coverage; CiteScore | Scopus source list | ☐ | ☐ | ☐ |
| 4 | Quartile, SJR, subject category | SCImago | ☐ | ☐ | ☐ |
| 5 | If open access: DOAJ listing | DOAJ | ☐ | ☐ | ☐ |
| 6 | ISSN belongs to this journal | ISSN Portal | ☐ | ☐ | ☐ |
| 7 | COPE membership | COPE | ☐ | ☐ | ☐ |
| 8 | Three board members verified | institutional pages | ☐ | ☐ | ☐ |
| 9 | Two recent articles read and judged | the journal | ☐ | ☐ | ☐ |
| 10 | Not a hijacked imitation | Ch. 52 | ☐ | ☐ | ☐ |

**Fit and cost**

| Item | J1 | J2 | J3 |
|---|---|---|---|
| Journal / publisher | | | |
| **Scope phrase covering my topic (quote it)** | | | |
| Papers **I cite** published here (target ≥3) | | | |
| Index (SCIE / SSCI / ESCI / Scopus only / neither) | | | |
| Quartile **with source and category** | | | |
| Article type; page and float limits | | | |
| Reported time to first decision | | | |
| APC; waiver or institutional agreement | | | |
| Access model | | | |
| Template available | | | |
| Special issue open + deadline | | | |
| **Accepted by my degree regulations** | | | |
| **Decision: TARGET / BACKUP / REJECT** | | | |

**Predatory warning signs (Table 52.1)** — one tick warrants investigation; two or more, walk away
☐ unsolicited flattering invitation ☐ publication promised in days ☐ unrecognised metric claimed ☐ indexing claim fails steps 2–3 ☐ impossibly broad scope ☐ APC undisclosed until acceptance or payable to an individual ☐ board without affiliations ☐ site imitates a known journal ☐ no DOIs or preservation policy ☐ free-email contact only ☐ errors on the homepage ☐ "review" with no substantive comments

<div class="pagebreak"></div>

## Appendix 12 — Manuscript Checklist
*(Chapter 53)*

**Content**
☐ Journal template, unmodified ☐ within page/word and float limits ☐ title, abstract, keywords final ☐ all required sections in the expected order ☐ figures vector or ≥300 dpi, fonts embedded, greyscale-legible, all referenced ☐ tables captioned per convention, all referenced, units stated ☐ equations numbered where cited, symbols defined ☐ references in journal style, sequential ☐ language checked ☐ anonymised if double-blind, including repository links

**References**
☐ every in-text citation in the list and vice versa ☐ **every DOI resolves and matches the publisher record** ☐ consistent author formats and venue abbreviations ☐ no duplicates ☐ preprints labelled as preprints ☐ retraction check on load-bearing references ☐ foundational works cited ☐ **every reference opened and read** ☐ reference count appropriate for the venue

**Declarations**
☐ ethics approval or documented non-applicability ☐ informed consent ☐ conflict of interest ☐ funding with grant numbers ☐ data availability with a persistent identifier or a justified restriction ☐ code availability ☐ AI use per venue policy ☐ author contributions (CRediT) ☐ prior presentation disclosed

**Files and system**
☐ **system-generated PDF proof-read page by page** ☐ source files ☐ supplementary material ☐ marked-up and clean versions if requested ☐ graphical abstract if required ☐ cover letter ☐ ethics documentation ☐ links tested in a private window ☐ all author details and identifiers correct ☐ corresponding email monitored for months ☐ funding entered in structured fields ☐ archived locally with the submission identifier

**Integrity**
☐ similarity report reviewed match by match ☐ patchwriting specifically checked ☐ reused figures have citation **and** permission ☐ self-overlap cited and disclosed ☐ submitting to one journal only

<div class="pagebreak"></div>

## Appendix 13 — Reviewer Response Template
*(Chapter 56)*

**Cover note to the editor**

> Dear Professor **[editor]**,
>
> Thank you for the opportunity to revise manuscript **[ID]**, *"**[title]**"*. We are grateful to the reviewers for their careful reading; the revision is substantially stronger as a result.
>
> We have addressed all **[N]** comments. The principal changes are: **(1)** ____________; **(2)** ____________; **(3)** ____________.
>
> A point-by-point response follows. New and modified text is highlighted in the marked-up manuscript; page and line numbers refer to that file. We have retained our original position on one point (**[comment ID]**) and explain our reasoning there, together with the additional material added to address the underlying concern.
>
> Sincerely, **[corresponding author]** on behalf of all authors

**Response table**

| # | Reviewer comment (verbatim, abbreviated) | Our response | Change and exact location |
|---|---|---|---|
| R1.1 | | We thank the reviewer… We agree that… | Revised §__, p. __, ll. __–__; new Table __ |
| R1.2 | | | |
| R2.1 | | | |
| R2.2 | | | |
| R3.1 | | | |

**Response patterns (§56.2–56.3)**

| Situation | Pattern |
|---|---|
| Valid criticism you can fix | Agree → what you changed → where → the new evidence |
| Request you cannot fulfil | Name the constraint factually → satisfy the underlying concern by an alternative → state the residual limitation in the paper |
| Misunderstanding | "We apologise that this was unclear" → what you clarified → where. **Never** blame the reviewer |
| Legitimate disagreement | Acknowledge → state position → give **evidence** → **concede something** |
| Conflicting reviewers | State the conflict → explain your resolution → invite the editor's guidance |
| Positive comment | "We thank the reviewer for this positive assessment." |

**Never write:** "the reviewer clearly did not read the paper" · "this comment is wrong" · "as already stated on page 4" · "this is beyond the scope" · "we have added a discussion" *(vague)*

**Tracking**
☐ waited 48 hours ☐ every comment answered ☐ precise locations throughout ☐ new text quoted where short ☐ marked-up version ☐ clean version ☐ private change log keyed to comment IDs ☐ version tagged ☐ abstract numbers updated if results changed ☐ tone reviewed by a co-author who did not draft it ☐ deadline met or extension requested in advance

<div class="pagebreak"></div>

## Appendix 14 — AI Research Prompt Library
*(Chapters 45–46)*

**The standard safety clause — append to every research prompt**

> *"Use only the information I have supplied. Do not invent references, datasets, numbers, author names, or identifiers. If something is uncertain or you do not know, say so explicitly rather than guessing. Mark any statement I will need to verify independently."*

| Task | Prompt skeleton | Verification you owe |
|---|---|---|
| **Narrowing a topic** | "I am interested in [area]. My resources are [compute, data, time, skills]. Propose five candidate research problems completable in [N months]. For each state: the specific unknown; why it matters and to whom; datasets needed; baselines required; the principal feasibility risk. Do not cite papers or claim novelty." | Run the feasibility audit yourself |
| **Search strings** | "Produce three search strings of increasing precision in [Scopus/WoS] syntax with concept blocks and field codes. Include -ise/-ize variants, acronyms with expansions, and dataset proper nouns. Explain each block. Do not cite papers." | Run and log every string yourself |
| **Understanding a method** | "Explain [method] to someone who knows [prerequisite]. State its assumptions, when it fails, and three things to check in an implementation. Distinguish established facts from your inference." | Verify against the original paper |
| **Extracting from a paper** | "Here is the full text [attach]. Fill this table using only this document: datasets, split protocol and unit, preprocessing and where statistics were fitted, baselines and tuning parity, metrics, seeds, statistical test, headline numbers with their table. **Quote the sentence or table you took each cell from.** Write NOT STATED where absent." | Check every quotation |
| **Comparing papers** | "Here are extraction tables for five papers. State which are directly comparable and which are not, and why; the dimensions on which they differ; any contradictions. Do not average or rank across different datasets or split protocols." | Judge validity yourself |
| **Literature matrix** | "Convert these extraction sheets into a table with columns [list]. Leave cells blank rather than inferring." | Verify every cell against the PDF |
| **Candidate gaps** | "Here are my matrix tallies and fifteen limitations sections. Group the limitations into themes with counts; identify which appear in a substantial share; map each to one of these gap types [list]. **Do not assert that anything is novel or unstudied.**" | Absence claims are yours to evidence |
| **Adversarial self-review** | "Act as a critical reviewer for [venue]. Here are my abstract, method, and results. List the ten strongest objections, ranked by severity, and the specific experiment or clarification that would neutralise each. Be harsh; do not praise. Identify where my claims exceed my evidence." | These become your next experiments |
| **Language editing** | "Improve clarity and grammar for [venue]. Do not change technical content, add claims, remove hedging, or strengthen any claim. List every change and why." | Read the change list; confirm hedging survived |
| **Structuring an introduction** | "Here is my gap statement, contributions, and results summary. Propose a six-paragraph outline stating each paragraph's job in one sentence. Flag any contribution with no supporting result." | Structure must match your evidence |
| **Methodology review** | "Here is my protocol. Identify any leakage pathway; any comparison where more than one factor differs; any transformation possibly fitted before splitting; any missing baseline category; whether the tuning budget is stated and equal. Give the specific fix for each." | Fix them yourself |
| **Logical consistency** | "Here are my abstract, contribution list, results, and conclusion. Check for: abstract claims unsupported by a result; contributions with no results subsection; numbers differing between sections; claim strength escalating; causal language on observational design. Report each with the two conflicting locations." | Resolve each conflict |
| **Generating code** | "Write a [language] function computing [X], with a docstring stating inputs, outputs, and edge-case behaviour, plus three unit tests covering [cases]. Explain any choice affecting the numerical result." | **Run the tests** |
| **Debugging** | "Here is my function and its unexpected output [paste code, inputs, expected, actual]. Give three hypotheses ranked by likelihood and a specific diagnostic for each. Do not rewrite the whole function." | Run the diagnostics |
| **Explaining statistics** | "Here is the output of [test] and my design. Explain what it does and does not license me to claim, whether the test suits this design, whether the assumptions are plausible, and what effect size to report. Note anything that would invalidate it." | Confirm against a statistics reference |

**Prompts never to use:** "give me ten citations with DOIs" · "write my related work" · "fill in the missing numbers" · "rewrite this so plagiarism software will not detect it" · "summarise this paper so I need not read it" *(for a core paper)*

**Disclosure statement to adapt (§45.5)**

> *"AI assistance was used for [language editing / search-query generation / code scaffolding]. All literature was independently retrieved and verified by the authors against publisher records; all experimental results were produced by the authors' own code and data. The authors are responsible for the content of the manuscript."*

<div class="pagebreak"></div>

## Appendix 15 — IEEE Paper Structure Template
*(Chapters 9, 30–37, 42)*

```
  TITLE                       8–15 words; method + problem + domain; no dead words
  AUTHORS, AFFILIATIONS, persistent identifiers
  ABSTRACT                    150–300 words; seven moves; no citations; numbers
                              matching Results exactly
  KEYWORDS                    4–8, from the journal's or a standard thesaurus

  I.   INTRODUCTION           ¶1 background and stakes
                              ¶2 current state and its inadequacy
                              ¶3 existing approaches, 2–3 grouped families
                              ¶4 limitations → GAP  ◄ the hinge; include counts
                              ¶5 proposed approach + mechanism
                              ¶6 numbered contributions + roadmap sentence

  II.  RELATED WORK           A. problem formulations, datasets, evaluation
                              B. method family 1  (+ table, + critique ¶)
                              C. method family 2  (+ table, + critique ¶)
                              D. evaluation practices in prior work   ◄ high value
                              E. synthesis: settled / contested / untested → gap

  III. METHODOLOGY            A. overview + Fig. 1 (novel block highlighted)
                              B. formal problem statement, all symbols defined
                              C. component subsections; novelty isolated
                              D. Algorithm 1 + complexity
                              E. loss / objective
                              (design-rationale "because" sentences throughout)

  IV.  EXPERIMENTAL SETUP     A. datasets + Table I (incl. SPLIT UNIT, licence)
                              B. preprocessing  ◄ include the LEAKAGE sentence
                              C. baselines + tuning ◄ include the FAIRNESS sentence
                              D. metrics + one-sentence justification each
                              E. implementation: seeds, hardware, versions

  V.   RESULTS                A. RQ1 …  B. RQ2 …  C. ablation  D. error analysis
                              E. cost
                              (point → pattern → magnitude → uncertainty;
                               no interpretation; report null findings)

  VI.  DISCUSSION             interpretation with mechanism · comparison with
                              literature incl. disagreements · implications ·
                              limitations with DIRECTION · threats to validity

  VII. CONCLUSION             problem → what you did → what was found →
                              what it means → principal limitation → next question
                              (no new evidence; no claim beyond the abstract)

  ACKNOWLEDGEMENTS
  DECLARATIONS                ethics · consent · conflicts · funding ·
                              data availability · code availability · AI use ·
                              author contributions (CRediT) · prior presentation
  REFERENCES                  numbered by first appearance; every DOI resolved
  APPENDICES / SUPPLEMENTARY  full hyperparameters · additional results ·
                              run identifiers
```

**LaTeX skeleton**

```latex
\documentclass[journal]{IEEEtran}
\usepackage{graphicx,amsmath,booktabs,siunitx,algorithm,algorithmic,hyperref}
\begin{document}
\title{...}
\author{...}
\maketitle
\begin{abstract} ... \end{abstract}
\begin{IEEEkeywords} ... \end{IEEEkeywords}
\section{Introduction} \label{sec:intro}
...
\bibliographystyle{IEEEtran}
\bibliography{refs}
\end{document}
```

> Use the publisher's class file **unmodified**. Never adjust margins or spacing to fit more text; publishers check, and it causes rejection.

<div class="pagebreak"></div>

## Appendix 16 — Research Workflow Checklist
*(the whole handbook, on one page)*

| # | Stage | Key artefact | Gate |
|---|---|---|---|
| 1 | Research area | Sub-area with a readable literature | One-breath test passes (§4.3.1) |
| 2 | Research problem | Five-block problem statement | Four-part test passes (§5.3) |
| 3 | Research questions | 2–4 typed questions with DMBCOT slots | Each answerable by an experiment you can run |
| 4 | Literature search | Search log: database, date, string, filters, counts | ≥3 databases; saturation reached (§10.9) |
| 5 | Paper reading | 16-field extraction per core paper | Split unit recorded for every paper |
| 6 | Literature matrix | ≥10 rows × 22 columns | ≥6 column tallies computed |
| 7 | Critical review | Synthesis grouped by family, ending in the gap | No paragraph begins with an author's name |
| 8 | Research gap | Evidenced gap statement, 2–3 types | Survives the six-question stress test (§19.6) |
| 9 | Objectives | Aim, O1–O4, H1–H3, C1–C4 | Traceability table complete |
| 10 | Novelty and contribution | Closest prior work named; delta stated | Every contribution has all four elements (§21.3) |
| 11 | Methodology | Six layers; pipeline fully specified | Leakage and fairness sentences written |
| 12 | Dataset | Licences, ethics route, split unit | All seven leakage pathways audited |
| 13 | Experimental design | Protocol with four baseline categories | Equal tuning budget; ≥5 seeds; test pre-specified |
| 14 | Execution | Logged runs; configs; seeds; environment | Test set touched once, with a log |
| 15 | Evaluation | Metrics justified by the decision served | Dispersion and effect sizes throughout |
| 16 | Results | 6–8 floats; null findings reported | No interpretation in Results |
| 17 | Discussion | Mechanism, reconciliation, implications | Limitations name a direction |
| 18 | Manuscript | Written in writing order | Consistency check across all sections |
| 19 | References | Verified bibliography | **Every DOI resolved** |
| 20 | Ethics | Similarity report classified; declarations | Patchwriting specifically checked |
| 21 | Journal selection | Target + 2 backups | Ten-step verification passed |
| 22 | Submission | Cover letter; system PDF proofed | One journal only |
| 23 | Peer review | — | Wait; enquire only after the stated period |
| 24 | Revision | Response table with locations | Every comment answered |
| 25 | Publication | Proofs corrected; artefacts deposited | Proofs read completely |

<div class="pagebreak"></div>
