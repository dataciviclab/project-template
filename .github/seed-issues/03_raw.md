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

- [ ] Verificare `raw.sources[]`, `primary` ed eventuale extractor in `dataset.yml`
- [ ] Eseguire `toolkit run raw --config dataset.yml`
- [ ] Usare `toolkit inspect paths --config dataset.yml --year <year> --json` per localizzare gli artifact RAW
- [ ] Controllare `manifest.json`, `metadata.json` e `raw_validation.json`
- [ ] Controllare metadata, manifest e validation report del RAW
- [ ] Confermare che `data/` non contenga output committati
- [ ] Aggiornare `docs/decisions.md` con eventuali eccezioni o failure modes

## Output atteso

RAW eseguibile con report minimi di validazione e metadata disponibili negli artifact di run.

## Supporto operativo

- notebook consigliato: `notebooks/01_inspect_raw.ipynb`
- path attesi: `root/data/raw/<dataset>/<year>/`
- comando di discovery: `toolkit inspect paths --config dataset.yml --year <year> --json`

## File da toccare

- `dataset.yml`
- `docs/decisions.md`
- `docs/sources.md`

## Acceptance criteria

- il run RAW completa o il blocco e documentato in modo riproducibile
- nessun output RAW viene aggiunto sotto `data/`
- gli artifact minimi del RAW sono attesi sotto `root/data/raw/<dataset>/<year>/`
- il progetto puo passare a CLEAN con input RAW deterministico
