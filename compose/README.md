# compose

Dataset **derivati**: leggono i dataset di `datasets/` (e `support/`) per
produrre output nuovi — join tra fonti, confronti, indicatori compositi.

```
support/  →  datasets/  →  compose/
```

## Quando usarlo

- l'output nasce dall'incrocio di due o più dataset della repo
- la trasformazione non appartiene a nessuna fonte in particolare
- vuoi un mart di confronto senza duplicare la logica nei singoli dataset

Se il calcolo riguarda una sola fonte, resta in `datasets/<slug>/sql/mart_*.sql`.

## Struttura

Identica a un dataset (il contratto è lo stesso `dataset.yml`):

```
compose/<slug>/
├── dataset.yml
└── sql/
    ├── clean.sql      opzionale: normalizzazione degli input
    └── mart_*.sql     output del compose
```

In `dataset.yml` il compose dichiara le sorgenti che legge; `root: "../../out"`
punta alla stessa dir `out/` dei dataset, così ritrova i loro output.

## Esecuzione

I compose girano **dopo** i dataset, nella stessa pipeline:

```bash
make compose     # solo compose
make run-all     # support → dataset → compose (CI e post-merge)
make run-<slug>  # un singolo compose
```

`make check` valida anche i config di `compose/`; il workflow `check` li
include nel rilevamento dei dataset cambiati.
