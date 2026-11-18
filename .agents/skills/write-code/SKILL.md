---
name: write-code
description: >-
  Python code implementation following project structure and conventions.
  Use this skill whenever the user asks to implement, write, create, build, add,
  modify, refactor, or extend Python code — including new functions, modules,
  scripts, or tests. Covers placing code in the right tier and folder, reusing
  existing functions, using shared path helpers, writing tests, and
  producing LaTeX-ready output. Do NOT use for pure data analysis questions
  (use /analyze-data instead). This skill is about building and modifying
  reusable code components.
disable-model-invocation: true
argument-hint: "[what to implement, e.g. 'add a function to compute HHI from firm-level data']"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Edit", "Bash", "Task"]
---

# Write Code

Implement Python code (with optional R via rpy2 for regressions) following project conventions.

**Input:** `$ARGUMENTS` — what to implement (e.g., "write a function that computes Herfindahl index from firm-level shares", "add a script that runs IV regressions with county fixed effects", "refactor the cleaning pipeline to handle missing zip codes").

---

## Research choices

Ask in plain text when an unresolved choice affects the implementation.
- Which tier (core vs exploration) if not obvious from context
- Variable-to-label mappings for regression tables (no obvious default — ask)
- Whether to extend an existing module or create a new one
- Which fixed effects, clustering, or sample restrictions to use

Never use AskUserQuestion — always ask in plain text within your response.

---

## Step 1: Classify & Survey

**Classify the task:**

1. **Tier**: core / exploration / archive — check where the user is working (open files, recent edits, cwd). Default to exploration if unsure.
2. **Variant name**: snake_case approach name (e.g., `iv_approach`, `bootstrap_se`). This determines subfolder paths across all layers.

**Survey existing code — this is the most important step:**

Search `code/src/mypackage/` and `code/scripts/` for functions and patterns that already do what's needed. Use Grep and Glob to find:
- Functions with similar signatures or purposes
- Scripts that handle similar data loading, output saving, or plotting
- Existing config paths that might already cover what's needed

List what you can import or adapt vs what must be written fresh. The goal is to build on existing code, not reinvent it. If a function exists that does 80% of what's needed, extend it rather than writing a parallel version.

---

## Step 2: Set Up Folders & Paths

Read the [file I/O guide](../../rules/standalone-file-io.md) for data and output locations and `references/folder-structure.md` for code placement.

Check which folders and config.py paths already exist. Create only what's missing:
- Folders across layers (src/, scripts/, output/, etc.)
- Calls to `output_path(tier, kind, variant)` for result directories, with filenames composed in scripts

**Output path convention:** Figures and tables go in separate subdirectories under `output/{tier}/`, not flat in a variant folder:
```
output/{tier}/figures/{variant_name}/   # .pdf + .png
output/{tier}/tables/{variant_name}/    # .tex + .csv
```
Use `output_path(tier, "figures", variant)` and `output_path(tier, "tables", variant)` to construct these directories.

Read `references/code-patterns.md` for calculation, script, and test examples.

---

## Step 3: Write Code

Build on what you found in Step 1. Import existing functions first.

**Calculation modules:**
- Keep research calculations independent of file access and display.
- Functions take data in, return data out
- Type hints on public functions, docstrings with Args/Returns
- Seed passed as parameter when needed, not set globally

Configuration and reusable I/O modules may access the filesystem. Put shared readers or writers in clearly named modules when reuse warrants it and pass paths explicitly.

**scripts/** (I/O glue):
- Import base paths and `output_path` from config.py, and reusable functions from src/
- Parameters as module-level constants (SEED, etc.)
- `DIR.mkdir(parents=True, exist_ok=True)` before saving
- Figures use the directory returned by `output_path(tier, "figures", variant)`, saved as `.pdf` + `.png` with `dpi=300, bbox_inches='tight'`.
- Tables use `output_path(tier, "tables", variant)`, saved as `.tex` usable with `\input{}` + `.csv`.
- Never save outputs into a flat variant folder — always use the `figures/` and `tables/` subdirectories

**If regressions are needed:** read `references/regression-rpy2.md` for the rpy2 + fixest pattern.

---

## Step 4: Write Tests

Every new public function in `code/src/mypackage/` gets a test in `code/tests/`.

See `references/code-patterns.md` (Test Pattern section) for the full template with fixtures and examples.

Key conventions:
- Class-based, grouped by function
- Use synthetic data and temporary files under `tmp_path` for I/O tests.
- `pytest.approx()` for float comparisons
- Test edge cases: empty input, single row, missing values
- Test reproducibility if function uses randomness

---

## Step 5: Verify

1. **Run the code**: execute scripts, check outputs are created at expected paths
2. **Run tests**: `cd code && uv run pytest tests/test_{variant_name}.py -v`
3. **Run `/review-code`** on all new/modified files — report saves to `docs/quality_reports/reviews/{tier}/review-code-{variant_name}.md`
4. **Read the review report**: if issues are found, fix them and re-run `/review-code` until the report is clean

---

## Checklist

Before finishing, confirm:

- [ ] Paths use config.py base directories and helpers
- [ ] Scripts coordinate inputs and outputs, with reusable readers and writers in named I/O modules
- [ ] Tests exist for new public src/ functions
- [ ] Seed set for any stochastic operations
- [ ] Output files saved to `output/{tier}/figures/{variant}/` and `output/{tier}/tables/{variant}/` (not flat)
- [ ] Figures saved as .pdf + .png
- [ ] Tables saved as .tex (LaTeX-importable) + .csv
- [ ] data/raw/ not modified
- [ ] No dead code or commented-out alternatives
- [ ] Existing functions reused where possible

---

## Principles

**Why reuse matters.** Every function written is a function to maintain. Before writing new code, spend a minute searching for existing implementations. A slightly imperfect existing function that you can extend is better than a pristine new function that duplicates logic. This keeps the codebase coherent and reduces the surface area for bugs.

Keep calculations easy to test with data in memory. Shared I/O functions can be tested with temporary files, and scripts coordinate the pipeline.

Use config.py's project root and path helpers so a script works from different working directories. During a tier change, update paths and their consumers together as described in the exploration workflow.

**When to ask vs when to decide.** If there's a clear convention (naming, placement, format), follow it without asking. If there's genuine ambiguity that affects the user's research (which specification to run, what labels to use, which sample to restrict to), ask in plain text. The cost of asking is low; the cost of guessing wrong on a research decision is high.
