---
title: "[Sources] Verificare fonte, licenza e configurazione di ingestione"
labels: ["DATA", "METODO"]
assignees: []
---
## Obiettivo

Qualificare una fonte e codificare in modo riproducibile come il toolkit deve leggerla.

Usare questa issue quando il blocco vero e ancora sulla fonte, non su CLEAN o MART.

## Checklist

- [ ] Identificare fonte primaria, URL canonico e frequenza di aggiornamento
- [ ] Aggiornare `raw.sources[].type` e `raw.sources[].args` in `datasets/<slug>/dataset.yml`
- [ ] Documentare licenza, coverage e refresh in `docs/sources.md`
- [ ] Registrare trade-off rilevanti in `docs/decisions.md`
- [ ] Verificare che non esistano path assoluti o riferimenti locali
- [ ] Rieseguire `python -m pytest tests/`

## File da toccare

- `datasets/<slug>/dataset.yml`
- `docs/sources.md`
- `docs/decisions.md`

## Acceptance criteria

- la fonte e verificabile e documentata
- `raw.sources` e compilato con campi sufficienti all'esecuzione
- `docs/sources.md` contiene note minime su licenza, refresh e limiti noti
- `python -m pytest tests/` passa
