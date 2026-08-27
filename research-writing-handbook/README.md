# Research Paper Writing and Research Tools
## A Complete Practical Guide from Research Idea to Journal Publication

A **261-page academic training and reference handbook** for PhD scholars, research scholars, postgraduate students, faculty members, and early-career researchers.

**Output:** `build/handbook.pdf`

---

## At a glance

| | |
|---|---|
| **Total pages** | 261 (A4) |
| **Substantive content** | **214 pages** — Chapters 1–58, pp. 21–234 |
| **Words** | **81,895** |
| **Parts / chapters** | 18 parts, 58 chapters, 540 numbered sections |
| **Figures** | 30 (text/structured diagrams) |
| **Tables** | 43 |
| **Appendices** | 16 reusable templates (pp. 235–253) |
| **References + glossary** | pp. 254–261; 60+ real works, ~70 glossary entries |
| **Exercises** | 130+, all operating on the reader's own topic |

Page accounting follows the brief: the 180–220 page target counts **substantive content only**, excluding the title page, table of contents, and appendices.

---

## Structure

| Part | Chapters | Content |
|---|---|---|
| **I** | 1–3 | What research is; research vs development vs problem solving; originality, novelty, validity, reliability, reproducibility, generalizability; seven contribution types; research types; the full lifecycle with feedback paths |
| **II** | 4–7 | Selecting an area (five constraints, field momentum); the narrowing funnel; feasibility audit with compute arithmetic; problem statements; research questions (DMBCOT); measurable objectives, hypotheses, traceability |
| **III** | 8–10 | Why the review matters and what weakness costs; 11 databases with workflows and limitations; concept blocks, Boolean logic, field codes, portable search strings, citation chaining, saturation, search logs |
| **IV** | 11–13 | Paper anatomy and what to extract per section; the three-pass reading method; a 16-field extraction framework with a full worked example |
| **V** | 14–16 | Summary vs synthesis (worked contrast on the same five papers); the synthesis phrasebook; the literature matrix and reading it by *column*; literature tools with the verification each requires |
| **VI** | 17–19 | 13-type gap taxonomy; nine detection signals; systematic derivation from matrix tallies to gap; weak vs strong gap statements; four acceptable forms of evidence; six-question stress test |
| **VII** | 20–21 | Nine kinds of novelty; why combination is not novelty; contribution statements with a four-element anatomy; calibration |
| **VIII** | 22–26 | Methodology as six layers; dataset selection, licensing, ethics; seven data-leakage pathways; preprocessing documentation; model justification; experimental design — splits, tuning parity, four baseline categories, ablations, statistics, reproducibility |
| **IX** | 27–29 | Evaluation metrics in depth (classification, regression, detection, segmentation) with formula, meaning, use, limitations, example; ROC vs PR under imbalance; results presentation and nine ways visualisations mislead; the Results/Discussion boundary |
| **X** | 30–37 | Title; abstract (seven moves, weak→improved rewrite); introduction (six-paragraph blueprint + a complete worked introduction); related work; methodology; results; discussion; conclusion |
| **XI** | 38–40 | Architecture diagrams, flowcharts, plots; four table types; algorithms, pseudocode, mathematical formulation |
| **XII** | 41–44 | Word; LaTeX and Overleaf; Zotero; Mendeley |
| **XIII** | 45–46 | AI-assisted research — functional classification, the red lines, verification protocol, disclosure; a 15-task prompt library with safeguards |
| **XIV** | 47–49 | Plagiarism (incl. the patchwriting boundary, demonstrated); similarity checking and why the percentage is the wrong target; misconduct, authorship, conflicts of interest |
| **XV** | 50–52 | Venue types and access models; journal selection criteria and metrics with their real definitions and caveats; predatory venues and a verification checklist |
| **XVI** | 53–56 | Pre-submission checklist; cover letter; peer review and its decision points; responding to reviewers, including how to disagree |
| **XVII** | 57 | **A complete case study**, end to end — search log, matrix, tallies, gap, objectives, method, results, discussion, abstract, journal choice, reviewer response — showing every artefact rather than describing it |
| **XVIII** | 58 | Nine stage-gated researcher checklists |

---

## Editorial standards applied

- **No fabricated sources.** Every reference is a real, published work. **Digital object identifiers and page ranges are deliberately omitted** where they could not be confirmed character-for-character, since inventing them is precisely the failure the handbook warns against. The References page says this explicitly and instructs the reader to resolve each work themselves.
- **Hypothetical material is labelled.** The running example (cross-hospital chest-radiograph classification), the method "CLUSTER-DG", the placeholder papers "P1"–"P15", and **every number attached to them** are marked **[HYPOTHETICAL]** and carry an explicit warning that they may not be cited. The underlying phenomenon is real and cited (Zech et al., 2018).
- **Volatile claims are flagged.** Platform features, database syntax, journal metrics, and publisher policies are marked **[VERIFY]** with the authoritative source named, because all of them change.
- **Facts are separated from recommendations.** Where a claim could be mistaken for consensus, the text says which it is.
- **No claim that AI output is "plagiarism-free."** §45.3 states the opposite and explains why, and the handbook repeatedly affirms that the researcher remains responsible for the accuracy, originality, citations, methodology, data, and results of their work.
- **Every chapter adds new material.** Cross-references are used instead of restating; for example the weak/strong related-work contrast lives in §14.4 and Chapter 33 points to it rather than repeating it.

---

## Build

Requires Node.js 18+ and a Chromium-family browser.

```bash
npm install                    # markdown-it, puppeteer-core
node make-fonts-css.js         # embeds DejaVu fonts (run once)
export CHROME_PATH=/usr/bin/google-chrome
node build.js                  # -> build/handbook.pdf, .html, .md
```

`node build.js --html-only` skips PDF rendering.

### Why the fonts are embedded

The 30 figures are structured text diagrams using box-drawing and arrow characters (U+2500 and U+2190 ranges), and the checklists use ballot boxes (U+2610). Many default system fonts — including the Noto Sans that minimal Linux images fall back to — do not cover these ranges, and the glyphs then render as empty boxes. `make-fonts-css.js` embeds DejaVu Sans and DejaVu Sans Mono as base64 `@font-face` rules so the PDF builds identically on any machine. This was a real defect caught during production, not a hypothetical one.

If you build without running `make-fonts-css.js`, `build.js` prints a warning and the diagrams will be damaged.

---

## Files

```
manual/                 18 Markdown source files, one per part
  00-front.md           title page, preface, how to use, lists of figures and tables
  01-part1.md … 16-appendices.md
  17-references.md      references and glossary
assets/print.css        A4 print stylesheet (book typography, page breaks)
assets/fonts.css        generated — embedded DejaVu faces (3.6 MB)
build.js                Markdown -> HTML -> paginated PDF, generates the TOC
make-fonts-css.js       font embedding
build/handbook.pdf      the deliverable
build/handbook.html     browsable single-file version
build/handbook.md       concatenated Markdown
```

To edit, change the Markdown and rebuild. Slides are not involved; this is a separate deliverable from the two-day workshop package.

---

## Known limitations

- **A DOCX version is not produced.** No converter (pandoc, LibreOffice) was available in the build environment. `build/handbook.md` and `build/handbook.html` both import cleanly into Word if an editable version is needed.
- **Figures are structured text, not vector graphics.** They are designed to survive plain-text and Markdown rendering. Chapter 38 recommends vector tools for the reader's *own* papers; the handbook's own diagrams are deliberately text so that they remain legible in every output format.
- **Discipline coverage is weighted toward computational research**, as the brief specified. Chapters 2, 15, 27, and 58 include explicit translations for qualitative, health, education, management, and non-CS engineering research, but a reader in those fields will still find the metric chapter the least directly applicable.
