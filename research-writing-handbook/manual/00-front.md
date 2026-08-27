# Research Paper Writing and Research Tools

## A Complete Practical Guide from Research Idea to Journal Publication

**A Training and Reference Handbook for PhD Scholars, Research Scholars, Postgraduate Students, Faculty Members, and Early-Career Researchers**

<div class="titlemeta">

Edition 1.0

Prepared as an independent-study and workshop manual

</div>

<div class="pagebreak"></div>

# Preface

This handbook exists because of a gap between two things that are both widely available and rarely connected.

The first is instruction in research *methods*: how to train a model, run a regression, design an interview protocol, compute a statistic. Most postgraduate programmes teach this reasonably well.

The second is instruction in research *practice*: how to decide what is worth studying, how to establish that nobody has established it already, how to construct an argument that a sceptical expert will accept, how to choose where to publish, and how to respond when three anonymous specialists tell you that your work is inadequate. This is usually transmitted by apprenticeship — absorbed from a supervisor, a lab culture, or a reading group — and when that apprenticeship is weak, absent, or overloaded, the researcher is left to reconstruct it alone. The visible symptoms are familiar: a scholar who has built an impressive system and cannot explain what is new about it; a manuscript desk-rejected in four days; a literature review that lists forty papers and concludes nothing; a "research gap" that amounts to *nobody has tried this combination yet*; three years of work published in a venue that no committee recognises.

This handbook is an attempt to write that apprenticeship down.

## What this handbook assumes

It assumes you can already do the technical work of your field, or are learning to. It does not teach machine learning, statistics, or qualitative coding. It teaches what to do with those skills so that the result becomes a defensible contribution to a permanent record.

It assumes you are working on something real. Every chapter ends with exercises that operate on *your* topic, not on a toy example. The handbook is designed to be worked through with a notebook and a laptop open, not read passively.

It assumes good faith and rewards it. A recurring theme is that the shortcuts available to a researcher under pressure — an unverified citation, a favourable subset of results, a paraphrase that is really a copy, a similarity score massaged below a threshold — are not merely unethical but *ineffective*, because they fail precisely at the point where the work is examined most closely.

## What this handbook is not

It is not a substitute for a supervisor, an ethics committee, or your institution's regulations. Where it describes general practice, your specific programme may impose stricter or simply different requirements, and those requirements win.

It is not a guide to gaming metrics. There is no chapter on raising your h-index. The premise throughout is that the durable strategy is to do work that is worth citing and to describe it accurately.

It is not current forever. Chapters 9, 16, 41–46 and 50–52 describe software platforms, database features, journal metrics, and publisher policies, all of which change — some of them yearly. Every such chapter therefore tells you *how to verify the current state of affairs from an authoritative source* rather than asking you to trust a printed description. Where this handbook and a publisher's own current documentation disagree, the publisher is right.

## A note on examples and on honesty

Two categories of example appear in this handbook, and they are deliberately distinguished.

**Real works** are cited normally and appear in the References. These are established, verifiable publications — foundational methods, well-known datasets, reporting guidelines, and published studies of research practice. You are encouraged to read them.

**Hypothetical examples** are constructed for teaching. The extended case study in Part XVII, the running example of cross-hospital chest-radiograph classification, the method named CLUSTER-DG, the placeholder papers labelled P1–P15, and every number attached to them are **invented for instructional purposes**. They are realistic — the underlying phenomenon is documented in real literature, cited where relevant — but they are not findings, and nothing in them may be cited. Wherever such material appears it is marked **[HYPOTHETICAL]**.

This distinction is not pedantry. A significant fraction of the integrity failures this handbook warns against begin with a plausible-looking example being copied out of a teaching document and into a manuscript. If you take one habit from this book, take the habit of opening every source you cite.

<div class="pagebreak"></div>

# How to Use This Guide

## Four ways in

**1. Sequentially, as a course.** Parts I–VII cover everything that happens before you run an experiment; Parts VIII–IX cover producing trustworthy evidence; Parts X–XIII cover writing and tooling; Parts XIV–XVI cover ethics and publication. Worked in order, with the exercises, this is roughly a semester of part-time study and will take you from an unfocused interest to a submitted manuscript.

**2. By current stage.** Use the table below.

| If you are here right now | Start at |
|---|---|
| I have an interest but no topic | Chapter 4 |
| I have a topic but it feels too broad | Chapter 4, §4.3; Chapter 5 |
| I have read some papers but cannot find a gap | Chapters 13, 15, 17–19 |
| I have a gap; I do not know what to promise | Chapters 6, 7, 20, 21 |
| I am designing experiments | Chapters 22–26 |
| I have results and cannot start writing | Chapter 30 onwards; and §29.1 |
| I have a draft and it feels weak | Chapters 31–37; Part XVIII checklists |
| I am choosing a journal | Chapters 50–52 |
| I have reviewer comments | Chapter 56 |

**3. As a reference.** The chapters on evaluation metrics (27), research gaps (17), search strategies (10), and journal verification (51–52) are written to be consulted in isolation. Each defines its own terms.

**4. As teaching material.** Every chapter contains exercises, common-mistake tables, and checklists that can be lifted into a workshop or a lab meeting. Part XVIII and the Appendices are reusable templates.

## The structure of a chapter

Most substantive sections follow a fixed pattern, so you can navigate to the part you need:

> **Definition** → **Purpose** → **Detailed explanation** → **Step-by-step procedure** → **Example** → **Common mistakes** → **Best practices** → **Tools** → **Verification checklist**

Not every section needs all nine elements, and they are omitted where they would be padding.

## Conventions

| Convention | Meaning |
|---|---|
| **[HYPOTHETICAL]** | Invented for teaching. Not a finding. Do not cite. |
| **[VERIFY]** | Platform features, metrics, or policies that change. Check the authoritative source named. |
| ❌ / ✅ | A weak example followed by an improved version of the same thing |
| *Exercise n.n* | Work to do on your own topic |
| **Fact** vs **Recommendation** | Where a claim could be mistaken for consensus, the handbook states which it is |

## The single most important idea in this handbook

If you read nothing else, read this.

A research paper is not a report of what you did. It is an **argument** that something is now known which was not known before, supported by evidence a sceptic would accept. Every section of a paper exists to defend one link in that argument. Work that cannot be expressed as such an argument may still be valuable — as software, as a service, as a thesis chapter — but it will not survive peer review at a serious venue, because there is nothing for the reviewer to be convinced *of*.

Most of this handbook is the practical consequence of that one sentence.

<div class="pagebreak"></div>

# List of Figures

| Figure | Title |
|---|---|
| 1.1 | The relationship between activity, evidence, and contribution |
| 2.1 | Choosing a research type from a research question |
| 3.1 | The research lifecycle, with feedback paths |
| 3.2 | Where time is actually spent versus where beginners expect to spend it |
| 4.1 | The narrowing funnel: from research area to research objective |
| 5.1 | Anatomy of a problem statement |
| 7.1 | Aim, objectives, questions, hypotheses, and contributions |
| 8.1 | Consequences of a weak literature review, by stage |
| 10.1 | Building a search string from concept blocks |
| 10.2 | Citation chaining: backward, forward, and sideways |
| 12.1 | The three-pass reading method |
| 14.1 | Paper-by-paper listing versus critical synthesis |
| 15.1 | Reading a literature matrix by column rather than by row |
| 18.1 | From fifteen papers to a defensible research gap |
| 20.1 | Degrees of novelty |
| 22.1 | Methodology as the bridge from objectives to evidence |
| 23.1 | Data leakage pathways |
| 26.1 | Splitting schemes and when each applies |
| 27.1 | The confusion matrix and the metrics derived from it |
| 27.2 | ROC versus precision–recall under class imbalance |
| 28.1 | Misleading and honest presentations of the same result |
| 29.1 | The boundary between Results and Discussion |
| 32.1 | The six-paragraph introduction, as a pressure curve |
| 38.1 | Anatomy of a good architecture diagram |
| 40.1 | From prose description to pseudocode to implementation |
| 46.1 | The verification loop for AI-assisted research |
| 48.1 | Interpreting a similarity report |
| 55.1 | The peer-review process and its decision points |
| 57.1 | The case study, end to end |

# List of Tables

| Table | Title |
|---|---|
| 1.1 | Research versus project development |
| 1.2 | Validity, reliability, reproducibility, generalizability |
| 2.1 | Research types, questions they answer, and typical evidence |
| 3.1 | Lifecycle stages: inputs, outputs, decisions, mistakes, tools |
| 4.1 | Five constraints on the choice of a research area |
| 5.1 | General problems transformed into research problems |
| 6.1 | Question types and the study designs they imply |
| 7.1 | Weak and strong research objectives |
| 9.1 | Research databases compared |
| 10.1 | Boolean operators and field codes by platform |
| 10.2 | Ineffective and effective search queries |
| 11.1 | What to extract from each section of a paper |
| 12.1 | Reading passes: time, coverage, and output |
| 13.1 | The sixteen-field extraction framework |
| 15.1 | Literature matrix fields and why each earns its place |
| 16.1 | Literature tools: purpose, workflow, limitations, verification |
| 17.1 | Thirteen types of research gap |
| 19.1 | Weak and strong gap statements |
| 21.1 | Weak and strong contribution statements |
| 23.1 | Dataset selection criteria |
| 24.1 | Preprocessing decisions and their documentation requirements |
| 25.1 | Model families and the conditions that justify them |
| 26.1 | Baseline categories |
| 27.1 | Classification metrics: use and misuse |
| 27.2 | Regression metrics: use and misuse |
| 27.3 | Detection and segmentation metrics |
| 27.4 | Metric selection by problem situation |
| 29.1 | Results language versus Discussion language |
| 30.1 | Weak and improved titles |
| 31.1 | The seven moves of an abstract |
| 33.1 | Citation practices |
| 39.1 | Table types and their required columns |
| 42.1 | LaTeX constructs for academic papers |
| 45.1 | AI tools: capability and verification burden |
| 46.1 | Prompt library index |
| 47.1 | Forms of plagiarism |
| 49.1 | Categories of research misconduct |
| 50.1 | Venue types compared |
| 51.1 | Journal metrics: source, definition, and caveat |
| 52.1 | Predatory-journal warning signs |
| 53.1 | Pre-submission checklist |
| 56.1 | Reviewer response patterns |

<div class="pagebreak"></div>
