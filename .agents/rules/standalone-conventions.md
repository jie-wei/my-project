# Project Conventions

## Naming

- **Variant names**: `snake_case` everywhere (e.g., `iv_approach`, `bootstrap_se`). Used for subfolder names across all layers (`code/`, `docs/`, `output/`, `data/`). Python requires underscores for importable package names, and we use the same convention uniformly to avoid splits.
- **Skill names and summaries**: `kebab-case` (e.g., `write-code`, `review-summary`).
- **Python files, functions, variables**: `snake_case` (PEP 8).

## Research Reasoning

- Use the latest agreed model formulation and assumptions. Before reusing an earlier result, check that its hypotheses still hold. Treat superseded notes as historical context and flag unresolved conflicts that affect the answer.
- Preserve established notation and use model primitives directly. Use optional new shorthand when the user requests or agrees to it. Define genuinely new model objects at first use.
- Derive forward from the object in question. Explain which assumption or result justifies each substantive move. Keep proofs compact while retaining the steps and boundary cases needed for the claim.
- In chat replies as well as written documents, present proofs in layers: first explain the few major steps and why they jointly establish the result, then use top-level bullets for those steps and nested bullets for the reasons, calculations, and cases that justify each one. A list of step names alone is not a proof strategy.
- Use one main idea per paragraph in both chat and documents, with blank lines between paragraphs and visible spacing between list items. Keep concise writing readable by removing repetition rather than squeezing material together.
- In chat, separate distinct topics with blank lines. In paginated research notes, start major sections on separate pages and keep figures with their explanations.
- Evaluate proposed ideas critically regardless of their source, including suggestions from the user or an adviser. Check reasoning and counterexamples, and distinguish assumptions, conjectures, and established results.
- Match the stage of discussion. When intuition is requested, explain the economic mechanism in plain language. Develop formal analysis to the extent needed for the current question.

## Code Organization

- Research calculations in `code/src/mypackage/{tier}/` take data in and return results. Shared readers and writers may live in a clearly named I/O module and receive paths as arguments.
- Scripts select inputs, parameters, and destinations. Production scripts live directly in `code/scripts/core/` with numbered filenames. Exploration and archive scripts live under the variant name.
- Use `config.py` for base locations and `output_path` for variant outputs. Compose filenames in scripts. Follow the [file I/O guide](standalone-file-io.md) for locations, examples, and testing.
- Tests in `code/tests/` use synthetic data. I/O tests read and write temporary files with `tmp_path`.
- Set the random seed once at the start of a stochastic run.

## Data

- `data/raw/` is sacred — never modify raw data.
- `data/intermediate/` and `data/processed/` are rebuilt by scripts.
- Data flow:
  ```
  data/raw/ → scripts → data/intermediate/ → scripts → data/processed/ → scripts → output/{tier}/
                                                                                        ↓
                                                                          ┌──────────────┴──────────────┐
                                                                          ↓                             ↓
                                                                   write-summary → docs/{tier}/    paper/ and slides/ (figures/tables)
  ```

## Three-Tier Structure (core / exploration / archive)

- The project uses three parallel tiers across four layers:
  - `code/src/mypackage/{core, exploration, archive}/` — research functions and reusable helpers
  - `code/scripts/{core, exploration, archive}/` — file I/O scripts and notebooks
  - `output/{core, exploration, archive}/` — generated outputs
  - `docs/{core, exploration, archive}/` — analysis notes
- The user initiates all tier transitions. Follow `workflow-exploration.md` to move files and update their consumers together.
- Each exploration gets a **named subfolder** (e.g., `exploration/iv_approach/`) across the layers it uses.

## Exploration

- Notebooks go in `code/scripts/exploration/[name]/` — always import from `src/`, never copy-paste.
- Reusable exploration code goes in `code/src/mypackage/exploration/[name]/`.
- Analysis notes go in `docs/exploration/[name]/`.
- No dead code in `src/`. Move abandoned code to `archive/` or delete and let git history hold it.
- See `workflow-exploration.md` for workflow and tier transitions.

## Versions and Variations

- Only separate what's actually different. Shared logic stays in shared files.
- Use CLI arguments to select versions — never duplicate scripts.

## Generic vs Specific

- **Generic** (commit to repo): workflow patterns, templates, rules, skills that help all users
- **Specific** (keep local): machine paths, tool versions, personal preferences, API keys
- Litmus test: would a researcher in a different field benefit from this? Yes → commit. No → `.claude/state/personal-memory.md` (gitignored).

## LaTeX

See the [paper build guide](standalone-latex-compile.md) for manuscript compilation, subfiles, and failure diagnostics. For presentations, follow the [slides guide](../../slides/README.md); decks have their own source and build configuration in `slides/`.

## Math in Chat

The VS Code panel renders CommonMark + monospace only — no LaTeX (`$...$`, `$$...$$`), no MathJax, no KaTeX, and inline HTML (`<sub>`, `<sup>`) does **not** render either (both were tested, both show as literal text). Present math in Unicode, with the form matching the content:

- **Inline, in prose.** Unicode symbols directly: Greek (α β γ θ λ μ π σ τ φ ψ ω Γ Δ Θ Λ Π Σ Φ Ψ Ω), operators (∈ ⊂ ⊆ ∪ ∩ ≤ ≥ ≠ ≈ ∼ ≡ ∝), logic (∀ ∃ ∧ ∨ ¬ ⇒ ⇔), calculus (∂ ∇ ∫ ∑ ∏ √ ∞), decorated letters (v̂ τ̃ x̄), sub/superscripts (ₜ ᵢ ⁿ ⁻¹ ²). Example: `the equilibrium price p* solves E[v | s] = c + (1−λ)·Δ`.
- **Displayed equations.** Put them in a fenced code block (no language tag) so monospace alignment works. One equation per line; pad with spaces to align `=` signs.
- **Derivation chains.** Equation on one line, reason on the next indented with `—`. State (1) which result justifies the step, (2) why it applies, (3) what the step buys you. Derive forward from the expression in hand, simplifying toward the result.
- **Matrices.** ASCII brackets inside a code block, one row per line.

**Rendering established notation** (Unicode lacks many subscript characters):

1. **Use Unicode where it exists.** `xₜ`, `σ²`, `vᵢ`.
2. **Preserve the symbol when Unicode cannot render it.** Use caret/underscore with braces for multi-token expressions (`x^{k+1}`, `σ_{ij}`, `Σ_{t=0}^{T}`). Single-token forms such as `x_t` and `β^T` are fine. Mixing is OK, as in `σ²_{ij}`. Change the display encoding rather than renaming model objects.

**Hazards to avoid:**

- `\exp(·)` (use `e^{·}`), `\frac{a}{b}` (use `a/b`), `\sqrt{x}` (use `√x`).
- Bare `*` in math prose triggers Markdown italics (`σ*_θ vs β*` italicizes everything between the asterisks). Escape as `\*` or use the Unicode asterisk operator `∗` (U+2217) when it's a math symbol.

For dense math (long proofs, multi-page derivations), move to a rendered view (VS Code Markdown preview with MathJax, Obsidian, Overleaf). This panel is optimal for *informal* math, not *dense* math.

## Environment

- Use `uv` for Python and dependency management.
