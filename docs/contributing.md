# Contributing

Guida rapida per contribuire ai dati senza dover leggere tutta la documentazione tecnica del progetto.

## Setup minimo

Prerequisiti:

- avere accesso al repo
- avere Python e il toolkit disponibili nel proprio ambiente, oppure un checkout locale del toolkit
- lavorare sempre dalla root del progetto

## Contract tests

Esegui sempre prima:

```sh
pytest tests/test_contract.py
```

## Smoke locale

Per uno smoke test end-to-end:

```sh
sh scripts/smoke.sh 2024
```

Se il toolkit non è nel `PATH`, usa il fallback documentato nello script.

## Regole veloci

- non committare output sotto `data/`, salvo sample piccoli in `data/_examples`
- aggiorna `docs/decisions.md` quando cambi scelte o trade-off
- aggiorna `docs/data_dictionary.md` quando cambia il significato dei campi
- usa path root-relative e POSIX nella documentazione tecnica

## Come aiutare in 15 minuti

- controlla che `docs/sources.md` e `docs/overview.md` siano coerenti
- migliora una descrizione in `docs/data_dictionary.md`
- esegui `pytest tests/test_contract.py` e segnala eventuali problemi

## Poi dove vado?

- workflow umano: [../WORKFLOW.md](../WORKFLOW.md)
- docs locali: [README.md](README.md)
- standard Lab: [lab_links.md](lab_links.md)
