---
title: "[MART] Costruire tabelle analitiche e regole di validazione MART"
labels: ["DATA", "METODO"]
assignees: []
---
## Perche questa fase conta

Qui il progetto inizia a produrre risposte utilizzabili.
I mart sono la parte che alimenta analisi, dashboard e insight condivisibili.

## Output visibile al pubblico

Tabelle finali leggibili, da cui ricavare indicatori e confronti.

## Obiettivo

Produrre uno o piu mart orientati a KPI e output finali, con tabella/e e validation rules esplicite.

## Checklist

- [ ] Creare o aggiornare `sql/mart/<table>.sql` per ogni tabella dichiarata
- [ ] Allineare `mart.tables` in `dataset.yml` e aggiungere eventuali regole di validazione supportate dal toolkit
- [ ] Eseguire `toolkit run mart --config dataset.yml --year <year>`
- [ ] Eseguire `toolkit validate --config dataset.yml --year <year>`
- [ ] Verificare required columns, chiavi, `not_null`, `min_rows` e KPI sanity
- [ ] Aggiornare `docs/data_dictionary.md` con granularita, KPI e semantica dei mart

## Output atteso

Mart pronti per dashboard o report, con SQL separata per tabella e regole di validazione chiare.

## Supporto operativo

- notebook consigliato: `notebooks/03_explore_mart.ipynb`
- comando minimo: `toolkit run mart --config dataset.yml`

## File da toccare

- `sql/mart/<table>.sql`
- `dataset.yml`
- `docs/data_dictionary.md`
- `docs/decisions.md`

## Acceptance criteria

- ogni tabella dichiarata in `mart.tables[]` ha un file SQL dedicato
- eventuali regole MART dichiarate in `dataset.yml` sono coerenti con le tabelle pubblicate
- rowcount sanity e duplicate check sono stati eseguiti
- il progetto puo passare a QA con mart leggibili e validabili
