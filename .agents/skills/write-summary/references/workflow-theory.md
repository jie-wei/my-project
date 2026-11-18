# Workflow: Theory Summary

Steps 2–7 for producing theory notes or a full proof walkthrough from the current formulation and arguments. Apply the relevant parts to the scope selected in Step 1.

---

## Step 2: Read the Math Formulations

Start with the latest agreed question, notation, and assumptions. Read the relevant notes in `docs/{tier}/{variant_name}/` and the discussion supplied with the request. Existing `question.md`, `definitions.md`, `assumptions.md`, `findings.md`, `results/`, and review files can help when present. Use the available sources without requiring that file structure.

For the results within scope, identify their hypotheses, logical dependencies, proofs, and status as established, assumed, conjectured, or superseded. Check that earlier arguments still apply to the current formulation. Flag a material unresolved conflict instead of silently combining model versions.

Organize the explanation by logical dependence so the reader can derive forward from the model to the result.

---

## Step 3: (No separate scan step — the "outputs" are the result files themselves.)

---

## Step 4: Map the Proof Architecture

- Identify which results close gaps vs. open new questions
- What is the main theorem? What are the supporting lemmas?
- What is the logical skeleton: which lemmas feed into which?
- Are there alternative proof paths?

Use the dependencies needed for the requested result to determine the document structure. An equation sheet or brief statement of established results need not reproduce every supporting proof.

---

## Step 5: Plan the Discussion

Use economic interpretation and discussion where they serve the requested document. Any included proof must retain the steps and boundary cases needed for its claim.

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

Read `references/template-latex-theory.tex` for a full proof walkthrough. For a brief note, reuse only the necessary preamble and environments. The following patterns are useful when the requested document needs the corresponding sections:
- Opening overview states the question, answer, and ordered proof strategy
- Setup holds primitives and maintained assumptions only
- Each results section defines its objects at first use, motivates and states the theorem, then explains the supporting lemmas' roles
- A proof strategy explains why the major steps suffice; the proof develops those steps as top-level bullets with nested justifications
- When supporting lemmas are needed, first show how they establish the main result, then give their statements and layered proofs
- Closing discussion identifies the result's scope, maintained assumptions, and remaining gaps
- Optional appendix for alternative proofs or extensions

---

## Step 7: Write the Summary (body first, opening overview last)

Use a standalone article class. Include theorem environments when the document contains formal statements or proofs. Match the requested length and preserve the sections outside an authorized edit.

### Proof-writing guidance

Use these defaults where relevant to the requested deliverable. The shared [research reasoning conventions](../../../rules/standalone-conventions.md#research-reasoning) apply to every length. A brief note can omit the full walkthrough's section structure, while its claims still need accurate hypotheses and support.

1. **Major steps above their justifications.** Use `itemize`/`enumerate` to
   organize the proof in layers. The top level contains the few substantive
   steps and says what each achieves. Nested bullets explain why each step is
   true: assumptions, cited results, calculations, and case checks. Use a
   further level when a justification itself needs an argument. Usually two
   or three levels suffice; give a long subargument a named lemma rather than
   burying it in deep indentation. Keep one logical point per bullet.
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
5. **Established notation; state only what you use.** Follow the shared notation
   policy. Keep an established symbol even when this note uses it only a few
   times. Include the facts the argument uses and state hypotheses broad enough
   to cover their actual uses.
6. **Established quantities and explicit computations.** Use the project's
   existing quantities in statements. Show primitive expressions and algebra
   where they clarify a statement or justify a proof step.
7. **Argument-explicit functions in statements.** Objects that depend on a
   configuration are written as functions of it in statements (e.g.
   `CS(b_1,...,b_K)`), with a one-sentence convention allowing the bare symbol
   inside proofs where the configuration is fixed. This answers "surplus *of
   what*?" inside every statement.
8. **Motivate results where useful.** Before a theorem, explain its economic
   point in prose. Keep one main idea per paragraph. A short proof note may
   need only a sentence; a standalone result needs enough context to make its
   significance clear.
9. **Explain why the strategy succeeds.** After the statement, give a short
   overview of the major steps and explain how their conclusions combine to
   prove it. For example, say why an upper bound plus a feasible choice
   attaining it establishes optimality. Merely listing "bound, construct,
   conclude" is insufficient. Then expand each step with nested justifications.
   Identify each supporting lemma's role and where key assumptions enter.
10. **Show the assembly before supporting lemmas when lemmas are needed.**
    Give the main proof first, forward-citing the lemmas, so their roles are
    clear before their details. A direct proof can keep the justifications
    under its major steps without inventing extra lemmas. Shared inputs used
    by several lemmas get a numbered display before those lemmas, rather than
    being buried in one lemma's proof and silently used by another.
11. **Every claim computes, cites, or justifies.** Give a reason, a
    `\ref`/`\eqref`, or a computation for each substantive move. Case analyses
    must cover the claim's domain, including cases that share a conclusion but
    require different arguments.
12. **Self-contained: internal citations only.** Cite the source paper by
    equation/observation number; never cite project-internal ledgers or notes a
    fresh reader cannot see. If an external result is needed, either prove it
    inline in two lines or reproduce its statement.
13. **Separate ideas on the page.** Start major sections on fresh pages,
    including in brief notes with distinct sections. Use one main idea per
    paragraph and visible space between paragraphs, major steps, and nested
    bullets. Keep figures non-floating and with their explanations, never
    isolated on a page. Let long proofs continue at sensible step boundaries;
    do not shrink text, eliminate list spacing, or force every small substep
    onto its own page.
14. **No meta-commentary in the text.** Never explain *why the document* does
    something ("G is needed only because..."); just do it. Redundant restatements
    (saying one fact two ways) are deleted — state the strongest true form once.

The following phases describe a full walkthrough. Use only the parts needed for a brief note or equation sheet.

**Phase A — Overview:**
- State the question precisely
- State the answer (theorem/result)
- Roadmap of the document sections

**Phase B — Setup (primitives only):**
- Model primitives and the market description, as bullets (rule 1)
- The maintained assumption, stated once with what is proved vs. maintained
- NO welfare aggregates, no benchmarks, no derived objects — those are defined
  at first use in their sections (rule 4)

**Phase C — Results (one section per step/theorem):**

For an extended theorem walkthrough, a useful order is (rules 8–10):
1. Definitions the section needs (first use)
2. Motivation prose (economics, in words)
3. The theorem, with full inline hypotheses (rule 3)
4. Strategy explaining why the major steps jointly imply the result
5. Layered proof: major steps above their justifications
6. When separate lemmas are useful, show their roles in the main proof first,
   then shared inputs as numbered displays and the lemmas with layered proofs

- Cross-reference via `\ref{}`/`\eqref{}` — every dependency is a visible link

**Proof format.** Use the same layered structure for direct proofs and proofs
assembled from lemmas:

- **Strategy:** explain why the conclusions of the major steps are sufficient
  for the theorem. The reader should understand the route before the details.
- **Top level:** one bullet per major step, stating its claim and its role in
  the strategy. Use `enumerate` when named step numbers help cross-references.
- **Lower levels:** nest each reason, computation, supporting lemma, or case
  beneath the claim it establishes. A label such as "by monotonicity" also
  needs the applicable conditions and the resulting implication.
- **Derivation chains:** put an `align*` block inside the supporting bullet
  where the calculation is needed, with justifications alongside substantive
  equalities. The chain supports that step rather than replacing the strategy.

A reader should be able to scan the major steps to understand why the proof
works, then descend into a chosen step to check its justification. Keep short
arguments short while making these logical levels visible.

```latex
% State the strategy first: why do these steps jointly establish the claim?
\noindent\textbf{Proof strategy.}
[Explain how the conclusions of the major steps imply the theorem.]

\begin{proof}
\leavevmode\par % Keep the proof heading above the bullet tree.
\begin{itemize}
  \item \textbf{[First major step and its role.]}
    \begin{itemize}
      \item [Reason or supporting result, with its conditions checked.]
      \item [Calculation or implication establishing this step.]
    \end{itemize}
  \item \textbf{[Second major step and its role.]}
    \begin{itemize}
      \item [How the first step and a current assumption apply.]
      \item [Why the relevant cases exhaust the domain.]
        \begin{itemize}
          \item [Case A and its justification.]
          \item [Case B and its justification.]
        \end{itemize}
    \end{itemize}
  \item \textbf{[Conclude the claim.]}
    \begin{itemize}
      \item [Explicitly combine the preceding conclusions.] \qedhere
    \end{itemize}
\end{itemize}
\end{proof}

% A key derivation chain belongs inside the bullet it justifies:
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
- **Derive forward** — after stating the result, develop the argument from definitions and assumptions toward the conclusion. Explain how each step advances the argument.
- **Justify substantive transformations** — name the rule and check its conditions. Routine algebra can be combined when the justification remains clear.
- **Keep proofs concise, complete, and visibly layered.** A reader should be able to reproduce the argument. Expand the key steps, assumptions, and boundary cases in the appropriate lower layer. Remove repetition while retaining readable spacing and the explanation of why the strategy succeeds.
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

- When including external figures or tables, use paths that resolve from the document directory and follow the [file I/O guide](../../../rules/standalone-file-io.md).
- For a full walkthrough, assemble the overview, setup, results, discussion, and any useful appendix. For a brief document, assemble only the requested material and the context needed to interpret it.

### Checklist

Apply the items relevant to the requested document. Formal statement and proof checks apply whenever those elements are included.

- [ ] Question and answer stated upfront in the opening overview
- [ ] Proof strategy explains why the major steps jointly imply the claim;
      top-level bullets show those steps and nested bullets justify them
      (rules 1, 9, 11)
- [ ] Key identities sit under the step they justify, with substantive
      transformations explained
- [ ] All summation/product indices carry explicit bounds (rule 2)
- [ ] Every statement carries its full hypotheses inline; no ambient scope
      (rule 3)
- [ ] Every object defined at first use; setup holds primitives only
      (rule 4)
- [ ] Established notation retained, all objects used are defined, and facts
      needed by the argument are stated (rule 5)
- [ ] Established quantities and explicit computations where needed; function
      arguments are clear in statements (rules 6–7)
- [ ] Each result has the context it needs, a statement, a sufficient strategy,
      and a layered proof; separate lemmas appear only when useful, with their
      roles explained first and shared inputs stated before their use
      (rules 8–10)
- [ ] No external/internal-ledger citations a fresh reader cannot resolve
      (rule 12)
- [ ] Major sections start on separate pages; each paragraph has one main
      idea, nested lists have readable spacing, and figures stay with their explanations
      (rule 13)
- [ ] No meta-commentary; no redundant restatements (rule 14)
- [ ] Discussion: what drives the result, what it does NOT use, remaining gaps
- [ ] Opening overview written last, reflects actual findings
- [ ] Document compiles without errors; auxiliary files cleaned up
- [ ] Included claims verified using Step 10 of `SKILL.md`, with unresolved
      claims identified explicitly
