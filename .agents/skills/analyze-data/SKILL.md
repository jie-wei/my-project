---
name: analyze-data
description: End-to-end Python data analysis workflow from exploration through modeling to publication-ready tables and figures
disable-model-invocation: true
argument-hint: "[dataset path or description of analysis goal]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Edit", "Bash", "Task"]
---

# Data Analysis Workflow

Run an end-to-end data analysis in Python: load, explore, analyze, and produce publication-ready output.

**Input:** `$ARGUMENTS` -- a dataset path (e.g., `data/raw/county_panel.csv`) or a description of the analysis goal (e.g., "regress wages on education with state fixed effects using CPS data").

---

## Constraints

- **Follow project conventions** in `.agents/rules/standalone-conventions.md`
- Follow the [file I/O guide](../../rules/standalone-file-io.md). Calculations and reusable readers or writers live in `src/`. Scripts choose inputs, parameters, and destinations.
- Import base directories and `output_path` from `mypackage.config`, then compose filenames in the script.
- **Never modify `data/raw/`** -- it is sacred.
- Save processed datasets under `data/processed/{variant_name}/` and shared rebuilt datasets under `data/intermediate/`. Save tables and figures in the locations returned by `output_path`.
- **Run `/review-code`** on generated code before presenting results.

---

## Workflow Phases

### Phase 1: Setup and Data Loading

1. Read `.agents/rules/standalone-conventions.md` for project standards.
2. Select the tier and variant, check `config.py` for existing paths, and use the path construction example in the file I/O guide.
3. Create script with proper header (see Script Structure below).
4. Load required packages at top.
5. Set seed once at top for any stochastic operations: `np.random.seed(42)` or `random.seed(42)`.
6. Load and inspect the dataset.

### Phase 2: Exploratory Data Analysis

Generate diagnostic outputs:
- **Summary statistics:** shape, dtypes, missingness rates, descriptive stats
- **Distributions:** histograms for key continuous variables
- **Relationships:** scatter plots, correlation matrices
- **Time patterns:** if panel data, plot trends over time
- **Group comparisons:** if treatment/control, compare pre-treatment means

Save diagnostic figures under `output_path(tier, "figures", variant)`, using descriptive filenames.

### Phase 3: Main Analysis

Based on the research question:
- **Regression analysis:** Use `statsmodels`, `linearmodels` (for panel/IV), or `scikit-learn` as appropriate
- **Standard errors:** Cluster at the appropriate level (document why)
- **Multiple specifications:** Start simple, progressively add controls
- **Effect sizes:** Report standardized effects alongside raw coefficients
- **Robustness checks:** Alternative samples, specifications, or estimators

### Phase 4: Publication-Ready Output

**Tables:**
- Use `stargazer` (Python port), `statsmodels.summary`, or manual formatting
- Include all standard elements: coefficients, SEs, significance stars, N, R-squared
- Export as `.tex` for LaTeX inclusion and `.csv` for quick viewing

**Figures:**
- Use `matplotlib` or `seaborn`
- Include proper axis labels (sentence case, units)
- Save with explicit dimensions and DPI: `fig.savefig(..., dpi=300, bbox_inches='tight')`
- Save as both `.pdf` (for LaTeX) and `.png` (for quick viewing)

### Phase 5: Save and Review

1. Save shared rebuilt data to `data/intermediate/` and variant datasets to `data/processed/{variant_name}/`.
2. Save figures and tables to `output/{tier}/figures/{variant_name}/` and `output/{tier}/tables/{variant_name}/`.
3. Create output directories as needed with `os.makedirs(..., exist_ok=True)`.
4. Run `/review-code` on generated code:
   "Review the script at code/scripts/[tier]/[script_name].py"

5. Address any Critical or High issues from the review.

---

## Code Organization

Decide where code goes based on the src/scripts split:

**Reusable calculations and I/O functions in `code/src/mypackage/`:**
- Data cleaning/transformation functions
- Statistical model specifications
- Table/figure formatting functions
- Reusable readers and writers that receive explicit paths

**Goes in `code/scripts/` (I/O):**
- Loading data from disk
- Calling src/ functions with specific datasets
- Saving outputs to disk
- The orchestration script that ties it all together

For a quick exploration, it's fine to put everything in a single script under `code/scripts/exploration/[name]/`. For production analysis, split properly.

---

## Script Structure

Follow this template for scripts:

```python
"""
[Descriptive Title]

Purpose: [What this script does]
Inputs: [Data files -- use config.py path names]
Outputs: [Figures, tables, processed data]
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from mypackage.config import PROCESSED, RAW, output_path
# from mypackage.core.analysis import your_function  # if using src/ functions

# ── Setup ──────────────────────────────────────────
np.random.seed(42)
TIER = "exploration"
VARIANT = "example_variant"
input_file = RAW / "dataset.csv"
processed_dir = PROCESSED / VARIANT
tables_dir = output_path(TIER, "tables", VARIANT)
figures_dir = output_path(TIER, "figures", VARIANT)

# ── Data Loading ───────────────────────────────────
# [Load and clean data]

# ── Exploratory Analysis ───────────────────────────
# [Summary stats, diagnostic plots]

# ── Main Analysis ──────────────────────────────────
# [Regressions, estimation]

# ── Tables and Figures ─────────────────────────────
# [Publication-ready output]

# ── Export ─────────────────────────────────────────
# [Save all outputs]
```

---

## Output Location

Use the tier and variant selected during setup. Follow the [file I/O guide](../../rules/standalone-file-io.md) for script placement and data and output directories. Create the destination directories before saving, then verify that the summary workflow can find the generated files.

---

## Principles

- **Reproduce, don't guess.** If the user specifies an analysis, run exactly that.
- **Show your work.** Print summary statistics before jumping to modeling.
- **Check for issues.** Look for multicollinearity, outliers, missing data patterns, perfect prediction.
- Use config.py base directories and `output_path`, with ordinary filenames composed in the script.
- **No dead code.** Remove commented-out alternatives before finishing.
- **Explain choices.** If you pick a specific estimator or specification, say why in a code comment.
