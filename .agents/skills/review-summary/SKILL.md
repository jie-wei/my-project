---
name: review-summary
description: >-
  Review a summary document. Two modes: (A) empirics — fact-check numerical
  claims against pipeline outputs; (B) theory — audit mathematical proofs for
  logical gaps, incorrect claims, and missing boundary cases. Use this skill
  whenever the user asks to verify a summary, fact-check a draft, check a proof,
  review math, audit a theory note, or review a summary against data. Distinct from
  /review-manuscript (qualitative academic review) and /review-details
  (grammar/typos). Do NOT use for writing summaries (use /write-summary).
disable-model-invocation: false
argument-hint: "[summary to review, e.g. 'review the {variant_name} summary']"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Bash"]
---

# Review Summary

Review a summary document with fresh, harsh eyes. Treat every claim as potentially wrong until independently verified — both the summary AND the source materials it draws from.

**Input:** `$ARGUMENTS` — what to review (e.g., "fact-check the {variant_name} summary", "review the proof in {variant_name}", "audit the math in {variant_name}").

---

## Step 1: Identify the Review Scope and Mode

For empirical work, read the [file I/O guide](../../rules/standalone-file-io.md) before tracing the pipeline's inputs and outputs.

Locate the requested document or supplied proof from `$ARGUMENTS` and context. For a saved summary, use the given path or look under `docs/{tier}/{variant_name}/`. For a proof supplied in chat, review that text. If the necessary material is unavailable, identify what is missing.

Establish the requested scope and follow the [research reasoning conventions](../../rules/standalone-conventions.md#research-reasoning). A brief note can intentionally omit background or unrelated results. Check every included claim, its necessary qualifications, and any evidence needed to interpret it. A referenced result need not reproduce its proof, while a document claiming to provide a proof must supply a complete argument.

Check exposition against the same conventions: one main idea per paragraph, readable spacing, separate pages for major sections, and layered proofs. Report presentation problems separately from mathematical or numerical errors. Intentional page breaks and whitespace are not defects, and a short note needs no extra interpretation paragraphs merely to fill a template.

Choose the mode from the claims and sources. An equation sheet or mathematical argument is **Theory**, even without theorem environments. Numerical claims drawn from pipeline outputs are **Empirics**. For mixed documents, review each type of claim with the relevant workflow. Figure commands or output-directory existence alone do not determine the mode.

**Empirics:** Read `references/workflow-empirics.md` and follow it.

**Theory:** Read `references/workflow-theory.md` and follow it.

---

## Step 2–9: Mode-Specific Workflow

Follow the workflow file loaded in Step 1. It covers: reading sources, inventorying ground truth, reading the summary, verifying claims, and checking consistency.

---

## Step 10: Produce the Report

For a saved-document review, use the relevant workflow’s report format. For a review confined to chat, present the findings directly. In both cases, identify any unsupported claims and explain the reasoning or source comparison.

---

## Step 11: Save

For a saved-document review, save the report to `docs/quality_reports/reviews/{tier}/review-summary-{variant_name}.md`. Create the directory if needed and replace the previous report on re-run. For a review confined to discussion or a proof supplied in chat, return the findings in chat unless a saved report is requested.

---

## Principles

**Why treat everything as wrong until checked.** Both summaries and source notes can be written by LLMs. LLMs produce plausible-looking text with subtle errors — each step looks correct in isolation but the overall argument has a hole. Treat every claim as a conjecture until independently verified.

**Why read sources before the summary.** If you read the summary first, you'll be anchored to its framing. Reading the sources first lets you form an independent view, then compare. Discrepancies jump out.
