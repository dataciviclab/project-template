# Contribuire a questo repo

Questo è un **template** per i dataset repo del Lab. Per creare un nuovo dataset:

1. **Copia la struttura** di `datasets/demo-saldi-stato/` (rimuovi il demo)
2. **Crea `datasets/<slug>/dataset.yml`** seguendo lo schema in `standards/pipeline.md`
3. **Scrivi `sql/clean.sql`** — usa le macro standard (`cast_int`, `cast_double`, `normalize_string`)
4. **Scrivi `sql/mart_*.sql`** — 1 file = 1 tabella mart
5. **Aggiungi `Makefile` targets** se servono customizzazioni
6. **Apri una PR** — la CI valida config e struttura

## Comandi

```bash
make check       # validazione config (preflight)
make run         # esegui tutti i dataset
make seeds       # esegui support datasets (prima dei principali)
make clean       # pulisci output
```

## Standard

- **Dataset**: `standards/pipeline.md`
- **Test**: `standards/tests.md`
- **Workflow**: `standards/workflows.md`
- **Repo**: `standards/repo.md`

## Struttura

```
datasets/<slug>/
├── dataset.yml       contratto pipeline
├── sql/
│   ├── clean.sql     RAW → CLEAN (usa macro standard)
│   └── mart_*.sql    CLEAN → MART (1 file = 1 tabella)
└── notes.md          quirk, decisioni, deroga

support/<slug>/       anagrafiche usate dai dataset principali
registry/             artifact registry (registry.json)
dashboard/            Streamlit + lab-connectors
tests/                test con marcatori
```

## Link

- [Discussioni](https://github.com/dataciviclab/dataciviclab/discussions)
- [Toolkit docs](https://github.com/dataciviclab/toolkit/tree/main/docs)
- [ADR-001](https://github.com/dataciviclab/.github/blob/main/docs/adr/001-workflow-architecture.md)
