# Reviewer Response Template

Use the table format. Every comment gets a response, a change, and a **location**.

---

## Cover note to the editor

> Dear Prof. **[Editor]**,
>
> Thank you for the opportunity to revise our manuscript **[MS-ID]**, *"**[title]**"*. We are grateful to the reviewers for their careful reading; the revision is substantially stronger as a result.
>
> We have addressed all **[N]** comments. The principal changes are: **(1)** all experiments rerun with 10 seeds and paired significance tests (new §V-B); **(2)** an equalised hyperparameter budget for every method (new Table VII); **(3)** a new leave-one-site-out evaluation (new §V-E, Fig. 5); and **(4)** an expanded limitations discussion (§VI-B).
>
> A point-by-point response follows. New and modified text is highlighted in the marked-up manuscript; page and line numbers refer to that file. We have retained our original choice on one point (R2's suggestion regarding accuracy as the primary metric) and explain our reasoning in response R2.3, together with the additional information we have added to address the underlying concern.
>
> Sincerely, **[Corresponding author]** on behalf of all authors

---

## Point-by-point response table

| # | Reviewer comment (verbatim, abbreviated if long) | Our response | Change made + exact location |
|---|---|---|---|
| **R1.1** | | We thank the reviewer… We agree that… | Revised §__, p. __, ll. __–__; new Table __ |
| **R1.2** | | | |
| **R1.3** | | | |
| **R2.1** | | | |
| **R2.2** | | | |
| **R3.1** | | | |

Quote your new text verbatim inside the response cell where it is short, so the reviewer does not have to hunt:

> *Added text (§V-B, p. 8, ll. 355–362):* "All methods were retrained with ten random seeds. Differences are assessed with paired Wilcoxon signed-rank tests and 95% bootstrap confidence intervals (1,000 resamples); reported p-values are Holm-corrected across the five architectures."

---

## The five-part response pattern

1. **Thank** — one short clause, not a paragraph.
2. **Restate** the concern in your own words, so it is clear you understood it.
3. **Act** — what you changed, or why you did not.
4. **Locate** — section, page, line numbers, table/figure numbers.
5. **Evidence** — the new number, citation, definition, or computation.

---

## Response patterns by comment type

### (a) Valid criticism you can fix
> "We agree. We have rerun all experiments with 10 seeds and report paired Wilcoxon tests with 95% bootstrap CIs. The improvement remains significant (p = 0.004, Cohen's d = 1.6). See revised Table II and new §V-B (p. 8, ll. 355–372)."

### (b) A request you cannot fulfil — name the constraint, then satisfy the concern another way
> "We were unable to obtain a fourth institution-disjoint public dataset with the required labels within the revision period; the two candidates we identified lack finding-level annotations (now noted in §VI-B). To address the underlying concern about generality, we have added a **leave-one-site-out** evaluation across the three existing datasets, yielding five held-out site configurations (new §V-E, Fig. 5). We have also stated this residual limitation explicitly (p. 11, ll. 502–511)."

### (c) A misunderstanding — never blame the reviewer
> "We apologise that this was unclear. Our splits are institution-disjoint, not merely patient-disjoint; the original phrasing did not make this explicit. We have rewritten §IV-B and added a schematic of the split construction (Fig. 2), p. 5, ll. 198–214."

### (d) Legitimate disagreement — the four-step pattern
1. Acknowledge the concern as reasonable.
2. State your position plainly.
3. Give **evidence**, not preference.
4. **Concede something** so the concern is visibly served.

> "We appreciate this concern and have considered it carefully. Because pneumothorax prevalence is 1.2%, accuracy is dominated by the negative class: a constant-negative predictor attains 98.8% accuracy with zero recall. We therefore retain average precision and recall at fixed specificity as primary metrics. To address the reviewer's underlying interest in comparability with prior work, we have **added accuracy to Table II** and justified our metric choice explicitly in §IV-D (p. 6, ll. 268–274)."

### (e) Reviewers who conflict with each other
> "We note that R1 requests a shorter related-work section while R3 requests additional coverage of test-time adaptation. We have resolved this by condensing the capacity-scaling discussion (§II-A, now 40% shorter) and adding a focused paragraph on test-time adaptation (§II-C). We would welcome the editor's guidance if a different balance is preferred."

### (f) A positive comment
> "We thank the reviewer for this positive assessment."

---

## Phrases to avoid

| Never write | Write instead |
|---|---|
| "The reviewer clearly did not read the paper." | "We apologise that this was unclear; we have expanded §III-B." |
| "This comment is wrong." | "We respectfully retain our original choice, for the following reason: …" |
| "As already stated on page 4…" | "This was stated only briefly; we have now made it explicit in §III-B." |
| "This is beyond the scope of our work." | "This is an important question that we cannot address within the available data; we have added it as a stated limitation and future direction (§VI-B)." |
| "We have added a discussion." *(vague)* | "We have added §V-E and Fig. 5 (p. 9, ll. 402–431)." |

---

## Revision tracking checklist

- [ ] Every comment numbered and answered — including positive ones
- [ ] Every response gives a **precise location** (section, page, lines, table/figure)
- [ ] New text quoted verbatim in the letter where short
- [ ] Marked-up manuscript prepared (`latexdiff`, `\hl{}`, or Word track changes)
- [ ] Clean manuscript prepared for typesetting
- [ ] No undisclosed changes; nothing silently deleted
- [ ] Tone checked by a co-author who did not write the response
- [ ] Deadline met, or an extension requested **before** it passed
- [ ] Version tagged in Git (`v2-r1-response`)
- [ ] Abstract numbers updated if any result changed
- [ ] All new claims supported by new evidence in the manuscript — **nothing asserted only in the letter**

---

## Practice set (for Activity 24.1)

Write a full response-table entry for each.

| # | Comment |
|---|---|
| **A** | "The paper reports results from a single run. Given known seed variance in these architectures, the claimed 0.014 improvement is not credible as presented." |
| **B** | "The authors should evaluate on at least two additional datasets from different countries to support the generality claim." |
| **C** | "Accuracy should be reported as the primary metric, as it is standard in this literature and allows comparison with earlier work." |

*Suggested handling:* **A** — valid, fix it (rerun with ≥10 seeds, add paired test and CIs). **B** — may be infeasible; name the constraint and satisfy the concern with leave-one-site-out or an added limitation. **C** — disagree using the four-step pattern; add accuracy for completeness while retaining the appropriate primary metric.

---

## Decision decoding

| Decision | What it means | What to do |
|---|---|---|
| Minor revision | Likely acceptance | Respond fully; do not expand scope |
| Major revision | Genuine interest, substantial work needed | Do the experiments — this is a success |
| Reject and resubmit | Often a major revision with a reset clock | Treat as major revision; keep reviewer goodwill |
| Reject | Wrong venue, or a fundamental flaw | Fix what the reviews exposed, then choose the next venue deliberately |

**Wait 48 hours** after receiving harsh reviews before drafting your response. Never reply on the day they arrive.
