---
paths:
  - "code/**/*.py"
  - "paper/**/*.tex"
  - "slides/**/*.tex"
  - "output/**"
---

# Task Completion Verification Protocol

Verify the outputs affected by a change.

## For Python code

1. Use the project's Python environment and confirm affected modules import.
2. From `code/`, run the relevant tests with `python -m pytest tests/ -x`.
3. Keep calculations independently testable. Configuration and reusable I/O modules follow the [file I/O guide](standalone-file-io.md).
4. For path or I/O changes, exercise synthetic files in a temporary directory and verify their destinations and contents. Run `tests/test_config.py` when changing path configuration.

## For Python Scripts (`code/scripts/core/*.py`):
1. `python3 code/scripts/core/NN_name.py` -- runs without error
2. Check this run wrote the expected files under the correct tier and variant, and that they have non-zero size
3. Spot-check: data shape, column names, value ranges are reasonable
4. If stochastic: verify seed is set

## For LaTeX Manuscripts (`paper/*.tex`):
1. Follow the [LaTeX build instructions](standalone-latex-compile.md) for the full paper and any edited subfile.
2. Check the final build output for undefined references, missing citations, and overfull boxes. Confirm the expected PDFs exist and inspect the affected pages when layout changes.

## For Presentations (`slides/*.tex`):
1. Follow the [slides guide](../../slides/README.md) and compile the affected deck independently of the paper.
2. Check the build log for unresolved citations and references, missing glyphs, and overfull boxes. Inspect the affected PDF pages for readable text, equations, figures, and tables.

## For Data Pipeline (end-to-end):
1. Identify the scripts for the affected pipeline and run each explicit filename in dependency order.
2. Verify `data/intermediate/` is populated after early scripts
3. Verify `data/processed/` is populated after later scripts
4. Verify `output/core/` has expected files (tables, figures)
5. Spot-check final outputs for reasonable values

## Common Pitfalls

- Use configured base locations and `output_path` so paths resolve from any working directory.
- Shared readers and writers receive explicit paths. Keep calculations independent of file access.
- **Stale intermediate data** -- when in doubt, rerun pipeline from script 01
- **Missing seeds** -- stochastic results are unreproducible without explicit seeds
- **data/raw/ modification** -- NEVER modify raw data; copy to intermediate/ first

## Verification Checklist

```
[ ] Output file(s) created successfully
[ ] No compilation/execution errors
[ ] Tests pass (for src/ modules)
[ ] Paths resolve correctly (imported from config.py)
[ ] Spot-checked output values for reasonableness
[ ] Reported results to user
```
