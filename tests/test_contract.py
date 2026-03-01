from __future__ import annotations

import re
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
DATASET_FILE = REPO_ROOT / "dataset.yml"
DATA_DIR = REPO_ROOT / "data"
BLOCKED_DATA_EXTENSIONS = {".parquet", ".csv", ".jsonl", ".zip", ".xlsx", ".tsv"}
REQUIRED_FILES = [
    REPO_ROOT / "dataset.yml",
    REPO_ROOT / "sql" / "clean.sql",
    REPO_ROOT / "sql" / "mart" / "project_summary.sql",
    REPO_ROOT / "docs" / "sources.md",
    REPO_ROOT / "docs" / "decisions.md",
    REPO_ROOT / "docs" / "data_dictionary.md",
    REPO_ROOT / "scripts" / "smoke.sh",
    REPO_ROOT / ".github" / "workflows" / "ci.yml",
]


def _iter_path_values(node: object):
    if isinstance(node, dict):
        for key, value in node.items():
            if isinstance(value, str) and key in {"root", "source", "sql", "target", "dir", "path", "filename"}:
                yield key, value
            yield from _iter_path_values(value)
    elif isinstance(node, list):
        for item in node:
            yield from _iter_path_values(item)


def test_required_files_exist() -> None:
    missing = [str(path.relative_to(REPO_ROOT)) for path in REQUIRED_FILES if not path.exists()]
    assert not missing, f"Missing required template files: {missing}"


def test_dataset_uses_supported_contract_keys() -> None:
    dataset = yaml.safe_load(DATASET_FILE.read_text(encoding="utf-8"))
    clean_read = dataset["clean"]["read"]

    assert "dataset" in dataset
    assert "name" in dataset["dataset"]
    assert "years" in dataset["dataset"]
    assert dataset["validation"]["fail_on_error"] is True
    assert "source" in clean_read
    assert "header" in clean_read
    assert "columns" in clean_read
    assert "csv" not in clean_read
    assert dataset["clean"]["required_columns"]
    assert dataset["clean"]["validate"]["primary_key"]
    assert dataset["clean"]["validate"]["not_null"]
    assert "mart" in dataset
    assert "tables" in dataset["mart"]
    assert isinstance(dataset["mart"]["tables"], list)
    assert dataset["mart"]["tables"]
    assert dataset["mart"]["required_tables"]
    assert dataset["mart"]["validate"]["table_rules"]["project_summary"]["required_columns"]


def test_dataset_matches_smoke_contract_shape() -> None:
    dataset = yaml.safe_load(DATASET_FILE.read_text(encoding="utf-8"))

    assert dataset["output"]["artifacts"] == "minimal"
    assert "csv" not in dataset["clean"]["read"]


def test_dataset_paths_are_relative_and_posix() -> None:
    dataset = yaml.safe_load(DATASET_FILE.read_text(encoding="utf-8"))

    for key, value in _iter_path_values(dataset):
        if value.startswith("http://") or value.startswith("https://"):
            continue
        assert value, f"Empty path value for key '{key}'"
        assert "\\" not in value, f"Path for key '{key}' must use POSIX separators: {value}"
        assert not value.startswith("/"), f"Absolute POSIX path found for key '{key}': {value}"
        assert not value.startswith("~"), f"Home-relative path found for key '{key}': {value}"
        assert not re.match(r"^[A-Za-z]:[\\/]", value), f"Absolute Windows path found for key '{key}': {value}"


def test_yaml_sql_paths_match_template_files() -> None:
    dataset = yaml.safe_load(DATASET_FILE.read_text(encoding="utf-8"))

    assert dataset["clean"]["sql"] == "sql/clean.sql"

    mart_tables = dataset["mart"]["tables"]
    project_summary = next((table for table in mart_tables if table["name"] == "project_summary"), None)
    assert project_summary is not None, "Missing mart table 'project_summary'"
    assert project_summary["sql"] == "sql/mart/project_summary.sql"


def test_output_artifacts_is_configured() -> None:
    dataset = yaml.safe_load(DATASET_FILE.read_text(encoding="utf-8"))

    assert dataset["output"]["artifacts"] == "minimal"


def test_data_directory_does_not_contain_committed_outputs() -> None:
    offenders: list[str] = []

    if not DATA_DIR.exists():
        return

    for path in DATA_DIR.rglob("*"):
        if not path.is_file():
            continue
        if "_examples" in path.parts:
            continue
        if path.name == "README.md":
            continue
        if path.suffix.lower() not in BLOCKED_DATA_EXTENSIONS:
            continue
        offenders.append(str(path.relative_to(REPO_ROOT)).replace("\\", "/"))

    assert not offenders, (
        "Non committare output in data/: usa data/_examples per sample piccoli. "
        f"Found: {offenders}"
    )
