"""Project locations for an editable install or a source checkout."""

from pathlib import Path


def _find_root() -> Path:
    config_file = Path(__file__).resolve()
    root = config_file.parents[3]
    if (
        config_file.parent.parent != root / "code" / "src"
        or not (root / "code" / "pyproject.toml").is_file()
    ):
        raise FileNotFoundError(
            "Expected code/src/<package>/config.py and code/pyproject.toml. "
            "Install this project in editable mode from its code directory."
        )
    return root


ROOT = _find_root()

RAW = ROOT / "data" / "raw"
INTERMEDIATE = ROOT / "data" / "intermediate"
PROCESSED = ROOT / "data" / "processed"
OUTPUT = ROOT / "output"
TABLES = OUTPUT / "core" / "tables"
FIGURES = OUTPUT / "core" / "figures"
EXPLORATION_OUTPUT = OUTPUT / "exploration"


def output_path(tier: str, kind: str, variant: str) -> Path:
    """Return a variant's tables or figures directory without creating it.

    Args:
        tier: core, exploration, or archive.
        kind: tables or figures.
        variant: A single directory name, conventionally in snake_case.

    Raises:
        ValueError: A tier, kind, or directory name is invalid.
    """
    if tier not in {"core", "exploration", "archive"}:
        raise ValueError("tier must be core, exploration, or archive")
    if kind not in {"tables", "figures"}:
        raise ValueError("kind must be tables or figures")
    if not variant or variant in {".", ".."} or "/" in variant or "\\" in variant:
        raise ValueError("variant must be a single directory name")
    return OUTPUT / tier / kind / variant
