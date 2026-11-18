---
paths:
  - "code/**"
  - "data/**"
  - "output/**"
---

# File I/O

Read this guide when writing or reviewing code that loads data, saves results, or moves a research variant. It is the shared reference for the analysis, coding, and summary skills.

| Content | Location |
| --- | --- |
| Original inputs, preserved as received | `data/raw/` |
| Rebuilt data shared across analyses | `data/intermediate/` |
| Rebuilt data specific to a variant | `data/processed/{variant}/` |
| Tables for a variant | `output/{tier}/tables/{variant}/` |
| Figures for a variant | `output/{tier}/figures/{variant}/` |
| Notes and summaries | `docs/{tier}/{variant}/` |

Use `core`, `exploration`, or `archive` as the tier. Use a descriptive snake_case variant name consistently across code, data, output, and notes. Processed data belongs to the variant across its lifecycle. Give independent versions distinct variant names when they need different datasets.

Import base directories and `output_path` from [config.py](../../code/src/mypackage/config.py). Compose filenames in the calling script. A new experiment can use the helper directly.

```python
from mypackage.config import PROCESSED, RAW, output_path

TIER = "exploration"
VARIANT = "wage_posting"
input_file = RAW / "wages.csv"
processed_dir = PROCESSED / VARIANT
tables_dir = output_path(TIER, "tables", VARIANT)
figures_dir = output_path(TIER, "figures", VARIANT)
```

`config.py` locates the source project through `code/src/<package>/config.py` and `code/pyproject.toml`. Use the editable installation in the README. Paths also work in source copies and inside a parent repository.

Keep research calculations in functions that accept data and return results. Scripts choose inputs, parameters, and destinations and call those functions. Shared readers and writers can live in a clearly named module such as `code/src/mypackage/io.py` when reuse warrants it. Pass paths explicitly to these helpers. Configuration and I/O modules may access the filesystem.

Before writing, create the destination with `mkdir(parents=True, exist_ok=True)`. Preserve files in `data/raw/`. Save tables as CSV plus LaTeX and figures as PDF plus PNG for the existing summary workflow. Scripts should identify their inputs and outputs in a short module docstring.

Keep production scripts flat under `code/scripts/core/`, numbered in execution order. Include the variant in a filename when needed to distinguish pipelines. Exploration and archive scripts use `code/scripts/{tier}/{variant}/`.

For a user-requested tier change, follow the [transition instructions](workflow-exploration.md). Update the tier supplied to `output_path`, any existing variant constants, imports, and document references together. Run the moved pipeline and check its actual output destinations.

Use synthetic data for tests. I/O tests may read and write files under pytest's `tmp_path`. Check both destination and contents, including a run from a different working directory when paths change. [test_config.py](../../code/tests/test_config.py) covers root discovery, output locations, and a move between tiers.
