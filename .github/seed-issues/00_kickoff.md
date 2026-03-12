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
- [ ] Compilare `dataset.yml` con `dataset.name`, `dataset.years` e `root`
- [ ] Confermare la struttura canonica `sql/clean.sql` e `sql/mart/<table>.sql`
- [ ] Verificare che i path in config siano root-relative POSIX
- [ ] Verificare che `tests/test_contract.py` sia verde in locale

## File da toccare

- `dataset.yml`
- `README.md`

## Acceptance criteria

- `dataset.yml` esiste ed e coerente con il contratto del template
- il perimetro del progetto e leggibile nel `README`
- `py -m pytest tests/test_contract.py` passa
