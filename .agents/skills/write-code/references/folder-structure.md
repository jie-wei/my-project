# Folder Structure Reference

This project uses a three-tier structure (core / exploration / archive) mirrored across multiple layers. When implementing code for a variant, you may need to create folders across several of these layers.

## Code Layers

### src/ — research functions and reusable helpers

```
code/src/mypackage/{tier}/{variant_name}/
├── __init__.py
├── module_a.py
└── module_b.py
```

- Create `__init__.py` in every new package directory (even if empty)
- One module per logical unit (e.g., `cleaning.py`, `estimation.py`, `formatting.py`)
- Calculations take data in and return results. Reusable readers and writers receive explicit paths and may live in a clearly named module such as `mypackage/io.py`.

### scripts/ — I/O glue

**Core tier** — numbered scripts, flat:
```
code/scripts/core/NN_{descriptive_name}.py
```
- Check existing scripts to find the next number in sequence
- Numbers reflect execution order, not importance

**Exploration tier** — named subfolder:
```
code/scripts/exploration/{variant_name}/
├── run_analysis.py
└── explore_results.py
```

**Archive tier** — same as exploration:
```
code/scripts/archive/{variant_name}/
```

### tests/

```
code/tests/test_{variant_name}.py
```

- One test file per variant
- Test research functions with synthetic data. Test I/O behavior with temporary files under `tmp_path` and run affected scripts.

## Data and outputs

Read the [file I/O guide](../../../rules/standalone-file-io.md) for the shared directory map and path construction example.

## Documentation (optional)

```
docs/{tier}/{variant_name}/
```

- Analysis notes, methodology docs — create only if needed
- Not required for every variant

## Before Creating

Check what already exists:

1. **Glob for existing folders**: `code/src/mypackage/{tier}/`, `code/scripts/{tier}/`
2. Read `config.py` for base directories and `output_path(tier, kind, variant)`. Reuse any project-specific paths already present.
3. Create only the directories this task uses.

Use `os.makedirs(..., exist_ok=True)` in scripts to create output directories at runtime.
