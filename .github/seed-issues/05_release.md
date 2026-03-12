---
title: "[Release] Preparare README, output minimo e handoff"
labels: ["DOCS", "LEAD"]
assignees: []
---
## Obiettivo

Portare il progetto a una release riproducibile, spiegabile e pronta per handoff.

Usare questa issue solo quando il progetto ha gia un output reale da presentare.

## Checklist

- [ ] Aggiornare `README.md` con scopo, metodo, output e limiti
- [ ] Verificare `docs/lab_links.md` per hub DataCivicLab, policy comuni e riferimenti al toolkit
- [ ] Confermare che `output.artifacts` resti su `minimal` o motivare eccezioni
- [ ] Collegare eventuale dashboard o report ai mart corretti
- [ ] Verificare che documentazione e artifact minimi siano coerenti
- [ ] Preparare PR o release notes interne

## File da toccare

- `README.md`
- `docs/overview.md`
- `docs/lab_links.md`
- `docs/data_dictionary.md`

## Acceptance criteria

- README e docs descrivono chiaramente cosa e stato rilasciato
- il progetto e riprendibile da terzi senza conoscenza implicita
- gli artifact minimi attesi sono coerenti con la policy del template
- i gate precedenti sono chiusi o le eccezioni sono documentate
