# Regression via rpy2 + fixest

When you need R's `fixest` package for fixed-effect regressions (feols, fepois, etc.) or `lfe` for felm, call R from Python via rpy2. This keeps the project in Python while using R's superior regression packages.

## Setup

```python
import pandas as pd
import rpy2.robjects as ro
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter
from rpy2.robjects.packages import importr

fixest = importr("fixest")
base = importr("base")
```

## Transfer Data to R

```python
def _transfer_to_r(df: pd.DataFrame, name: str = "df") -> None:
    """Send a pandas DataFrame to R's global environment."""
    with localconverter(ro.default_converter + pandas2ri.converter):
        r_df = ro.conversion.py2rpy(df)
    ro.globalenv[name] = r_df
```

Usage:
```python
_transfer_to_r(panel_df, "df")
```

## Run Regressions

```python
# Single regression
model = fixest.feols(
    ro.Formula("y ~ x1 + x2 | county_id + year"),
    data=ro.globalenv["df"],
    cluster=ro.Formula("~county_id"),
)

# Multiple specifications — use a dict to track them
specs = {
    "baseline": "y ~ x1 | county_id + year",
    "controls": "y ~ x1 + x2 + x3 | county_id + year",
    "interactions": "y ~ x1 * post | county_id + year",
}

models = {}
for name, formula in specs.items():
    models[name] = fixest.feols(
        ro.Formula(formula),
        data=ro.globalenv["df"],
        cluster=ro.Formula("~county_id"),
    )
```

## Generate LaTeX Tables

Use `etable()` with `style.tex("aer")` for AER-formatted output:

```python
# Combine models into a list for etable
model_list = ro.ListVector(models)

# R expects a named character vector: internal names -> display labels.
label_map = {
    "x1": "Treatment Variable",
    "x2": "Control 1",
    "x3": "Control 2",
    "x1:post": "Treatment x Post",
}
r_labels = ro.StrVector(list(label_map.values()))
r_labels.names = ro.StrVector(list(label_map.keys()))

tex_output = fixest.etable(
    model_list,
    style_tex=fixest.style_tex("aer"),
    headers=ro.StrVector(["Baseline", "Controls", "Interactions"]),
    dict=r_labels,
    drop=ro.StrVector(["Constant"]),
    tex=True,
)

# etable returns a character vector of LaTeX lines.
tex_str = "\n".join(tex_output) + "\n"
```

### Variable Label Mapping

The `dict` argument takes a named R character vector: its values are display labels and its `names` attribute contains the internal variable names. An unnamed vector of alternating strings is not a mapping. Use `dict=` in the Python call; `dict` is a valid Python keyword argument. See the [official `etable` reference](https://lrberge.github.io/fixest/reference/etable.html).

If there's no obvious mapping for a variable, ask the user what label to use rather than guessing. Research-facing labels matter — they appear in the published paper.

### Saving .tex Output

```python
from mypackage.config import output_path

tables_dir = output_path(TIER, "tables", VARIANT)
tables_dir.mkdir(parents=True, exist_ok=True)
tex_path = tables_dir / "regression_results.tex"

with open(tex_path, "w", encoding="utf-8") as f:
    f.write(tex_str)
```

Use the calling script's `TIER` and `VARIANT`. Resolve the table path relative to the document being compiled. In an empirical summary with its configured `\outdir`, include the file with:
```latex
\input{\outdir/tables/{variant_name}/regression_results.tex}
```

## Notes

- Install R packages before first use: `R -e 'install.packages("fixest")'`
- rpy2 requires R to be installed and accessible from the Python environment
- For panel data with many fixed effects, fixest is substantially faster than statsmodels
- `etable()` handles significance stars, standard errors in parentheses, and fit statistics automatically
- Always cluster standard errors at the appropriate level — document why in a code comment
