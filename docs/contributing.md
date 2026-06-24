# Contributing

Guida rapida per contribuire a un repo dataset senza dover capire tutto l'ecosistema in un colpo solo.

Le policy comuni dell'organizzazione non vengono duplicate qui: per quelle, il posto giusto e `.github`.
Questo documento resta pratico e locale al repo dataset.

## Setup minimo

Prerequisiti:

- avere accesso al repo
- avere Python e il toolkit disponibili nel proprio ambiente, oppure un checkout locale del toolkit
- lavorare sempre dalla root del progetto

Questa repo contiene configurazione dataset, SQL, documentazione e test di contratto.
Il motore della pipeline sta nel repo `toolkit`.

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

Se il toolkit non e nel `PATH`, usa il fallback documentato nello script.
Se lo smoke fallisce per un problema del motore, apri il bug nel repo `toolkit`.
Se fallisce per config, SQL o assunzioni sul dato, correggi questa repo.

Su Windows, se `sh` non e disponibile nel `PATH`, usa una shell POSIX come Git Bash oppure esegui i comandi toolkit equivalenti:

```powershell
toolkit run all --config dataset.yml
toolkit validate all --config dataset.yml
toolkit inspect summary --dataset <dataset> --year <year> --latest --config dataset.yml
```

## Dove scrivere cosa

- Discussions della repo: domande, interpretazioni, proposte e contesto
- Issues della repo: bug, task e blocchi operativi
- Project board o milestone della repo, se presenti: avanzamento e priorita
- Discord o altri canali veloci del team: utili per scambio rapido, non come fonte canonica

Regola pratica:

- non aprire issue grandi di lifecycle "per principio"
- usa poche issue piccole, legate a un blocco reale o al prossimo passo concreto
- le seed issue in `.github/seed-issues/` servono come base da adattare, non come pacchetto da aprire in blocco

## Publish su Drive

Se il progetto usa un archivio pubblico su Drive, la pubblicazione va fatta dopo `run all` e `validate all`, non durante il run.
Questo passaggio e `maintainer-only`: non e richiesto ai contributor per lavorare su SQL, docs, test o notebook.

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
toolkit validate all --config dataset.yml
toolkit inspect summary --dataset <dataset> --year <year> --latest --config dataset.yml
toolkit inspect paths --config dataset.yml --year <year> --json
```

Per workflow avanzati come `run raw|clean|mart`, `resume` o `profile raw`, vedi la documentazione advanced del toolkit.
Per il contratto stabile dei notebook e la matrice di stabilita delle feature, vedi anche:

- `docs/notebook-contract.md`
- `docs/feature-stability.md`

Quando lavori per layer invece che con `run all`, usa questa regola semplice:

- `toolkit run raw|clean|mart ...` produce gli artifact
- `toolkit inspect paths --config dataset.yml --year <year> --json` ti dice dove leggerli
- notebook e controlli manuali devono leggere i path restituiti, non ricostruirli a mano

## Fasi operative leggere

- kickoff e contratto: `dataset.yml`, `README.md`, `tests/test_contract.py`
- sources e raw: `dataset.yml`, `docs/sources.md`, `docs/decisions.md`, `notebooks/01_inspect_raw.ipynb`
- clean: `sql/clean.sql`, `dataset.yml`, `notebooks/02_inspect_clean.ipynb`
- mart: `sql/mart/*.sql`, `dataset.yml`, `notebooks/03_explore_mart.ipynb`
- release e handoff: `README.md`, `docs/overview.md`, `docs/data_dictionary.md`
- maintenance: `dataset.yml`, `sql/`, `docs/`, `tests/test_contract.py`

Queste fasi non sono una catena rigida: spesso bastano 2-4 issue piccole per far avanzare davvero il progetto.

## Checklist lifecycle

| Fase | File principali | Comando minimo | Notebook |
|---|---|---|---|
| Kickoff | `dataset.yml`, `README.md` | `py -m pytest tests/test_contract.py` | `00_quickstart.ipynb` |
| Sources/RAW | `dataset.yml`, `docs/sources.md`, `docs/decisions.md` | `toolkit run raw --config dataset.yml`, poi `toolkit inspect paths --config dataset.yml --year <year> --json` | `01_inspect_raw.ipynb` |
| CLEAN | `sql/clean.sql`, `dataset.yml`, `docs/data_dictionary.md` | `toolkit run clean --config dataset.yml`, poi `toolkit inspect paths --config dataset.yml --year <year> --json` | `02_inspect_clean.ipynb` |
| MART | `sql/mart/*.sql`, `dataset.yml` | `toolkit run mart --config dataset.yml`, poi `toolkit inspect paths --config dataset.yml --year <year> --json` | `03_explore_mart.ipynb` |
| Release | `README.md`, `docs/overview.md`, `docs/data_dictionary.md` | `toolkit inspect summary --dataset <dataset> --year <year> --latest --config dataset.yml` | `00_quickstart.ipynb` |
| Maintenance | `dataset.yml`, `sql/`, `docs/`, `tests/test_contract.py` | `toolkit run all --config dataset.yml` | `01_inspect_raw.ipynb`, `02_inspect_clean.ipynb`, `03_explore_mart.ipynb` |

I notebook usano `toolkit inspect paths --config dataset.yml --year <year> --json` come contratto stabile per localizzare gli output.

Ruoli minimi da tenere distinti nei notebook:

- `metadata.json` = payload ricco del layer
- `manifest.json` = summary stabile del layer con puntatori a metadata e validation
- `data/_runs/.../<run_id>.json` = stato del run usato da `status` e `resume`

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
- contesto DataCivicLab, policy comuni e motore: [lab_links.md](lab_links.md)
