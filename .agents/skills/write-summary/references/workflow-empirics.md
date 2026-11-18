# Workflow: Empirics Summary

Steps 2–7 for producing an empirical note or full report from pipeline outputs. Apply the relevant parts to the scope selected in Step 1.

---

## Step 2: Read the Code Pipeline

Read enough of the relevant pipeline to establish what the selected results measure and how they were produced. A full report may need a methodology section and appendix. A brief figure note may need only the source, sample, units, and qualifications in its captions.

- List scripts in `code/scripts/{tier}/{variant_name}/` (exploration/archive) or numbered scripts in `code/scripts/{tier}/` (core)
- Read the scripts producing the selected outputs and their dependencies: what data they load, what transformations they apply, and what they output
- Read relevant src modules in `code/src/mypackage/{tier}/{variant_name}/` for the pure logic
- Note which script produces which output file (for appendix cross-references)
- Extract mathematical operations that should become LaTeX equations

Also check `docs/{tier}/{variant_name}/` for any analysis notes the user may have written.

---

## Step 3: Read the Outputs in Scope

Read the outputs needed for the requested note or report, including evidence that qualifies or contradicts an included claim:

**Tables** (`output/{tier}/tables/{variant_name}/`):
- Read `.csv` files to understand the data (column names, values, sample sizes)
- Read `.tex` table files to see formatted results (coefficients, standard errors, significance stars)

**Figures** (`output/{tier}/figures/{variant_name}/`):
- View `.png` files to understand distributions, trends, comparisons

Identify what each selected output shows and the qualifications needed to interpret it. Use this to choose captions and any results discussion.

---

## Step 4: Identify Connections Across Results

Where the requested document combines results, look for:
- Results that explain or qualify each other
- Patterns recurring across multiple tables/figures
- Results that contradict or complicate each other
- A narrative arc: what story do these results tell together?

This cross-result analysis informs the Discussion and the Introduction.

---

## Step 5: Brainstorm Explanations & Conjectures

When interpretation is part of the request, consider plausible economic mechanisms and distinguish them from demonstrated findings. A figure extract need not add a conjectures section.
- What economic mechanisms could generate the key patterns?
- For each conjecture: (a) which results support it, (b) which complicate or contradict it, (c) what additional analysis or data would help distinguish between competing explanations
- Flag which conjectures are well-supported vs speculative
- Consider alternative interpretations: compositional artifact? Selection effect? Mechanical consequence of the methodology?

### Interpretation Patterns

**From coefficient to mechanism:**
- "The positive coefficient on X suggests that [mechanism], possibly because [channel]."
- Consider competing explanations where the evidence permits them
- Prefer mechanisms that are specific and falsifiable over vague ones

**Testing conjectures against data:**
- "If [mechanism A] drives this result, we would expect [prediction]. Table N [confirms/contradicts] this."
- Does a pattern in one table explain an anomaly in another?
- Do robustness checks strengthen or weaken the main finding?

**Distinguishing competing explanations:**
- "This pattern is consistent with both [A] and [B]. To distinguish them, one would examine [variable/subgroup]."
- Which explanation is most parsimonious? Consistent with the broadest set of results?

**Identifying artifacts vs. real effects:**
- Could the result reflect changes in sample composition rather than behavior?
- Is the result a tautological consequence of how variables are defined?
- Would a different estimation approach produce the same result?

**Framing null results:**
- A null result is information: "The absence of effect on [X], combined with the strong effect on [Y], suggests the mechanism operates through [channel Y]."
- Distinguish precise zeros (tight CI) from underpowered tests (wide CI)

**Synthesizing across results:**
- What is the central finding when all results are considered together?
- Clearly distinguish: well-established findings vs. suggestive patterns vs. speculative conjectures
- Use language that matches evidence strength: "demonstrates" vs. "suggests" vs. "raises the possibility"

The goal is to turn the summary from a report ("here's what we found") into a research document ("here's what we found, here's what it might mean, and here's how to tell").

---

## Step 6: Read the Template

Read `references/template-latex-empirics.tex` for the preamble and a full-report example. Retain the sections needed by the requested document.

---

## Step 7: Write the Summary (body first, introduction last)

The phases below describe a full report. For a brief note, use only the relevant parts. A figure note can consist of the selected figures, captions, and essential context. If an introduction is useful, write it after the findings it previews.

Use one main idea per paragraph and visible spacing. Begin each major section on a fresh page; a brief note can still have separate pages for distinct topics. Keep each figure with its caption and explanation. Add interpretation only where needed, without a fixed paragraph quota.

**Phase A — Methodology (main body, brief):**
- High-level overview: data sources, key methodological choices, estimation strategy
- Key equations from the src/ modules
- Point to the appendix for the detailed pipeline walkthrough

**Phase B — Results (one subsection per logical group):**
For each table or figure:
- Include via `\input{\outdir/tables/{variant_name}/{filename}}` or `\includegraphics[width=0.9\textwidth]{\outdir/figures/{variant_name}/{filename}.png}`
- Write a caption with descriptive text and a `\label{}`
- Add the interpretation needed for the requested scope. For a brief extract, a clear caption may be sufficient. For a report, explain patterns and connections in the text.
- Cross-reference related tables/figures via `\ref{}`

Where appropriate, create hand-coded summary tables that synthesize across multiple outputs.

**Phase C — Discussion:**
- Synthesize cross-result connections from Step 4
- Present the conjectures from Step 5: supporting evidence, complications, what further analysis could resolve each
- Distinguish well-supported explanations from speculative ones
- Central finding and its implications
- Limitations of the current analysis

**Phase D — Conclusion:**
- Main takeaways concisely
- Open questions and promising directions

**Phase E — Appendix A: Detailed Methodology:**
- Step-by-step pipeline walkthrough
- For each stage: what it does, key parameters, which script implements it
- Equations where code implements mathematical procedures

**Phase F — Appendix B: Additional Results (if applicable):**
- Robustness checks, variant comparisons
- Additional figures across pipeline variants

**Phase G — Introduction (written last):**
- Overview of the approach and key innovations
- Preview key findings (from results already written)
- Frame findings in terms of the conjectures — what they mean, not just what they show
- Set up the narrative arc: the introduction should make promises the body delivers on

### Assemble

- Compute `\outdir` relative path: from `docs/{tier}/{variant_name}/` to `output/{tier}/` = `../../../output/{tier}`
- Fill in the preamble and assemble the selected material. For a full report, a useful order is Introduction, Methodology, Results, Discussion, Conclusion, and any needed Appendices.

### Checklist

Apply the items relevant to the requested scope. Verify every included claim even in a brief note.

- [ ] Requested results included, with evidence needed to qualify their interpretation
- [ ] `\outdir` relative path is correct
- [ ] Each included table or figure has a label and enough caption or prose context to interpret it
- [ ] One main idea per paragraph, readable spacing, and separate pages for major sections; figures remain with their explanations
- [ ] Cross-references (`\ref{}`) link related results
- [ ] Connections across results are discussed
- [ ] Economic conjectures presented with supporting/contradicting evidence
- [ ] Hand-coded summary tables where needed
- [ ] Main methodology is brief; detailed pipeline in appendix with script references
- [ ] Introduction written last, reflects actual findings
- [ ] Document compiles without errors
- [ ] Auxiliary files cleaned up
- [ ] Included claims verified using Step 10 of `SKILL.md`, with figure references checked
