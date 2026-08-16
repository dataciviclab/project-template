"""Contract test per repo dataset multi-dataset (ADR-001).

Verifica la struttura del repo, non il motore del toolkit:
  - layout multi-dataset (datasets/ + support/)
  - ogni dataset espone un contratto minimo (dataset.yml, SQL dichiarati)
  - i path dichiarati sono relativi e POSIX
  - non si committano output di run (out/)
  - presenza dei componenti condivisi (Makefile, requirements.txt, workflows)

Markers: contract (contratto pubblico, artifact format).
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = REPO_ROOT / "out"
REQUIRED_FILES = [
    REPO_ROOT / "Makefile",
    REPO_ROOT / "requirements.txt",
    REPO_ROOT / "conftest.py",
    REPO_ROOT / "LICENSE",
    REPO_ROOT / "README.md",
    REPO_ROOT / "docs" / "sources.md",
    REPO_ROOT / "docs" / "decisions.md",
    REPO_ROOT / "docs" / "data_dictionary.md",
    REPO_ROOT / ".github" / "workflows" / "check.yml",
    REPO_ROOT / ".github" / "workflows" / "pipeline.yml",
]
BLOCKED_OUT_EXTENSIONS = {".parquet", ".csv", ".jsonl", ".zip", ".xlsx", ".tsv"}


def _iter_dataset_configs() -> list[Path]:
    configs: list[Path] = []
    for dirname in ("datasets", "support"):
        base = REPO_ROOT / dirname
        if base.exists():
            configs.extend(sorted(base.glob("*/dataset.yml")))
    return configs


@pytest.fixture(scope="module")
def dataset_configs() -> list[Path]:
    configs = _iter_dataset_configs()
    assert configs, "Il repo deve dichiarare almeno un dataset in datasets/ o support/"
    return configs


@pytest.mark.contract
def test_required_files_exist() -> None:
    missing = [str(p.relative_to(REPO_ROOT)) for p in REQUIRED_FILES if not p.exists()]
    assert not missing, f"Missing required template files: {missing}"


@pytest.mark.contract
def test_layout_is_multidataset() -> None:
    assert (REPO_ROOT / "datasets").is_dir(), "datasets/ è obbligatoria nel modello multi-dataset"
    root_config = REPO_ROOT / "dataset.yml"
    assert not root_config.exists(), "Nel modello multi-dataset non esiste dataset.yml in root"


@pytest.mark.contract
def test_each_dataset_declares_minimum_contract(dataset_configs: list[Path]) -> None:
    for cfg in dataset_configs:
        dataset = yaml.safe_load(cfg.read_text(encoding="utf-8"))
        rel = str(cfg.relative_to(REPO_ROOT))
        assert dataset.get("schema_version") == 1, f"{rel}: schema_version != 1"
        assert "root" in dataset, f"{rel}: manca root (path relativo a out/)"
        assert "dataset" in dataset, f"{rel}: manca blocco dataset"
        assert dataset["dataset"].get("name"), f"{rel}: manca dataset.name"
        assert isinstance(dataset["dataset"].get("years"), list), f"{rel}: years deve essere una lista"
        assert dataset["dataset"]["years"], f"{rel}: years non deve essere vuota"
        assert "raw" in dataset and dataset["raw"].get("sources"), f"{rel}: manca raw.sources"
        assert dataset["raw"]["sources"][0].get("primary") is True, f"{rel}: la prima source deve essere primary"
        assert dataset["clean"]["sql"], f"{rel}: manca clean.sql"
        assert dataset["clean"].get("required_columns"), f"{rel}: manca clean.required_columns"
        assert dataset["clean"]["validate"].get("primary_key"), f"{rel}: manca clean.validate.primary_key"
        assert dataset["clean"]["validate"].get("not_null"), f"{rel}: manca clean.validate.not_null"
        assert dataset["clean"]["validate"].get("min_rows") == 1, f"{rel}: min_rows deve essere 1"
        assert dataset["mart"]["tables"], f"{rel}: manca mart.tables"
        assert dataset["mart"].get("required_tables"), f"{rel}: manca mart.required_tables"
        assert dataset["mart"]["validate"].get("table_rules"), f"{rel}: manca mart.validate.table_rules"
        assert dataset["validation"]["fail_on_error"] is True, f"{rel}: fail_on_error deve essere true"
        assert dataset["output"]["artifacts"] in {"minimal", "standard", "debug"}, f"{rel}: artifacts non valido"


def _iter_path_values(node: object):
    if isinstance(node, dict):
        for key, value in node.items():
            if isinstance(value, str) and key in {"root", "source", "sql", "target", "dir", "path", "filename"}:
                yield key, value
            yield from _iter_path_values(value)
    elif isinstance(node, list):
        for item in node:
            yield from _iter_path_values(item)


@pytest.mark.contract
def test_dataset_paths_are_relative_and_posix(dataset_configs: list[Path]) -> None:
    for cfg in dataset_configs:
        dataset = yaml.safe_load(cfg.read_text(encoding="utf-8"))
        rel = str(cfg.relative_to(REPO_ROOT))
        for key, value in _iter_path_values(dataset):
            if value.startswith("http://") or value.startswith("https://"):
                continue
            assert value, f"{rel}: path vuoto per '{key}'"
            assert "\\" not in value, f"{rel}: path '{key}' deve usare separatori POSIX: {value}"
            assert not value.startswith("/"), f"{rel}: path assoluto POSIX per '{key}': {value}"
            assert not value.startswith("~"), f"{rel}: path home-relative per '{key}': {value}"
            assert not re.match(r"^[A-Za-z]:[\\/]", value), f"{rel}: path Windows per '{key}': {value}"


@pytest.mark.contract
def test_declared_sql_files_exist(dataset_configs: list[Path]) -> None:
    for cfg in dataset_configs:
        dataset = yaml.safe_load(cfg.read_text(encoding="utf-8"))
        cfg_dir = cfg.parent
        rel = str(cfg.relative_to(REPO_ROOT))

        clean_sql = (cfg_dir / dataset["clean"]["sql"]).resolve()
        assert clean_sql.is_file(), f"{rel}: manca clean SQL dichiarato: {dataset['clean']['sql']}"

        for table in dataset["mart"]["tables"]:
            assert table.get("name"), f"{rel}: ogni mart table deve dichiarare un name"
            assert table.get("sql"), f"{rel}: mart '{table['name']}' deve dichiarare un path SQL"
            sql_path = (cfg_dir / table["sql"]).resolve()
            assert sql_path.is_file(), f"{rel}: manca SQL mart dichiarato: {table['sql']}"


@pytest.mark.contract
def test_mart_table_names_are_unique(dataset_configs: list[Path]) -> None:
    for cfg in dataset_configs:
        dataset = yaml.safe_load(cfg.read_text(encoding="utf-8"))
        names = [t["name"] for t in dataset["mart"]["tables"]]
        rel = str(cfg.relative_to(REPO_ROOT))
        assert len(names) == len(set(names)), f"{rel}: nomi mart duplicati: {names}"


@pytest.mark.contract
def test_required_tables_and_rules_match_declared_marts(dataset_configs: list[Path]) -> None:
    for cfg in dataset_configs:
        dataset = yaml.safe_load(cfg.read_text(encoding="utf-8"))
        rel = str(cfg.relative_to(REPO_ROOT))
        names = {t["name"] for t in dataset["mart"]["tables"]}
        required = set(dataset["mart"]["required_tables"])
        rules = set(dataset["mart"]["validate"]["table_rules"].keys())
        assert required <= names, f"{rel}: mart.required_tables non riferisce tabelle dichiarate"
        assert rules <= names, f"{rel}: mart.validate.table_rules non riferisce tabelle dichiarate"


@pytest.mark.contract
def test_no_run_outputs_committed() -> None:
    if not OUT_DIR.exists():
        return
    offenders: list[str] = []
    for path in OUT_DIR.rglob("*"):
        if not path.is_file():
            continue
        if path.name == "README.md":
            continue
        if path.suffix.lower() in BLOCKED_OUT_EXTENSIONS or "_runs" in path.parts:
            offenders.append(str(path.relative_to(REPO_ROOT)).replace("\\", "/"))
    assert not offenders, f"Non committare output di run in out/: {offenders}"
