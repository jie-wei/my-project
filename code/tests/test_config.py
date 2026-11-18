"""Regression checks for project roots and research output destinations."""

import csv
import runpy
import shutil
from pathlib import Path

import pytest

CONFIG_FILE = Path(__file__).resolve().parents[1] / "src" / "mypackage" / "config.py"


@pytest.fixture
def source_project(tmp_path):
    """Copy the path configuration into a small project with synthetic data."""
    project = tmp_path / "parent_repo" / "research" / "project"
    config = project / "code" / "src" / "mypackage" / "config.py"
    config.parent.mkdir(parents=True)
    shutil.copyfile(CONFIG_FILE, config)
    (project / "code" / "pyproject.toml").write_text("[project]\n", encoding="utf-8")
    return project, config


@pytest.mark.parametrize("git_marker", ["absent", "parent", "directory", "file"])
def test_root_uses_source_project(source_project, tmp_path, monkeypatch, git_marker):
    project, config = source_project
    if git_marker == "parent":
        (tmp_path / "parent_repo" / ".git").mkdir()
    elif git_marker == "directory":
        (project / ".git").mkdir()
    elif git_marker == "file":
        (project / ".git").write_text("gitdir: external-worktree\n", encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    settings = runpy.run_path(str(config))

    assert settings["ROOT"] == project
    assert settings["RAW"] == project / "data" / "raw"
    assert settings["INTERMEDIATE"] == project / "data" / "intermediate"
    assert settings["PROCESSED"] == project / "data" / "processed"
    assert settings["TABLES"] == project / "output" / "core" / "tables"
    assert settings["FIGURES"] == project / "output" / "core" / "figures"
    assert settings["EXPLORATION_OUTPUT"] == project / "output" / "exploration"
    assert not (project / "output").exists()


def test_missing_project_marker_fails_without_using_parent_repo(source_project, tmp_path):
    project, config = source_project
    (project / "code" / "pyproject.toml").unlink()
    (tmp_path / "parent_repo" / ".git").mkdir()
    with pytest.raises(FileNotFoundError, match="code/pyproject.toml"):
        runpy.run_path(str(config))


@pytest.mark.parametrize("tier", ["core", "exploration", "archive"])
@pytest.mark.parametrize("kind", ["tables", "figures"])
def test_output_locations_match_summary_layout(source_project, tier, kind):
    project, config = source_project
    settings = runpy.run_path(str(config))
    destination = settings["output_path"](tier, kind, "wage_posting")
    assert destination == project / "output" / tier / kind / "wage_posting"
    assert not destination.exists()


@pytest.mark.parametrize(
    "tier,kind,variant",
    [
        ("other", "tables", "demo"),
        ("core", "other", "demo"),
        ("core", "tables", ""),
        ("core", "tables", "."),
        ("core", "tables", ".."),
        ("core", "tables", "../demo"),
        ("core", "tables", "/tmp/demo"),
        ("core", "tables", "nested/demo"),
        ("core", "tables", "nested\\demo"),
    ],
)
def test_invalid_output_location_fails(source_project, tier, kind, variant):
    _, config = source_project
    settings = runpy.run_path(str(config))
    with pytest.raises(ValueError):
        settings["output_path"](tier, kind, variant)


def test_synthetic_io_after_tier_change(source_project, tmp_path, monkeypatch):
    project, config = source_project
    settings = runpy.run_path(str(config))
    raw = settings["RAW"] / "wages.csv"
    raw.parent.mkdir(parents=True)
    original = "wage\n10\n20\n"
    raw.write_text(original, encoding="utf-8")
    old_tables = settings["output_path"]("exploration", "tables", "wage_posting")
    old_tables.mkdir(parents=True)
    (old_tables / "summary.csv").write_text("mean_wage\n15.0\n", encoding="utf-8")
    core_tables = settings["output_path"]("core", "tables", "wage_posting")
    core_tables.parent.mkdir(parents=True)
    old_tables.rename(core_tables)
    monkeypatch.chdir(tmp_path)

    with raw.open(newline="", encoding="utf-8") as file:
        wages = [float(row["wage"]) for row in csv.DictReader(file)]
    destination = settings["output_path"]("core", "tables", "wage_posting")
    destination.mkdir(parents=True, exist_ok=True)
    with (destination / "summary.csv").open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["mean_wage"])
        writer.writerow([sum(wages) / len(wages)])

    assert (project / "output/core/tables/wage_posting/summary.csv").read_text() == (
        "mean_wage\n15.0\n"
    )
    assert raw.read_text() == original
    assert not old_tables.exists()
