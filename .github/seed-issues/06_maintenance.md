---
title: "[Maintenance] Gestire nuove annualita, drift schema e regressioni"
labels: ["DATA", "MAINTENANCE"]
assignees: []
---
## Obiettivo

Definire il lavoro necessario per mantenere il dataset nel tempo quando cambiano fonte, schema o regole.

Usare questa issue quando il progetto esiste gia e arriva un cambio reale di anno, fonte o schema.

## Checklist

- [ ] Aggiornare `dataset.yml` per nuove annualita o sorgenti
- [ ] Verificare impatto su `sql/clean.sql` e `sql/mart/*.sql`
- [ ] Rieseguire contract tests
- [ ] Rieseguire smoke opzionale in caso di cambio sostanziale
- [ ] Aggiornare `docs/sources.md`, `docs/data_dictionary.md` e `docs/decisions.md`
- [ ] Documentare regressioni o incompatibilita

## File da toccare

- `dataset.yml`
- `sql/clean.sql`
- `sql/mart/<table>.sql`
- `docs/sources.md`
- `docs/data_dictionary.md`
- `docs/decisions.md`

## Acceptance criteria

- i cambi sono tracciati nei documenti corretti
- i contract tests restano verdi
- la manutenzione non introduce path assoluti o output committati in `data/`
- il progetto puo essere rieseguito per un nuovo anno o schema senza lavoro manuale implicito
