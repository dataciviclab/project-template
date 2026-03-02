from __future__ import annotations

import json
import re
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
DATASET_FILE = REPO_ROOT / "dataset.yml"
DATA_DIR = REPO_ROOT / "data"
NOTEBOOKS_DIR = REPO_ROOT / "notebooks"
BLOCKED_DATA_EXTENSIONS = {".parquet", ".csv", ".jsonl", ".zip", ".xlsx", ".tsv"}
REQUIRED_FILES = [
    REPO_ROOT / "dataset.yml",
    REPO_ROOT / "sql" / "clean.sql",
    REPO_ROOT / "docs" / "sources.md",
    REPO_ROOT / "docs" / "decisions.md",
    REPO_ROOT / "docs" / "data_dictionary.md",
    REPO_ROOT / "scripts" / "smoke.sh",
    REPO_ROOT / ".github" / "workflows" / "ci.yml",
]


def _load_dataset() -> dict:
    return yaml.safe_load(DATASET_FILE.read_text(encoding="utf-8"))


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


def test_dataset_declares_minimum_contract() -> None:
    dataset = _load_dataset()

    assert dataset.get("schema_version") == 1
    assert "root" in dataset
    assert "dataset" in dataset
    assert "name" in dataset["dataset"]
    assert "years" in dataset["dataset"]
    assert isinstance(dataset["dataset"]["years"], list)
    assert dataset["dataset"]["years"]
    assert "raw" in dataset
    assert "sources" in dataset["raw"]
    assert isinstance(dataset["raw"]["sources"], list)
    assert dataset["raw"]["sources"]
    assert dataset["raw"]["sources"][0]["primary"] is True
    assert "clean" in dataset
    assert dataset["clean"]["sql"]
    assert dataset["clean"]["read_mode"] in {"strict", "fallback", "robust"}
    assert "read" in dataset["clean"]
    assert isinstance(dataset["clean"]["read"], dict)
    assert dataset["clean"]["read"]["source"] in {"auto", "config_only"}
    assert dataset["clean"]["read"]["mode"] in {"explicit", "latest", "largest", "all"}
    assert "header" in dataset["clean"]["read"]
    assert "columns" in dataset["clean"]["read"]
    assert dataset["clean"]["required_columns"]
    assert dataset["clean"]["validate"]["primary_key"]
    assert dataset["clean"]["validate"]["not_null"]
    assert dataset["clean"]["validate"]["min_rows"] == 1
    assert "mart" in dataset
    assert "tables" in dataset["mart"]
    assert isinstance(dataset["mart"]["tables"], list)
    assert dataset["mart"]["tables"]
    assert dataset["mart"]["required_tables"]
    assert "table_rules" in dataset["mart"]["validate"]
    assert dataset["validation"]["fail_on_error"] is True
    assert dataset["output"]["artifacts"] in {"minimal", "standard", "debug"}


def test_dataset_avoids_legacy_clean_read_shape() -> None:
    dataset = _load_dataset()

    assert "csv" not in dataset["clean"]["read"]


def test_dataset_paths_are_relative_and_posix() -> None:
    dataset = _load_dataset()

    for key, value in _iter_path_values(dataset):
        if value.startswith("http://") or value.startswith("https://"):
            continue
        assert value, f"Empty path value for key '{key}'"
        assert "\\" not in value, f"Path for key '{key}' must use POSIX separators: {value}"
        assert not value.startswith("/"), f"Absolute POSIX path found for key '{key}': {value}"
        assert not value.startswith("~"), f"Home-relative path found for key '{key}': {value}"
        assert not re.match(r"^[A-Za-z]:[\\/]", value), f"Absolute Windows path found for key '{key}': {value}"


def test_declared_sql_files_exist() -> None:
    dataset = _load_dataset()

    clean_sql = REPO_ROOT / dataset["clean"]["sql"]
    assert clean_sql.exists(), f"Missing clean SQL file declared in dataset.yml: {dataset['clean']['sql']}"

    mart_tables = dataset["mart"]["tables"]
    for table in mart_tables:
        assert "name" in table and table["name"], "Each mart table must declare a non-empty name"
        assert "sql" in table and table["sql"], f"Mart table '{table['name']}' must declare an SQL path"
        sql_path = REPO_ROOT / table["sql"]
        assert sql_path.exists(), f"Missing mart SQL file declared in dataset.yml: {table['sql']}"


def test_mart_table_names_are_unique() -> None:
    dataset = _load_dataset()
    names = [table["name"] for table in dataset["mart"]["tables"]]
    assert len(names) == len(set(names)), f"Duplicate mart table names found: {names}"


def test_required_tables_and_rules_match_declared_marts() -> None:
    dataset = _load_dataset()

    names = {table["name"] for table in dataset["mart"]["tables"]}
    required_tables = set(dataset["mart"]["required_tables"])
    table_rules = set(dataset["mart"]["validate"]["table_rules"].keys())

    assert required_tables <= names, "mart.required_tables must reference declared mart.tables"
    assert table_rules <= names, "mart.validate.table_rules must reference declared mart.tables"


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


def test_notebooks_do_not_rebuild_runtime_output_paths() -> None:
    forbidden_patterns = [
        "OUT_ROOT =",
        "/ 'data' / 'raw' /",
        "/ 'data' / 'clean' /",
        "/ 'data' / 'mart' /",
        "/ 'data' / '_runs' /",
        "Path(INSPECT['paths']['mart']['dir']) /",
    ]

    offenders: list[str] = []

    for path in sorted(NOTEBOOKS_DIR.glob("*.ipynb")):
        notebook = json.loads(path.read_text(encoding="utf-8"))
        for cell in notebook.get("cells", []):
            if cell.get("cell_type") != "code":
                continue
            source = "".join(cell.get("source", []))
            for pattern in forbidden_patterns:
                if pattern in source:
                    offenders.append(f"{path.relative_to(REPO_ROOT)} -> {pattern}")

    assert not offenders, (
        "I notebook devono usare `toolkit inspect paths --json` come fonte di verita` "
        "e non ricostruire a mano i path del runtime. "
        f"Found: {offenders}"
    )
