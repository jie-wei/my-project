---
paths:
  - "**/exploration/**"
  - "**/archive/**"
---

# Exploration Workflow

Save experimental work in a named `exploration/` folder.

## Steps

1. **Research value check** — Does this help answer a research question or test an idea? If NO, don't build it.
2. **Pick a name** — short, descriptive, snake_case (e.g., `iv_approach`, `bootstrap_se`, `did_event_study`)
3. **Create named subfolder** across the layers you need:
   - Pure logic → `code/src/mypackage/exploration/[name]/`
   - Scripts/notebooks → `code/scripts/exploration/[name]/`
   - Figures and tables → `output/exploration/figures/[name]/` and `output/exploration/tables/[name]/`
   - Notes → `docs/exploration/[name]/`
   - Only create layers you'll actually use.
4. For an experiment with code, run it and check the results. Exploration scripts can use descriptive filenames without a numeric prefix.

## When to Stop (Kill Switch)

The user can stop an exploration at any point and decide whether to archive it.

## Tier Transitions (User-Initiated Only)

Only the user initiates a promotion, archive, or revival. Wait for their request before proposing or making a transition.

### Promote: `exploration/[name]/` → `core/`

Move the layers used by the variant:
- `code/src/mypackage/exploration/[name]/` → `code/src/mypackage/core/[name]/`
- Move scripts from `code/scripts/exploration/[name]/` directly into `code/scripts/core/`. Use filenames such as `NN_[name]_estimate.py`, numbered in execution order.
- Move each variant folder under `output/exploration/figures/` or `output/exploration/tables/` to the corresponding directory under `output/core/`.
- `docs/exploration/[name]/` → `docs/core/[name]/`

For every promotion, archive, or revival, update the references as part of the move.

1. Change the tier supplied to `output_path` in scripts or CLI defaults, and update any existing variant-specific constants in `config.py`.
2. Update Python imports, script invocations, and tests to the new module and script locations.
3. Update summary `\outdir`, table and figure references, and any manuscript links that use the moved outputs. Processed data continues to use `data/processed/[name]/`.
4. Run the affected pipeline and tests. Confirm results replicate within the appropriate tolerance, verify the new output paths, and check that the run does not recreate the old variant output directories.
5. Rebuild affected summaries and manuscript files, checking that their figures and tables resolve.

### Archive: `exploration/[name]/` → `archive/[name]/`

Move each used layer to its archive destination and apply the reference updates above. Collect a variant's flat core scripts under `code/scripts/archive/[name]/` when archiving production work. Add a brief note using `docs/templates/archive-readme.md`.

### Revive: `archive/[name]/` → `exploration/[name]/`

Move back to exploration and apply the reference updates above.
