---
title: "[CLEAN] Implementare normalizzazione, required columns e validazioni CLEAN"
labels: ["DATA"]
assignees: []
---
## Perche questa fase conta

Qui il dato diventa davvero leggibile e confrontabile.
Una buona fase CLEAN riduce errori, ambiguita e lavoro manuale futuro.

## Output visibile al pubblico

Un dataset piu chiaro, con colonne coerenti e significato documentato.

## Obiettivo

Portare il dataset da RAW a CLEAN con SQL esplicita, schema documentato e validazioni minime.

## Checklist

- [ ] Implementare o aggiornare `sql/clean.sql`
- [ ] Allineare `clean.read`, `clean.required_columns` e `clean.validate` in `dataset.yml`
- [ ] Verificare chiavi logiche, `not_null`, `min_rows` e duplicati
- [ ] Eseguire `toolkit run clean --config dataset.yml`
- [ ] Eseguire `toolkit validate clean --config dataset.yml`
- [ ] Aggiornare `docs/data_dictionary.md` per il layer CLEAN
- [ ] Loggare assunzioni e mapping in `docs/decisions.md`

## Output atteso

Layer CLEAN riproducibile, con schema e regole di validazione sufficienti per alimentare i mart.

## Supporto operativo

- notebook consigliato: `notebooks/02_inspect_clean.ipynb`
- path attesi: `root/data/clean/<dataset>/<year>/`

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
