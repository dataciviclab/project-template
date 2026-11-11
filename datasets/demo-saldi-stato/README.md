# demo-saldi-stato

Dataset di esempio del template: mostra la struttura minima di un dataset
(`dataset.yml` + `sql/clean.sql` + `sql/mart_*.sql`), non un'analisi da
pubblicare.

Sostituiscilo con i tuoi dataset quando avvii un progetto reale.

## Struttura

```
datasets/demo-saldi-stato/
├── dataset.yml        contratto: fonte, colonne richieste, validazioni, mart
└── sql/
    ├── clean.sql      RAW → CLEAN
    └── mart_ok.sql    CLEAN → MART
```

## Comandi

```bash
make check      # preflight del config (include il probe della fonte)
make run        # RAW → CLEAN → MART
```

## Nota sulla fonte

La fonte (BDAP — Rendiconto, serie storica dei saldi) è un CSV pubblico reale:
serve a rendere l'esempio eseguibile end-to-end.

Il preflight fa un probe HTTP verso l'host della fonte, quindi `make check` e il
workflow `check` **richiedono rete**. Se l'host BDAP è momentaneamente
irraggiungibile o blocca il client (risposta vuota, timeout), il preflight
fallisce senza che il contratto del dataset sia rotto: verifica prima lo stato
del servizio, poi il config.
