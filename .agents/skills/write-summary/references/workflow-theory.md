# Workflow: Theory Summary

Steps 2–7 for producing a self-contained proof walkthrough from math formulation notes.

---

## Step 2: Read the Math Formulations

The source material typically lives in `docs/{tier}/{variant_name}/` and follows the structure produced by `/solve-econ-as-math`. Read files in this order:

**1. `question.md`** — The model specification, the question, and verification conditions. This tells you what the summary needs to explain.

**2. `definitions.md`** and **`assumptions.md`** (if present) — The shared vocabulary and assumptions in force. These determine the notation and scope.

**3. `findings.md`** — The central document. Contains the guided proof walkthrough, the logical dependency tree, and the result index with statuses. Start here for the big picture: what was the answer, what are the key steps, what is the proof architecture.

**4. `results/` directory** — Individual result files (one per lemma/theorem), each with IF/THEN/BECAUSE/FAILS WHEN structure. Read these for the detailed proofs and boundary conditions.

**5. Any `reviews/` files** — Past review reports that may flag known issues or superseded results.

From these, extract:
- The logical dependency tree: which results build on which
- The status of each result (active, superseded, open) — check the result index in `findings.md`
- The key definitions, lemmas, theorems, and their proofs
- What is established vs. what remains open

If the source material does not follow this structure (e.g., it's just free-form notes), read all `.md` files and reconstruct the dependency tree yourself.

The summary document should follow the logical flow of the proofs, not the chronological order of discovery. Use the dependency tree to determine the right presentation order.

---

## Step 3: (No separate scan step — the "outputs" are the result files themselves.)

---

## Step 4: Map the Proof Architecture

- Identify which results close gaps vs. open new questions
- What is the main theorem? What are the supporting lemmas?
- What is the logical skeleton: which lemmas feed into which?
- Are there alternative proof paths?

This architecture determines the document structure.

---

## Step 5: Plan the Discussion

Think like a theorist. This planning informs what goes in the Discussion section, not the proofs themselves (all proofs should be detailed regardless).

- Translate mathematical results back to economic language
- Note which steps carry the real insight vs. which are routine
- What are the key mathematical properties that drive the result?

### Interpretation Patterns

**What drives the result:**
- Identify the 1-2 key mathematical properties that make the proof work (e.g., convexity, monotonicity, a cancellation)
- State them explicitly: "The proof relies on [property]. Without it, [what would break]."

**What the result does NOT depend on:**
- List aspects of the model that the proof never touches
- "The argument works for any [object] satisfying [condition] — it never examines [aspect]."
- This is where the reader learns the true scope of the theorem

**Where the intellectual content lives:**
- Routine steps: standard arguments. Acknowledge them but don't dwell in the Discussion.
- Key steps: the moves specific to this problem. These deserve intuition paragraphs and discussion of what would happen if they failed.
- Surprising steps: results that contradict naive intuition. Flag them.

**Connecting results to economics:**
- "Lemma N says [math]. Economically, this means [plain language]."
- When a parameter changes, trace through the proof to see which steps are affected.

**Remaining gaps and open questions:**
- Be precise about what is proved vs. assumed vs. conjectured
- State assumptions clearly: "The argument assumes [X]. Whether this is without loss is [open/proved elsewhere]."
- What happens if the model is generalized? Which proof steps would survive, which would break?
- State conjectures precisely with evidence for/against from the current proof structure

---

## Step 6: Read the Template

Read `references/template-latex-theory.tex` for the proof walkthrough structure. Key patterns:
- Opening overview states the question, answer, and ordered proof strategy
- Setup holds primitives and maintained assumptions only
- Each results section defines its objects at first use, motivates and states the theorem, then explains the supporting lemmas' roles
- The assembly proof precedes shared inputs and the supporting lemmas, with one logical move per bullet
- Closing discussion identifies the result's scope, maintained assumptions, and remaining gaps
- Optional appendix for alternative proofs or extensions

---

## Step 7: Write the Summary (body first, opening overview last)

The document is a self-contained proof walkthrough. Use a standalone article class with theorem environments. Do not use the empirics template.

### House style (the user's standing rules — apply to every theory summary)

These were established line-by-line with the user (2026-07-30, `summary-cs_floor`
revision round) and are non-negotiable defaults. Each carries its reason — the
reasons matter, because they tell you how to apply the rule in a new situation.

1. **One logical point per line.** Proof bodies are `itemize`/`enumerate` with one
   move, one claim, or one case per bullet; sub-bullets for case splits (but avoid
   depth > 3 — deep nesting recreates the confusion bullets exist to kill). The
   user audits line-by-line; packed prose hides the logical skeleton.
2. **Every summation/product index carries explicit bounds.** Never `\sum_k`;
   write `\sum_{k=1}^{K}`, `\sum_{j=k}^{K}`, or an explicit index set
   `\sum_{S \in \pi}`. A bare index leaves the range ambiguous.
3. **Statement-local hypotheses.** No ambient scope declarations ("types are
   uniform from here on"). Every lemma/theorem restates its full hypothesis set
   inline — distribution, domain, parameter ranges — so it reads correctly in
   isolation. Put parameter ranges in the hypothesis or trailing in the display
   (`..., for K ≥ 3.`), never only in the lemma's *name*.
4. **Definition at first use.** Define each object (and each welfare aggregate) at
   the top of the section that first uses it — not in a global setup. The setup
   holds only primitives and the market description.
5. **Minimal notation; state only what you use.** A symbol earns its place only if
   used pervasively (rule of thumb: a symbol used in ≤ 5 places is written out
   inline instead). Don't state a general form of a lemma if only a special case
   is ever cited — and conversely, don't scope a lemma narrower than its uses.
   Audit both directions before finalizing: "is this fact ever used?" and "is
   anything used but unstated?"
6. **Registered/benchmark notation in statements; raw computation in proofs.**
   Statements speak the project's named quantities; fractions and algebra appear
   only inside proofs where the computation needs them.
7. **Argument-explicit functions in statements.** Objects that depend on a
   configuration are written as functions of it in statements (e.g.
   `CS(b_1,...,b_K)`), with a one-sentence convention allowing the bare symbol
   inside proofs where the configuration is fixed. This answers "surplus *of
   what*?" inside every statement.
8. **Motivation prose before each theorem, paper-style.** A short flowing
   paragraph (not bullets) giving the economics: the forces at play, why the
   result should hold, and its message in words — so the formal statement lands
   as a crystallization, not a formula to decode.
9. **Strategy paragraph after the statement, with per-lemma roles.** Name the
   proof's parts and give each supporting lemma's role in one clause (bulleted if
   3+ parts). Flag where the crux is and where each key assumption first enters.
10. **Assembly before lemmas.** Give the main theorem's proof (the assembly,
    forward-citing the lemmas) *before* the lemmas, so each lemma arrives with
    its role already fixed. Shared inputs used by several lemmas (e.g. a system
    of first-order conditions) get their own numbered display before the lemmas
    — never buried inside one lemma's proof and silently used by another.
11. **Every claim computes, cites, or justifies.** No bullet may assert. Each
    carries its two-line reason, a `\ref`/`\eqref`, or an explicit computation.
    Case analyses must be exhaustive and each case must carry the *correct*
    reason (watch for cases that share a conclusion but need different
    arguments).
12. **Self-contained: internal citations only.** Cite the source paper by
    equation/observation number; never cite project-internal ledgers or notes a
    fresh reader cannot see. If an external result is needed, either prove it
    inline in two lines or reproduce its statement.
13. **Layout:** each section after the first starts on a new page (`\clearpage`);
    the main theorem's proof may also start a fresh page if its section is long.
    Figures are non-floating (`center` or `[H]`), placed where the text needs
    them, sized so they never occupy a page alone; prefer no caption when panel
    titles carry the message.
14. **No meta-commentary in the text.** Never explain *why the document* does
    something ("G is needed only because..."); just do it. Redundant restatements
    (saying one fact two ways) are deleted — state the strongest true form once.

**Phase A — Overview:**
- State the question precisely
- State the answer (theorem/result)
- Roadmap of the document sections

**Phase B — Setup (primitives only):**
- Model primitives and the market description, as bullets (house rule 1)
- The maintained assumption, stated once with what is proved vs. maintained
- NO welfare aggregates, no benchmarks, no derived objects — those are defined
  at first use in their sections (house rule 4)

**Phase C — Results (one section per step/theorem):**

For each theorem, in this order (house rules 8–10):
1. Definitions the section needs (first use)
2. Motivation prose (economics, in words)
3. The theorem, with full inline hypotheses (house rule 3)
4. Strategy paragraph with per-lemma roles
5. The assembly proof (forward-citing lemmas)
6. Shared inputs as numbered displays, then the lemmas with bulleted proofs

- Cross-reference via `\ref{}`/`\eqref{}` — every dependency is a visible link
- **Notation:** use model primitives directly in equations rather than introducing shorthand notation. If you notice a recurring expression that would benefit from shorthand, suggest it to the user — they can approve it and register it as project notation. Do not introduce shorthand on your own.

**Proof format.** Two shapes, chosen per proof (house rule 1 governs both):

- **Bulleted proofs** (the default): `itemize` with one move per bullet; each
  bullet computes, cites (`\ref`/`\eqref`), or carries its two-line reason.
  `enumerate` when the moves are a named sequence; sub-bullets for case splits.
- **Derivation chains** (for the key regrouping/identity steps): an `align*`
  block with one equality per line and the justification alongside via
  `&& \text{...}` — "the definition", "insert eq. (1)", "the swap: who pays for
  slab j?". Expand the key step in full even when a compressed one-liner would
  verify; the chain teaches, the one-liner only certifies.

The goal is a proof that *teaches*, not just verifies. A reader should finish able to replicate the argument on a different problem. Every step is a decision point; the format makes those decisions explicit.

```latex
% Pattern for a bulleted proof (the default):
\begin{proof}
\begin{itemize}
  \item [one move: a computation, or a claim with its two-line reason];
  \item By \eqref{eq:X}, [next move];
  \item [case split:]
    \begin{itemize}
      \item [case A, with its own correct reason];
      \item [case B, with its own correct reason]. \qedhere
    \end{itemize}
\end{itemize}
\end{proof}

% Pattern for a key derivation chain:
\begin{align*}
X &= [\text{first form}]
  && \text{the definition; [what enters here]}\\
  &= [\text{second form}]
  && \text{insert \eqref{eq:X}}\\
  &= [\text{third form}]
  && \text{[the named crux move, in words]}
\end{align*}
```

**Key principles:**
- **Derive forward** — start from the object in question and work toward the conclusion. Never state the answer first and verify backward.
- **Every algebraic step must be justified** — name the rule, check the conditions, explain the content. Do not skip "obvious" steps.
- **Proofs should be detailed and crystal clear.** Every step should be expanded enough that a reader with fresh eyes can follow without filling in gaps. Do not compress proofs for brevity — clarity is the priority. If a step takes half a page, that's fine.
- **Flag the hard steps.** If a step is the intellectual crux (not just bookkeeping), say so in the commentary. This helps the reader distinguish routine algebra from the moves that carry real mathematical content.

**Phase D — Discussion:**
- What the argument does NOT use (clarifies generality): identify the 1-2 key mathematical properties that drive the result and what would break without them
- What the argument does NOT depend on: aspects of the model the proof never touches
- Remaining gaps: what is assumed but not proved
- Which steps are routine vs. where the real intellectual content lives

**Phase E — Opening overview (written last):**
- Question, answer, and proof strategy in miniature
- Preview the key steps and where the intellectual content lives

### Assemble

- No `\outdir` needed (no external figures/tables to reference)
- Assemble in document order: opening overview, Setup, one results section per step/theorem, closing discussion, optional Appendix

### Checklist

- [ ] Question and answer stated upfront in the opening overview
- [ ] Every proof bulleted, one move per bullet; key identities as align chains
      with per-line justifications (house rules 1, 11)
- [ ] All summation/product indices carry explicit bounds (house rule 2)
- [ ] Every statement carries its full hypotheses inline; no ambient scope
      (house rule 3)
- [ ] Every object defined at first use; setup holds primitives only
      (house rule 4)
- [ ] Notation audit run both directions: nothing stated-but-unused, nothing
      used-but-unstated; single-use symbols inlined (house rule 5)
- [ ] Registered notation in statements, raw computation in proofs; functions
      argument-explicit in statements (house rules 6–7)
- [ ] Each theorem: motivation prose → statement → strategy with per-lemma
      roles → assembly → lemmas; shared inputs as numbered displays
      (house rules 8–10)
- [ ] No external/internal-ledger citations a fresh reader cannot resolve
      (house rule 12)
- [ ] Sections start on new pages; figures never occupy a page alone
      (house rule 13)
- [ ] No meta-commentary; no redundant restatements (house rule 14)
- [ ] Discussion: what drives the result, what it does NOT use, remaining gaps
- [ ] Opening overview written last, reflects actual findings
- [ ] Document compiles without errors; auxiliary files cleaned up
- [ ] `/review-summary` Mode B passes with no CRITICAL or MAJOR issues
