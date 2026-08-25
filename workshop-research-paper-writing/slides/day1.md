---
marp: true
theme: workshop
paginate: true
footer: 'Day 1 · Research Paper Writing and Research Tools: From Research Idea to Journal Publication'
---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _footer: '' -->

# Research Paper Writing and Research Tools
## From Research Idea to Journal Publication

**A 2-Day Hands-On Workshop**

For PhD scholars · Research scholars · PG students · Early-career researchers

<br>

### DAY 1
Research Fundamentals · Literature Search · Literature Review · Research Gap

<!--
SPEAKER NOTES — Opening (3 min)
1. Set the contract: this is a working workshop, not a lecture series. Participants leave with a literature matrix, a defensible research gap, and a manuscript outline — artefacts, not notes.
2. Ask for a show of hands: (a) never submitted a paper, (b) submitted but rejected, (c) published 1-2, (d) published 3+. Calibrate your depth accordingly and pair novices with the experienced for activities.
3. State the honesty rule for the two days: "We will use AI tools aggressively and verify everything manually. No fabricated citations, no fabricated numbers. If you cannot defend a sentence in a viva, it does not belong in your paper."
4. Confirm laptops are open and the pre-workshop setup (institutional VPN/library login, Zotero, a Google account for Sheets, an Overleaf account) is done.
-->

---

# How to Use This Deck

<div class="cols">
<div>

#### For the facilitator
- Every section follows the same rhythm:
  **Concept → Explanation → Example → Tool → Live Demo → Exercise → Common Mistakes → Takeaway**
- <span class="tag">DEMO</span> slides = switch to a live browser/software window. A demo script is in the speaker notes.
- <span class="tag act">ACTIVITY</span> slides = stop presenting, start the timer, walk the room.
- Speaker notes contain what to *say*, what to *show*, and what to *watch out for*.

</div>
<div>

#### For the participant
- Handouts referenced on slides are in the `handouts/` folder:
  - `paper-extraction-template.md`
  - `literature-matrix-template.csv`
  - `research-gap-worksheet.md`
  - `journal-selection-checklist.md`
  - `reviewer-response-template.md`
  - `mini-proposal-template.md`
- You are expected to produce **your own artefacts** on your own topic — not to copy the worked examples.

</div>
</div>

<div class="warn">

**Worked examples in this deck are illustrative composites** built to teach structure. Bibliographic details of well-known public works (e.g. ResNet, BERT, U-Net, ViT) are used as examples of *type*; always verify any citation against the publisher record before using it in your own manuscript.

</div>

<!--
SPEAKER NOTES — (2 min)
Emphasise the last box. Participants will be tempted to copy example citations from a slide into their paper. Tell them explicitly: every reference in their own manuscript must be opened, read, and verified from the publisher's page or DOI. This is the first ethics rule of the workshop and it recurs on Day 2.
-->

---

# Two-Day Agenda

| | DAY 1 — Idea to Research Gap | DAY 2 — Gap to Published Paper |
|---|---|---|
| **09:30–11:00** | S1 Research & publication fundamentals<br>S2 Selecting a research topic | S9 Anatomy of a paper<br>S10 Title · S11 Abstract |
| **11:15–13:00** | S3 Searching for papers (demo)<br>S4 Reading papers efficiently | S12 Introduction<br>S13 Related work |
| **14:00–15:30** | S5 Literature review<br>S6 Literature matrix (demo) | S14 Methodology<br>S15 Experimental design · S16 Metrics |
| **15:45–17:30** | S7 Finding the research gap<br>S8 Objectives & contributions<br>**Day 1 activity + presentations** | S17 Results/Discussion · S18 Figures/Tables<br>S19 References · S20 AI tools · S21 Ethics<br>S22 Journals · S23 Submission · S24 Reviewers<br>S25 Case study + **final activity** |

<div class="demo">

**Continuous thread:** you pick *one* topic on Day 1 morning and carry it through all 25 sections. By 17:30 on Day 2 you have a mini research proposal ready to show your supervisor.

</div>

<!--
SPEAKER NOTES — (2 min)
Insist on the continuous thread. The single biggest failure mode of writing workshops is that participants do the exercises on toy examples and then never transfer the skill. Ask each participant to write their chosen topic on a sticky note / in the shared chat within the first hour so you can sanity-check scope early (Section 2 has a scope-narrowing clinic for exactly this).
-->

---

# Learning Outcomes

By the end of Day 2, a participant will be able to:

<div class="cols">
<div>

1. Distinguish a **research problem** from an engineering/project problem and state one in publishable form.
2. Build a **reproducible search string** and run it across Scopus, Web of Science, IEEE Xplore, ACM DL, Scholar and Semantic Scholar.
3. Read a paper in **three passes** and extract 14 structured fields.
4. Build and interpret a **literature matrix** over 10–15 papers.
5. Identify and *justify* a **research gap** using a named gap taxonomy.
6. Convert a gap into **RQs → objectives → hypotheses → contributions**.

</div>
<div>

7. Write each section of an **IEEE-style manuscript** to a checklist.
8. Design an experiment with **baselines, ablations and reproducibility controls**.
9. Choose **evaluation metrics** that match the problem, not the convenience.
10. Manage references in **Zotero/BibTeX/Overleaf** with zero citation errors.
11. Use **AI tools productively and defensibly**, with an explicit verification protocol.
12. Select a **legitimate target journal** and respond to reviewers professionally.

</div>
</div>

<!--
SPEAKER NOTES — (2 min)
Read outcomes 5, 9 and 11 aloud — these are the three where PhD scholars most often lose reviewers. Tell participants you will return to this list at the end of Day 2 as a self-assessment.
-->

---

<!-- _class: lead -->

# Section 1
## Introduction to Research and Publication

*What research is, what it is not, and the full path from idea to publication*

---

# What Is Research?

**Research is a systematic, documented, and critically evaluated inquiry that produces knowledge which did not exist in the accessible record before, and which others can verify.**

<div class="cols">
<div>

#### Four non-negotiable properties
| Property | Test question |
|---|---|
| **Systematic** | Could someone repeat your procedure from your description alone? |
| **Novel** | What is now known that was not known (or not *shown*) before? |
| **Evidenced** | What evidence supports each claim, and how strong is it? |
| **Communicated** | Is it in the permanent, citable, peer-reviewed record? |

</div>
<div>

#### The three questions every reviewer asks
1. **What is new?** (novelty)
2. **Why should I care?** (significance)
3. **Why should I believe you?** (validity)

<div class="warn">

If you cannot answer all three in **two sentences each**, you do not yet have a paper — you have an activity.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (4 min)
Do not lecture the definition; interrogate it. Ask: "I trained ResNet-50 on a public chest X-ray dataset and got 94% accuracy. Is that research?" Let them argue. Guide to: it is systematic and evidenced but not novel — the same result exists in dozens of papers — and it produces no new knowledge. Then ask what minimal change would make it research: e.g. showing that the reported 94% collapses to 71% under a hospital-level (site-wise) split, i.e. that prior evaluation protocols leaked site information. That flips a reproduction into a contribution about evaluation validity.
Write the three reviewer questions on the whiteboard and leave them there for two days.
-->

---

# Research vs Project Development

| Dimension | Project / Development | Research |
|---|---|---|
| **Goal** | Deliver a working artefact | Produce verifiable new knowledge |
| **Success criterion** | It works, on time, to spec | Claim is novel, significant, and validated |
| **Question form** | "How do I build X?" | "Under what conditions does X hold, and why?" |
| **Comparison** | Against requirements | Against **baselines and state of the art** |
| **Evaluation** | Testing / user acceptance | Controlled experiments, statistics, ablations |
| **Failure** | Bug to be fixed | **Finding** to be reported and explained |
| **Reuse of others' work** | Encouraged and sufficient | Necessary but insufficient — must be *exceeded* |
| **Output** | Software, report, demo | Paper, thesis, dataset, theorem, protocol |

<div class="demo">

**Overlap is normal.** Most CS research *contains* a project. The project is the instrument; the knowledge claim is the product. A paper that reports only the instrument is a technical report, not a research paper.

</div>

<!--
SPEAKER NOTES — (4 min)
This slide prevents 60% of the rejections in this audience. Many PhD scholars in CS have built impressive systems and cannot understand why reviewers say "no contribution".
Analogy to use: the telescope vs the discovery. Galileo's telescope was the project; "Jupiter has moons" was the research. Reviewers cite the discovery, not the lens grinder.
Ask two volunteers to describe their work in one sentence, then classify it live as project/research and, if project, ask "what knowledge claim could this instrument support?"
-->

---

# Research Problem vs Project Problem

<div class="cols">
<div>

<div class="bad">

#### ❌ Project problem
"Our college needs a web system to detect plagiarism in student assignments."

- Bounded by *local* need
- Solved by integrating existing tools
- Success = deployment
- Generalisation irrelevant
- No baseline comparison required

</div>

<div class="bad">

#### ❌ Project problem dressed as research
"Design and implementation of a CNN-based plant disease detection system using transfer learning."

*Why it fails:* every verb is engineering. Nothing is unknown.

</div>

</div>
<div>

<div class="good">

#### ✅ Research problem
"Transformer-based plagiarism detectors are reported at >0.90 F1 on English benchmarks, but their behaviour on **code-mixed Hindi–English** student text is unmeasured; character-level obfuscation is hypothesised to degrade them disproportionately."

- Names a **specific unknown**
- Implies a **measurable** study
- Implies **baselines** (existing detectors)
- Result is informative **whichever way it goes**

</div>

#### The 4-part test for a research problem
1. Is the answer **currently unknown** in the literature?
2. Can it be **measured or proven**?
3. Would a **negative result still be publishable**?
4. Does it matter to someone **outside your institution**?

</div>
</div>

<!--
SPEAKER NOTES — (5 min)
Point 3 is the sharpest diagnostic and the least known. If the only publishable outcome is "my method wins", the study is engineering advocacy. If both outcomes teach the field something, it is science.
Common objection from participants: "But everybody publishes 'we applied CNN to X'." Response: such papers exist mostly in low-quality venues, are rarely cited, and increasingly get desk-rejected at Q1/Q2 journals. Be honest that these papers get published — and that they do not build a career or survive a viva.
-->

---

# From Problem to Hypothesis: The Five Statements

<div class="flow">
RESEARCH PROBLEM  →  RESEARCH QUESTION  →  OBJECTIVE  →  HYPOTHESIS  →  CONTRIBUTION
   (the unknown)       (interrogative)      (actionable)   (falsifiable)    (the claim)
</div>

| Statement | Function | Grammatical form | Worked example (code-mixed plagiarism detection) |
|---|---|---|---|
| **Problem** | Names the unknown + why it matters | Declarative, with a gap marker | "Detector robustness on code-mixed text is unquantified, so institutions in multilingual settings cannot trust off-the-shelf tools." |
| **Question** | Makes the unknown answerable | Interrogative, one variable pair | "**RQ1:** How much does F1 of SBERT-based detection drop from monolingual to code-mixed paraphrase, and does script normalisation recover it?" |
| **Objective** | Commits to work | "To + verb + object + condition" | "To quantify F1 degradation of three detectors on a 4,000-pair code-mixed benchmark under four obfuscation levels." |
| **Hypothesis** | Predicts, and can be wrong | H0 / H1 with a measurable effect | "**H1:** Transliteration-normalised embeddings improve F1 by ≥0.05 over raw code-mixed input (paired, α=0.05)." |
| **Contribution** | What the field gains | Noun phrase, calibrated | "A public code-mixed paraphrase benchmark and the first quantification of script-induced degradation in SBERT detectors." |

<!--
SPEAKER NOTES — (5 min)
Stress the grammar. Objectives that begin with "Study of…", "Analysis of…", "Implementation of…" are not objectives — they are titles of activities with no completion criterion. Every objective must start with "To" + a verb whose completion is observable: quantify, compare, derive, prove, characterise, construct, validate.
Note that not every discipline uses formal hypotheses (much of CS/ML does not state H0/H1 explicitly), but every paper has an implicit predictive claim, and being able to write it as H0/H1 exposes whether the experiment can actually test it. Section 8 drills this.
-->

---

# Methodology and Contribution

<div class="cols">
<div>

## Research methodology
Not "the tools I used". It is the **defensible logic** connecting your question to your evidence.

| Layer | Question it answers |
|---|---|
| **Design** | Comparative? Ablative? Observational? Proof-based? |
| **Data** | Which datasets, why those, what splits, what biases |
| **Procedure** | Preprocessing, model, training, tuning protocol |
| **Controls** | Baselines, seeds, fixed budgets, blinding |
| **Analysis** | Metrics, statistical tests, error analysis |
| **Threats** | Validity limits and how you mitigate them |

<div class="warn">

"Methodology = Python + TensorFlow + Colab" is an *environment*, not a methodology.

</div>

</div>
<div>

## Research contribution
The **transferable** thing the field keeps after your paper.

| Contribution type | Example |
|---|---|
| **New method** | A loss function that handles label noise |
| **New theory/analysis** | Convergence bound for that loss |
| **New empirical knowledge** | Site-wise splits cut reported AUC by 0.18 across 6 published models |
| **New resource** | An annotated code-mixed benchmark |
| **New evaluation** | A protocol that detects shortcut learning |
| **Synthesis** | A systematic review that reconciles contradictory findings |
| **Reproduction/refutation** | Failure to reproduce a headline result, with diagnosis |

</div>
</div>

<!--
SPEAKER NOTES — (4 min)
Ask participants to name their contribution type out loud. Most will say "new method" by reflex; in practice, the strongest early-career papers are often "new empirical knowledge", "new resource" or "new evaluation" because they are achievable within one PhD year and are hard for reviewers to dispute.
Warn about contribution inflation: claiming "novel architecture" for a concatenation of two existing blocks. Reviewers who know the field will find the precedent, and the credibility cost contaminates the whole paper.
-->

---

# Types of Research

<div class="cols3">
<div>

### Experimental vs theoretical
| | |
|---|---|
| **Experimental** | Manipulate variables, measure outcomes. *Most ML papers.* |
| **Theoretical** | Derive results from assumptions; proofs, bounds, complexity. |
| **Computational/simulation** | Study systems too costly to build physically. |
| **Observational/empirical** | Measure what exists without intervening (mining 10k GitHub repos). |

</div>
<div>

### Applied vs fundamental
| | |
|---|---|
| **Fundamental (basic)** | Understand a phenomenon. *Why do transformers generalise despite overparameterisation?* |
| **Applied** | Solve a specified practical problem. *Detect diabetic retinopathy on low-cost fundus cameras.* |
| **Translational** | Bridge the two; deployment constraints become research variables. |

</div>
<div>

### Quantitative vs qualitative
| | |
|---|---|
| **Quantitative** | Numbers, statistics, generalisation. *Accuracy across 5 seeds.* |
| **Qualitative** | Meaning, mechanism, experience. *Interviews with 12 radiologists on trust in AI output.* |
| **Mixed methods** | Both, deliberately integrated. Strong for HCI/SE/health-AI. |

</div>
</div>

<div class="demo">

**Why this classification matters practically:** it determines your **validity threats**, your **sample-size logic**, your **reporting standards** (e.g. CONSORT-AI for clinical trials, PRISMA for systematic reviews, ACM/IEEE artefact badging for systems), and often your **target venue**.

</div>

<!--
SPEAKER NOTES — (4 min)
For non-CS participants in the room (management, education, life sciences), highlight the qualitative column and say explicitly that everything in Day 2 about structure, gaps, and reviewer response applies to them; only the metrics section (S16) is discipline-specific, and you will give them an alternative during that slot (validity, reliability, inter-rater agreement, saturation).
Concrete example of mixed methods to mention: a model achieves higher accuracy but clinicians reject it — the quantitative result alone would have been misleading.
-->

---

# What Is a Research Paper?

**A research paper is an argument, supported by evidence, formatted as a permanent citable record.**

<div class="cols-3-2">
<div>

#### The argument skeleton hiding in every paper
<div class="flow">
Something matters              → Introduction ¶1
It is not solved / not known   → Introduction ¶2-3
Prior work falls short because → Related work
So we did this, carefully      → Methodology
Here is what we observed       → Results
Here is what it means, and its → Discussion
   limits
Therefore this is now known    → Conclusion
</div>

Every section exists to defend one link in that chain. If a paragraph defends no link, delete it.

</div>
<div>

#### Not research papers
- Technical report / white paper
- Project report / thesis chapter (until reworked)
- Tutorial or blog post
- Extended abstract or poster
- Preprint (a *stage*, not peer review)
- Patent (protection, not knowledge claim)

<div class="warn">

A preprint on arXiv establishes **priority and visibility**, not peer-reviewed status. Most journals allow it; **always check the specific journal's preprint policy** before posting.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (3 min)
Say the sentence "a paper is an argument" twice. Participants trained in engineering treat the paper as a report of activities in chronological order. That produces the classic unpublishable structure: "first we collected data, then we tried SVM, then we tried CNN, then we tried CNN+LSTM and it was better."
On preprints: mention that policies differ by publisher and that a small number of venues still treat preprints as prior publication; the safe move is to read the specific journal's policy page and screenshot it for your records.
-->

---

# Conference Paper vs Journal Paper

| Dimension | Conference paper | Journal paper |
|---|---|---|
| **Review** | Single round, fixed deadline, PC-based | Multiple rounds, rolling, editor + referees |
| **Decision** | Accept / reject (sometimes minor revision) | Major/minor revision cycles; can iterate for months |
| **Turnaround** | 2–4 months to decision, fixed presentation date | 3–12+ months to first decision |
| **Length** | 6–10 pages, hard page limit | 8–35 pages, often flexible + appendices |
| **Depth expected** | A crisp new idea, adequate validation | Complete study: exhaustive baselines, ablations, statistics, related work |
| **Prestige in CS/AI** | **Very high** — NeurIPS/ICML/ICLR/CVPR/ACL/AAAI often outrank journals | High — required in most non-CS fields and by many PhD regulations |
| **Extension** | Often extended into a journal version (typically **≥30% new material**; check policy) | Usually terminal |
| **Cost/effort** | Registration + travel; camera-ready fast | APC may apply; sustained revision effort |

<div class="warn">

**Check your university's PhD regulations first.** Many Indian and European universities require *N* SCI/SCIE- or Scopus-indexed **journal** papers regardless of how strong your conference record is. Plan the mix deliberately.

</div>

<!--
SPEAKER NOTES — (4 min)
This is one of the highest-value slides for early-career CS researchers, who often receive contradictory advice. Clarify: in CS/AI the top conferences are the primary archival venue; in nearly every other discipline the journal is. Your publication strategy must satisfy both the field norm and your degree regulation.
On extension: warn about self-plagiarism/duplicate publication. An extended journal version must cite the conference paper explicitly, state what is new, and comply with both venues' policies. This connects forward to S21.
-->

---

# Research Paper vs Review vs Survey

| | **Primary research paper** | **Review paper** | **Survey / Systematic review** |
|---|---|---|---|
| **Unit of study** | Data, systems, subjects | Published literature | Published literature, with a protocol |
| **New experiments?** | Yes | Usually no | No (but may include meta-analysis) |
| **Contribution** | New result | Interpretation, taxonomy, agenda | Reproducible synthesis of evidence |
| **Method section** | Datasets, models, protocol | Selection rationale | **Explicit protocol**: databases, strings, dates, inclusion/exclusion, PRISMA flow, quality appraisal |
| **Typical length** | 8–15 pages | 15–30 | 20–60 |
| **Who should write it** | Anyone with a result | Usually experienced researchers, often invited | A team; suitable for a **first** PhD paper if done rigorously |
| **Risk** | Reviewer disputes validity | "Just a list of papers" → reject | Protocol not reproducible → reject |

<div class="good">

**A rigorous systematic review is an excellent first publication:** it forces mastery of the literature, produces your literature matrix *and* your research gap as by-products, and is citable for years. Follow **PRISMA 2020** (Page et al., *BMJ*, 2021) or **Kitchenham's guidelines** for software engineering.

</div>

<!--
SPEAKER NOTES — (4 min)
Sell the systematic review honestly: it is more work than participants expect (typically 400–1,500 records screened) but it converts Day 1 of this workshop directly into a publication. Point out that the literature matrix they build this afternoon is literally the data extraction table of a systematic review.
Warn against the failure mode: a "survey" that is 40 paragraphs of "Author A did X. Author B did Y." with no taxonomy, no comparison table, no synthesis. Section 5 addresses this directly.
-->

---

# The Journal Publication Lifecycle

<div class="flow">
 SUBMIT ──► EDITORIAL / TECHNICAL CHECK ──► DESK REJECT (scope, format, similarity, English)
                     │
                     ▼
            EDITOR ASSIGNS ASSOCIATE EDITOR ──► finds 2–4 referees  (this stage can silently take weeks)
                     │
                     ▼
              PEER REVIEW ──► FIRST DECISION
                     │
     ┌───────────────┼───────────────┬──────────────────┐
     ▼               ▼               ▼                  ▼
  REJECT      MAJOR REVISION   MINOR REVISION      ACCEPT (rare on round 1)
     │               │               │
     │               ▼               ▼
     │        REVISE + RESPONSE LETTER ──► RE-REVIEW ──► (loop 1–3 times)
     ▼                                          │
 REFRAME &                                      ▼
 RESUBMIT ELSEWHERE                          ACCEPT ──► PROOFS ──► EARLY ACCESS ──► ISSUE ──► DOI, INDEXING
</div>

| Stage | Typical duration | What you control |
|---|---|---|
| Desk check | 3 days – 3 weeks | Scope fit, formatting, similarity report, language quality |
| Under review | 1 – 6 months | Nothing — but you may send a polite status query after the journal's stated period |
| Revision | You are given 30–90 days | Response quality; ask for an extension *before* the deadline |
| Production | 2 – 8 weeks | Proof accuracy (this is your **last** chance to fix errors) |

<!--
SPEAKER NOTES — (5 min)
Make the emotional point once, plainly: rejection is the modal outcome at good venues, and "major revision" is a success. Give a realistic number — many Q1 journals accept 10–25% of submissions.
Practical tips to say aloud: (1) desk rejection is usually preventable and usually about scope or formatting — it is the cheapest failure to eliminate; (2) never resubmit a rejected paper to another journal on the same day — first fix what the reviewers exposed; (3) keep every version, every review, and every response letter in a dated folder, because you will reuse them.
-->

---

# The Complete Research Workflow

<div class="flow">
  ┌─ DAY 1 of this workshop ───────────────────────────────────────────────────────┐
  │  RESEARCH AREA → RESEARCH PROBLEM → LITERATURE SEARCH → LITERATURE REVIEW      │
  │        → RESEARCH GAP → OBJECTIVES                                             │
  └────────────────────────────────────────────────────────────────────────────────┘
                                    │
  ┌─ DAY 2 of this workshop ────────▼──────────────────────────────────────────────┐
  │  METHODOLOGY → EXPERIMENT → RESULTS → DISCUSSION → CONCLUSION                  │
  │        → MANUSCRIPT → JOURNAL SELECTION → SUBMISSION → REVIEW → REVISION       │
  │        → PUBLICATION                                                           │
  └────────────────────────────────────────────────────────────────────────────────┘

  Feedback edges the linear diagram hides (and reviewers punish you for ignoring):
   • Gap not defensible ................ go back to LITERATURE SEARCH
   • Results contradict hypothesis ..... go back to METHODOLOGY (not to the data)
   • Reviewer finds missing baseline ... go back to EXPERIMENT
   • Scope mismatch at desk check ...... go back to JOURNAL SELECTION
</div>

| Phase | Realistic time for a first paper | Where beginners under-invest |
|---|---|---|
| Area → gap (Day 1 skills) | **4–10 weeks** | Almost always rushed — the root cause of later rejection |
| Method → experiments | 8–20 weeks | Baselines and ablations skipped |
| Writing → submission | 3–6 weeks | Abstract, related work, response letter |
| Review → publication | 3–12 months | Emotional preparation |

<!--
SPEAKER NOTES — (4 min)
Draw attention to the time table. The single most common structural mistake is spending 90% of effort on model building and 5% on the gap; the gap is what determines whether the model work was worth doing at all.
Emphasise the feedback edge "results contradict hypothesis → go back to methodology, NOT to the data". Going back to the data to make the hypothesis true is p-hacking / data dredging, and if it involves changing numbers it is falsification. Flag that S21 covers this as misconduct.
-->

---

# Section 1 — Wrap-Up

<div class="cols">
<div>

#### Common mistakes
- Calling an implementation a contribution
- Writing objectives as activity titles ("Study of…")
- Choosing a venue after writing, not before
- Treating the workflow as strictly linear
- Believing a preprint is peer reviewed
- Extending a conference paper without disclosing it

#### Recommended tools for this stage
| Tool | Purpose |
|---|---|
| Zotero / Mendeley | Reference library from day one |
| Notion / Obsidian / OneNote | Research journal, decision log |
| Overleaf | LaTeX manuscript + version history |
| Git + GitHub | Code, data scripts, artefact release |

</div>
<div>

<span class="tag act">ACTIVITY 1.1 — 10 min</span>
**"Project or research?"**

1. Write your current work in **one sentence**.
2. Classify it: project / research / unclear.
3. If project or unclear, write the knowledge claim it could support:
   *"We do not currently know whether ______ , and this study would show it."*
4. Swap with a neighbour. The neighbour applies the 4-part test and marks each item pass/fail.

<div class="good">

**Takeaway:** A paper is not a record of what you built. It is a defended claim about what is now known — and the claim must be chosen before the building starts.

</div>

</div>
</div>

<!--
SPEAKER NOTES — Activity facilitation (10 min + 5 min debrief)
Walk the room. Typical rescues you will perform:
• "I built a chatbot for our library" → "Do retrieval-augmented answers reduce hallucination on domain-specific queries compared to a fine-tuned baseline, and at what latency cost?"
• "I am applying YOLOv8 to helmet detection" → "Does detection performance degrade on low-light and occluded conditions in Indian traffic imagery, and does a lightweight enhancement front-end recover it within an edge compute budget?"
Collect 3 sentences for public debrief — choose one strong, one weak, one borderline. Do not embarrass anyone; ask permission first.
-->

---

<!-- _class: lead -->

# Section 2
## How to Select a Research Topic

*From a broad area to a problem you can finish, defend, and publish*

---

# The Narrowing Funnel

<div class="flow">
BROAD AREA          Artificial Intelligence / Machine Learning
     │              (thousands of papers per week — unmanageable)
     ▼
SUB-AREA            Medical image analysis with deep learning
     │              (still ~10,000 papers/year)
     ▼
NARROW SUB-AREA     Domain generalisation in chest X-ray classification
     │              (a readable literature: ~100–300 papers)
     ▼
SPECIFIC PROBLEM    Published CXR models degrade across hospitals, and current
     │              benchmarks hide this by using random rather than site-wise splits
     ▼
RESEARCH QUESTION   RQ1 How large is the drop under site-wise evaluation across
     │              published architectures?  RQ2 Does site-adversarial training
     │              recover it without loss of in-domain AUC?
     ▼
RESEARCH OBJECTIVE  To re-evaluate five published CXR models under site-wise splits on
                    three public datasets and quantify the recovery from site-adversarial
                    training, measured by AUC, ECE, and worst-site AUC.
</div>

<div class="demo">

**Test of adequate narrowing:** you can name the **datasets**, the **baselines**, and the **metrics** in one breath. If you cannot, you are still one level too broad.

</div>

<!--
SPEAKER NOTES — (5 min)
Walk down the funnel live on the board with a topic supplied by a participant, not with this prepared example. Do it twice with two volunteers. The audience learns the move by watching the transformation, not by reading the finished funnel.
Give the readability arithmetic: at 200 relevant papers and 30 minutes per first-pass read, that is 100 hours — a semester of part-time reading. At 5,000 papers, the topic is not a topic. This makes "too broad" concrete rather than aesthetic.
-->

---

# How to Select a Research Area

Choose at the intersection of **five** constraints — not on interest alone.

| Constraint | Question to answer honestly | Failure if ignored |
|---|---|---|
| **Personal endurance** | Can I read this literature for 3–5 years without resentment? | Abandonment at year 2 |
| **Supervisor capability** | Can my supervisor actually critique my technical work here? | Unsupervised drift, weak papers |
| **Local resources** | Do I have the data, GPUs, subjects, licences, ethics approval? | Stalled experiments |
| **Field momentum** | Is publication volume rising, flat, or collapsing? | Working in a dead area, or in a saturated hype peak |
| **Career market** | Do jobs/funding calls name this area? | Employability mismatch |

<div class="cols">
<div>

#### Momentum check (10 minutes, do it now)
1. Scopus → search area keywords → **Analyze search results** → *Documents by year*.
2. Rising and not yet vertical = good entry point.
3. Vertical (e.g. "LLM agents" 2023–2026) = high visibility, brutal competition, fast obsolescence.
4. Flat/declining = easier novelty, fewer readers, harder to publish in high-IF venues.

</div>
<div>

#### Where competitive novelty actually lives
- **Intersections**: your area × another field's constraint (privacy, low-resource languages, edge compute, clinical workflow, agriculture, regional data)
- **Neglected populations/domains** in an otherwise mature area
- **Evaluation and reproducibility** of hyped methods
- **Efficiency** frontiers of large models
- Anywhere a paper says *"we leave this to future work"*

</div>
</div>

<!--
SPEAKER NOTES — (5 min)
Be blunt about supervisor capability; participants rarely hear it said. If the supervisor cannot critique the work, the student must build an external critique network: reading groups, arXiv-sanity style alerts, conference reviewing, Discord/Slack research communities, and — most effective — emailing authors of papers they read.
On hype: acknowledge that LLM/agent work maximises visibility and risk. A defensible strategy for a PhD is one hype-adjacent paper for visibility plus a durable core contribution that will still be citable in five years.
-->

---

# Identifying Emerging Topics and Unresolved Problems

<div class="cols">
<div>

#### Emerging-topic radar <span class="tag tool">TOOLS</span>
| Source | What to look at | Cadence |
|---|---|---|
| **arXiv** (cs.LG, cs.CV, cs.CL) | New listings; set Google Alerts on key phrases | Weekly |
| **Semantic Scholar** | Feeds, "Highly Influential Citations", citation velocity | Weekly |
| **Connected Papers** | Graph around a seed paper: *Prior / Derivative* works | Per topic |
| **Litmaps / ResearchRabbit** | Auto-updating literature maps with alerts | Monthly |
| **Scopus / WoS** | Documents-by-year trend; top source titles; author networks | Per topic |
| **Journal CFPs** | **Special issue calls = editors publicly declaring gaps** | Monthly |
| **Workshop titles** at NeurIPS/CVPR/ACL | The field's 12-month agenda | Yearly |
| **Benchmark leaderboards** (Papers with Code, OpenML) | Where progress has *stalled* | Per topic |

</div>
<div>

#### Six places unresolved problems are stated *explicitly*
1. **"Limitations"** section of recent papers
2. **"Future work"** in conclusions
3. **Reviewer-visible weaknesses** on OpenReview (ICLR/NeurIPS) — free access to expert criticism
4. **Rebuttals**: what authors admitted they could not do
5. **Survey papers**: their "open challenges" section
6. **Reproducibility reports** (ML Reproducibility Challenge, ReScience)

<div class="good">

**OpenReview is the most underused resource in this list.** Read the reviews of accepted *and rejected* papers in your area: you learn the field's actual standards of evidence, in the field's own words.

</div>

</div>
</div>

<!--
SPEAKER NOTES — DEMO (8 min)
Live demo sequence:
1. Papers with Code (or a current leaderboard for a benchmark in your area): show a metric curve that has flattened — say "this flattening is a research opportunity: either progress is genuinely saturating, or the benchmark has stopped measuring what matters."
2. OpenReview: open a recent accepted paper in the participants' area, expand the reviews, and read one weakness aloud. Then say: "That sentence, written by an expert, is a candidate research gap with a free peer endorsement."
3. Connected Papers: paste one seed DOI, show the graph, point out the Prior Works and Derivative Works tabs.
Have static screenshots in reserve in case of network/paywall failure. Note out loud which of these resources need institutional access (Scopus, WoS) and which are free (arXiv, Semantic Scholar, OpenReview, Connected Papers basic, Papers with Code).
-->

---

# Mining Limitations From Papers Into Topics

<div class="cols-3-2">
<div>

#### Procedure (repeat over 10–15 recent papers)
1. Open the paper's **Limitations**, **Threats to validity**, **Discussion** and **Conclusion/Future work**.
2. Copy each admitted weakness into a spreadsheet **verbatim**, with paper + section + page.
3. Tag it: `data` / `method` / `evaluation` / `scale` / `generality` / `explainability` / `efficiency` / `ethics`.
4. **Count tags across papers.** A weakness admitted by 6 of 15 papers is a *field-level* gap, not one author's excuse.
5. For each recurring weakness ask: *is it unsolved, or solved elsewhere and simply not applied here?*
   - Unsolved → potential **novel contribution**
   - Solved elsewhere → potential **transfer/application contribution** (still publishable; be honest about the framing)

</div>
<div>

#### Worked mining example
> "Our evaluation is limited to English; performance on morphologically rich languages remains unexplored." — *typical NLP paper*

| Reading | Resulting topic |
|---|---|
| Naïve | "Apply the method to Hindi" (weak: pure application) |
| Sharp | "**Which** property of the method breaks on morphologically rich languages — the tokeniser, the positional scheme, or the pretraining corpus? Isolate it by ablation across 4 language families." |

<div class="warn">

Do not stop at *"apply X to Y"*. Ask **why** X would fail on Y, then measure that mechanism. Mechanism turns application into science.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (5 min)
This slide contains the single most transferable trick in Day 1: converting "apply X to Y" into "identify which component of X breaks on Y and why". Say it twice.
Anticipate the objection "but 'apply X to Y' papers get published in Scopus journals". Answer: yes, in low-quality ones, and they are rarely cited; the ablation-based version is publishable in Q1/Q2 and defensible in a viva.
Tell participants that step 2 (verbatim quotes with page numbers) is not busywork — those quotes become the citations that justify their gap paragraph in the Introduction (Day 2, S12).
-->

---

# Avoiding an Overly Broad Topic

| ❌ Too broad | Why it fails | ✅ Narrowed and defensible |
|---|---|---|
| "Deep learning for healthcare" | No question, no boundary, no finishable study | "Site-wise generalisation of CXR classifiers across three public datasets" |
| "Improving NLP for Indian languages" | 22 official languages, dozens of tasks | "Tokeniser-induced degradation in Marathi and Kannada extractive QA, with a morphology-aware BPE variant" |
| "AI in agriculture" | Domain, not problem | "Few-shot leaf-disease detection under field lighting with ≤50 labelled images per class on a Jetson-class device" |
| "Blockchain for security" | Two buzzwords, no unknown | "Gas-cost and latency limits of on-chain revocation for verifiable academic credentials at 10⁵ users" |
| "Explainable AI" | Whole research field | "Do Grad-CAM saliency maps agree with radiologist-annotated regions in CXR pneumonia cases, and does agreement predict model correctness?" |

<div class="cols">
<div>

#### Narrowing operators — apply until it fits
**Population** (which subjects/domains) · **Task** (which exact output) · **Condition** (noise, low-light, low-resource, adversarial) · **Constraint** (latency, memory, privacy, labels) · **Comparison** (against which baselines) · **Outcome** (which metrics)

</div>
<div>

#### The one-breath test
> *"I compare **[methods]** on **[datasets]** under **[condition]** measured by **[metrics]**, to find out whether **[question]**."*

If you cannot fill all five slots, you are not ready to start experiments.

</div>
</div>

<!--
SPEAKER NOTES — Scope clinic (10 min)
Run this as a public clinic. Ask for 3 volunteer topics, write each on the board, and apply narrowing operators live with the room suggesting slot values. Insist on filling all five slots of the one-breath sentence.
Watch for over-narrowing (rare but real): a topic so specific that no one else cares, e.g. "accuracy of one proprietary model on one 200-image private dataset". The fix is to raise the level of the *claim* while keeping the study specific — the study is narrow, the knowledge claim must be transferable.
-->

---

# Is the Problem Research-Worthy?

<div class="cols">
<div>

#### The 7-question gate
| # | Question | Fail signal |
|---|---|---|
| 1 | Is the answer unknown in the literature? | You find 5 papers already answering it |
| 2 | Is it measurable/provable? | No metric, no proof strategy |
| 3 | Is a negative result publishable? | Only "we win" is reportable |
| 4 | Can it be done with my resources in my time? | Needs 512 GPUs or 5,000 patients |
| 5 | Will anyone cite it? | No community, no benchmark, no application |
| 6 | Is it ethically and legally doable? | No consent, no licence, no IRB path |
| 7 | Can I state the contribution in one sentence? | Vague, plural, or grandiose |

</div>
<div>

## Novelty vs improvement

| | **Novelty** | **Improvement** |
|---|---|---|
| Claim | "This is a different way of thinking about the problem" | "This is measurably better at the same task" |
| Evidence | Conceptual argument + empirical support | Rigorous comparison + statistics + ablation |
| Reviewer risk | "Is it *sound*?" | "Is it *significant*?" — the 0.3% problem |

<div class="good">

**Both are publishable.** Improvement papers succeed when the gain is (a) statistically significant across seeds, (b) explained mechanistically by an ablation, and (c) not bought with hidden extra compute/data/tuning.

</div>

<div class="bad">

+0.4% accuracy on one dataset, one seed, no significance test, against a weakly tuned baseline = **the most common rejection in ML.**

</div>

</div>
</div>

<!--
SPEAKER NOTES — (5 min)
Question 3 again — it is the field's best bad-topic detector.
On improvement papers, cite the well-known critique that many reported gains vanish under equal hyperparameter-tuning budgets (a recurring finding in reproducibility studies across recommender systems, GANs, and language-model fine-tuning). Tell participants: tune your baseline as hard as you tune your own model, and say in the paper that you did — this single sentence buys enormous reviewer trust.
-->

---

# Feasibility Audit — Do This Before You Commit

| Dimension | What to verify **now** | Red flag | Where to check |
|---|---|---|---|
| **Dataset exists** | Named dataset, size, labels, licence, access path | "We will collect our own data" with no plan | Kaggle, HuggingFace Datasets, UCI, PhysioNet, OpenML, Papers with Code, Zenodo, government portals |
| **Licence permits use** | Redistribution and commercial terms; CC-BY vs CC-BY-NC vs custom DUA | Dataset is behind a DUA needing a PI signature | Dataset landing page / licence file |
| **Ethics/consent** | IRB/IEC approval need, anonymisation, GDPR/DPDP constraints | Human/patient data, no approval route | Institutional ethics committee |
| **Compute budget** | GPU-hours for **your model × baselines × ablations × seeds** | "Fine-tune a 70B model" on one 8 GB GPU | Your lab; Colab/Kaggle free tiers; institutional HPC |
| **Baselines available** | Official code + weights; do they run? | No code and no reimplementation in 2 weeks | GitHub, Papers with Code, HuggingFace |
| **Evaluation defined** | Metrics, splits, statistical test, significance plan | "We'll see the accuracy" | Benchmark papers, S15–S16 of this workshop |
| **Time** | Working backwards from your submission deadline | No slack for failures (assume 40%) | Your Gantt chart |

<div class="demo">

**Compute arithmetic, done honestly:** 4 baselines + your model = 5 configs × 5 seeds × 3 datasets = **75 training runs**. At 2 GPU-hours each = 150 GPU-hours, *plus* tuning, *plus* the ablation study (often 2–3× more), *plus* reruns after reviewers ask. Budget 3× your first estimate.

</div>

<!--
SPEAKER NOTES — (6 min) + ACTIVITY 2.1
Do the compute arithmetic on the board with the room's numbers. This slide has saved many students a wasted year.
ACTIVITY 2.1 (12 min): each participant completes the funnel (Area → Sub-area → Problem → RQ → Objective) for their own topic AND fills the feasibility table with actual dataset names, baseline repo URLs, and a GPU-hour estimate. Deliverable: one page. They must name at least one real dataset with its licence and one real baseline repository — if they cannot, that is the finding, and it must be resolved before Day 2 afternoon.
Debrief: ask who discovered their topic was infeasible. Celebrate it loudly — discovering infeasibility on day one is a win worth a year.
-->

---

# Section 2 — Wrap-Up

<div class="cols">
<div>

#### Common mistakes
- Choosing a topic from a title, not from reading
- Confusing a *domain* with a *problem*
- Ignoring dataset licences and ethics until submission
- Ignoring baseline availability until the last month
- Chasing hype without a durable core contribution
- "Apply X to Y" with no mechanism question
- No feasibility arithmetic for compute or time

#### Tools recap <span class="tag tool">TOOLS</span>
Scopus/WoS trends · arXiv + Google Alerts · Semantic Scholar feeds · Connected Papers / Litmaps / ResearchRabbit · OpenReview · Papers with Code · HuggingFace Datasets · journal special-issue CFPs

</div>
<div>

#### Deliverable from Section 2 (keep it, you will use it all workshop)
<div class="flow">
Area:        ______________________
Sub-area:    ______________________
Problem:     ______________________
RQ1/RQ2:     ______________________
Objective:   ______________________
Datasets:    ______ (licence: ____)
Baselines:   ______ (repo: ______)
Metrics:     ______________________
Compute est: ______ GPU-hours
Killer risk: ______________________
</div>

<div class="good">

**Takeaway:** A good topic is *narrow enough to finish*, *general enough to matter*, and *specific enough to name its datasets, baselines and metrics in one sentence.*

</div>

</div>
</div>

<!--
SPEAKER NOTES — (3 min)
Ask participants to photograph their completed deliverable — it is the input to every remaining section. Tell them the "killer risk" line is the most valuable one: naming the single thing most likely to sink the project makes it manageable, and it is exactly what a good supervisor or reviewer will ask about first.
-->


---

<!-- _class: lead -->

# Section 3
## How to Search for Research Papers

*Reproducible searching: strings you can put in a paper, not clicks you cannot remember*

---

# The Database Landscape

| Platform | What it indexes | Access | Strength | Limitation |
|---|---|---|---|---|
| **Google Scholar** | Everything: journals, conferences, preprints, theses, patents | Free | Widest recall; full-text search; "Cited by" | No quality control; no export of result sets; weak field syntax; irreproducible result counts |
| **Scopus** (Elsevier) | ~28k+ peer-reviewed sources, curated | Subscription | Best query syntax + analytics; author/affiliation profiles; CiteScore | Coverage gaps for CS conferences and books |
| **Web of Science** (Clarivate) | Core Collection: SCIE, SSCI, A&HCI, CPCI, ESCI | Subscription | Highest curation; JCR **Impact Factor**; citation-report analytics | Narrower than Scopus; complex editions |
| **IEEE Xplore** | IEEE + IET journals, conferences, standards | Subscription | Essential for EE/CS; standards; Command Search | Publisher-limited |
| **ACM Digital Library** | ACM journals, conferences, SIGs | Subscription | Definitive for core CS venues | Publisher-limited |
| **ScienceDirect** | Elsevier full text | Subscription | Full-text of Elsevier journals | One publisher |
| **SpringerLink** | Springer/Nature journals, LNCS, books | Subscription | LNCS conference proceedings; books | Weak advanced syntax (no truncation) |
| **Semantic Scholar** | ~200M+ records, AI-enhanced | **Free** | TLDRs, citation *intent*, influential citations, open API, alerts | Metadata noise |
| **PubMed / PMC** | Biomedical | Free | **MeSH** controlled vocabulary | Health only |
| **OpenAlex / Lens.org / Dimensions / CORE / BASE** | Open bibliographic graphs | Free tiers | Excellent when you have no subscription | Less curation than Scopus/WoS |
| **DOAJ** | Vetted open-access journals | Free | Legitimacy check for OA venues (see S22) | Journals, not articles |

<div class="warn">

**Never search only one platform.** A systematic search uses ≥3 databases plus one grey-literature source (arXiv), and reports each string and each date.

</div>

<!--
SPEAKER NOTES — (5 min)
Establish the mental model: Scholar = recall (find everything, verify nothing); Scopus/WoS = precision + reproducibility + analytics; publisher platforms = full text; Semantic Scholar/OpenAlex = free graph + API.
Ask who has institutional access to Scopus/WoS. In most Indian institutions, access varies; for those without it, name the free stack explicitly: Semantic Scholar + OpenAlex + Scholar + arXiv + DOAJ + Lens.org, plus their library's remote-access proxy or INFLIBNET/e-ShodhSindhu if applicable. Nobody should leave thinking a rigorous search is impossible without a subscription.
-->

---

# Step 1: Turn a Question Into Concepts and Synonyms

**Question:** *Do deep models for chest X-ray classification generalise across hospitals, and do domain-generalisation methods help?*

| Concept block | Preferred terms | Synonyms / variants / spellings | Narrower terms |
|---|---|---|---|
| **C1 Population/data** | chest radiograph | "chest X-ray", CXR, "thoracic radiograph", "chest radiography" | CheXpert, MIMIC-CXR, NIH ChestX-ray14, PadChest |
| **C2 Task** | classification | detection, diagnosis, screening, "multi-label classification" | pneumonia, pneumothorax, cardiomegaly |
| **C3 Method** | "deep learning" | CNN, "convolutional neural network", transformer, "vision transformer", ViT, DenseNet | ResNet, EfficientNet, Swin |
| **C4 Phenomenon (the core!)** | "domain generalisation" | "domain generalization", "domain shift", "distribution shift", "out-of-distribution", OOD, "external validation", "cross-institution", "site effect", "dataset bias" | "site-wise split", "hospital-level split" |
| **C5 Outcome** | AUC | AUROC, "area under the curve", sensitivity, specificity, calibration | "worst-group accuracy", ECE |

<div class="cols">
<div>

#### Rules
- One block per **concept**, joined by **OR** inside, **AND** between.
- Include **both** -ise/-ize spellings and British/American variants.
- Include **acronyms and their expansions**.
- Include **dataset names** — they retrieve papers that never use your abstract vocabulary.

</div>
<div>

#### Where synonyms come from <span class="tag tool">TOOLS</span>
- Keywords of 5 papers you already trust
- **Index terms** on IEEE Xplore; **Author Keywords** in Scopus
- **MeSH** (PubMed) / **ACM CCS** concepts / **IEEE Thesaurus**
- Titles of the papers your seed paper cites
- Ask an LLM for synonym candidates — then **verify each one retrieves real, relevant papers** before trusting it

</div>
</div>

<!--
SPEAKER NOTES — (6 min)
Build this table live for a participant's topic. The dataset-names row (C1 narrower) is the pro move: searching "CheXpert OR MIMIC-CXR" surfaces exactly the empirical papers you need and excludes theory that merely mentions domain shift.
Emphasise the -ise/-ize trap: "domain generalisation" alone loses the majority of the literature, because most is written in US spelling. Show that missing a spelling variant can silently halve your recall — and a reviewer who notices will question the whole review.
-->

---

# Step 2: Boolean Operators and Field Codes

<div class="cols">
<div>

#### Universal logic
| Operator | Effect | Note |
|---|---|---|
| `AND` | Both — narrows | Default on most platforms |
| `OR` | Either — widens | Wrap OR blocks in parentheses |
| `AND NOT` / `NOT` | Excludes — **use sparingly** | Silently kills relevant papers |
| `" "` | Exact/loose phrase | Essential for multiword concepts |
| `( )` | Grouping | Precedence differs per platform — always parenthesise |
| `*` | Truncation: `generali*` → generalise/generalize/generalisation | Not on SpringerLink; Scholar unreliable |
| `?` | Single character: `wom?n` | Scopus, WoS, IEEE |
| `W/n`, `NEAR/n`, `ONEAR/n` | Proximity within *n* words | Scopus `W/n`, WoS `NEAR/n`, IEEE `NEAR/n` (`ONEAR/n` = ordered) |
| `PRE/n` | First term precedes second by ≤ n | Scopus, ScienceDirect |

</div>
<div>

#### Field codes worth memorising
| Platform | Field syntax |
|---|---|
| **Scopus** | `TITLE-ABS-KEY( )`, `TITLE( )`, `AUTHKEY( )`, `SRCTITLE( )`, `DOCTYPE(ar)`, `PUBYEAR > 2021` |
| **Web of Science** | `TS=` (topic), `TI=`, `AB=`, `AK=`, `SO=`, `PY=2022-2026`, `DT=(Article)` |
| **IEEE Xplore** (Command Search) | `("Document Title":…)`, `("Abstract":…)`, `("Index Terms":…)`, `("All Metadata":…)` |
| **ScienceDirect** | `tak(…)` title-abs-key; ≤8 Boolean operators per field |
| **Google Scholar** | `intitle:`, `author:`, `source:`, `-term`; ~256-character limit |

<div class="warn">

Platform syntax changes. **Verify against the platform's own help page on the day you search**, and paste the exact string + date into your notes.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (6 min)
Teach one habit above all: proximity operators. `("deep learning" W/5 "chest radiograph")` in Scopus is dramatically more precise than AND, because AND matches a paper whose introduction mentions deep learning and whose unrelated related-work paragraph mentions chest radiographs.
Warn about NOT with a concrete example: `NOT COVID` to avoid pandemic papers also removes excellent methodology papers that merely validated on a COVID subset.
Tell them why the date matters: databases are updated continuously, so a string run in March and re-run in July gives different counts. Systematic reviews must report "searched on 12 March 2026".
-->

---

# Step 3: Build the Search String <span class="tag">DEMO</span>

#### Scopus (the reference implementation — build here, then port)
```
TITLE-ABS-KEY(
   ("chest X-ray*" OR "chest radiograph*" OR CXR OR "thoracic radiograph*"
      OR CheXpert OR "MIMIC-CXR" OR "ChestX-ray14" OR PadChest)
   AND ("deep learning" OR CNN OR "convolutional neural network*" OR transformer*
      OR "vision transformer" OR ViT)
   AND ("domain generali*ation" OR "domain shift" OR "distribution shift"
      OR "out-of-distribution" OR OOD OR "external validation"
      OR "cross-institution*" OR "site effect*" OR "dataset bias")
)
AND PUBYEAR > 2021 AND PUBYEAR < 2027
AND (LIMIT-TO(DOCTYPE,"ar") OR LIMIT-TO(DOCTYPE,"cp"))
AND (LIMIT-TO(LANGUAGE,"English"))
```

<div class="cols">
<div>

#### Ported to Web of Science
```
TS=(("chest X-ray*" OR "chest radiograph*" OR CXR
      OR CheXpert OR "MIMIC-CXR")
  AND ("deep learning" OR CNN OR transformer*)
  AND ("domain generali?ation" OR "domain shift"
      OR "distribution shift" OR "out-of-distribution"
      OR "external validation"))
AND PY=2022-2026
```

</div>
<div>

#### Ported to IEEE Xplore Command Search
```
("All Metadata":"chest X-ray" OR "All Metadata":CXR
   OR "All Metadata":CheXpert)
AND ("All Metadata":"deep learning"
   OR "All Metadata":transformer)
AND ("All Metadata":"domain shift"
   OR "All Metadata":"domain generalization"
   OR "All Metadata":"out-of-distribution")
```
Then set **Year: 2022–2026**, **Content type: Journals / Conferences**.

</div>
</div>

<!--
SPEAKER NOTES — LIVE DEMO (10 min)
Run this live if you have Scopus. Narrate the numbers: paste block C1 alone (thousands), add C3 (fewer), add C4 (hundreds), add year and doctype limits (a readable set). Participants must *see* recall shrinking under each AND — that is what "building" a string means.
Then click "Analyze search results" and show Documents by year, by source title, by author, by country. Say: "This 20-second view tells you who your reviewers will be, which journals publish this, and whether the topic is rising."
Export: CSV/RIS/BibTeX → import into Zotero (used in S6). Show the export dialog and select "Citation information + Abstract + Keywords" so the literature matrix can be filled semi-automatically.
Fallback if no subscription: run the Semantic Scholar and Scholar versions instead, and show the free OpenAlex API in a browser tab (api.openalex.org works without a key).
-->

---

# Effective vs Ineffective Queries

| ❌ Ineffective | Why it fails | ✅ Effective |
|---|---|---|
| `deep learning chest x ray` | No phrases, no synonyms, no field limit → 100k+ noisy hits | `TITLE-ABS-KEY(("chest X-ray*" OR CXR) AND "deep learning")` |
| `how can I improve generalisation of CNN models across hospitals?` | Natural-language question in a Boolean database | Concept blocks joined by AND/OR (previous slide) |
| `"domain generalisation"` only | One spelling → silently loses most of the literature | `"domain generali*ation" OR "domain shift" OR "out-of-distribution"` |
| `CXR AND DL AND DG` | Ambiguous acronyms (DL = deep learning? downlink? Dice loss?) | Acronym **plus** expansion, in an OR block |
| `(A OR B) AND (C OR D) NOT COVID NOT survey NOT review` | Over-exclusion; loses methodology papers and your own related-work sources | Include everything; **screen** by title/abstract instead |
| `chest x-ray classification 2026` | Year typed as a keyword, not a filter | Use `PUBYEAR > 2021` / `PY=2022-2026` |
| One database only | Coverage bias; not reproducible | ≥3 databases + arXiv, all strings logged |
| Sorting by relevance only | Buries recent work | Run **both** "sort by citations" and "sort by date" |

<div class="good">

**Precision–recall trade-off, stated practically:** aim for a set of **80–300 records** for a focused review. Above 500, add a concept block or tighten to titles. Below 40, drop a block, add synonyms, or widen the year window — and check your spelling variants first.

</div>

<!--
SPEAKER NOTES — (5 min)
The acronym row is worth dwelling on: search `DG` in Scopus and show the garbage. It makes the point better than any explanation.
Explain the "include everything, screen later" principle: exclusion belongs in the screening stage, where it is documented (PRISMA-style: 412 records → 118 after title/abstract screening → 34 after full text → 15 in the matrix), not hidden inside a NOT operator where no reader can audit it.
-->

---

# Filters, Citation Signals, and Progressive Refinement

<div class="cols">
<div>

#### Filters that matter
| Filter | Use |
|---|---|
| **Year** | Methods: 2022–2026. Foundations: no limit (you *must* cite the origin) |
| **Document type** | Article (`ar`), Conference paper (`cp`), Review (`re`) — search reviews **first**, then primary studies |
| **Subject area** | Removes cross-domain false hits |
| **Source title** | Restrict to your target journals to learn their style and cite them |
| **Open access** | Only when you lack full-text access — never as a quality filter |
| **Language** | Declare it as a limitation if you restrict to English |

#### Reading citation counts honestly
- Counts are **age-confounded**: a 2025 paper with 8 citations may be hotter than a 2019 paper with 60.
- Use **citations/year**, and Semantic Scholar's *Highly Influential Citations* (citation **intent**, not just count).
- A highly cited paper may be highly *criticised*. Check **who cites it and why**.
- Self-citation clusters and citation cartels exist — inspect the citing set.

</div>
<div>

#### Progressive refinement loop <span class="tag">DEMO</span>
<div class="flow">
1  Reviews/surveys 2022–2026  ─┐
       ↓ harvest their taxonomies + terms
2  Rebuild string with better terms
       ↓
3  Sort by CITATIONS → find the 5–8 canonical papers
       ↓
4  Sort by DATE      → find the 2025–2026 frontier
       ↓
5  For each key paper:
     • BACKWARD: mine its reference list
     • FORWARD : "Cited by" (Scholar/Scopus/WoS)
     • SIDEWAYS: Connected Papers graph
       ↓
6  Stop when new searches return only
   papers you have already seen  ← SATURATION
       ↓
7  Save the search + set an EMAIL ALERT
</div>

<div class="demo">

**Saturation is the stopping rule.** Not "when I have 15 papers" — when the literature stops surprising you.

</div>

</div>
</div>

<!--
SPEAKER NOTES — DEMO (8 min)
Demo the citation-chaining triad on one paper: (1) open its reference list (backward), (2) Google Scholar "Cited by" then use "Search within citing articles" with a keyword to filter it, (3) Connected Papers graph (sideways). Say: "Backward finds foundations; forward finds who improved or refuted it; sideways finds the parallel work that never cites your seed."
Then set up a Scopus/Scholar/Semantic Scholar alert live. Tell them: "Do this today. Your literature review must still be current at submission time, which may be nine months from now."
-->

---

# Section 3 — Wrap-Up

<div class="cols">
<div>

#### Common mistakes
- Typing a sentence into a Boolean database
- One spelling, one acronym, one database
- Over-using `NOT`
- Year typed as a keyword
- Not logging the string and the search date
- Never running a **backward + forward** citation chase
- Never setting an alert
- Downloading 200 PDFs and reading none

#### Search log template (put this in your paper)
| Field | Value |
|---|---|
| Database | Scopus |
| Search date | 12 March 2026 |
| String | *(verbatim)* |
| Filters | 2022–2026; ar, cp; English |
| Records | 412 |
| After screening | 118 → 34 → **15** |

</div>
<div>

<span class="tag act">ACTIVITY 3.1 — 20 min</span>
**Build and run your own string**

1. Write your concept/synonym table (≥3 blocks, ≥3 synonyms each, include dataset names). **5 min**
2. Compose a Scopus- or WoS-style string. **5 min**
3. Run it on ≥2 platforms; record record counts in the log. **5 min**
4. Refine until you have **80–300** records; export **RIS/BibTeX**. **5 min**
5. Shortlist **10–15** papers for tomorrow's matrix (mix: 2–3 reviews, 5–8 recent primary, 2–3 highly cited foundations).

<div class="good">

**Takeaway:** A search is a *documented, reproducible instrument*. If you cannot paste your search string into your methods section and have someone reproduce your record count, you have browsed — you have not searched.

</div>

</div>
</div>

<!--
SPEAKER NOTES — Activity facilitation (20 min)
Circulate with three diagnostics: (a) does the string have ≥3 concept blocks? (b) are both -ise/-ize spellings present? (c) is the year filter a filter, not a keyword?
Common rescue: participants whose count is 4,000 — usually a missing concept block, most often the phenomenon block (C4). Participants whose count is 3 — usually an over-specific phrase or a NOT.
Insist on the RIS/BibTeX export before the break; the next sections depend on having the records in a reference manager.
-->

---

<!-- _class: lead -->

# Section 4
## How to Read a Research Paper Efficiently

*Three passes, one template, zero wasted PDFs*

---

# The Three-Pass Method

Based on the widely used approach of **S. Keshav, "How to Read a Paper," ACM SIGCOMM CCR, 2007** — adapted here with an ML-specific extraction template.

| | **Pass 1 — Triage** | **Pass 2 — Comprehension** | **Pass 3 — Deep / reconstructive** |
|---|---|---|---|
| **Time** | 5–10 min | 45–60 min | 2–5 h (or days) |
| **Read** | Title, abstract, intro, section headings, all figures/tables + captions, conclusion, references skim | Everything except heavy proofs/derivations; **all figures and tables carefully** | Everything, including proofs, appendices, supplementary, and the **code** |
| **Goal** | Decide: discard / cite-only / read fully | Understand *what* they did and *whether the evidence supports it* | Understand *why* it works; be able to reimplement or refute it |
| **Output** | 1 line in your triage sheet | Filled extraction template + matrix row | Reimplementation, notes on hidden assumptions, a new research idea |
| **Applies to** | Everything you download (100%) | Your core set (10–20%) | 3–6 papers per project (2–5%) |
| **Question** | "Is this relevant to *my* question?" | "Do I believe the claim?" | "Can I build on, extend, or break this?" |

<div class="warn">

**Never read linearly from page 1 to page 12 on first contact.** You will spend 40 minutes on a paper you should have discarded in 5 — and you will absorb the authors' framing before you have evaluated it.

</div>

<!--
SPEAKER NOTES — (4 min)
Attribute Keshav explicitly and recommend the original 2-page paper as tonight's reading; it is free and takes 10 minutes.
Give the arithmetic: 200 papers × 45 min = 150 hours; 200 papers triaged at 7 min (23 h) + 25 read at 50 min (21 h) + 4 deep-read = about 60 hours for better coverage. Efficiency here is not laziness; it is what makes a literature review finishable.
-->

---

# Pass 1 — Triage in 5–10 Minutes

<div class="cols">
<div>

#### Read in this order
1. **Title + venue + year** → is it peer reviewed? which community?
2. **Abstract** → problem, method, headline result
3. **Figure 1 / architecture diagram** → the idea in one image
4. **All tables** → what was compared, on what data
5. **Section headings** → the shape of the argument
6. **Conclusion + limitations** → their own admission of weakness
7. **References**: do you recognise the canon? Is anything suspiciously absent?

#### The five triage answers to write down
`Problem` · `Method in ≤8 words` · `Datasets` · `Headline metric` · `Relevance to me: core / context / discard`

</div>
<div>

#### Discard signals (be ruthless)
- Different task/domain with no transferable mechanism
- No baseline comparison at all
- No dataset named, or an unnamed private dataset with no access
- Venue is unindexed / suspected predatory (S22)
- Results impossible or unexplained (99.9% on a hard benchmark)
- Paper is superseded by a later, better version you already have

#### Keep-but-only-cite signals
- Provides a definition, dataset, or statistic you need
- Is the canonical origin of a method you will use
- Contradicts another paper you are keeping — **flag it**, contradictions are gap material (S7)

</div>
</div>

<div class="demo">

<span class="tag tool">TOOLS</span> **Zotero** (save with PDF + metadata; colour tags: 🟥 core, 🟨 context, ⬜ discard) · **Semantic Scholar TLDR** for a one-line gist · **Connected Papers** to find the version you should have read instead · **Scholar "Cited by"** to check whether it was refuted.

</div>

<!--
SPEAKER NOTES — TIMED DEMO (10 min)
Do this live with a real open-access paper on the screen and a visible countdown of 7 minutes. Narrate every click and say aloud what you are deciding. Then show your 5-line triage note. Participants are astonished at how much is decidable in 7 minutes.
Key coaching point: reading Figure 1 and all tables *before* the introduction protects you from the authors' framing. Tables show what was actually compared; introductions show what the authors want you to believe was compared.
-->

---

# Pass 2 — Comprehension in 45–60 Minutes

<div class="cols">
<div>

#### Procedure
1. Re-read the abstract; write **their claim in your own words**. If you cannot, that is the paper's writing problem — note it, then dig.
2. Methodology: draw **their pipeline as a block diagram yourself**. Drawing exposes gaps their prose hides.
3. Experimental setup: list datasets, splits, baselines, metrics, hyperparameters, hardware, seeds.
4. Results: for **each table**, ask
   - What is the comparison?
   - Is the baseline **fairly tuned**?
   - Is the gain **larger than the variance**?
   - Are **all** datasets reported, or only the favourable ones?
5. Mark unknown terms/citations → build a **follow-up reading queue**.
6. Fill the extraction template (next slide).

</div>
<div>

#### Critical-reading questions that expose weak papers
| Target | Question |
|---|---|
| **Novelty** | Which *exact* component is new? Which existing paper is closest? |
| **Fairness** | Same data, splits, preprocessing, and tuning budget for all methods? |
| **Leakage** | Any patient/site/user appearing in both train and test? Any tuning on the test set? |
| **Variance** | Multiple seeds? Std devs? Confidence intervals? Any significance test? |
| **Selectivity** | Are the omitted datasets/metrics the inconvenient ones? |
| **Cost** | Parameters, FLOPs, latency, training time reported? |
| **Reproducibility** | Code and weights available? Do they match the paper? |
| **Explanation** | Do the authors explain *why* it works, or only *that* it wins? |

</div>
</div>

<!--
SPEAKER NOTES — (6 min)
Step 2 (draw their pipeline yourself) is the most effective single habit on this slide — say so. When you cannot draw it, you have found either a comprehension gap in yourself or an under-specified method in the paper, and both are useful.
The "Selectivity" question is delicate. Teach it as a hypothesis to test, not an accusation: check whether the datasets in the abstract are all the datasets in the appendix, and whether the metric used for the headline claim is used consistently everywhere.
-->

---

# Pass 3 — Deep / Reconstructive Reading

<div class="cols">
<div>

#### When to invest
- The paper is your **primary baseline**
- You intend to **extend** its method
- You suspect the result is **wrong** or **overstated**
- It is the theoretical foundation of your contribution

#### What you actually do
1. Re-derive the key equations; check dimensions and assumptions.
2. Reconcile notation between paper and code (they often disagree).
3. Clone the repo. Run it **as published**, then on **your** data.
4. Record every discrepancy: undocumented preprocessing, different hyperparameters in code vs paper, a metric implemented non-standardly.
5. Read supplementary material and appendices — the honest details live there.
6. Read **OpenReview** reviews/rebuttals if available.
7. Email the authors with one precise question. Most reply.

</div>
<div>

#### What a deep read produces
- A **trustworthy baseline number** you can defend to a reviewer
- A list of **hidden assumptions** = candidate research gaps
- Sometimes: a **reproducibility finding**, which is itself publishable

<div class="good">

**Real pattern, worth stating plainly:** the reason reported numbers often cannot be reproduced is rarely fraud. It is usually undocumented preprocessing, different splits, unequal tuning budgets, or a non-standard metric implementation. Documenting *which* one it was is a contribution.

</div>

<div class="warn">

Report reproduction failures **about the method, not the authors**: "we could not reproduce the reported 0.91 AUC using the released code with the described protocol; we obtained 0.86 ± 0.01 over 5 seeds," plus your exact configuration.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (5 min)
Insist on the professional register in the last box. Reproduction failure is normal and reportable; accusation is neither. A sentence that names a number, a protocol, a seed count and a configuration is unanswerable; a sentence that implies dishonesty invites a hostile review.
Encourage emailing authors — early-career researchers systematically underestimate how often authors respond helpfully to a specific, respectful question.
-->

---

# The Paper Extraction Template <span class="tag tool">HANDOUT</span>

Fill **one per paper** in Pass 2. These 14 fields become one row of your literature matrix (S6) and the raw material of your related-work section (Day 2, S13).

<div class="cols">
<div>

| # | Field | What to capture |
|---|---|---|
| 1 | **Citation key + venue + year** | `Author2025Domain`; venue; indexed? |
| 2 | **Research problem** | The unknown they address, in *your* words |
| 3 | **Motivation** | Why it matters (application or theory) |
| 4 | **Stated objective** | Their explicit aim/RQ |
| 5 | **Claimed gap** | What they say prior work lacked |
| 6 | **Dataset(s)** | Names, size, classes, split protocol, public? |
| 7 | **Preprocessing** | Resizing, normalisation, augmentation, balancing |

</div>
<div>

| # | Field | What to capture |
|---|---|---|
| 8 | **Proposed method** | Architecture/algorithm; the *new* component |
| 9 | **Baselines** | What they compared against; tuned equally? |
| 10 | **Metrics** | Which, and is the choice appropriate? |
| 11 | **Experimental setup** | Seeds, epochs, optimiser, LR, hardware, CV |
| 12 | **Key results** | 2–3 numbers with the comparison point |
| 13 | **Limitations** | Theirs (quote verbatim) **+ yours** (what they missed) |
| 14 | **Future work + gap for me** | Their suggestions + your one-line opportunity |

</div>
</div>

<div class="demo">

**Discipline rule:** field 13 must contain **both** their admitted limitation *and* your independent critique. A template with only the authors' self-assessment reproduces their framing — that is summarising, not reviewing.

</div>

<!--
SPEAKER NOTES — (4 min)
Hand out `handouts/paper-extraction-template.md`. Tell participants to keep the filled templates in one folder named by citation key; when they write related work on Day 2, they will write from these templates, not from the PDFs. That is the difference between three days of writing and three weeks.
Mention AI assistance honestly: an LLM or a tool like Elicit can pre-fill fields 6, 7, 9, 10, 11 reasonably well from a PDF, but fields 2, 5, 13 (your critique) and 14 must be yours. Field 12 must always be verified against the actual table — this is where AI summarisers make numeric errors. This is previewed here and drilled in S20.
-->

---

<!-- _class: dense -->
# Worked Example — Extraction of One Paper

<div class="cols-3-2">
<div>

**Paper P7** *(illustrative composite constructed for this workshop — not a real citation)*:
"Site-Adversarial Training for Cross-Hospital Chest Radiograph Classification", *hypothetical journal*, 2024.

| Field | Extracted content |
|---|---|
| **Problem** | CXR classifiers lose accuracy on unseen hospitals; degradation unquantified under site-wise splits |
| **Motivation** | Deployment across hospitals with different scanners/protocols |
| **Objective** | Reduce cross-site AUC drop without harming in-domain AUC |
| **Claimed gap** | Prior DG work evaluated on random splits, which leak site identity |
| **Datasets** | CheXpert (train), NIH ChestX-ray14 (external), MIMIC-CXR (external); **site-wise** splits |
| **Preprocessing** | 224×224, histogram equalisation, random crop/flip; no lung segmentation |
| **Method** | DenseNet-121 + gradient-reversal site-discriminator branch (λ ramped 0→1) |
| **Baselines** | ERM DenseNet-121, IRM, CORAL, Mixup |
| **Metrics** | Macro AUC, worst-site AUC, ECE |
| **Setup** | 3 seeds, Adam 1e-4, 30 epochs, 1×A100; code released |
| **Results** | Worst-site AUC 0.78 → 0.83; in-domain AUC 0.89 → 0.88; ECE improved 0.09 → 0.05 |

</div>
<div>

#### Field 13 — limitations
**Theirs (verbatim-style):** "restricted to frontal adult radiographs; site labels assumed known at training time."

**Mine (independent critique):**
- Only **3 seeds**; the 0.05 worst-site gain has **no significance test** or CI
- **Site labels required** — unavailable in most real deployments
- No **subgroup** analysis (age, sex, device); worst-*site* may hide worst-*group*
- No cost report (training time/params)
- ECE improvement not analysed — is it the adversary or just the extra regularisation? **No ablation on λ**

#### Field 14 — future work → my opportunity
Theirs: extend to lateral views and paediatric data.

**My one-liner:** *Site labels are the binding constraint. Can unsupervised site clustering recover most of the worst-site gain without site labels? And does the reported gain survive 10 seeds with a paired test?*

</div>
</div>

<!--
SPEAKER NOTES — (7 min) + ACTIVITY 4.1
Walk through the right column slowly — this is the intellectual core of Day 1. Point out that "my critique" produced *three* candidate gaps: an unsupervised variant (methodological gap), a statistical re-evaluation (evaluation/reproducibility gap), and a subgroup analysis (evaluation/fairness gap). None required a new idea from thin air; all came from reading one paper critically.
ACTIVITY 4.1 (35–40 min): each participant Pass-1 triages 5 papers (7 min each) and Pass-2 extracts 1 paper fully using the handout. Then pair up and each explains their paper's claim and their own critique in 3 minutes. The partner's job is to ask "how do you know?" three times.
Emphasise again: P7 is a constructed teaching example. Do not cite it anywhere.
-->

---

# Section 4 — Wrap-Up

<div class="cols">
<div>

#### Common mistakes
- Reading linearly from page 1
- Highlighting instead of extracting into fields
- Believing the abstract's number without checking the table
- Recording only the authors' limitations, never your own
- Never checking whether the paper was refuted by later work
- Letting an AI summary replace the read for a **core** paper
- Not recording the citation key at extraction time → hours lost later

#### Tools <span class="tag tool">TOOLS</span>
Zotero + Zotfile/tags · Semantic Scholar (TLDR, influential citations) · Connected Papers · OpenReview · Papers with Code · SciSpace / Elicit / NotebookLM *(assistive, verify everything)* · Excel/Sheets for the triage log

</div>
<div>

#### Your reading dashboard target
| Stage | Count | Depth |
|---|---|---|
| Retrieved | 80–300 | metadata only |
| Triaged (Pass 1) | all | 5–10 min each |
| Core set (Pass 2) | 10–20 | template filled |
| Deep read (Pass 3) | 3–6 | code run |

<div class="good">

**Takeaway:** Efficient reading is not faster reading — it is **selective depth**. Triage everything, comprehend the core, reconstruct the few papers your contribution stands on.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (3 min)
Close by asking: "How many of you have a folder of 200 unread PDFs?" Almost every hand goes up. Reframe: that folder is not a reading debt, it is an un-triaged inbox. Triage 20 of them tonight at 7 minutes each — two hours — and the debt largely disappears.
-->


---

<!-- _class: lead -->

# Section 5
## Literature Review

*Synthesis, not summary: writing that argues rather than lists*

---

# What a Literature Review Is — and Is Not

<div class="cols">
<div>

**A literature review is an argument about a body of work** that (a) organises it into a structure of your making, (b) evaluates its evidence, and (c) demonstrates that a specific gap exists.

#### Why it is required
| Function | Consequence if missing |
|---|---|
| Proves the gap is real | "This has been done before" → reject |
| Positions your contribution | Reviewer cannot see novelty |
| Justifies your method choices | "Why this baseline/metric?" |
| Identifies your baselines | Missing comparison → major revision |
| Shows command of the field | Loss of credibility; viva failure |
| Chooses your reviewers | They *will* be among the authors you cite |

</div>
<div>

#### Summary vs review
| | **Summary (paper-by-paper)** | **Review (synthesis)** |
|---|---|---|
| Unit of a paragraph | One paper | One **idea, method family, or finding** |
| Order | Whatever order you read them | Your taxonomy |
| Verbs | "proposed", "used", "achieved" | "converge on", "diverge", "in contrast", "remains untested" |
| Comparison | None | Explicit, on shared dimensions |
| Ends with | The last paper | **The gap** |
| Citations per sentence | 1 | Often 2–5 grouped |

<div class="bad">

**The tell-tale sign of a summary:** every paragraph starts with an author's name.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (4 min)
The "chooses your reviewers" row is a practical revelation for most participants: the editor often picks referees from the reference list and from Scopus author profiles in the topic. So an unfair dismissal of someone's work in your related work section can literally be read by that person. Teach criticism that is specific, evidence-based, and non-personal — "reported on a single random split" rather than "poorly evaluated".
Give the paragraph-opening diagnostic and tell them to run it on their own draft tonight: if paragraphs begin with author names, they have a summary.
-->

---

# Five Ways to Organise a Review

| Structure | Organising principle | Use when | Risk |
|---|---|---|---|
| **Chronological** | Time: early → recent | The field has clear paradigm shifts (HMM → RNN → Transformer) | Becomes a timeline with no argument |
| **Thematic** | Sub-problems / themes | Several distinct facets (data, method, evaluation, deployment) | Themes overlap; papers repeat |
| **Methodological** | Technique families | You will argue that a *family* has a shared weakness | Ignores task differences |
| **Comparative** | Dimensions in a matrix | You have quantitative evidence across papers | Reads like a spreadsheet if not interpreted |
| **Critical / argumentative** | Your thesis about the field | You have a strong, defensible position | Needs deep mastery; can look biased |

<div class="cols">
<div>

#### What strong reviews actually do
**Hybrid:** a **thematic** top level, **methodological** groups inside each theme, a **comparative table** per theme, and a **critical** synthesis paragraph closing each theme — with the last paragraph of the section stating the gap.

</div>
<div>

#### Skeleton you can copy (related work, ~4 subsections)
<div class="flow">
2.1 Problem formulations & datasets
2.2 Method family A  (+ table, + critique ¶)
2.3 Method family B  (+ table, + critique ¶)
2.4 Evaluation practices in this area
2.5 Synthesis: what is settled, what is
    contested, what is untested  ► THE GAP
</div>

</div>
</div>

<!--
SPEAKER NOTES — (4 min)
Recommend the hybrid explicitly and tell them to steal the skeleton. Also tell them a professional trick: open the two most recent survey papers in their area and look at their section structure — the taxonomy already exists and can be adopted (with citation) or deliberately improved upon. Improving an existing taxonomy and saying why is itself a contribution.
Note subsection 2.4 "evaluation practices" — most students omit it, and it is where evaluation gaps (the easiest defensible gaps for a first paper) become visible.
-->

---

# Weak vs Strong: The Same Five Papers

<div class="bad">

#### ❌ Weak (summary chain — the most common related-work failure)
"Sharma et al. [3] used a CNN for chest X-ray classification and achieved 88% accuracy. Wang et al. [4] used DenseNet-121 and achieved 90%. Li et al. [5] proposed a transformer-based model with 91% accuracy. Kumar et al. [6] used CORAL for domain adaptation and reported improvement. Ahmed et al. [7] used IRM and achieved better generalisation."

**Diagnosis:** five facts, zero relationships. No shared dimension (different datasets and splits, so the accuracies are not comparable). No evaluation of quality. No gap. The reader cannot tell what is *known*.

</div>

<div class="good">

#### ✅ Strong (synthesis with a critical edge)
"Work on cross-hospital CXR classification splits along two lines. The first improves **representation capacity** — DenseNet variants [4] and vision transformers [5] — and reports 88–91% in-domain accuracy, but *all three studies evaluate on random splits in which images from the same institution appear in both training and test sets*, so their numbers describe in-distribution performance rather than transfer [3]–[5]. The second line explicitly targets **distribution shift** using invariance objectives such as CORAL [6] and IRM [7]; these do evaluate across institutions and report 3–6 point gains in external AUC, but both assume **site labels are available at training time** and neither reports variance over more than three seeds, so it is unclear whether the reported gains exceed run-to-run noise. Across all five studies, **worst-site** performance and **calibration** go unreported, although these are the quantities that determine clinical usability. The literature therefore establishes *that* shift matters, but not *how large* the degradation is under leakage-free protocols, nor whether invariance methods help when site labels are unavailable."

</div>

<!--
SPEAKER NOTES — (7 min)
Read the weak version aloud in a flat voice, then the strong one. The contrast lands better than any explanation.
Then dissect the strong version's machinery on the board: (1) it groups (two lines); (2) it names a shared dimension (evaluation protocol); (3) it states what is credible and what is not, with a reason; (4) it groups citations [3]-[5]; (5) it identifies what is missing across all of them (worst-site, calibration); (6) its final sentence is a gap statement.
Ask participants to count how many sentences begin with an author name: zero. Then have them mark up their own draft paragraph the same way.
-->

---

# The Synthesis Language Toolkit

<div class="cols">
<div>

#### Agreement / convergence
- "Consistently across [3]–[7], …"
- "There is broad agreement that …, though the effect size varies from X to Y."
- "Both lines of work converge on …"

#### Contrast / contradiction
- "In contrast to [4], who report …, [8] find the opposite when …"
- "This discrepancy is plausibly attributable to differing split protocols rather than to the methods themselves."
- "Whereas early work assumed …, more recent evidence suggests …"

#### Evaluation of quality
- "…, although the comparison uses an untuned baseline."
- "…; the reported gain (0.4 points) is smaller than the seed-to-seed variance reported in [9]."
- "…, on a single dataset, which limits generality."

</div>
<div>

#### Establishing absence (gap moves)
- "To the best of our knowledge, no study has …" *(only after a documented search)*
- "**X** remains unquantified under **[condition]**."
- "Existing evaluations do not report **[quantity]**, although it determines **[consequence]**."
- "This assumption (**[assumption]**) is unlikely to hold in **[setting]**, yet is untested."

<div class="warn">

**Never write "no work exists" casually.** Reviewers *will* find a counterexample. Safer, and stronger: *"we found no study that evaluates X under Y; the closest is [12], which does Z but not Y."* This shows you looked and it survives contact with a specialist.

</div>

#### Citation hygiene
- Group citations by claim: `[3]–[5]` not one per sentence
- Cite the **origin** of a method, not only a recent user
- Never cite a paper you have not opened

</div>
</div>

<!--
SPEAKER NOTES — (5 min) + ACTIVITY 5.1
Tell participants to keep this slide as a phrasebook; non-native English writers find it the most immediately useful page in Day 1. Also tell them this is a legitimate use of AI: asking an LLM to suggest connective phrasing for a paragraph whose *content and citations you supply* is language help, not content generation (S20 formalises the distinction).
ACTIVITY 5.1 (15 min): take 4 rows from your extraction templates and write ONE synthesis paragraph (120-180 words) that groups them, evaluates them, and ends with an absence statement. Swap with a partner; the partner marks every sentence that merely reports and every sentence that actually synthesises.
-->

---

<!-- _class: lead -->

# Section 6
## The Literature Matrix

*The single artefact that turns 15 PDFs into a research gap*

---

# Matrix Columns

One row per paper. Build it in a spreadsheet — **not** in a Word document.

| Col | Column name | Fill with | Why it earns its place |
|---|---|---|---|
| A | **Paper (citation key)** | `Wang2023DenseCXR` | Links matrix → Zotero → BibTeX |
| B | **Year** | 2023 | Chronology; recency of the frontier |
| C | **Venue + indexing** | *IEEE TMI*, SCIE Q1 | Weighs evidence quality; hints at your target journal |
| D | **Research problem** | Cross-site degradation | Groups papers into themes |
| E | **Dataset(s) + split protocol** | CheXpert; **random** split | **The most diagnostic column** — reveals leakage & incomparability |
| F | **Method** | DenseNet-121 + CORAL | Builds your method taxonomy |
| G | **Baselines** | ERM only | Reveals weak-comparison papers |
| H | **Metrics** | Accuracy, AUC | Reveals evaluation gaps |
| I | **Key results** | 0.90 AUC in-domain | Comparable *only* within same dataset+split |
| J | **Strengths** | Public code; 3 datasets | Fair credit; tells you what to emulate |
| K | **Limitations (theirs + yours)** | Random split; 1 seed | Raw material for your gap |
| L | **Research gap it leaves** | Leakage-free re-evaluation missing | Aggregated → your gap |
| M | **Future work (verbatim)** | "extend to lateral views" | Free, author-endorsed ideas |
| N | **Reproducibility** | Code ✔ / weights ✘ / seeds 1 | Feasibility of using it as a baseline |
| O | **Relevance to me** | Baseline / context / discard | Sorting and prioritisation |

<!--
SPEAKER NOTES — (5 min)
Justify column E out loud; it is the column that most often produces a publishable finding. When participants fill it for 15 papers and discover that 11 used random splits on a dataset with multiple images per patient, they have just found a methodological/evaluation gap that a reviewer cannot dismiss.
Warn about column I: numbers across rows are usually NOT comparable. The matrix's job is to expose incomparability, not to build a leaderboard. Students who average column I across papers make a serious error.
-->

---

<!-- _class: dense -->
# Filled Matrix Extract (Illustrative)

<div class="small">

| Paper | Yr | Dataset + split | Method | Baselines | Metrics | Key result | Limitation (mine) | Gap it leaves |
|---|---|---|---|---|---|---|---|---|
| P1 | 2022 | CheXpert, **random** | ResNet-50 | none | Acc, AUC | 0.89 AUC | Leakage across patients; 1 seed | In-domain only; no transfer claim possible |
| P2 | 2022 | NIH14, **random** | DenseNet-121 | ResNet-50 | AUC | 0.90 AUC | Baseline untuned; no CI | Fair-tuning comparison missing |
| P3 | 2023 | CheXpert→NIH14, site-wise | ViT-B/16 | DenseNet | AUC | 0.84 external | 1 external set; no worst-site | Multi-site breadth |
| P4 | 2023 | MIMIC-CXR, **random** | CNN+attention | 2 CNNs | Acc, F1 | 0.91 Acc | Accuracy on imbalanced multi-label | Metric inappropriate → PR-AUC needed |
| P5 | 2023 | CheXpert→NIH14 | CORAL | ERM | AUC | +0.03 external | Needs site labels; 3 seeds | Label-free adaptation |
| P6 | 2024 | 3 sets, site-wise | IRM | ERM, CORAL | AUC, ECE | +0.04 worst-site | No significance test | Statistical validation |
| P7 | 2024 | 3 sets, site-wise | Site-adversarial | ERM, IRM, CORAL, Mixup | AUC, worst-site, ECE | 0.78→0.83 worst-site | Site labels; 3 seeds; no λ ablation | Label-free + ablation + stats |
| P8 | 2024 | Private, undisclosed | Ensemble | 1 CNN | Acc | 0.95 Acc | Not reproducible; no access | — (discard as baseline) |
| P9 | 2025 | CheXpert, random | Self-supervised pretrain | ERM | AUC | +0.02 | No external validation | SSL under shift untested |
| P10 | 2025 | 2 sets, site-wise | Test-time adaptation | ERM, CORAL | AUC | +0.03 | Needs target batch; latency unreported | Deployment cost of TTA |

</div>

<div class="demo">

**Read the columns, not the rows.** Column patterns are the finding: **6/10 used random splits** · **4/10 compared against a single baseline** · **0/10 ran a significance test** · **2/10 reported calibration** · **0/10 worked without site labels**.

</div>

<!--
SPEAKER NOTES — (6 min)
This is the payoff slide of Day 1. Cover the rows with your hand and read only the pattern box. Say: "Nobody had to invent an idea. Five defensible research gaps just fell out of the columns."
Make the counting explicit as a technique: for each column, tally the values. The tallies are the sentences of your gap paragraph and, later, the evidence in your Introduction. They are also excellent figures — a bar chart of "evaluation protocols used across 15 studies" is a publishable figure in a review paper.
State again that P1-P10 are illustrative placeholders, not citable works.
-->

---

# Building the Matrix — Tools <span class="tag">DEMO</span>

| Tool | Purpose | How to use | Limitation / verification |
|---|---|---|---|
| **Excel / Google Sheets** | The matrix itself | Row 1 = headers, **freeze**; one row per paper; `Data → Create a filter`; conditional formatting to colour split protocol; `COUNTIF` for column tallies; Sheets = collaborative + version history | Manual entry; keep one authoritative copy to avoid fork chaos |
| **Zotero** (free, open) | Reference library + PDFs + notes | Import the RIS/BibTeX from S3 → *Add Item by Identifier* for DOIs → colour **tags** (core/context/discard) → **child notes** using the extraction template → *Export Collection → CSV* to seed the matrix | Metadata from publishers is often wrong (missing pages, wrong capitalisation) — **fix every field manually** |
| **Mendeley** | Same role, Elsevier ecosystem | Web importer; Mendeley Cite for Word; annotate PDFs | Fewer plugins than Zotero; account-bound |
| **EndNote** | Institutional standard in many labs | Groups; Cite While You Write | Paid; heavier |
| **Semantic Scholar / Elicit / SciSpace / NotebookLM** | AI-assisted extraction | Upload your PDF set; ask for dataset/metric/baseline columns; export a draft table | <span class="tag risk">VERIFY</span> Every extracted number, dataset name and claim must be checked against the PDF. AI tools mis-attribute numbers between tables and hallucinate absent fields. Treat output as a **first draft of a data-entry task**, never as evidence |
| **Connected Papers / Litmaps / ResearchRabbit** | Find what your matrix is missing | Seed with 3–5 core papers; look for prominent nodes you have not read | Coverage depends on the underlying graph |

<div class="warn">

**Division of labour rule for the whole workshop:** AI may help you **find, sort, translate, and pre-fill**. **You** must **read, verify, compare, judge, and claim.**

</div>

<!--
SPEAKER NOTES — LIVE DEMO (12 min)
Demo sequence:
1. Zotero: drag a PDF in → show retrieved metadata → deliberately show a wrong/missing field and fix it → add a colour tag → add a child note with the template → right-click collection → Export as CSV → open in Sheets.
2. Sheets: paste, freeze row 1, add a filter, conditional-format column E so "random" turns red. Then live-type =COUNTIF(E2:E16,"*random*") and let the room see the tally appear. This moment converts the abstract idea of "reading the columns" into a concrete skill.
3. AI-assisted: upload 2 PDFs to an AI tool, ask for a dataset/metric/baseline table, then open the actual PDF table and check one number against it. If it is right, say so. If it is wrong, that is the best teaching moment of the day — either way, the lesson is that you checked.
Have screenshots as fallback. Announce clearly which tools are free (Zotero, Sheets, Semantic Scholar, NotebookLM basic) and which need payment/subscription.
-->

---

# Section 6 — Activity and Wrap-Up

<div class="cols">
<div>

<span class="tag act">ACTIVITY 6.1 — 45 min (core activity of Day 1)</span>

**Build your literature matrix**

1. From your S3 shortlist, load **10–15 papers** into Zotero. **5 min**
2. Pass-1 triage all of them; discard the irrelevant, replace them to keep ≥10. **15 min**
3. Fill the matrix: columns A–O. Use AI assistance for E–I if you like, then **verify each cell against the PDF**. **20 min**
4. Compute **column tallies** for split protocol, number of baselines, metrics, significance testing, code availability. **5 min**
5. Write the five tallies as five sentences. *(These become your gap paragraph in Section 7.)*

**Deliverable:** one spreadsheet + five tally sentences.

</div>
<div>

#### Common mistakes
- Building the matrix in Word (cannot sort, filter or tally)
- One column called "Notes" instead of 15 specific columns
- Averaging results across incomparable datasets/splits
- Recording only the authors' limitations
- Trusting AI-extracted numbers without opening the PDF
- Not recording the split protocol — the highest-value cell
- Stopping at 5 papers (patterns are invisible below ~10)

<div class="good">

**Takeaway:** The matrix converts reading into *data*. Gaps are then found by **counting columns**, not by hoping for inspiration.

</div>

</div>
</div>

<!--
SPEAKER NOTES — Activity facilitation (45 min)
This is the longest activity of Day 1; protect its time by trimming the Section 5 discussion if needed.
Circulate and enforce three things: (1) minimum 10 rows, (2) column E filled for every row, (3) participants' own critique in column K, not just the authors'.
For participants in non-CS disciplines, the columns adapt: dataset → sample/population/context; method → intervention or analytical approach; baselines → comparison groups; metrics → measures/instruments and their validity/reliability. Say this aloud so they do not feel excluded.
At minute 40, ask three participants to read their five tally sentences aloud. This previews Section 7 perfectly and shows the room that gaps are emerging from counting.
-->

---

<!-- _class: lead -->

# Section 7
## Finding the Research Gap

*The section that decides whether your paper is publishable*

---

# What a Research Gap Is

**A research gap is a specific, evidenced absence in the literature whose resolution would change what the field knows or can do.**

<div class="cols">
<div>

#### A gap statement has four obligatory parts
| Part | Example |
|---|---|
| **What is absent** | No leakage-free, multi-site quantification of CXR classifier degradation |
| **Evidence of absence** | 11 of 15 studies use random splits; 0 of 15 report worst-site performance |
| **Why it matters** | Reported AUCs overstate deployable performance; hospitals cannot judge risk |
| **What resolving it enables** | A trustworthy degradation estimate + a label-free mitigation |

</div>
<div>

#### These are **not** gaps
| Non-gap | Why |
|---|---|
| "Nobody has applied model X to dataset Y" | Absence of an activity ≠ absence of knowledge. Ask *why it would be informative* |
| "Accuracy can be improved" | Always true, everywhere, forever |
| "The topic is new/trending" | Novelty of hype ≠ gap |
| "Existing methods are complex" | Only a gap if you show complexity *costs* something measurable |
| "No work exists in my country/language" | Becomes a gap only with a mechanism: *why* would results differ here? |
| "No one has combined A and B" | Combination is not a contribution unless you show *why* the combination should behave differently |

</div>
</div>

<!--
SPEAKER NOTES — (5 min)
The right-hand column is the harshest and most useful part of Day 1. Deliver it as diagnosis, not scolding: nearly every first draft contains at least one of these.
Rescue moves to demonstrate live:
• "Nobody applied X to Y" → "Which assumption of X is violated by Y, and what happens to performance when it is?"
• "No work in my language" → "Language L is morphologically rich and has no pretrained tokeniser coverage; we predict subword fragmentation drives the error, and we measure it."
The rescue is always the same: add a MECHANISM and a MEASUREMENT.
-->

---

# Gap Taxonomy (1 of 2)

| # | Gap type | Definition | AI/ML example | Typical evidence you need |
|---|---|---|---|---|
| 1 | **Knowledge gap** | A phenomenon is unexplained or unmeasured | Why does self-supervised pretraining help under shift but not under label noise? | Prior work reports the effect but not the cause |
| 2 | **Methodological gap** | Existing methods rest on an assumption that fails in practice | All DG methods for CXR require **site labels**; deployments do not have them | Assumption stated in each paper's setup |
| 3 | **Dataset / resource gap** | No suitable data exists: language, modality, population, annotation | No code-mixed Hindi–English paraphrase benchmark with obfuscation levels | Search of dataset registries returns nothing |
| 4 | **Performance gap** | Best known result is insufficient for the use case | Worst-site AUC 0.83 vs the ≥0.90 needed for triage support | Requirement from the application domain |
| 5 | **Application / translation gap** | Method works in the lab, unstudied under deployment constraints | Test-time adaptation needs target batches; latency/memory unreported on edge devices | Absence of cost reporting in prior work |
| 6 | **Population / domain gap** | Evidence exists for one group/domain and is untested for another, *with reason to expect difference* | Models trained on adult frontal CXR untested on paediatric; anatomy differs | Domain argument + absence of studies |

<!--
SPEAKER NOTES — (5 min)
Do not read the table. Instead, ask participants to raise a hand for the gap type they believe their topic fits, and probe two of them: "what is your evidence of absence?"
Highlight #6's crucial qualifier: "with reason to expect difference". Without that clause, a population gap is just an untried combination. With it, it is science. This is the same mechanism lesson as before, now inside a taxonomy.
Note that types 3, 5 and 6 are the most achievable for a first paper with limited compute.
-->

---

# Gap Taxonomy (2 of 2)

| # | Gap type | Definition | AI/ML example | Typical evidence you need |
|---|---|---|---|---|
| 7 | **Evaluation gap** | Metrics or protocols do not measure what matters | Multi-label imbalanced CXR evaluated by accuracy; PR-AUC and calibration unreported | Column tally of metrics across papers |
| 8 | **Scalability gap** | Works at small scale; behaviour at target scale unknown | Graph method validated to 10⁴ nodes; production graphs are 10⁸ | Complexity analysis + absence of large-scale results |
| 9 | **Generalisation gap** | Results do not transfer across distributions | Random-split AUC 0.90 → site-wise 0.78 | Direct re-evaluation |
| 10 | **Reproducibility gap** | Results cannot be independently obtained | 6/15 papers release no code; reported numbers not recoverable | Your own reproduction attempt, documented |
| 11 | **Computational-efficiency gap** | Accuracy achieved at unreported/unacceptable cost | +0.02 AUC for 4× parameters and 3× latency — never reported | Cost measurements absent in prior work |
| 12 | **Explainability / trust gap** | Decisions unexplained, or explanations unvalidated | Grad-CAM used but never checked against expert annotation | Absence of explanation-validation studies |

<div class="good">

**Strategic note for early-career researchers:** gaps **7, 9, 10, 11** are usually the cheapest to address rigorously (they need careful experiments, not new theory or big compute), and they are hard for reviewers to dismiss because the evidence is arithmetic.

</div>

<!--
SPEAKER NOTES — (5 min)
Dwell on the strategic note. A student with one mid-range GPU cannot beat a lab with 500; they *can* run the leakage-free re-evaluation that the big lab never bothered to run, and such papers are cited heavily because they change practice.
Give the honest caution too: re-evaluation papers must be executed impeccably (equal tuning, released code, statistics) or they are indefensible — you are criticising others' rigour, so yours must be beyond reproach.
-->

---

# Where Gaps Hide: Nine Signals

| Signal in the literature | How to detect it | Gap type it usually yields |
|---|---|---|
| **Stated limitations** | Read every Limitations/Threats section; tally recurring ones | 2, 5, 6, 12 |
| **Future work** | Collect verbatim; a suggestion repeated by 3+ papers is a field priority | any |
| **Contradictory results** | Two papers, same task, opposite conclusions → find the confound (data? split? tuning?) | 1, 7, 9 |
| **Missing datasets** | Search dataset registries; note languages/populations/modalities absent | 3, 6 |
| **Poor evaluation** | Tally metrics column: accuracy on imbalanced data, no CI, no significance test | 7 |
| **Weak baselines** | Tally baselines column: "compared to ERM only", or to a 5-year-old method | 4, 7 |
| **Missing comparisons** | Method families that have never been compared *under one protocol* | 7, 9 |
| **Small samples / few seeds** | n < 100 subjects; 1–3 seeds; single split | 7, 10 |
| **Domain/scope limitations** | "We consider only English/adults/frontal views/synthetic data" | 6, 8, 9 |

<div class="demo">

**Contradictions are the richest signal and the most under-used.** When P4 reports that attention helps and P9 reports it does not, the *explanation* of the discrepancy is a knowledge contribution — and you can often produce it with a controlled re-run rather than a new method.

</div>

<!--
SPEAKER NOTES — (5 min)
Give the contradiction workflow concretely: (1) tabulate both setups side by side, (2) list every difference (dataset, split, preprocessing, tuning budget, metric, seeds), (3) hypothesise which difference is the causal confound, (4) design a single controlled experiment varying only that factor. That is a clean, publishable study with a genuine knowledge claim, achievable in a semester.
-->

---

<!-- _class: xdense -->
# From 10 Papers to a Gap (1/2) — Counting

<div class="cols-3-2">
<div>

<div class="flow">
STEP 1 · 15 papers in the matrix (2022–2026)

STEP 2 · COLUMN TALLIES
  • 11/15 random splits (patient/site leakage)
  • 12/15 report only accuracy or AUC
  •  0/15 report worst-site performance
  •  2/15 report calibration (ECE)
  •  0/15 report any significance test
  •  9/15 compare against ≤1 baseline
  •  6/15 release no code
  • 15/15 DG methods require site labels

STEP 3 · COMMON LIMITATIONS
  L1 Evaluation leaks site/patient identity
     (11/15) → in-distribution numbers only
  L2 Reported gains within seed noise
     (0/15 significance tests, ≤3 seeds)
  L3 Site labels assumed available
     (15/15) → untestable in deployment
  L4 Clinically relevant quantities
     unreported (worst-site 0/15, ECE 2/15)
</div>

</div>
<div>

#### The move
Each **L** is a *field-level* limitation, not one author's excuse — because it is a **count across papers**, taken from one matrix column.

<div class="warn">

**Do this in a spreadsheet, not in your head.** The tallies are your evidence; you will cite them in your Introduction (¶4) and your reviewers will check them.

</div>

<div class="demo">

**Rule of thumb:** a weakness admitted or exhibited by **≥ 40%** of your set is a gap candidate. A weakness in one paper is a critique of that paper.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (4 min)
Trace the chain with a finger, slowly, asking at each number "where did this come from?" — answer: the matrix column. Participants must internalise that the matrix is the evidence base of the gap, not a filing system.
Point out the difference between L1 (a protocol flaw that invalidates interpretation) and L4 (a reporting omission). Both are gaps, but they license different contributions: L1 licenses a re-evaluation, L4 licenses an added measurement.
-->

---

<!-- _class: xdense -->
# From 10 Papers to a Gap (2/2) — Converting

<div class="cols-3-2">
<div>

<div class="flow">
STEP 4 · UNRESOLVED PROBLEM
  The true cross-hospital degradation of CXR
  classifiers is unknown, and no mitigation
  has been shown to work WITHOUT site labels.

STEP 5 · RESEARCH GAP (evidenced)
  No study quantifies degradation under
  leakage-free site-wise protocols across
  multiple institutions with statistical
  validation, and no label-free mitigation
  has been evaluated on worst-site AUC and
  calibration.
        ↑ from L1, L2        ↑ from L3, L4

STEP 6 · PROPOSED CONTRIBUTION
  C1 Leakage-free multi-site re-evaluation of
     5 published models (3 datasets, 10 seeds,
     paired tests, CIs)              ← L1, L2
  C2 A label-free site-clustering adaptation
     method; ablation isolates the
     mechanism                       ← L3
  C3 Public benchmark + code + splits ← L1, L4
</div>

</div>
<div>

#### Why this chain convinces a reviewer
- Every step is **countable**, from a documented search
- The gap is **not** "accuracy can be improved"
- Contributions map **1:1** to the limitations they answer
- Two of three contributions need **no new theory** and modest compute
- A **negative** result is still publishable: if degradation turns out to be small, that is important news

<div class="good">

Notice: contributions C1 and C3 were *created by the tallies*. **The gap analysis designed the study** — the method was chosen last, not first.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (5 min)
The arrows are the teaching point: every contribution is traceable to a counted limitation. Ask the room to check C2 → L3 out loud.
Then make the intellectual point plainly: the research design fell out of the gap analysis. Students usually design the method first and reverse-engineer a gap to justify it — that is why reviewers smell it. Doing it in this order produces coherent papers and coherent vivas.
-->

---

<!-- _class: dense -->
# Weak vs Strong Gap Statements

<div class="cols">
<div>

<div class="bad">

#### ❌ Weak
1. "Many researchers have worked on CXR classification, but there is still room for improvement."
2. "Deep learning has not been applied to our hospital's dataset."
3. "Existing methods have low accuracy."
4. "No one has combined transformers with domain adaptation for CXR."
5. "Research on explainability in medical imaging is limited."
6. "Prior work is old; we use a newer model."

</div>

**Why each fails**
1. Vague; no absence identified; unfalsifiable
2. Local activity, not knowledge; no mechanism
3. Unquantified; low relative to what threshold?
4. Untried combination without a reason to expect different behaviour
5. "Limited" is not evidence; how limited, in what respect?
6. Recency is not a contribution

</div>
<div>

<div class="good">

#### ✅ Strong
1. "Across 15 studies (2022–2026), 11 evaluate CXR classifiers on random splits in which images from the same institution occur in both partitions; consequently the reported AUCs (0.88–0.91) cannot be interpreted as cross-hospital performance, and the magnitude of degradation under leakage-free protocols remains unquantified."
2. "All eight domain-generalisation methods we identified require site labels during training [5]–[7], [11]; in deployment, provenance metadata is typically stripped for privacy, so it is unknown whether comparable gains are attainable without site supervision."
3. "None of the 15 studies reports worst-site AUC or calibration error, although both determine clinical usability; performance is therefore reported for the average institution and not for the institution most at risk."

</div>

#### The template
> *"Across **[N]** studies identified by **[documented search]**, **[pattern]** holds. Consequently, **[specific quantity/mechanism]** remains **[unquantified / untested / unexplained]**, even though **[why it matters]**. This study addresses that by **[action]**."*

</div>
</div>

<!--
SPEAKER NOTES — (6 min)
Have participants read their own draft gap statement against the six weak patterns and self-diagnose. Ask for one volunteer weak statement and rewrite it live using the template with the room supplying the numbers from their matrix. If they cannot supply numbers, that is the lesson: go back to the matrix.
Note the register: strong statements are longer, contain numbers and citations, and hedge precisely ("we found no study that…") rather than absolutely ("no study exists").
-->

---

# Section 7 — Activity and Wrap-Up

<div class="cols">
<div>

<span class="tag act">ACTIVITY 7.1 — 30 min</span>
**Derive your gap** (worksheet: `handouts/research-gap-worksheet.md`)

1. Tally 5 columns of your matrix. **5 min**
2. Write 3–5 **common limitations** (L1…L5), each with the count and 2–3 supporting citations. **8 min**
3. State the **unresolved problem** in one sentence. **3 min**
4. Write the **gap** using the template, including numbers. **7 min**
5. Classify it against the **12 gap types** (it may be 2–3 types). **2 min**
6. List **2–3 contributions** mapping 1:1 to the gap. **5 min**
7. **Stress test with a partner:** the partner must attempt to break it with — *"has this been done?"*, *"how do you know?"*, *"why does it matter?"*, *"can you do it with your resources?"*

</div>
<div>

#### Common mistakes
- "Room for improvement" as a gap
- A gap with no numbers
- Claiming "no work exists" without a documented search
- A gap that requires resources you do not have
- Gap and contributions that do not correspond
- Finding the gap **after** choosing the method
- One gap type only, when the honest answer is "evaluation + generalisation"
- Never stress-testing it with a critical reader

<div class="good">

**Takeaway:** A research gap is not discovered by inspiration. It is **computed** from a documented literature matrix, stated with numbers, and stress-tested by a hostile reader before it reaches a reviewer.

</div>

</div>
</div>

<!--
SPEAKER NOTES — Activity facilitation (30 min)
Step 7 is the part participants will want to skip; it is the most valuable. Model it first: ask a volunteer to state their gap and interrogate it publicly (kindly but relentlessly) with the four questions. Then let pairs do it.
Watch for the most common failure: a gap that is actually a method proposal ("we will use a graph transformer"). Push back with "that is your method; what is unknown?"
Keep the best 3 gap statements for the Day 1 closing presentations.
-->

---

<!-- _class: lead -->

# Section 8
## Research Objectives and Contributions

*Turning a gap into a work plan a reviewer can audit*

---

# Aim → Objective → Method → Contribution

| Element | Count | Function | Grammar | Example |
|---|---|---|---|---|
| **Aim** | Exactly **1** | The overall purpose; broad but bounded | "To + purpose" | "To establish how much chest-radiograph classifiers degrade across hospitals and whether label-free adaptation mitigates it." |
| **Objective** | **3–5** | Concrete, completable steps that jointly achieve the aim | "To + measurable verb + object + condition" | "**O2:** To quantify the AUC and calibration degradation of five published models under site-wise splits on three datasets over 10 seeds." |
| **Method** | per objective | *How* the objective will be executed | Procedure | "Re-train each model with identical augmentation, tuning budget and seeds; evaluate with macro/worst-site AUC, ECE; compare with paired Wilcoxon tests + bootstrap CIs." |
| **Contribution** | **2–4** | What the field gains once objectives are met | Noun phrase, calibrated | "**C1:** The first leakage-free multi-site degradation benchmark for CXR classification, with statistical validation." |

<div class="flow">
GAP  ──►  AIM  ──►  OBJECTIVES  ──►  METHODS  ──►  RESULTS  ──►  CONTRIBUTIONS
                        │                                            ▲
                        └──── every objective must produce ──────────┘
                              at least one contribution
</div>

<div class="warn">

**Traceability audit (reviewers do this):** each objective → a method → a results subsection → a contribution bullet. An objective with no results subsection reads as an abandoned promise; a results subsection with no objective reads as an afterthought.

</div>

<!--
SPEAKER NOTES — (5 min)
The traceability audit is the practical core. Tell participants to build a 4-column table (Objective | Method | Results section | Contribution) and keep it beside them while writing the paper on Day 2. Reviewers and examiners literally construct this table; building it yourself removes an entire class of criticism.
Common confusion to pre-empt: aim vs objective. Aim = the destination (one). Objectives = the legs of the journey (3-5). Methods = the vehicle. Contributions = what you bring back.
-->

---

# Gap → Research Questions → Objectives

<div class="cols">
<div>

#### The conversion is mechanical
| Gap element | Becomes |
|---|---|
| "…magnitude of degradation is unquantified" | **RQ1** How large is it? |
| "…requires site labels" | **RQ2** Can it be done without them? |
| "…worst-site and calibration unreported" | **RQ3** What happens to those quantities? |
| "…gains may be within noise" | **RQ4** Are differences statistically significant? |

#### RQ quality rules
- **One** relationship per RQ (two variables)
- Answerable by an experiment you can actually run
- Not answerable by yes/no alone → prefer *how much*, *under what conditions*, *why*
- Ordered: descriptive (RQ1) → comparative (RQ2) → explanatory (RQ3)

</div>
<div>

#### From RQ to objective — worked
| | |
|---|---|
| **RQ1** | How much does classification performance degrade from random to site-wise evaluation? |
| **O1** | To re-evaluate five published architectures on three public datasets under both random and site-wise protocols, over 10 seeds, reporting macro AUC, worst-site AUC and ECE with 95% bootstrap CIs. |
| **RQ2** | Can degradation be mitigated without site labels? |
| **O2** | To develop and evaluate a label-free adaptation method based on unsupervised site clustering, compared against ERM, CORAL, IRM and site-adversarial training under an identical tuning budget. |
| **RQ3** | Which component drives the mitigation? |
| **O3** | To conduct an ablation over the clustering granularity, the invariance weight λ, and the augmentation set, isolating each component's effect. |

</div>
</div>

<!--
SPEAKER NOTES — (5 min)
Show that each objective already contains the experiment: datasets, models, seeds, metrics, comparisons. That is the test of a good objective — it is a specification, not an aspiration.
Point out the "identical tuning budget" clause in O2. Writing fairness controls into the objective, not just the method, is a mark of a mature researcher and is exactly what reviewers look for.
-->

---

<!-- _class: dense -->
# Hypotheses and Contribution Calibration

<div class="cols">
<div>

## Hypotheses (state them even if you never print them)
| Form | Example |
|---|---|
| **H0 (null)** | Site-wise and random-split AUC do not differ (paired, α=0.05). |
| **H1 (alternative, directional)** | Site-wise AUC is lower than random-split AUC. |
| **H2** | Label-free clustering adaptation improves worst-site AUC by ≥0.03 over ERM. |

#### Rules
- Must be **falsifiable** and **pre-specified** (before you look at test results)
- Name the **test** and **α** in advance: paired *t*-test / Wilcoxon signed-rank / McNemar (same test set, two classifiers)
- Include an **effect size**, not only significance: 0.001 gain can be significant and useless
- Correct for **multiple comparisons** (Holm/Bonferroni) when testing many models × datasets

<div class="bad">

Choosing the test *after* seeing the results, or reporting only the comparisons that reached significance, is **p-hacking** — a form of misconduct (S21).

</div>

</div>
<div>

## Calibrating contribution claims
| ❌ Over-claim | ✅ Calibrated |
|---|---|
| "We propose a novel state-of-the-art architecture" | "We propose a label-free adaptation module that improves worst-site AUC by 0.04 ± 0.01 over the strongest baseline on three datasets" |
| "Our method solves domain shift" | "Our method recovers ~60% of the degradation observed under site-wise evaluation" |
| "First work in this area" | "To our knowledge, the first leakage-free multi-site evaluation of these five architectures" |
| "Outperforms all existing methods" | "Outperforms four representative baselines under an identical tuning budget; we did not evaluate methods requiring paired multi-site supervision" |

<div class="good">

**Calibrated claims are stronger, not weaker.** A number with a CI and a scope limit is unassailable; "state of the art" invites a reviewer to find the counterexample — and they will.

</div>

</div>
</div>

<!--
SPEAKER NOTES — (6 min)
Explain McNemar's test specifically — it is the right test for comparing two classifiers on the same test set and is under-used in student papers. Mention 5x2-fold cross-validated paired t-tests (Dietterich) and corrected resampled t-tests for those who want the rigorous route.
On calibration: give the reviewer's-eye view. When a reviewer reads "novel state-of-the-art", the first instinct is to search for a paper that beats it. When they read a bounded numeric claim with stated scope, there is nothing to attack. Under-claiming slightly is a professional strategy.
-->

---

# Weak vs Strong Objectives

| ❌ Weak objective | Diagnosis | ✅ Strong objective |
|---|---|---|
| "To study deep learning for medical imaging" | No boundary, no completion criterion | "To quantify the change in macro and worst-site AUC of five published CXR architectures when random splits are replaced by site-wise splits, across three public datasets and 10 seeds" |
| "To implement a CNN model" | Activity, not knowledge; done in a day | "To determine whether label-free site clustering recovers ≥50% of the site-wise degradation achieved by site-supervised adversarial training" |
| "To improve accuracy" | Unquantified, no comparison point | "To reduce worst-site AUC degradation by ≥0.03 relative to ERM at equal parameter count and inference latency" |
| "To analyse various algorithms" | "Various" = unspecified | "To compare ERM, CORAL, IRM and site-adversarial training under an identical 50-trial tuning budget on identical splits" |
| "To develop a novel framework" | Unfalsifiable; "framework" hides the claim | "To develop an adaptation module requiring no site metadata and evaluate it on worst-site AUC, ECE and inference latency" |
| "To achieve 99% accuracy" | Fixates on a number; unachievable/meaningless target | "To characterise the accuracy–latency trade-off across four model scales on a Jetson-class device" |

<div class="demo">

**Self-check per objective:** Does it name a **measurable outcome**? A **comparison**? A **condition/scope**? Could an examiner mark it **done or not done**? Does it map to a **contribution**?

</div>

<!--
SPEAKER NOTES — (5 min) + ACTIVITY 8.1
ACTIVITY 8.1 (20 min): participants write Aim (1), RQs (2-4), Objectives (3-5), Hypotheses (1-3, with named test and alpha) and Contributions (2-4) for their own topic, then complete the traceability table (Objective | Method | Expected result | Contribution).
Exchange with a partner: the partner marks any objective they could NOT mark "done/not done" as an examiner. Those must be rewritten before the closing presentations.
Coaching note: the word "framework" is a red flag; ask what it actually is (a module? a protocol? a pipeline? a loss?) and make them name it.
-->

---

<!-- _class: lead -->

# Day 1 Hands-On Activity
## From Area to Expected Contribution

*90 minutes of work, then presentations*

---

<!-- _class: dense -->
# Day 1 Capstone — Brief

<div class="cols-3-2">
<div>

<div class="flow">
        RESEARCH AREA
              ↓
       RESEARCH PROBLEM
              ↓
       10–15 PAPERS  (searched, logged)
              ↓
      LITERATURE MATRIX  (columns A–O)
              ↓
      COMMON LIMITATIONS  (L1…L5 + counts)
              ↓
        RESEARCH GAP  (evidenced, typed)
              ↓
     RESEARCH QUESTIONS  (RQ1…RQ3)
              ↓
         OBJECTIVES  (O1…O4)
              ↓
    EXPECTED CONTRIBUTION  (C1…C3)
</div>

#### Timing (90 min)
| Min | Task |
|---|---|
| 0–10 | Finalise area + problem statement |
| 10–25 | Finalise the paper set (≥10, logged strings) |
| 25–55 | Complete the matrix; compute tallies |
| 55–70 | Limitations → unresolved problem → gap |
| 70–85 | RQs, objectives, contributions, traceability table |
| 85–90 | Prepare a 3-slide / 3-minute presentation |

</div>
<div>

#### Submission format (one file, `LASTNAME_day1.md/.docx` + the matrix spreadsheet)
1. Area, sub-area, problem (3 sentences)
2. Search log: databases, strings, dates, counts, screening funnel
3. Matrix: ≥10 rows × 15 columns
4. Five tally sentences
5. Common limitations L1–L5 with counts and citations
6. Gap statement (template) + gap type(s)
7. RQ1–RQ3
8. Aim + objectives O1–O4
9. Hypotheses with named tests and α
10. Contributions C1–C3
11. Traceability table
12. Feasibility line: datasets + licences, baselines + repos, GPU-hours, killer risk

<div class="warn">

**Rule:** every number in your submission must be traceable to a matrix cell, and every citation must be one you have actually opened.

</div>

</div>
</div>

<!--
SPEAKER NOTES — Capstone facilitation (90 min)
Circulate continuously with the same four questions: Has this been done? How do you know? Why does it matter? Can you do it with what you have?
Triage your own attention: spend the most time with participants whose gap is still a method proposal or whose matrix has fewer than 10 rows.
Two useful interventions: (1) for anyone stuck on the gap, tell them to read only their tally sentences aloud — the gap is usually audible; (2) for anyone with an infeasible plan, help them find the achievable evaluation/reproducibility version of the same topic.
-->

---

# Presentations and Rubric

<div class="cols">
<div>

#### 3-minute presentation format
| Slide | Content | Time |
|---|---|---|
| 1 | Problem + why it matters | 45 s |
| 2 | Matrix tallies → gap (with numbers) | 90 s |
| 3 | RQs, objectives, contributions | 45 s |

#### Audience job (mandatory)
Each presentation gets **two questions**, drawn from:
- "Has this already been done? Which paper is closest?"
- "How do you know the gap is real — which count supports it?"
- "Who benefits if you succeed?"
- "What is your riskiest assumption?"
- "Can you run this with your compute?"
- "What would a negative result look like, and would it be publishable?"

</div>
<div>

#### Rubric (20 points)
| Criterion | Pts |
|---|---|
| Search is documented and reproducible (strings, dates, counts) | 3 |
| Matrix ≥10 rows, columns complete, split protocol recorded | 4 |
| Limitations supported by **counts**, not impressions | 3 |
| Gap is specific, evidenced, and correctly typed | 4 |
| Objectives are measurable and mark-able done/not-done | 3 |
| Contributions map 1:1 to the gap and are calibrated | 2 |
| Feasibility stated honestly (data, licence, compute, risk) | 1 |

<div class="good">

#### Day 1 takeaway
You now hold the two artefacts that decide a paper's fate long before writing begins: a **literature matrix** and an **evidenced research gap**. Tomorrow we turn them into a manuscript.

</div>

</div>
</div>

<!--
SPEAKER NOTES — Closing Day 1 (30-40 min for presentations, 5 min close)
Timebox ruthlessly: 3 minutes presenting, 2 minutes questions. Use a visible timer.
Model the first two question rounds yourself so the room learns the register: specific, evidence-seeking, never personal.
Close with tonight's homework, which must be small and certain to be done: (1) set one email alert on your search string, (2) fix every metadata field in Zotero for your 10-15 papers, (3) bring the matrix tomorrow — Day 2 writing exercises all draw on it. Tell them Day 2 starts with paper anatomy and ends with a mini proposal, and that they will write their actual abstract before lunch.
-->
