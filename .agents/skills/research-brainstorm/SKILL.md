---
name: research-brainstorm
description: Generate and assess research directions for theory, empirical, or mixed projects. Use to explore alternatives from a topic, model, phenomenon, or dataset; keep discussion in chat unless a saved note is requested.
disable-model-invocation: true
argument-hint: "[topic, model, phenomenon, or dataset]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "WebSearch", "WebFetch"]
---

# Research Brainstorm

Explore promising research directions at the level of detail the current discussion needs.

## Start from the Current Question

Read the request, relevant project notes, and any supplied model or data description. Use the latest agreed assumptions and notation. Do not repeat questions already answered in the conversation.

Infer whether the task is theoretical, empirical, or mixed. Ask only when an unresolved choice materially affects the directions worth exploring.

## Develop Useful Alternatives

Generate as many distinct directions as the request warrants, without a fixed quota or a required descriptive-to-causal sequence. For each promising direction, explain the question, why it matters, the proposed mechanism or claim, and the main obstacle to establishing it.

Adapt the analysis to the project:

- **Theory:** Identify the relevant primitives, assumptions, and solution concept. State the conjecture separately from established results. Explain a plausible proof strategy, why its major steps would establish the claim, and which counterexamples or boundary cases could defeat it. Empirical data is not a prerequisite for a theoretical contribution.

- **Empirics:** Identify the estimand or descriptive question, measurement and data needs, and the evidence that could answer it. Discuss identification and comparison groups when making causal claims; do not impose a causal design on a descriptive task.

- **Mixed work:** Explain which conclusions follow from the model and which require data. Show how empirical evidence would distinguish mechanisms or assess the model's predictions.

Compare contribution, feasibility, and uncertainty when that helps the user choose. Ground literature claims in sources actually checked; label unverified leads. Suggest the next useful calculation, counterexample, data check, or paper to read.

Follow the shared conventions for readable paragraphs and layered proof explanations.

## Output

Keep the brainstorm in chat by default. Invoking this skill alone does not request a saved report or new project folders.

When the user requests a saved note, use their destination or the active variant's notes folder. For a new direction without a destination, use `docs/exploration/[variant]/research_brainstorm_[topic].md`, choosing descriptive snake_case names. Use `docs/core/` only when the work belongs to the established core.

Include only the questions, assumptions, arguments, comparisons, and open issues needed for that note. Do not create code or output folders merely to save a discussion.
