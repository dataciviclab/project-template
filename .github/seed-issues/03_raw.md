---
title: "[RAW] Rendere riproducibile l'ingestione RAW con il toolkit"
labels: ["DATA"]
assignees: []
---
## Perche questa fase conta

Questa e la base del progetto: se il dato in ingresso non e stabile o tracciabile, anche le analisi finali diventano deboli.

## Output visibile al pubblico

Una fonte acquisita in modo ripetibile, con traccia di cosa e stato usato e quando.

## Obiettivo

Ottenere un layer RAW eseguibile e ripetibile, senza committare output in repo.

## Checklist

- [ ] Verificare `raw.source` e eventuale extractor in `dataset.yml`
- [ ] Eseguire `toolkit run raw --config dataset.yml --year <year>`
- [ ] Eseguire `toolkit validate --config dataset.yml --year <year>` oppure documentare il blocco
- [ ] Controllare metadata, manifest e validation report del RAW
- [ ] Confermare che `data/` non contenga output committati
- [ ] Aggiornare `docs/decisions.md` con eventuali eccezioni o failure modes

## Output atteso

RAW eseguibile con report minimi di validazione e metadata disponibili negli artifact di run.

## File da toccare

- `dataset.yml`
- `docs/decisions.md`
- `docs/sources.md`

## Acceptance criteria

- il run RAW completa o il blocco e documentato in modo riproducibile
- nessun output RAW viene aggiunto sotto `data/`
- gli artifact minimi del RAW sono attesi sotto `_runs/`
- il progetto puo passare a CLEAN con input RAW deterministico
