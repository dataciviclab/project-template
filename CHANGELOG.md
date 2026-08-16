# 📜 Changelog — project-template

## v0.4 — Modello multi-dataset (ADR-001)

### Cambiato
- Struttura repo multi-dataset: `datasets/` + `support/` (un `dataset.yml` per dataset), niente più `dataset.yml` in root
- `Makefile` come interfaccia stabile: `make check`, `make seeds`, `make run`, `make registry`
- Workflow condivisi dal `.github` org: `check` (dataset-config-check-reusable), `pipeline` (python-setup + gcs-auth + registry-update-pr), `test-audit` (test-audit-reusable)
- `requirements.txt` come fonte di verità (repo dataset puro, ADR-001 §8)
- `tests/test_contract.py` riscritto per il modello multi-dataset; aggiunto `conftest.py` con i marker canonici
- `.github/PULL_REQUEST_TEMPLATE.md` dal template org
- Rimosso: `sql/` in root, `scripts/smoke.sh`, `scripts/publish_to_drive.py`, notebook demo, `dashboard/`, `data/`
- Docs e seed-issues allineati al modello multi-dataset

## v0.1-v0.3

Storico del template precedente (single-dataset, smoke shell, CI inline).
