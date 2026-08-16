---
title: "[RAW] Rendere l'ingestione riproducibile e tracciabile"
labels: ["DATA"]
assignees: []
---
## Obiettivo

Ottenere un layer RAW eseguibile e ripetibile, senza committare output in repo.

Usare questa issue quando la fonte e gia stata scelta ma il run RAW non e ancora affidabile.

## Checklist

- [ ] Verificare `raw.sources[]`, `primary` ed eventuale extractor in `datasets/<slug>/dataset.yml`
- [ ] Eseguire `toolkit run raw --config datasets/<slug>/dataset.yml`
- [ ] Usare `toolkit inspect paths --config datasets/<slug>/dataset.yml --year <year> --json` per localizzare gli artifact RAW
- [ ] Controllare `manifest.json`, `metadata.json` e `raw_validation.json`
- [ ] Confermare che `out/` non contenga output committati
- [ ] Documentare eventuali eccezioni o failure modes in `docs/decisions.md`

## File da toccare

- `datasets/<slug>/dataset.yml`
- `docs/decisions.md`
- `docs/sources.md`

## Acceptance criteria

- il run RAW completa o il blocco e documentato in modo riproducibile
- nessun output RAW viene aggiunto sotto `out/`
- gli artifact minimi del RAW sono attesi sotto `out/data/raw/<dataset>/<year>/`
- l'input per CLEAN e deterministico
