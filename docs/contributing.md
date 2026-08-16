# Contributing

Guida rapida per contribuire a un repo dataset senza dover capire tutto l'ecosistema in un colpo solo.

Le policy comuni dell'organizzazione non vengono duplicate qui: per quelle, il posto giusto e `.github`.
Questo documento resta pratico e locale al repo dataset.

## Setup minimo

Prerequisiti:

- avere accesso al repo
- avere Python e il toolkit disponibili nel proprio ambiente, oppure un checkout locale del toolkit
- lavorare sempre dalla root del progetto

Questa repo contiene configurazione dataset (`datasets/`, `support/`), SQL,
documentazione e test di contratto. Il motore della pipeline sta nel repo `toolkit`.

## Contract tests

Esegui sempre prima:

```sh
python -m pytest tests/
```

Questi test non verificano il motore del toolkit.
Verificano che questa repo esponga un contratto coerente per ogni dataset:
file dichiarati, path, tabelle mart e struttura minima della config.

## Smoke locale

Per uno smoke test end-to-end (preflight + run di tutti i dataset):

```sh
make check   # valida i dataset.yml senza eseguire
make seeds   # esegue i support dataset
make run     # esegue tutti i dataset (RAW → CLEAN → MART)
```

Se il run fallisce per un problema del motore, apri il bug nel repo `toolkit`.
Se fallisce per config, SQL o assunzioni sul dato, correggi questa repo.

Su Windows, se `make` non e disponibile, usa i comandi toolkit equivalenti
per dataset (ogni `--config` punta a `datasets/<slug>/dataset.yml`):

```powershell
toolkit run --config datasets/<slug>/dataset.yml
toolkit validate all --config datasets/<slug>/dataset.yml
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

## Pubblicazione output

La pubblicazione avviene automaticamente nella pipeline (workflow `pipeline`):
sync su GCS (`gs://dataciviclab-clean/<repo-slug>/` e `gs://dataciviclab-mart/`)
e aggiornamento del registry (`registry/registry.json`, draft PR). Non serve un
passo manuale per pubblicare: basta far passare `make run` in CI.

## Comandi canonici toolkit

```sh
make check      # preflight su tutti i dataset (senza eseguire)
make seeds      # esegue i support dataset
make run        # esegue tutti i dataset (RAW → CLEAN → MART)
```

Per dataset singolo:

```sh
toolkit run --config datasets/<slug>/dataset.yml
toolkit validate all --config datasets/<slug>/dataset.yml
toolkit inspect summary --dataset <dataset> --year <year> --latest --config datasets/<slug>/dataset.yml
toolkit inspect paths --config datasets/<slug>/dataset.yml --year <year> --json
```

Per workflow avanzati come `run raw|clean|mart`, `resume` o `profile raw`, vedi
la documentazione del toolkit. Regola semplice per i layer:

- `toolkit run raw|clean|mart ...` produce gli artifact
- `toolkit inspect paths --config <dataset.yml> --year <year> --json` ti dice dove leggerli
- notebook e controlli manuali devono leggere i path restituiti, non ricostruirli a mano

## Fasi operative leggere (per dataset)

- kickoff e contratto: `datasets/<slug>/dataset.yml`, `README.md`, `tests/test_contract.py`
- sources e raw: `datasets/<slug>/dataset.yml`, `docs/sources.md`, `docs/decisions.md`
- clean: `datasets/<slug>/sql/clean.sql`, `datasets/<slug>/dataset.yml`
- mart: `datasets/<slug>/sql/mart_*.sql`, `datasets/<slug>/dataset.yml`
- release e handoff: `README.md`, `docs/overview.md`, `docs/data_dictionary.md`
- maintenance: `datasets/<slug>/dataset.yml`, `sql/`, `docs/`, `tests/test_contract.py`

Queste fasi non sono una catena rigida: spesso bastano 2-4 issue piccole per far avanzare davvero il progetto.

## Checklist lifecycle

| Fase | File principali | Comando minimo |
|---|---|---|
| Kickoff | `dataset.yml`, `README.md` | `python -m pytest tests/` |
| Sources/RAW | `dataset.yml`, `docs/sources.md`, `docs/decisions.md` | `toolkit run raw --config <dataset.yml>` |
| CLEAN | `sql/clean.sql`, `dataset.yml`, `docs/data_dictionary.md` | `toolkit run clean --config <dataset.yml>` |
| MART | `sql/mart_*.sql`, `dataset.yml` | `toolkit run mart --config <dataset.yml>` |
| Release | `README.md`, `docs/overview.md`, `docs/data_dictionary.md` | `toolkit inspect summary --config <dataset.yml>` |
| Maintenance | `dataset.yml`, `sql/`, `docs/`, `tests/` | `make run` |

Ruoli minimi da tenere distinti negli artifact:

- `metadata.json` = payload ricco del layer
- `manifest.json` = summary stabile del layer con puntatori a metadata e validation
- `out/data/_runs/.../<run_id>.json` = stato del run usato da `status` e `resume`

## Regole veloci

- non committare output sotto `out/` (parquet, csv, json, run record)
- aggiorna `docs/decisions.md` quando cambi scelte o trade-off
- aggiorna `docs/data_dictionary.md` quando cambia il significato dei campi
- usa path root-relative e POSIX nella documentazione tecnica

## Come aiutare in 15 minuti

- controlla che `docs/sources.md` e `docs/overview.md` siano coerenti
- migliora una descrizione in `docs/data_dictionary.md`
- esegui `python -m pytest tests/` e segnala eventuali problemi
- esegui `make check` e segnala dataset.yml non validi

## Poi dove vado?

- workflow umano: [../WORKFLOW.md](../WORKFLOW.md)
- docs locali: [README.md](README.md)
- contesto DataCivicLab, policy comuni e motore: [lab_links.md](lab_links.md)
