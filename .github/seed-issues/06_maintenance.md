---
title: "[Maintenance] Gestire nuove annualita, drift schema e regressioni"
labels: ["DATA", "MAINTENANCE"]
assignees: []
---
## Obiettivo

Definire il lavoro necessario per mantenere il dataset nel tempo quando cambiano fonte, schema o regole.

Usare questa issue quando il progetto esiste gia e arriva un cambio reale di anno, fonte o schema.

## Checklist

- [ ] Aggiornare `datasets/<slug>/dataset.yml` per nuove annualita o sorgenti
- [ ] Verificare impatto su `datasets/<slug>/sql/clean.sql` e `datasets/<slug>/sql/mart_*.sql`
- [ ] Rieseguire contract tests (`python -m pytest tests/`)
- [ ] Rieseguire `make check` per validare tutti i dataset
- [ ] Aggiornare `docs/sources.md`, `docs/data_dictionary.md` e `docs/decisions.md`
- [ ] Documentare regressioni o incompatibilita

## File da toccare

- `datasets/<slug>/dataset.yml`
- `datasets/<slug>/sql/clean.sql`
- `datasets/<slug>/sql/mart_*.sql`
- `docs/sources.md`
- `docs/data_dictionary.md`
- `docs/decisions.md`

## Acceptance criteria

- i cambi sono tracciati nei documenti corretti
- i contract tests restano verdi
- la manutenzione non introduce path assoluti o output committati in `out/`
- il progetto puo essere rieseguito per un nuovo anno o schema senza lavoro manuale implicito
