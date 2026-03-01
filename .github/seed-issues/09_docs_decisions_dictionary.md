---
title: "[Docs] Aggiornare decision log e data dictionary del progetto"
labels: ["DOCS", "METODO"]
assignees: []
---
## Perche questa fase conta

Un progetto dati e utile solo se altre persone riescono a capirlo e riprenderlo.
Questa fase rende visibili scelte, significato dei campi e limiti.

## Output visibile al pubblico

Documentazione leggibile che spiega cosa significano i dati e come interpretarli.

## Obiettivo

Tenere allineata la documentazione strutturata del dataset durante tutto il lifecycle del progetto.

## Checklist

- [ ] Aggiornare `docs/decisions.md` con decisioni, eccezioni e trade-off
- [ ] Aggiornare `docs/data_dictionary.md` per RAW, CLEAN e MART
- [ ] Verificare coerenza con `docs/sources.md`
- [ ] Verificare coerenza con `docs/lab_links.md`
- [ ] Allineare esempi e naming in README e workflow dataset

## Output atteso

Decision log e data dictionary completi, utili per review, handoff e manutenzione futura.

## File da toccare

- `docs/decisions.md`
- `docs/data_dictionary.md`
- `docs/sources.md`
- `docs/lab_links.md`
- `README.md`

## Acceptance criteria

- il decision log spiega le scelte non ovvie
- il data dictionary descrive i campi essenziali di CLEAN e MART
- la documentazione e coerente con `dataset.yml` e con la SQL canonica
- il progetto puo passare review metodologica senza knowledge transfer verbale
