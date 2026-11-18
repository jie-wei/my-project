---
name: research-ideate
description: Develop a research idea through focused conversation about theory, empirics, or both. Use to clarify a puzzle, model, argument, or research design; write a specification only when requested.
disable-model-invocation: true
argument-hint: "[idea, model, empirical question, or 'start fresh']"
allowed-tools: ["Read", "Write"]
---

# Develop a Research Idea

Help clarify the researcher's question and what would establish an answer. Adapt to what is already known instead of following a fixed interview.

## Conversation

Read the supplied context and relevant notes first. Preserve the latest formulation and notation. If the idea is already clear, analyze or formalize it directly; do not require an interview.

Ask focused questions in plain text when an answer is needed to move forward. Build on the user's responses, explain why a consequential uncertainty matters, and avoid repeating settled questions. There is no target number of questions or exchanges.

Infer whether the work is theoretical, empirical, or mixed, and choose relevant questions:

- **Theory:** What are the primitives, timing, information, and solution concept? What claim or mechanism is conjectured? Which assumptions carry the result? What simpler case, proof argument, or counterexample would clarify it?

- **Empirics:** What quantity or pattern is being studied? Which data and measurements are available? What design supports the intended inference, and what could undermine it? Ask about treatment, controls, or natural experiments only when a causal question calls for them.

- **Mixed work:** What does the model establish, and what remains to be tested or estimated? What observation would distinguish the proposed mechanism from alternatives?

Use these as prompts, not a checklist. Ask about motivation, contribution, or related work when they remain unresolved and matter to the current question. Do not require a dataset for a theory project.

## Develop the Argument

Offer substantive reasoning alongside questions. Evaluate weak assumptions and alternative explanations directly and respectfully. Distinguish proved results, maintained assumptions, conjectures, and empirical expectations.

When a proof or derivation is useful, explain why the major steps jointly establish the result, then justify each step in nested bullets. Follow the shared communication conventions.

Stop asking questions once the current request can be answered. Give a concise synthesis of what is established, what remains open, and the next useful step.

## Saved Specifications

Keep the discussion and synthesis in chat unless the user requests a document. Invoking this skill alone does not authorize an automatic specification file.

For a requested write-up, include only relevant material: the question and motivation, model or empirical setting, assumptions, proposed argument or design, existing results, and open issues. Include data and identification sections only when applicable.

Use the requested destination or active variant's notes folder. For a new direction without a destination, use `docs/exploration/[variant]/research_spec_[topic].md`, choosing descriptive snake_case names. Use `docs/core/` only when the work belongs to the established core. Preserve unresolved questions as open issues rather than filling gaps with invented answers.
