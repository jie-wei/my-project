# Code Patterns Reference

## Config.py

Read the [file I/O guide](../../../rules/standalone-file-io.md) for locations and the path construction example. Import base directories and `output_path(tier, kind, variant)` from [config.py](../../../../code/src/mypackage/config.py), then compose ordinary filenames in the caller.

Existing project-specific constants can be reused. Keep their locations in sync when moving a variant between tiers.

---

## src/ Module Pattern

Research calculations accept data and return results. Reusable readers and writers may live in clearly named I/O modules and accept explicit paths.

```python
"""Short description of what this module does."""

import numpy as np
import pandas as pd


def compute_hhi(shares: pd.Series) -> float:
    """Compute Herfindahl-Hirschman Index from market shares.

    Args:
        shares: Market shares (should sum to ~1.0).

    Returns:
        HHI value between 0 and 1.
    """
    return (shares**2).sum()


def winsorize(series: pd.Series, lower: float = 0.01, upper: float = 0.99) -> pd.Series:
    """Winsorize a series at given quantiles.

    Args:
        series: Data to winsorize.
        lower: Lower quantile cutoff.
        upper: Upper quantile cutoff.

    Returns:
        Winsorized series.
    """
    bounds = series.quantile([lower, upper])
    return series.clip(lower=bounds.iloc[0], upper=bounds.iloc[1])
```

Key rules:
- Keep calculation functions independent of file access and display.
- Type hints on all public functions
- Docstrings with Args/Returns on public functions
- Seed passed as parameter, not set globally: `def bootstrap(data, n=1000, seed=42)`
- Private helpers prefixed with `_`

---

## Script Pattern

Scripts in `code/scripts/` handle I/O — reading files, calling src/ functions, saving results.

```python
"""
Descriptive Title

Purpose: What this script does
Inputs: Data files (use config.py path names)
Outputs: Figures, tables, processed data
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from mypackage.config import RAW, output_path
from mypackage.{tier}.{variant_name}.module import function_name

# -- Parameters ---------------------------------------------------------------
SEED = 42
np.random.seed(SEED)
TIER = "exploration"
VARIANT = "example_variant"
tables_dir = output_path(TIER, "tables", VARIANT)
figures_dir = output_path(TIER, "figures", VARIANT)

# -- Data Loading --------------------------------------------------------------
df = pd.read_csv(RAW / "dataset.csv")

# -- Analysis ------------------------------------------------------------------
result = function_name(df)

# -- Save Outputs --------------------------------------------------------------
tables_dir.mkdir(parents=True, exist_ok=True)
figures_dir.mkdir(parents=True, exist_ok=True)

# Tables: .tex + .csv
result.to_csv(tables_dir / "summary.csv", index=False)
result.to_latex(tables_dir / "summary.tex", index=False)

# Figures: .pdf + .png
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(result["x"], result["y"])
ax.set_xlabel("X variable")
ax.set_ylabel("Y variable")
for ext in (".pdf", ".png"):
    fig.savefig(figures_dir / f"main_plot{ext}", dpi=300, bbox_inches="tight")
plt.close(fig)
```

Key rules:
- All imports at top — stdlib/third-party first, then config paths, then src/ functions
- Parameters as module-level constants (SEED, sample restrictions, etc.)
- `DIR.mkdir(parents=True, exist_ok=True)` before saving
- Figures always saved as both `.pdf` and `.png`
- Tables saved as `.tex` (LaTeX-importable) and `.csv`
- Close figures after saving: `plt.close(fig)`
- No function definitions that belong in src/ — if logic is reusable, put it there

---

## Test Pattern

Tests live in `code/tests/`. Use synthetic data for calculations and pytest's `tmp_path` for I/O tests. See [test_config.py](../../../../code/tests/test_config.py) for filesystem examples.

```python
import pytest
import numpy as np
import pandas as pd

from mypackage.{tier}.{variant_name}.module import function_name


@pytest.fixture
def sample_data():
    """Small fake dataset for testing."""
    return pd.DataFrame({
        "firm_id": [1, 2, 3, 4],
        "share": [0.4, 0.3, 0.2, 0.1],
        "revenue": [100, 200, 150, 50],
    })


class TestFunctionName:
    def test_basic(self, sample_data):
        result = function_name(sample_data)
        assert result == pytest.approx(0.3, abs=1e-6)

    def test_empty_input(self):
        df = pd.DataFrame({"share": []})
        result = function_name(df)
        assert result == 0.0

    def test_single_firm(self):
        df = pd.DataFrame({"share": [1.0]})
        result = function_name(df)
        assert result == pytest.approx(1.0)

    def test_reproducible(self, sample_data):
        r1 = function_name(sample_data, seed=42)
        r2 = function_name(sample_data, seed=42)
        assert r1 == r2
```

Key rules:
- Use `pytest.fixture` for shared test data
- Class-based grouping by function
- `pytest.approx()` for all float comparisons
- Use synthetic data, including synthetic files in temporary directories for I/O checks.
- Test edge cases: empty, single row, missing values, boundary conditions
- Test reproducibility if function involves randomness
- Run with: `cd code && uv run pytest tests/test_{variant_name}.py -v`
