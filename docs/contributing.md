# Contributing

Guida rapida per contribuire ai dati senza dover leggere tutta la documentazione tecnica del progetto.

## Setup minimo

Prerequisiti:

- avere accesso al repo
- avere Python e il toolkit disponibili nel proprio ambiente, oppure un checkout locale del toolkit
- lavorare sempre dalla root del progetto

Questa repo contiene configurazione dataset, SQL, documentazione e test di contratto.
Il motore della pipeline sta nel repo toolkit.

## Contract tests

Esegui sempre prima:

```sh
py -m pytest tests/test_contract.py
```

Questi test non verificano il motore del toolkit.
Verificano che questa repo esponga un contratto coerente per il dataset: file dichiarati, path, tabelle mart e struttura minima della config.

## Smoke locale

Per uno smoke test end-to-end:

```sh
sh scripts/smoke.sh
```

Se il toolkit non è nel `PATH`, usa il fallback documentato nello script.
Se lo smoke fallisce per un problema del motore, apri il bug nel repo toolkit.
Se fallisce per config, SQL o assunzioni sul dato, correggi questa repo.

Su Windows, se `sh` non è disponibile nel `PATH`, usa una shell POSIX come Git Bash oppure esegui i comandi toolkit equivalenti:

```powershell
toolkit run all --config dataset.yml
toolkit validate all --config dataset.yml
toolkit status --dataset <dataset> --year <year> --latest --config dataset.yml
```

## Publish su Drive

Se il progetto usa un archivio pubblico su Drive, la pubblicazione va fatta dopo `run all` e `validate all`, non durante il run.

Dry-run:

```powershell
py scripts/publish_to_drive.py --config dataset.yml --drive-root "G:\DataCivicLab" --dry-run
```

Publish di un anno:

```powershell
py scripts/publish_to_drive.py --config dataset.yml --drive-root "G:\DataCivicLab" --year 2022
```

Lo script pubblica per default payload RAW, metadata, manifest e validation di `raw`, `clean`, `mart`, i parquet CLEAN/MART e l'ultimo run record.
La destinazione su Drive mantiene gli stessi path relativi sotto `root`, quindi pubblica sotto `<drive-root>/data/...`.

## Comandi canonici toolkit

```sh
toolkit run all --config dataset.yml
toolkit run raw --config dataset.yml
toolkit run clean --config dataset.yml
toolkit run mart --config dataset.yml
toolkit validate all --config dataset.yml
toolkit status --dataset <dataset> --year <year> --latest --config dataset.yml
```

## Fasi operative

- kickoff e contratto: `dataset.yml`, `README.md`, `tests/test_contract.py`
- sources e raw: `dataset.yml`, `docs/sources.md`, `docs/decisions.md`, `notebooks/01_inspect_raw.ipynb`
- clean: `sql/clean.sql`, `dataset.yml`, `notebooks/02_inspect_clean.ipynb`
- mart: `sql/mart/*.sql`, `dataset.yml`, `notebooks/03_explore_mart.ipynb`
- qa: `tests/test_contract.py`, `.github/workflows/ci.yml`, `notebooks/04_quality_checks.ipynb`
- dashboard/export: `dashboard/`, `README.md`, `notebooks/05_dashboard_export.ipynb`

## Checklist lifecycle

| Fase | File principali | Comando minimo | Notebook |
|---|---|---|---|
| Kickoff | `dataset.yml`, `README.md` | `py -m pytest tests/test_contract.py` | `00_quickstart.ipynb` |
| Sources/RAW | `dataset.yml`, `docs/sources.md`, `docs/decisions.md` | `toolkit run raw --config dataset.yml` | `01_inspect_raw.ipynb` |
| CLEAN | `sql/clean.sql`, `dataset.yml`, `docs/data_dictionary.md` | `toolkit run clean --config dataset.yml` | `02_inspect_clean.ipynb` |
| MART | `sql/mart/*.sql`, `dataset.yml` | `toolkit run mart --config dataset.yml` | `03_explore_mart.ipynb` |
| QA | `tests/test_contract.py`, `.github/workflows/ci.yml` | `toolkit validate all --config dataset.yml` | `04_quality_checks.ipynb` |
| Output pubblico | `dashboard/`, `README.md`, `scripts/publish_to_drive.py` | `py scripts/publish_to_drive.py --config dataset.yml --drive-root "<drive>" --dry-run` | `05_dashboard_export.ipynb` |
| Release | `README.md`, `docs/overview.md`, `docs/data_dictionary.md` | `toolkit status --dataset <dataset> --year <year> --latest --config dataset.yml` | `00_quickstart.ipynb` |

## Regole veloci

- non committare output sotto `data/`, salvo sample piccoli in `data/_examples`
- aggiorna `docs/decisions.md` quando cambi scelte o trade-off
- aggiorna `docs/data_dictionary.md` quando cambia il significato dei campi
- usa path root-relative e POSIX nella documentazione tecnica

## Come aiutare in 15 minuti

- controlla che `docs/sources.md` e `docs/overview.md` siano coerenti
- migliora una descrizione in `docs/data_dictionary.md`
- esegui `py -m pytest tests/test_contract.py` e segnala eventuali problemi
- apri i notebook per ispezionare gli output generati dal toolkit, senza aggiungere logica di pipeline qui

## Poi dove vado?

- workflow umano: [../WORKFLOW.md](../WORKFLOW.md)
- docs locali: [README.md](README.md)
- standard Lab: [lab_links.md](lab_links.md)
