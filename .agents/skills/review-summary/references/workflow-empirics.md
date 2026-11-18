# Review Workflow: Empirics

Steps 2–9 for fact-checking an empirics summary against pipeline outputs.

---

## Step 2: Read the Code Pipeline

Understanding which script produces which output is essential for knowing what source files to check against.

- List scripts in `code/scripts/{tier}/{variant_name}/` (exploration/archive) or numbered scripts in `code/scripts/{tier}/` (core)
- Read the scripts producing the outputs in scope and their dependencies to identify what they load, produce, and save
- Read relevant src modules in `code/src/mypackage/{tier}/{variant_name}/`
- **Trace the full I/O chain**: for each script, verify that it reads from the correct input paths and writes to the correct output paths for this variant
- Build a map: output file → script that produced it → input data it used

---

## Step 3: Read Sources for the Claims in Scope

Read the sources needed to verify the included claims and relevant qualifications:

**Tables** (`output/{tier}/tables/{variant_name}/`):
- Read `.csv` files — column names, values, sample sizes
- Read `.tex` files — formatted regression output

**Figures** (`output/{tier}/figures/{variant_name}/`):
- List all `.png` and `.pdf` files — these are the valid figure references

**Processed data** (`data/processed/{variant_name}/`):
- Read any `.csv` files that scripts use as intermediate inputs

Build a ground-truth reference from these files before reading the summary.

---

## Step 4: Read the Summary

Read the summary document section by section. For every number, statistical claim, or figure reference, note its location (section, approximate line) and what it claims.

---

## Step 5: Verify Numerical Claims

For each number in the summary — coefficients, standard errors, p-values, significance stars, N, R-squared, sample sizes, means, percentages, counts:

- Find the corresponding value in the source file
- Compare exactly (accounting for rounding conventions)
- If they don't match, record: location, claimed value, actual value, source path

The most common errors are transcription mistakes, stale numbers (pipeline rerun but summary not updated), and rounding inconsistencies.

---

## Step 6: Verify Regression Tables

For each `\input{}` command that pulls in a `.tex` table:

- Read the actual `.tex` file from the output directory
- Compare every coefficient, standard error, and significance star
- Check that column headers and variable labels match
- Flag any discrepancy

---

## Step 7: Verify Figure References

For each `\includegraphics{}` command:

- Extract the file path (resolve `\outdir` by reading the `\newcommand{\outdir}{...}` definition from the preamble, then resolving relative to the `.tex` file's directory)
- Confirm the file exists
- Flag any missing figures

---

## Step 8: Check Qualitative Claims

Verify prose characterizations against the data:

- "Large positive effect" — is the coefficient actually large and positive?
- "Significant at the 1% level" — does the source show significance at that level?
- "Increases monotonically" — does the data actually show monotonic increase?
- "Robust across specifications" — do the robustness checks actually confirm this?

Flag claims that mischaracterize the direction, magnitude, significance, or pattern in the data.

---

## Step 9: Check Relevant Omissions

Check whether the document omits a requested result or evidence that qualifies or contradicts an included claim. A short note may intentionally cover selected tables or figures. Report an omission only when it affects the requested coverage or the interpretation of a claim.

---

## Report Template

**If discrepancies found:**

```markdown
# Fact-Check Report: {variant_name}

**Date:** YYYY-MM-DD
**Summary:** docs/{tier}/{variant_name}/summary-{variant_name}.tex
**Status:** DISCREPANCIES FOUND

## Numerical Errors

1. **[Section Name], line ~N:** Claims [value]. Actual value is [value] (source: `[path]`).

## Table Mismatches

1. **Table N (label):** [description of mismatch]

## Missing Figures

1. `\includegraphics` references `[path]` — file not found.

## Qualitative Errors

1. **[Section Name]:** Claims "[quoted text]". Data shows [actual pattern] (source: `[path]`).

## Relevant Omissions

These omitted outputs matter to the requested scope or an included claim:
- `[path]`
```

**If everything checks out:**

```markdown
# Fact-Check Report: {variant_name}

**Date:** YYYY-MM-DD
**Summary:** docs/{tier}/{variant_name}/summary-{variant_name}.tex
**Status:** CLEAN

All numerical claims verified against source files. All figure references valid. No omissions affecting the requested scope or the interpretation of included claims.
```
