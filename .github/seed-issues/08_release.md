---
title: "[Release] Preparare release del dataset, README e artifacts minimi"
labels: ["DOCS", "LEAD"]
assignees: []
---
## Perche questa fase conta

Questa fase rende il progetto condivisibile anche con chi arriva da fuori.
Una buona release rende chiaro cosa esiste, cosa si puo usare e con quali limiti.

## Output visibile al pubblico

Una homepage chiara, una overview leggibile e una release spiegata bene.

## Obiettivo

Portare il progetto a una release riproducibile, spiegabile e pronta per handoff.

## Checklist

- [ ] Aggiornare `README.md` con scopo, metodo, output e limiti
- [ ] Verificare `docs/lab_links.md` per release policy, DoD e riferimenti Lab-wide
- [ ] Confermare che `output.artifacts` resti su `minimal` o motivare eccezioni
- [ ] Collegare eventuale dashboard o report ai mart corretti
- [ ] Verificare che documentazione e artifact minimi siano coerenti
- [ ] Preparare PR o release notes interne

## Public-facing readiness

- [ ] README pubblico-first ok
- [ ] `docs/overview.md` presente
- [ ] almeno 3 domande o insight presenti nel README
- [ ] `docs/data_dictionary.md` aggiornato almeno al minimo

## Civic clarity check

- [ ] Le domande guida sono ancora rilevanti?
- [ ] Le metriche rispondono davvero alle domande?
- [ ] Ci sono insight scritti in linguaggio semplice?

## Output atteso

Release interna o pubblica con documentazione finale coerente con i dati e con i mart prodotti.

## Supporto operativo

- notebook consigliato: `notebooks/00_quickstart.ipynb`
- comandi minimi: `py -m pytest tests/test_contract.py` e `toolkit validate all --config dataset.yml`

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
