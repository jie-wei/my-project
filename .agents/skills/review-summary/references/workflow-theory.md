# Review Workflow: Theory

Steps 2–9 for auditing a theory summary's mathematical correctness.

**Mindset:** Treat everything as wrong until you have independently checked it — both the summary AND the source notes it draws from. The most valuable catches are not algebra typos but structural gaps: proofs that claim to handle all cases but actually leave one open.

---

## Step 2: Read the Source Math Formulations

Start with the user's current question, agreed notation, and maintained assumptions. Read the relevant source notes or supplied discussion. Files such as `question.md`, `definitions.md`, `assumptions.md`, `findings.md`, `results/`, and earlier reviews can help when available. A particular notes structure is not required.

Check whether each earlier result still applies to the current model. Treat superseded formulations as historical context. Source notes and result-status labels are evidence to verify, and an unresolved conflict affecting the claim should be identified explicitly.

Build an independent understanding of:
- What is the question?
- What results are established (active) vs. superseded?
- What is the logical dependency tree?
- What are the key mathematical objects and their properties?

When separate sources are available, form an independent view before assessing the summary. When the supplied proof is the only source, check its premises and reasoning directly.

---

## Step 3: Check Source Status

Distinguish current assumptions, established results, conjectures, and superseded claims. Verify these labels against the actual arguments.

---

## Step 4: Read the Summary

Read the requested note or proof end-to-end. For each mathematical claim and included proof step, note:
- What is claimed (the formal statement)
- What is the proof strategy
- What assumptions are used

---

## Step 5: Verify Each Proof Step

Work **top-down**: start by asking "is the main conclusion even true?" and try to construct counterexamples. If you can't, work backward through the proof steps.

**First pass — challenge the conclusion:**
- Assume the theorem is wrong. What would a counterexample look like?
- Try to construct one. Failure to find a counterexample does not establish the theorem. Identify which claims still require proof.
- If you can construct one, the proof has a gap. Find it.

**Second pass — check each step:**
- Does the conclusion actually follow from the premises?
- Are there implicit assumptions that are not stated?
- Is the proof complete, or does it only handle the "generic" case and miss boundaries?

**Check the proof's layers:**
- Does the opening strategy explain why the few major steps jointly imply the conclusion, rather than merely naming steps?
- Do the top-level bullets state those steps and their roles, with the reasons, calculations, and cases nested beneath the step they support?
- Does each lower-level argument establish its parent claim without circular dependence? Can the reader follow the strategy before reading the details?

A missing justification is a proof gap. Correct reasoning presented as a crowded or flat list is an exposition issue; distinguish these in the report.

**Boundary and degenerate cases:**
- What happens at the extremes of parameter ranges?
- Are there edge cases where a strict inequality becomes an equality, breaking the argument?
- Does the proof handle all possible configurations, or only the "obvious" ones?

**Quantifier errors:**
- Does a "for all" claim actually hold for all cases, or only for a subset?
- Does an "exists" claim actually have a valid construction?
- Are uniqueness claims truly ruling out all alternatives, or just the obvious ones? (Common failure mode: a proof rules out the "natural" alternatives but misses an exotic construction.)

---

## Step 6: Check Cross-References

- Does each lemma that cites a prior result actually use it correctly?
- Are the dependency claims accurate (e.g., "By Lemma 3" — does Lemma 3 actually give what's needed)?
- Are there circular dependencies?

---

## Step 7: Verify Consistency with Source Notes

**Treat both the summary AND the source notes as potentially wrong.** The source notes may also contain errors. Your job is to independently verify the math, not to rubber-stamp either document.

- Does the summary accurately represent what was proved in the notes?
- Are any results marked as "superseded" in the notes but presented as active in the summary? (Note: the summary may intentionally correct or update the notes — flag the discrepancy but don't assume the notes are right.)
- Does the summary's logical flow match the dependency tree from the source notes?
- Does the note omit a result or qualification needed for its stated purpose or included claims? Results outside the requested scope need not be included.
- **Critically: do the source results themselves contain errors?** If you find a bug in a source `.md` result file, report it — this is the most valuable kind of catch.

---

## Step 8: Check Notation and Definitions

- Are all symbols defined before use?
- Is notation consistent throughout (same symbol for the same object)?
- Follow the shared notation policy. Preserve established symbols and model primitives. Suggest optional shorthand when useful, and do not treat an expanded primitive expression as a defect.

---

## Step 9: Assess Scope Claims

- Does the "Discussion" or "What is established" section accurately describe the scope?
- Are the "remaining gaps" genuinely open, or have they been resolved in the source notes?
- Are the assumptions identified as the ones that actually drive the results?

---

## Report Template

```markdown
# Math Review Report: {variant_name}

**Date:** YYYY-MM-DD
**Summary:** docs/{tier}/{variant_name}/summary-{variant_name}.tex
**Status:** CLEAN | ISSUES_FOUND

## Summary
- CRITICAL: [N] (proof gaps that invalidate a claim)
- MAJOR: [N] (missing boundary cases, incomplete arguments)
- MINOR: [N] (notation issues, unclear exposition)

## Critical Issues

1. **[Lemma/Theorem N], [section]:** [description of the gap]. The proof claims [X] but does not rule out [Y]. [Why this matters for the overall argument.]

## Major Issues

1. **[Lemma N], boundary case:** [description]. The proof works for [generic case] but fails when [boundary condition]. [Suggested fix or what needs to be checked.]

## Minor Issues

1. **[Section], line ~N:** [notation inconsistency / unclear step / missing definition]

## Consistency with Source Notes

- [Any discrepancies between summary and source .md files]
- [Any errors found in the source notes themselves]

## Scope Assessment

- [Whether the "what is established vs. open" section is accurate]
```

When a proof gap invalidates a claim, recheck the underlying source result and identify which conclusions depend on it.
