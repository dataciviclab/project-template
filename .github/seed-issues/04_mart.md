---
title: "[MART] Costruire tabelle finali e validation rules essenziali"
labels: ["DATA", "METODO"]
assignees: []
---
## Obiettivo

Produrre uno o piu mart orientati a KPI e output finali, con tabella/e e validation rules esplicite.

Usare questa issue quando CLEAN regge gia e il prossimo blocco e arrivare a un output leggibile.

## Checklist

- [ ] Creare o aggiornare `datasets/<slug>/sql/mart_<table>.sql` per ogni tabella dichiarata
- [ ] Allineare `mart.tables` in `datasets/<slug>/dataset.yml` e aggiungere eventuali regole di validazione supportate dal toolkit
- [ ] Eseguire `toolkit run mart --config datasets/<slug>/dataset.yml --year <year>`
- [ ] Eseguire `toolkit validate --config datasets/<slug>/dataset.yml --year <year>`
- [ ] Usare `toolkit inspect paths --config datasets/<slug>/dataset.yml --year <year> --json` per localizzare i mart
- [ ] Verificare required columns, chiavi, `not_null`, `min_rows` e KPI sanity
- [ ] Aggiornare `docs/data_dictionary.md` con granularita, KPI e semantica dei mart

## File da toccare

- `datasets/<slug>/sql/mart_<table>.sql`
- `datasets/<slug>/dataset.yml`
- `docs/data_dictionary.md`
- `docs/decisions.md`

## Acceptance criteria

- ogni tabella dichiarata in `mart.tables[]` ha un file SQL dedicato
- eventuali regole MART dichiarate in `dataset.yml` sono coerenti con le tabelle pubblicate
- rowcount sanity e duplicate check sono stati eseguiti
- il progetto produce almeno un mart leggibile e validabile
