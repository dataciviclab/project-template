---
title: "[Kickoff] Definire perimetro, domanda e contratto iniziale"
labels: ["LEAD", "METODO"]
assignees: []
---
## Obiettivo

Aprire il progetto con un perimetro chiaro e un contratto minimo coerente con il template.

Usare questa issue solo se il repo e appena nato o se il perimetro e ancora ambiguo.

## Checklist

- [ ] Definire una domanda guida chiara
- [ ] Identificare i dataset principali e i support dataset (struttura `datasets/` + `support/`)
- [ ] Sostituire `datasets/demo-saldi-stato/` con un dataset reale (`dataset.name`, `dataset.years`, `root`)
- [ ] Compilare `Makefile` e workflow (bucket GCS, prefix registry) con lo slug del repo
- [ ] Verificare che i path in config siano root-relative POSIX
- [ ] Verificare che `python -m pytest tests/` sia verde in locale

## File da toccare

- `datasets/<slug>/dataset.yml`
- `README.md`
- `Makefile`
- `.github/workflows/pipeline.yml`

## Acceptance criteria

- `datasets/<slug>/dataset.yml` esiste ed e coerente con il contratto del template
- il perimetro del progetto e leggibile nel `README`
- `python -m pytest tests/` passa
- `make check` valida tutti i dataset
