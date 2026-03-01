---
title: "[Kickoff] Definire domanda civica, perimetro e contratto iniziale del dataset"
labels: ["LEAD", "METODO"]
assignees: []
---
## Perche questa fase conta

Qui si decide se il progetto ha una domanda utile, comprensibile e davvero sostenibile nel tempo.
Un kickoff fatto bene evita di costruire dati che poi non rispondono alla domanda iniziale.

## Output visibile al pubblico

Una spiegazione chiara di cosa vuole capire il progetto e di quali dati usera.

## Obiettivo

Avviare il progetto dataset con perimetro chiaro, domanda civica misurabile e contratto toolkit-first coerente con il template.

## Checklist

- [ ] Definire una sola domanda civica, chiara e misurabile
- [ ] Compilare `dataset.yml` con `dataset.name`, `dataset.years` e `root`
- [ ] Verificare che i path in config siano root-relative POSIX
- [ ] Confermare la struttura canonica `sql/clean.sql` e `sql/mart/<table>.sql`
- [ ] Allineare ruoli e ownership con `docs/lab_links.md`
- [ ] Verificare che `tests/test_contract.py` sia verde in locale

## Output atteso

Progetto inizializzato con contratto di base valido e documentazione minima pronta per il source onboarding.

## File da toccare

- `dataset.yml`
- `README.md`
- `docs/lab_links.md`

## Acceptance criteria

- `dataset.yml` esiste in root ed e coerente con il contratto smoke reale
- il perimetro del progetto e documentato in modo comprensibile
- `pytest tests/test_contract.py` passa
- il progetto puo passare alla fase Source onboarding senza ambiguita su nome dataset, anni e scope
