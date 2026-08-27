# PART III — LITERATURE SEARCH

<div class="partintro">

Part III turns literature searching from browsing into an instrument. Chapter 8 explains what the literature review is for and what specifically goes wrong when it is weak. Chapter 9 surveys the major databases with their strengths, limitations, and appropriate uses. Chapter 10 provides the mechanics: concept blocks, Boolean logic, field codes, portable search strings, and citation chaining.

The standard to aim for is stated once and applies throughout: **a search you cannot describe precisely enough for someone else to reproduce your result count is not a search — it is browsing.** Browsing is a legitimate way to become interested in a topic. It is not a legitimate basis for a claim that something has not been done.

</div>

<div class="pagebreak"></div>

# Chapter 8 — Why Literature Review Is Necessary

## 8.1 The eight functions of a literature review

A literature review is not a chapter you write to demonstrate diligence. It performs eight distinct functions, each of which has a direct consequence if omitted.

| # | Function | What it delivers | Consequence of omission |
|---|---|---|---|
| 1 | **Maps existing knowledge** | An accurate picture of what is settled, contested, and untested | You cannot tell whether your idea is new |
| 2 | **Prevents duplication** | Confidence that the specific question is open | Discovering mid-project that your result was published in 2023 |
| 3 | **Identifies the gap** | The evidenced absence your work addresses | "No contribution" — the most common substantive rejection |
| 4 | **Informs method selection** | Knowledge of what has been tried and what failed | Repeating a known dead end; reinventing a solved subproblem |
| 5 | **Identifies datasets and benchmarks** | The resources your field considers standard | Using a non-standard dataset, making your results incomparable |
| 6 | **Identifies evaluation conventions** | The metrics and protocols reviewers expect | Reporting metrics nobody can compare, or inappropriate ones |
| 7 | **Establishes your baselines** | The specific methods you must beat or match | "The authors omit comparison with [X]" — a standard revision demand |
| 8 | **Supplies your motivation** | Cited evidence that the problem matters | An introduction that asserts significance without support |

Functions 5, 6, and 7 are worth emphasising because beginners treat them as separable from the literature review. They are not. Your dataset, your metrics, and your baselines are all *findings of the literature review*, and discovering them late is one of the most common causes of wasted experimental effort.

## 8.2 What happens when the review is weak

**Figure 8.1 — Consequences of a weak literature review, by stage**

```
 STAGE WHERE THE WEAKNESS SURFACES        WHAT IT COSTS
 ─────────────────────────────────────    ────────────────────────────────────────
 Topic selection                          Months on a solved problem
   ↓ undetected
 Method design                            Reinventing a known technique badly;
   ↓ undetected                           missing the standard trick everyone uses
 Dataset choice                           Results incomparable to all prior work
   ↓ undetected
 Experimental design                      Wrong metric; missing the obvious baseline
   ↓ undetected
 Writing                                  Cannot articulate novelty; introduction
   ↓ undetected                           has no gap paragraph
 Submission                               DESK REJECT: "insufficient novelty"
   ↓ or survives to
 Peer review                              "The contribution over [ref] is unclear"
   ↓                                      "Comparison with [ref] is required"
                                          → major revision or rejection
   ↓ or survives to
 Post-publication                         Someone shows your result was known.
                                          The paper stops being citable.
   ↓ or, in the worst case
 Viva / defence                            "Why did you not compare with X?"
                                          — the question that cannot be answered late
```

The pattern is that the cost of a weak review **compounds with time**. A gap discovered in week two costs a week. The same gap discovered by Reviewer 2 in month nine costs a rewrite and a resubmission; discovered by an examiner, it costs far more.

## 8.3 How reviewers detect a weak review

It is useful to know the specific signals, because they are easy to eliminate once you know them.

| Signal | What the reviewer infers |
|---|---|
| All citations from the last three years | The author does not know the field's foundations |
| All citations from one research group | The author found one cluster and stopped |
| Standard method used without citing its origin | The author learned it from a blog post |
| A well-known competing method absent | Either ignorance or avoidance; both damaging |
| "Few researchers have studied this" with no evidence | The author did not search systematically |
| Related work is a list of one-sentence summaries | The author read abstracts, not papers |
| Citation count far below the venue's norm | Under-engagement with the literature |
| The dataset is unusual with no justification | The author did not learn the field's conventions |

## 8.4 How much is enough?

**This is a recommendation, and norms vary by field and venue.** As orientation for computational disciplines:

| Purpose | Papers read at some depth | Papers cited |
|---|---|---|
| Deciding on a topic | 10–20 | — |
| Defining a defensible gap | 20–40 | — |
| A conference paper | 30–60 | 25–40 |
| A journal paper | 50–100 | 35–70 |
| A systematic review | 300–1500 screened; 30–100 included | 60–150 |
| A doctoral thesis | 200–500 | 120–300 |

More useful than any number is the **saturation criterion** (§10.9): you have read enough when new searches return only papers you have already seen, and when you can predict what a new paper in the area will say before reading it.

## 8.5 Common mistakes

| Mistake | Correction |
|---|---|
| Reading only papers that support your idea | Actively seek work that would contradict or pre-empt it |
| Citing papers found through other papers' descriptions | Read the primary source; descriptions are frequently inaccurate |
| Treating the review as a one-off task | Set alerts (§10.9); your review must still be current at submission, possibly a year later |
| Reviewing only your own subfield | Adjacent fields often solved your problem under a different name |
| Ignoring older foundational work | Cite the origin of every method you use |
| Skipping the review because "the area is new" | New areas have precursors; find them |

## Exercises

**Exercise 8.1** For each of the eight functions in §8.1, write one sentence stating what your current review delivers. Any function you cannot answer is an open task.

**Exercise 8.2** Audit your current reference list against the eight signals in §8.3. Fix every one that applies.

**Exercise 8.3** Name the three most likely candidates for "the paper that already did this". Find them and read them properly. If they do not exist, record the searches that failed to find them — that record is evidence for your gap.

<div class="pagebreak"></div>

# Chapter 9 — Research Databases and Search Platforms

## 9.1 A mental model

Before the individual platforms, the important distinction:

- **Discovery engines** maximise *recall* — they find everything, including material of unknown quality. Google Scholar and Semantic Scholar are of this kind.
- **Curated indexes** maximise *precision and reproducibility* — a defined corpus, controlled metadata, powerful query syntax, and analytics. Scopus and Web of Science are of this kind, and they are also the basis of most indexing and quality claims (Chapter 51).
- **Publisher platforms** provide *full text* for one publisher's output: IEEE Xplore, ScienceDirect, SpringerLink, ACM Digital Library.
- **Open bibliographic sources** provide free, programmable metadata at scale: OpenAlex, Crossref, and similar.

A rigorous search uses at least one curated index, at least two publisher platforms relevant to your field, one discovery engine, and one preprint source — and logs each.

**[VERIFY] — an important caveat for this entire chapter.** Platform interfaces, feature names, operator support, and coverage change, sometimes annually. Every workflow below should be checked against the platform's own current help documentation on the day you search. Where this handbook and the platform disagree, the platform is correct. Coverage figures are deliberately omitted or given only as orders of magnitude for the same reason.

## 9.2 Platform-by-platform

**Table 9.1 — Research databases compared**

| Platform | Indexes | Access | Principal strength | Principal limitation |
|---|---|---|---|---|
| **Google Scholar** | Journals, conferences, preprints, theses, books, patents, some grey literature | Free | Widest recall; full-text indexing; "Cited by" | No quality control; limited field syntax; no bulk export of result sets; result counts not stable or reproducible |
| **Scopus** | Curated peer-reviewed sources | Subscription | Best query syntax and analytics; author and affiliation profiles; CiteScore | Coverage gaps for some CS conferences and books |
| **Web of Science** | Core Collection (multiple indexes including SCIE, SSCI, AHCI, ESCI) | Subscription | Strong curation; the basis of Journal Citation Reports and the Impact Factor | Narrower than Scopus in some fields; multiple editions cause confusion |
| **IEEE Xplore** | IEEE and partner journals, conferences, standards | Subscription | Essential for electrical engineering and much of CS; standards documents | Publisher-limited |
| **ACM Digital Library** | ACM journals, conferences, SIG proceedings | Subscription | Definitive for core computer science venues | Publisher-limited |
| **ScienceDirect** | Elsevier full text | Subscription | Full text of Elsevier journals | One publisher |
| **SpringerLink** | Springer/Nature journals, book series, LNCS proceedings | Subscription | Strong for LNCS conference proceedings and books | Weaker advanced query syntax |
| **PubMed / PMC** | Biomedical and life sciences | Free | **MeSH** controlled vocabulary — a genuine advantage for precision | Biomedical scope only |
| **Semantic Scholar** | Very broad, AI-enhanced metadata | Free | Machine-generated summaries, citation context, influential-citation signals, open API | Metadata noise; automated summaries are lossy |
| **OpenAlex / Crossref** | Open bibliographic metadata | Free | Programmable; excellent without a subscription | Less curation than Scopus or WoS |
| **DOAJ** | Vetted open-access journals | Free | A legitimacy signal for OA venues (Chapter 52) | Indexes journals, not articles |

### 9.2.1 Google Scholar

**When to use it.** Early exploration; finding a paper you already know of; forward citation chasing; locating accessible copies; grey literature and theses.

**Workflow.**
1. Search with quoted phrases for multiword concepts.
2. Use the left-hand panel to restrict by year; sort by relevance and then re-sort by date, because the two orderings surface different papers.
3. On a relevant paper, use **Cited by** for forward chaining, and — importantly — **search within citing articles** to filter that citing set by keyword.
4. Use **Related articles** for sideways discovery.
5. Save items to *My Library*; set up alerts for a query or for citations to a key paper.

**Limitations to respect.** Result counts are estimates and are not stable, so they must not be reported as if reproducible. Inclusion is automated, so predatory-venue material appears alongside rigorous work. There is no reliable document-type filter. Do not build a systematic review's search protocol on Scholar alone.

### 9.2.2 Scopus

**When to use it.** As your reference implementation for building a search string; for trend and venue analytics; for verifying indexing claims.

**Workflow.**
1. Advanced search with field codes, most usefully `TITLE-ABS-KEY( )`.
2. Restrict with year and document-type limits.
3. Inspect the analysis view for documents by year, source titles, authors, affiliations, and countries.
4. Refine iteratively, watching the result count change with each added concept block.
5. Export to RIS or BibTeX **including abstracts and keywords**, so your literature matrix can be partly populated from the export.

### 9.2.3 Web of Science

**When to use it.** Curated searching; citation reports; and — the distinctive function — verifying which index a journal belongs to and consulting Journal Citation Reports for the Impact Factor (Chapter 51).

**Workflow.** Field tags including `TS=` (topic), `TI=`, `AB=`, `AK=`, `SO=`, with `PY=` for the publication-year range and `DT=` for document type. The Analyze Results and Citation Report views provide the equivalent analytics to Scopus.

### 9.2.4 IEEE Xplore

**When to use it.** Electrical engineering, computer engineering, much of applied CS; and for standards, which are frequently the authoritative specification of something you are studying and are indexed nowhere else.

**Workflow.** The command-search interface accepts fielded queries with Boolean and proximity operators; fields include document title, abstract, index terms, and all metadata. Index terms are particularly useful for harvesting controlled vocabulary for your synonym table (§10.2).

### 9.2.5 ACM Digital Library

**When to use it.** Core computer science — systems, programming languages, HCI, software engineering, databases, theory. For many CS subfields the definitive venues are ACM conferences, and this is where they live.

### 9.2.6 ScienceDirect and SpringerLink

Both are primarily full-text access platforms for their respective publishers. ScienceDirect supports fielded and proximity searching, though with limits on the number of Boolean operators per field. SpringerLink's advanced syntax is comparatively limited, so it is best used to retrieve known items and to browse book series and LNCS proceedings rather than as a primary search instrument.

### 9.2.7 PubMed

**When relevant.** Any work touching health, biology, or medicine — including applied machine learning in those domains.

**The distinctive advantage** is MeSH, a curated controlled vocabulary. Searching a MeSH term retrieves papers indexed under that concept regardless of the authors' chosen wording, which solves the synonym problem that dominates searching elsewhere. If your work is biomedical, learning to use MeSH is the highest-return hour you can spend on searching.

### 9.2.8 Semantic Scholar

**When to use it.** As the strongest free substitute for a subscription index; for citation-context information; for programmatic access via its API when you want to build your own screening pipeline.

**Verification requirement.** Machine-generated summaries are convenient for triage and unreliable as evidence. Never characterise a paper's findings in your own writing on the basis of an automated summary (§13.6, §45.4).

## 9.3 Working without subscriptions

Many researchers lack Scopus or Web of Science access. A rigorous search is still achievable.

| Need | Free substitute |
|---|---|
| Curated searching | PubMed (if biomedical); Semantic Scholar; OpenAlex |
| Trend analysis | OpenAlex API aggregated by year; Semantic Scholar |
| Citation chaining | Google Scholar "Cited by"; Semantic Scholar; OpenAlex |
| Full text | Preprint servers; author copies; institutional repositories; interlibrary loan; polite email to the corresponding author |
| Venue legitimacy | DOAJ; publisher site; ISSN Portal; COPE membership (Chapter 52) |
| Bulk metadata | Crossref and OpenAlex APIs |

Two practical notes. Many national and institutional consortia provide access that researchers do not realise they have — ask your librarian before concluding you have none. And emailing an author for a copy of their own paper is normal, accepted practice with a high response rate.

## 9.4 Common mistakes

| Mistake | Correction |
|---|---|
| Using one platform only | Use at least three plus a preprint source |
| Reporting Google Scholar hit counts as reproducible | Use a curated index for reportable counts |
| Assuming a platform's absence means a paper does not exist | Coverage differs; cross-check |
| Not exporting abstracts and keywords | Re-export; you will need them for screening and for the matrix |
| Never using controlled vocabulary | Use MeSH, index terms, or author keywords to build synonyms |
| Trusting automated summaries as evidence | Read the paper before characterising it |

## Exercises

**Exercise 9.1** Determine which platforms in Table 9.1 you can actually access. Write the list down; it defines your search strategy.

**Exercise 9.2** Run the same simple query on three platforms and compare the first twenty results. The differences in coverage will be larger than you expect.

**Exercise 9.3** On one platform, locate the controlled vocabulary for your topic — MeSH terms, index terms, or author keywords — and record five terms you had not thought of.

<div class="pagebreak"></div>

# Chapter 10 — Search Strategies

## 10.1 The objective

A good search is **reproducible**, **documented**, and **calibrated** — recall high enough not to miss the paper that pre-empts you, precision high enough to be readable. The practical target for a focused review is a set of roughly **80–300 records** before screening. Substantially more means your query is too loose; substantially fewer means it is too tight or your synonyms are incomplete.

## 10.2 Step one: concept blocks and synonyms

**Procedure.** Decompose your question into three to five *concepts*. Within each concept, list every way the literature might express it. Concepts are joined by `AND`; synonyms within a concept by `OR`.

**Worked example.** *Do deep models for chest-radiograph classification generalise across hospitals, and do domain-generalisation methods help?*

| Block | Preferred term | Synonyms, variants, spellings | Narrower terms and proper nouns |
|---|---|---|---|
| **C1 Data** | chest radiograph | "chest X-ray", CXR, "thoracic radiograph", "chest radiography" | CheXpert, MIMIC-CXR, ChestX-ray14, PadChest |
| **C2 Task** | classification | detection, diagnosis, screening, "multi-label classification" | pneumonia, pneumothorax, cardiomegaly |
| **C3 Method** | "deep learning" | CNN, "convolutional neural network", transformer, "vision transformer", ViT | DenseNet, ResNet, EfficientNet, Swin |
| **C4 Phenomenon** | "domain generalisation" | "domain generalization", "domain shift", "distribution shift", "out-of-distribution", OOD, "external validation", "cross-institution", "site effect", "dataset bias" | "site-wise split", "hospital-level split" |
| **C5 Outcome** | AUC | AUROC, "area under the curve", sensitivity, specificity, calibration | "worst-group accuracy", ECE |

**Five rules that determine whether your search works:**

1. **Include both -ise and -ize spellings.** "Domain generalisation" alone loses the majority of the literature, because most is written in US spelling. This single omission is the most common cause of a catastrophically incomplete search.
2. **Include acronyms *and* their expansions.** Neither alone is sufficient; and an acronym alone is often ambiguous (§10.5).
3. **Include British and American variants** of ordinary words where relevant (behaviour/behavior, modelling/modeling).
4. **Include proper nouns** — dataset names, benchmark names, tool names. These retrieve exactly the empirical papers you need, including papers that never use your abstract vocabulary.
5. **Harvest synonyms from the literature, not from memory.** Sources: the keyword lists of five papers you already trust; index terms on publisher platforms; MeSH; the reference titles of a seed paper.

## 10.3 Step two: Boolean operators and field codes

**Table 10.1 — Boolean operators and field codes by platform**

| Function | Notation | Notes |
|---|---|---|
| Both terms | `AND` | Default on most platforms |
| Either term | `OR` | Always wrap `OR` groups in parentheses |
| Exclude | `NOT` / `AND NOT` | **Use sparingly** — see §10.5 |
| Exact phrase | `" "` | Essential for multiword concepts |
| Grouping | `( )` | Precedence differs between platforms; parenthesise everything |
| Truncation | `*` | `generali*ation`, `cluster*`. Support and semantics vary; **[VERIFY]** |
| Single character | `?` | Supported on several curated indexes; **[VERIFY]** |
| Proximity | `W/n`, `NEAR/n`, `PRE/n` | Notation is platform-specific; **[VERIFY]** |

**Field codes**, in outline. **[VERIFY] all of these against current platform documentation.**

| Platform | Typical fielded syntax |
|---|---|
| Scopus | `TITLE-ABS-KEY( )`, `TITLE( )`, `AUTHKEY( )`, `SRCTITLE( )`, `DOCTYPE( )`, `PUBYEAR` with comparison operators |
| Web of Science | `TS=` topic, `TI=` title, `AB=` abstract, `AK=` author keywords, `SO=` source, `PY=` year range, `DT=` document type |
| IEEE Xplore | Command search with named metadata fields (document title, abstract, index terms, all metadata) |
| ScienceDirect | Title-abstract-keyword field search; a cap on Boolean operators per field |
| PubMed | `[MeSH Terms]`, `[tiab]`, `[au]`, `[dp]` |
| Google Scholar | `intitle:`, `author:`, `source:`, leading `-` to exclude; a length limit on queries |

### 10.3.1 Proximity operators: the most underused tool

`AND` matches a paper in which your two concepts appear anywhere — perhaps in unrelated paragraphs. Proximity requires them to appear near each other, which usually means they are actually related.

```
  "deep learning" AND "chest radiograph"
     → matches a paper whose introduction mentions deep learning
       and whose unrelated related-work paragraph mentions chest radiographs

  "deep learning" W/5 "chest radiograph"          (Scopus notation)
  "deep learning" NEAR/5 "chest radiograph"       (Web of Science notation)
     → matches papers where the two concepts occur within five words,
       which is far more likely to indicate a genuine topical match
```

Adopting proximity operators typically improves precision dramatically at little cost in recall.

## 10.4 Step three: assembling and porting the string

**Figure 10.1 — Building a search string from concept blocks**

```
        ┌──── C1: DATA ────┐   ┌── C3: METHOD ──┐   ┌─ C4: PHENOMENON ─┐
        │ "chest X-ray*"   │   │ "deep learning"│   │ "domain          │
        │ OR "chest        │   │ OR CNN         │   │  generali*ation" │
        │    radiograph*"  │AND│ OR transformer*│AND│ OR "domain shift"│
        │ OR CXR           │   │ OR ViT         │   │ OR "out-of-      │
        │ OR CheXpert      │   │                │   │    distribution" │
        │ OR "MIMIC-CXR"   │   │                │   │ OR "external     │
        └──────────────────┘   └────────────────┘   │    validation"   │
                                                    └──────────────────┘
                                    │
                       AND  year range  AND  document type  AND  language
                                    │
                                    ▼
                      RESULT SET (target: 80–300 records)
                              │
                     ┌────────┴────────┐
                     ▼                 ▼
            too many (>500)      too few (<40)
            add a concept        drop a block;
            block; restrict      add synonyms;
            to title; tighten    check -ise/-ize;
            proximity            widen years
```

**Reference implementation (Scopus-style syntax).** Build here, then port.

```
TITLE-ABS-KEY(
   ("chest X-ray*" OR "chest radiograph*" OR CXR OR "thoracic radiograph*"
      OR CheXpert OR "MIMIC-CXR" OR "ChestX-ray14" OR PadChest)
   AND ("deep learning" OR CNN OR "convolutional neural network*"
      OR transformer* OR "vision transformer" OR ViT)
   AND ("domain generali*ation" OR "domain shift" OR "distribution shift"
      OR "out-of-distribution" OR OOD OR "external validation"
      OR "cross-institution*" OR "site effect*" OR "dataset bias")
)
AND PUBYEAR > 2021
```
…with document-type and language limits applied through the interface.

**Ported to Web of Science:**

```
TS=(("chest X-ray*" OR "chest radiograph*" OR CXR OR CheXpert OR "MIMIC-CXR")
  AND ("deep learning" OR CNN OR transformer*)
  AND ("domain generali?ation" OR "domain shift" OR "distribution shift"
      OR "out-of-distribution" OR "external validation"))
AND PY=(2022-2026)
```

**Ported to a publisher platform** (IEEE-style command search), then narrowed with the interface filters for year and content type:

```
("All Metadata":"chest X-ray" OR "All Metadata":CXR OR "All Metadata":CheXpert)
AND ("All Metadata":"deep learning" OR "All Metadata":transformer)
AND ("All Metadata":"domain shift" OR "All Metadata":"domain generalization"
     OR "All Metadata":"out-of-distribution")
```

**Simplified for Google Scholar**, which has a query-length limit and weaker field support — so use it for chaining, not as your primary protocol:

```
"chest radiograph" OR "chest x-ray" "domain shift" OR "external validation" "deep learning"
```

## 10.5 Ineffective and effective queries

**Table 10.2 — Ineffective and effective search queries**

| ❌ Ineffective | Why it fails | ✅ Effective |
|---|---|---|
| `deep learning chest x ray` | No phrases, no synonyms, no fields — enormous noisy result set | `TITLE-ABS-KEY(("chest X-ray*" OR CXR) AND "deep learning")` |
| `how can I improve generalisation of CNNs across hospitals?` | A natural-language question in a Boolean system | Concept blocks joined by `AND`/`OR` (§10.4) |
| `"domain generalisation"` | One spelling — silently loses most of the literature | `"domain generali*ation" OR "domain shift" OR "out-of-distribution"` |
| `CXR AND DL AND DG` | Ambiguous acronyms: DL is also *downlink*, *Dice loss*, *description logic* | Each acronym `OR` its expansion |
| `(A OR B) AND (C OR D) NOT COVID NOT survey NOT review` | Over-exclusion removes methodology papers and the reviews you need | Retain everything; exclude at the screening stage, where it is documented |
| `chest x-ray classification 2026` | Year typed as a keyword rather than applied as a filter | `PUBYEAR > 2021` or `PY=(2022-2026)` |
| Sorting by relevance only | Buries recent work | Sort by citations *and* separately by date |
| One database | Coverage bias; not reproducible | Three or more, each logged |

**On `NOT`.** Exclusion inside a query is invisible to your reader and frequently removes relevant work. Excluding "COVID" also removes strong methodological papers that happen to validate on a COVID subset. The principle: **retrieve broadly, exclude during screening, and report the screening funnel** — where the exclusion is visible and auditable.

## 10.6 Filters and how to use them

| Filter | Use | Caution |
|---|---|---|
| **Year** | Methods: a recent window. Foundations: no limit — you must cite origins | A recent-only window signals ignorance of the field (§8.3) |
| **Document type** | Search **reviews first** to harvest taxonomies and vocabulary, then primary studies | Excluding conference papers loses much of CS |
| **Subject area** | Removes cross-domain false positives | Can remove genuinely interdisciplinary work |
| **Source title** | Restrict to your candidate target journals to learn their conventions | Not for the main search |
| **Open access** | Only when you lack full-text access | Never a quality filter |
| **Language** | Practical necessity | If you restrict to English, **declare it as a limitation** |

## 10.7 Citation counts and how to read them honestly

Citation counts are useful and routinely misinterpreted.

- They are **age-confounded**. A 2025 paper with eight citations may be more influential than a 2018 paper with sixty. Normalise by citations per year.
- They measure **attention, not correctness**. A heavily cited paper may be heavily *criticised*; check what the citing papers actually say. Citation-context features on some platforms help here.
- They are **field-relative**. Absolute counts across disciplines are meaningless.
- They can be **inflated** by self-citation clusters and coordinated citation practices (§49.6).

Practical use: sort by citations to find the canonical works you must cite; sort by date to find the frontier you must not be scooped by. Do both, always.

## 10.8 Citation chaining

This is how you find the papers your keyword search missed — and every keyword search misses papers, because authors do not share your vocabulary.

**Figure 10.2 — Citation chaining: backward, forward, and sideways**

```
                          ┌─────────────────────┐
        BACKWARD          │                     │        FORWARD
   (older foundations)    │    YOUR SEED PAPER  │   (newer work: extensions,
                          │                     │    improvements, refutations)
   read its reference  ◄──┤                     ├──►  "Cited by", then search
   list; find the origin  │                     │     WITHIN the citing set
   of every method used   └──────────┬──────────┘
                                     │
                                SIDEWAYS
                     (parallel work that never cites your seed)
                     citation-graph tools; co-citation; shared references

   STOP when all three directions return only papers you have already seen.
```

**Procedure.** For each of your five to eight core papers:

1. **Backward** — read the reference list. Identify the origin paper for every method, dataset, and metric used. Cite origins, not only recent users.
2. **Forward** — use the "Cited by" function, then *filter within* the citing set by keyword to make a large citing list tractable. Forward chaining is how you find out whether your seed was later refuted, which is information you very much need.
3. **Sideways** — use a citation-graph tool to find prominent neighbours that share references with your seed but do not cite it. This is where independently developed parallel work hides.

## 10.9 Saturation, logging, and alerts

**The stopping rule** is saturation, not a target count: stop when new searches and all three chaining directions return only papers you have already seen, and when you can anticipate a new paper's content from its title and abstract.

**The search log.** Record this for every database, and reproduce it in your paper's method section if you are writing a review:

| Field | Example |
|---|---|
| Database | Scopus |
| Date searched | 12 March 2026 |
| Exact string | *(verbatim, including all parentheses)* |
| Filters applied | 2022–2026; article and conference paper; English |
| Records retrieved | 412 |
| After title/abstract screening | 118 |
| After full-text screening | 34 |
| Included in matrix | 15 |

The date matters because databases are updated continuously: the same string run four months later returns a different count. A review without search dates cannot be reproduced.

**Alerts.** Set a saved-search alert on your principal string in at least two systems, plus a citation alert on your two most important papers. Your literature review must still be current at submission — which may be a year after you first searched — and again at revision. This costs five minutes once and prevents the specific disaster of a reviewer pointing out a paper published while yours was under review.

## 10.10 Verification checklist for Part III

- [ ] I have three to five concept blocks with at least three synonyms each.
- [ ] Both -ise and -ize spellings are present.
- [ ] Every acronym appears with its expansion.
- [ ] Dataset and benchmark proper nouns are included.
- [ ] Synonyms were harvested from the literature, not from memory.
- [ ] I have used proximity operators where the platform supports them.
- [ ] Year is applied as a filter, not typed as a keyword.
- [ ] I have used `NOT` sparingly or not at all, and exclude at screening instead.
- [ ] My result set is between roughly 80 and 300 records.
- [ ] I searched at least three databases plus one preprint source.
- [ ] I have completed backward, forward, and sideways chaining on my core papers.
- [ ] I have reached saturation, or know how far from it I am.
- [ ] My search log records database, date, exact string, filters, and counts.
- [ ] I have set at least two alerts.
- [ ] I have exported records with abstracts and keywords into a reference manager.

## Exercises

**Exercise 10.1** Build your concept-synonym table with at least three blocks and three synonyms per block, including dataset names.

**Exercise 10.2** Compose a fielded string in Scopus or Web of Science syntax. Run it, then add one concept block at a time and record the result count at each step. Watching the count fall is how you learn to calibrate a query.

**Exercise 10.3** Port your string to two other platforms and record all three counts in your search log.

**Exercise 10.4** Pick your single most important paper. Perform all three chaining directions and record how many *new* relevant papers each direction produced. Most researchers find that chaining yields papers their keyword search missed entirely.

**Exercise 10.5** Set two alerts. Record the date you set them.

<div class="pagebreak"></div>
