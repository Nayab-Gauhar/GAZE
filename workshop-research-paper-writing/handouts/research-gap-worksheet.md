# Research Gap Worksheet

Complete **after** your literature matrix has ≥10 rows. Patterns are invisible below about 10 papers.

---

## Step 0 · Import the matrix and set up tallies

Open `literature-matrix-template.csv` in Excel or Google Sheets. Freeze row 1, add a filter, then create a tally block. Adjust the column letters and row range to your sheet.

| Tally | Formula (Google Sheets / Excel) |
|---|---|
| Papers using a random split | `=COUNTIF(H2:H30,"*random*")` |
| Papers using a grouped/site-wise/temporal split | `=COUNTIF(H2:H30,"*site*")+COUNTIF(H2:H30,"*temporal*")` |
| Papers with ≤1 baseline | `=COUNTIF(M2:M30,"<=1")` |
| Papers reporting variance/CI | `=COUNTA(P2:P30)-COUNTIF(P2:P30,"none")` |
| Papers running a statistical test | `=COUNTA(Q2:Q30)-COUNTIF(Q2:Q30,"none")` |
| Papers reporting cost | `=COUNTIF(S2:S30,"yes")` |
| Papers releasing code | `=COUNTIF(T2:T30,"yes")` |
| Papers reporting metric X | `=COUNTIF(N2:N30,"*ECE*")` |
| Total papers | `=COUNTA(A2:A30)` |

**Read the columns, not the rows.** The tallies are your evidence.

---

## Step 1 · Five tally sentences

Write each finding as a sentence with numbers. These sentences go directly into your Introduction ¶4 and your Related Work synthesis paragraph.

1. Of ___ studies, ___ use ______________________________ .
2. Of ___ studies, ___ report ______________________________ .
3. ___ of ___ studies compare against ______________________________ .
4. No study (0 of ___) reports ______________________________ .
5. All ___ studies assume/require ______________________________ .

---

## Step 2 · Common limitations (L1–L5)

Each limitation needs a **count** and **2–3 supporting citations**.

| ID | Limitation | Count (n of N) | Supporting papers | Source of evidence (their words / my analysis) |
|---|---|---|---|---|
| L1 | | | | |
| L2 | | | | |
| L3 | | | | |
| L4 | | | | |
| L5 | | | | |

---

## Step 3 · The unresolved problem

One sentence. What does the field collectively not know or not have?

> ______________________________________________________________________

---

## Step 4 · Gap statement

Use the template. Fill every slot.

> "Across **[N]** studies identified by **[databases, strings, date range]**, **[pattern with counts]** holds. Consequently, **[specific quantity or mechanism]** remains **[unquantified / untested / unexplained]**, even though **[why it matters and to whom]**. This study addresses that by **[action]**."

**My gap statement:**

> ______________________________________________________________________
> ______________________________________________________________________
> ______________________________________________________________________

### Gap type classification (tick all that genuinely apply — usually 2–3)

☐ 1 Knowledge ☐ 2 Methodological ☐ 3 Dataset/resource ☐ 4 Performance
☐ 5 Application/translation ☐ 6 Population/domain ☐ 7 Evaluation ☐ 8 Scalability
☐ 9 Generalisation ☐ 10 Reproducibility ☐ 11 Computational efficiency ☐ 12 Explainability

### Weak-gap self-check — my statement is **not** any of these

☐ "There is room for improvement"
☐ "Nobody has applied method X to dataset/domain Y" *(no mechanism, no measurement)*
☐ "Accuracy is low" *(unquantified, no threshold)*
☐ "No one has combined A and B" *(combination without a reason to expect different behaviour)*
☐ "The topic is new/trending"
☐ "No work exists in my country/language" *(without a mechanism for why results would differ)*
☐ "Prior work is old"
☐ Contains no numbers
☐ Claims absolute absence without a documented search

---

## Step 5 · Gap → contributions (1:1 mapping)

| Gap element | Contribution | Type | Needs new theory? | Compute needed | Feasible for me? |
|---|---|---|---|---|---|
| | C1 | | | | |
| | C2 | | | | |
| | C3 | | | | |

Contribution types: new method · new theory/analysis · new empirical knowledge · new resource · new evaluation protocol · synthesis · reproduction/refutation.

---

## Step 6 · Stress test (partner or supervisor must ask all six)

| Question | My answer | Survived? |
|---|---|---|
| Has this been done? Which paper is **closest**, and how exactly does mine differ? | | ☐ |
| How do you **know** the gap is real — which tally supports it? | | ☐ |
| **Who benefits** if you succeed, outside your institution? | | ☐ |
| What is your **riskiest assumption**? | | ☐ |
| Can you do this with **your** data, compute and time? | | ☐ |
| What would a **negative result** look like — and would it still be publishable? | | ☐ |

If the last question's answer is "no", the study is engineering advocacy rather than research. Reframe before proceeding.

---

## Step 7 · Feasibility line

| Item | Value |
|---|---|
| Dataset(s) + licence + access route | |
| Baseline repositories (URLs), verified runnable? | |
| Metrics + statistical test | |
| Estimated GPU-hours (configs × seeds × datasets × 3 for reruns) | |
| Ethics approval needed? Route? | |
| **Killer risk** (the one thing most likely to sink this) | |
| Mitigation for the killer risk | |
