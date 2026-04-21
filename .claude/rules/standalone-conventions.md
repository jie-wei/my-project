# Project Conventions

## Naming

- **Variant names**: `snake_case` everywhere (e.g., `iv_approach`, `bootstrap_se`). Used for subfolder names across all layers (`code/`, `docs/`, `output/`, `data/`). Python requires underscores for importable package names, and we use the same convention uniformly to avoid splits.
- **Skill names, session logs, summaries**: `kebab-case` (e.g., `write-code`, `review-summary`).
- **Python files, functions, variables**: `snake_case` (PEP 8).

## Code Organization

- Pure logic in `code/src/mypackage/core/` — no file I/O, no paths. Functions take data in, return data out.
- File I/O in `code/scripts/core/` — read files, call `src/` functions, save results. Number scripts in order (`01_clean.py`, `02_merge.py`, etc.).
- All paths defined in `code/src/mypackage/config.py` — import from there, never hardcode paths.
- Tests in `code/tests/` — test `src/` logic with fake data.
- Litmus test: needs the file system? → `scripts/`. No? → `src/`.

## Data

- `data/raw/` is sacred — never modify raw data.
- `data/intermediate/` and `data/processed/` are rebuilt by scripts.
- Data flow:
  ```
  data/raw/ → scripts → data/intermediate/ → scripts → data/processed/ → scripts → output/{tier}/
                                                                                        ↓
                                                                          ┌──────────────┴──────────────┐
                                                                          ↓                             ↓
                                                                   write-summary → docs/{tier}/    paper/ (figures/tables)
  ```

## Three-Tier Structure (core / exploration / archive)

- The project uses three parallel tiers across four layers:
  - `code/src/mypackage/{core, exploration, archive}/` — pure logic
  - `code/scripts/{core, exploration, archive}/` — file I/O scripts and notebooks
  - `output/{core, exploration, archive}/` — generated outputs
  - `docs/{core, exploration, archive}/` — analysis notes
- **Transitions** are just swapping the tier name in the path. User decides all tier transitions — Claude never promotes or archives on its own.
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

See `.claude/rules/standalone-latex-compile.md` for compile commands, the subfiles structure, the `cd paper/` rule, aux cleanup, and failure diagnostics.

## Math in Chat

The VS Code panel renders CommonMark + monospace only — no LaTeX (`$...$`, `$$...$$`), no MathJax, no KaTeX, and inline HTML (`<sub>`, `<sup>`) does **not** render either (both were tested, both show as literal text). Present math in Unicode, with the form matching the content:

- **Inline, in prose.** Unicode symbols directly: Greek (α β γ θ λ μ π σ τ φ ψ ω Γ Δ Θ Λ Π Σ Φ Ψ Ω), operators (∈ ⊂ ⊆ ∪ ∩ ≤ ≥ ≠ ≈ ∼ ≡ ∝), logic (∀ ∃ ∧ ∨ ¬ ⇒ ⇔), calculus (∂ ∇ ∫ ∑ ∏ √ ∞), decorated letters (v̂ τ̃ x̄), sub/superscripts (ₜ ᵢ ⁿ ⁻¹ ²). Example: `the equilibrium price p* solves E[v | s] = c + (1−λ)·Δ`.
- **Displayed equations.** Put them in a fenced code block (no language tag) so monospace alignment works. One equation per line; pad with spaces to align `=` signs.
- **Derivation chains.** Equation on one line, reason on the next indented with `—`. State (1) which result justifies the step, (2) why it applies, (3) what the step buys you. Per user-global CLAUDE.md: derive forward, never backward — start from the expression in hand and simplify toward the result, never state the result and verify.
- **Matrices.** ASCII brackets inside a code block, one row per line.

**Three-tier fallback for sub/superscripts** (Unicode is deliberately incomplete — e.g., no subscript Greek, no subscript `b/c/d/f/g/q/w/y/z`, no subscript uppercase):

1. **Use Unicode where it exists.** `xₜ`, `σ²`, `vᵢ`.
2. **Reshape the notation** before falling back to ASCII. Functional (`σ(θ)` instead of `σ_θ`), bracketed (`β[k]` instead of `β_k`), or argument-style (`Cov(xᵢ, xⱼ)` instead of `Σ_{ij}`) all work in Unicode.
3. **Caret/underscore with braces** only as last resort. Single token inline is fine (`x_t`, `β^T`); multi-token **must** be braced to kill ambiguity (`x^{k+1}`, `σ_{ij}`, `Σ_{t=0}^{T}` — never bare `x^k+1`). Mixing is OK: `σ²_{ij}` is fine.

**Hazards to avoid:**

- `\exp(·)` (use `e^{·}`), `\frac{a}{b}` (use `a/b`), `\sqrt{x}` (use `√x`).
- Bare `*` in math prose triggers Markdown italics (`σ*_θ vs β*` italicizes everything between the asterisks). Escape as `\*` or use the Unicode asterisk operator `∗` (U+2217) when it's a math symbol.

For dense math (long proofs, multi-page derivations), move to a rendered view (VS Code Markdown preview with MathJax, Obsidian, Overleaf). This panel is optimal for *informal* math, not *dense* math.

## Environment

- Use `uv` for Python and dependency management.
