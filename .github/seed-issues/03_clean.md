---
title: "[CLEAN] Normalizzare input e chiudere il contratto CLEAN minimo"
labels: ["DATA"]
assignees: []
---
## Obiettivo

Portare il dataset da RAW a CLEAN con SQL esplicita, schema documentato e validazioni minime.

Usare questa issue quando il problema vero e sulla lettura, normalizzazione o stabilita dello schema.

## Checklist

- [ ] Implementare o aggiornare `sql/clean.sql`
- [ ] Allineare `clean.read`, `clean.required_columns` e `clean.validate` in `dataset.yml`
- [ ] Verificare chiavi logiche, `not_null`, `min_rows` e duplicati
- [ ] Eseguire `toolkit run clean --config dataset.yml`
- [ ] Eseguire `toolkit validate clean --config dataset.yml`
- [ ] Usare `toolkit inspect paths --config dataset.yml --year <year> --json` per localizzare il layer CLEAN
- [ ] Aggiornare `docs/data_dictionary.md` per il layer CLEAN
- [ ] Loggare mapping o assunzioni non ovvie in `docs/decisions.md`

## File da toccare

- `sql/clean.sql`
- `dataset.yml`
- `docs/data_dictionary.md`
- `docs/decisions.md`

## Acceptance criteria

- `sql/clean.sql` legge da `raw_input`
- `clean.required_columns` e aggiornato
- `clean.validate` copre almeno chiavi, `not_null` e `min_rows` quando applicabile
- rowcount sanity e duplicate check sono stati eseguiti
- il progetto puo passare a MART senza ambiguita sullo schema CLEAN
