# Economics Research Project Template

An economics research starter with a LaTeX paper and slides, a Python package, and shared research skills for Claude Code and Codex. Adapted from Pedro H.C. Sant’Anna’s [Claude Code workflow](https://github.com/pedrohcgs/claude-code-my-workflow).

## Setup

1. Clone the template into a new project on a filesystem that supports symlinks.

   ```bash
   git clone -c core.symlinks=true <this-repo-url> my-new-project
   cd my-new-project
   ```

   Shared rules and skills live in `.agents/rules/` and `.agents/skills/`. Claude Code reaches them through the relative symlinks `.claude/rules` and `.claude/skills`. For a local copy, use `cp -a` from a checkout where both links resolve.

2. For Python work, use [uv](https://docs.astral.sh/uv/) to install the package and development dependencies.

   ```bash
   cd code
   uv venv --python 3.12
   source .venv/bin/activate
   uv pip install -e ".[dev]"
   python -c "import mypackage; print('OK')"
   ```

   To rename `mypackage`, update `code/src/mypackage/`, the project name in `code/pyproject.toml`, and the corresponding Python imports.

## Project layout

| Location | Purpose |
| --- | --- |
| `paper/` | Manuscript, section and appendix subfiles, and bibliography. The [paper index](paper/paper-structure.md) describes each file. |
| `slides/` | A Beamer starter with its own build configuration. See the [slides guide](slides/README.md). |
| `docs/core/`, `docs/exploration/`, `docs/archive/` | Research notes and write-ups. A named exploration holds the assumptions, results, and summary for one variant. |
| `docs/literature/` | Papers and literature notes. |
| `docs/templates/` | LaTeX journal files and reusable exploration, archive, and domain-review templates. |
| `docs/quality_reports/reviews/` | Findings from code and summary reviews, organized by tier. |
| `code/src/mypackage/` | Research functions and reusable helpers. `config.py` provides base paths and `output_path`. |
| `code/scripts/` and `code/tests/` | Pipeline entry points and numbered production scripts, plus tests using synthetic data and temporary files. |
| `data/` | Original data in `raw/`, rebuilt datasets in `intermediate/` and `processed/`, and variable definitions in `codebook.md`. |
| `output/` | Generated figures and tables used by the paper, slides, and empirical summaries. |
| `AGENTS.md`, `CLAUDE.md` | Shared project instructions and Claude Code’s import of those instructions. |
| `.agents/` | Shared rules, skills, and hook code. Edit these source files directly. |
| `.claude/`, `.codex/` | Client-specific settings, hook registration, and links to shared files. |

## Research workflows

Start an exploration in a named folder such as `docs/exploration/wage_posting/`. Create the code and output folders it uses. The researcher decides when to promote or archive the work. See the [exploration rules](.agents/rules/workflow-exploration.md).

`write-summary` turns existing theory discussions or empirical outputs into LaTeX notes, equation sheets, figure notes, or full reports, sized to the request. `review-summary` checks proofs against the source notes or numerical claims against the pipeline outputs. The [shared skills directory](.agents/skills/) also includes literature reviews, manuscript reviews, and code tools. Each skill’s `agents/openai.yaml` controls its Codex invocation settings.

The [file I/O guide](.agents/rules/standalone-file-io.md) defines data locations, output paths, and how scripts and reusable readers or writers fit together. Both agents reach it through `AGENTS.md` and the relevant skills. From `code/` in the project environment, run `python -m pytest tests/test_config.py` to check project roots and output paths.

For manuscript work, build from `paper/`. With the starter’s empty bibliography, run `latexmk -xelatex -bibtex- main.tex`. Once you add citations, use `latexmk -xelatex main.tex`. Rebuild an edited section or appendix after the full paper so its standalone PDF picks up current labels. See the [LaTeX build instructions](.agents/rules/standalone-latex-compile.md).

For presentations, build from `slides/` with `latexmk -xelatex slides.tex`. The deck reuses project figures, tables, and bibliography entries. See the [slides guide](slides/README.md) for paths and editing conventions.

Codex reads [AGENTS.md](AGENTS.md). [CLAUDE.md](CLAUDE.md) imports the same instructions for Claude Code. `AGENTS.md` tells both agents to read project memory at session start and when to consult the detailed guides.

`research-brainstorm` and `research-ideate` support theory, empirics, and mixed work. They keep discussion in chat unless a saved note is requested. `commit` creates a local commit by default; pushing, opening a PR, and merging follow the user's requested scope.

Invoke shared skills with `/write-summary` in Claude Code or `$write-summary` in Codex. After setup, start a fresh Claude Code session and use `/context all` to check the loaded project instructions and `/` to see the skill commands.

Both clients use the same [file-protection hook](.agents/hooks/files-protection.py) for files named `references.bib` or `settings.json`. It checks Claude Code’s `Edit` and `Write` tools and Codex’s `apply_patch` tool. In a new clone, accept Claude Code’s workspace trust prompt on first launch. In Codex, open the trusted project and use `/hooks` to review and trust the [project hook](.codex/hooks.json). Desktop notifications are configured in [Claude Code’s settings](.claude/settings.json).
