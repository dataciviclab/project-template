---
title: "[Maintenance] Gestire nuove annualita, cambi schema e regressioni"
labels: ["DATA", "MAINTENANCE"]
assignees: []
---
## Perche questa fase conta

I dataset non restano fermi: cambiano fonti, anni, regole e definizioni.
Questa fase serve a mantenere il progetto utile anche dopo la prima release.

## Output visibile al pubblico

Un progetto che resta aggiornabile e non si rompe al primo cambiamento di fonte.

## Obiettivo

Definire il lavoro necessario per mantenere il dataset nel tempo quando cambiano fonte, schema o regole.

## Checklist

- [ ] Aggiornare `dataset.yml` per nuove annualita o sorgenti
- [ ] Verificare impatto su `sql/clean.sql` e `sql/mart/*.sql`
- [ ] Rieseguire contract tests
- [ ] Rieseguire smoke opzionale in caso di cambio sostanziale
- [ ] Aggiornare `docs/sources.md`, `docs/data_dictionary.md` e `docs/decisions.md`
- [ ] Documentare regressioni o incompatibilita

## Output atteso

Piano di manutenzione chiaro e procedimento ripetibile per evolvere il dataset senza rompere il contratto del template.

## File da toccare

- `dataset.yml`
- `sql/clean.sql`
- `sql/mart/project_summary.sql`
- `docs/sources.md`
- `docs/data_dictionary.md`
- `docs/decisions.md`

## Acceptance criteria

- i cambi sono tracciati nei documenti corretti
- i contract tests restano verdi
- la manutenzione non introduce path assoluti o output committati in `data/`
- il progetto puo essere rieseguito per un nuovo anno o schema senza lavoro manuale implicito
