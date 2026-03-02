---
title: "[Sources] Onboarding fonti, licenza, refresh e decisioni di ingestione"
labels: ["DATA", "METODO"]
assignees: []
---
## Perche questa fase conta

Se la fonte non e chiara, tutto il resto del progetto diventa fragile.
Questa fase serve a capire da dove arrivano i dati e con quali limiti.

## Output visibile al pubblico

Una scheda semplice delle fonti usate, con link e note di contesto.

## Obiettivo

Qualificare la fonte e codificare in modo riproducibile come il toolkit deve leggerla.

## Checklist

- [ ] Identificare fonte primaria, URL canonico e frequenza di aggiornamento
- [ ] Aggiornare `raw.sources[].type` e `raw.sources[].args` in `dataset.yml`
- [ ] Documentare licenza, coverage, refresh cadence e note in `docs/sources.md`
- [ ] Registrare trade-off e assunzioni di ingestione in `docs/decisions.md`
- [ ] Verificare che non esistano path assoluti o riferimenti locali
- [ ] Rieseguire i contract tests

## Output atteso

Fonte verificata e configurata in `dataset.yml`, con documentazione sufficiente per procedere al layer RAW.

## Supporto operativo

- notebook consigliato: `notebooks/01_inspect_raw.ipynb`
- comando minimo: `toolkit run raw --config dataset.yml`

## File da toccare

- `dataset.yml`
- `docs/sources.md`
- `docs/decisions.md`

## Acceptance criteria

- la fonte e verificabile e documentata
- `raw.sources` e compilato con campi sufficienti all'esecuzione
- `docs/sources.md` contiene note su licenza, refresh e limiti noti
- `pytest tests/test_contract.py` passa
