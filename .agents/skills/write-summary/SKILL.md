---
name: write-summary
description: >-
  Write or revise a LaTeX research document from existing results or discussion.
  Supports brief notes, equation sheets, figure notes, and full reports in
  empirics or theory. Use for a saved summary, report, or proof write-up.
  For a conversational recap, respond in chat. For implementing code use
  /write-code; for running new analyses use /analyze-data.
disable-model-invocation: true
argument-hint: "[what to summarize, e.g. 'summarize the {variant_name} results']"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Edit", "Bash"]
---

# Write Summary

Produce the requested LaTeX note or report for one variant. Empirical documents draw on pipeline outputs, and theory documents draw on current formulations and arguments.

**Input:** `$ARGUMENTS` — what to summarize (e.g., "summarize the {variant_name} results", "write up the {variant_name} findings").

---

## Step 1: Identify the Requested Document and Sources

Determine the requested scope, length, tier (core / exploration / archive), and variant_name from context. A conversational recap stays in chat. When a saved document is requested, infer its shape from the request.

- A figure note can consist of the selected figures with captions and essential qualifications.
- An equation sheet needs definitions, maintained assumptions, and the requested characterizing equations.
- A proof note can cover one result with a complete, layered argument: explain why the major steps suffice, then justify each step below it.
- A full report uses the sections needed to explain the broader analysis.

Follow the [research reasoning conventions](../../rules/standalone-conventions.md#research-reasoning), including the current assumptions and established notation. For empirical work, read the [file I/O guide](../../rules/standalone-file-io.md) to locate the variant's data and outputs.

Select the mode from the requested content and its sources. Theory and empirical material can coexist in one variant.

**Empirics:** Read `references/workflow-empirics.md` and the relevant outputs in `output/{tier}/{tables,figures}/{variant_name}/`. Use `references/template-latex-empirics.tex` as a starting point.

**Theory:** Read `references/workflow-theory.md` and the relevant notes in `docs/{tier}/{variant_name}/` or the current discussion. Use `references/template-latex-theory.tex` as a starting point.

For mixed content, apply each workflow to its relevant claims. If essential source material is missing, identify what is needed. A discussion already available in this chat can be the source without first creating intermediate notes.

---

## Step 2–7: Mode-Specific Workflow

Apply the relevant workflow to the requested deliverable. The templates illustrate full reports. For a brief note, retain the preamble, environments, and sections it actually needs.

---

## Step 8: Assemble & Save

- Create `docs/{tier}/{variant_name}/` directory (if not already present)
- Use the requested file when revising a document, preserving content outside the edit scope. For a new document, default to `docs/{tier}/{variant_name}/summary-{variant_name}.tex` unless the user specifies another name.
- **Important:** compile from the directory containing the `.tex` file so relative paths resolve correctly

---

## Step 9: Compile & Verify

- Compile the actual file selected in Step 8 from its containing directory, using `latexmk -xelatex <filename>.tex`.
- Inspect the affected PDF pages for readable paragraph and list spacing, clear proof layers, sensible page breaks, and unclipped equations or figures. Preserve the separate-page layout when shortening a note.
- Clean auxiliary files (`.aux`, `.log`, `.bbl`, `.blg`, `.out`, `.toc`, `.fls`, `.fdb_latexmk`, `.synctex.gz`)
- If compilation fails, fix the issues and recompile

---

## Step 10: Fact-Check

Verify every included numerical and mathematical claim, regardless of document length. For a brief extract of previously checked work, compare its equations, values, figures, labels, and qualifications directly with the sources.

Run `/review-summary` for a full report, a document containing a complete proof or substantive derivation, or an explicitly requested independent review. Scope the review to the requested content. Its report saves to `docs/quality_reports/reviews/{tier}/review-summary-{variant_name}.md`.

Fix numerical discrepancies and proof gaps, then recompile and recheck affected claims. If a claim cannot be established, identify the gap and label it as unresolved or conjectural. A short note must not conceal qualifications needed for its claims.

---

## Principles

**Separate ideas visibly.** Use one main idea per paragraph. Start major sections on fresh pages, including in short notes with distinct sections, and retain space between paragraphs and nested bullets. Keep figures with their explanations. Reduce unnecessary content rather than shrinking text or tightening spacing to reduce page count.

**Explain proofs in layers.** First give the few major steps and explain why they jointly imply the claim. Use top-level bullets for those steps and nested bullets for their assumptions, computations, supporting results, and cases. The [theory workflow](references/workflow-theory.md#proof-writing-guidance) gives the detailed pattern.

**Give results the context they need.** Include definitions, units, assumptions, and qualifications needed to interpret the selected material. Add economic interpretation where it serves the request. A clear caption can be sufficient for a brief figure note.

**When an introduction is useful, write it last.** It should accurately preview the results the document actually contains. A brief note can begin directly with its question, equations, or figures.
