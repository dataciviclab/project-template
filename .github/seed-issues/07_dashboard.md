---
title: "[Release] Dashboard o output pubblico collegato ai MART"
labels: ["VIZ", "OPTIONAL"]
assignees: []
---
## Perche questa fase conta

E la fase in cui il lavoro diventa leggibile anche fuori dal team tecnico.
Serve a trasformare tabelle finali in un output che aiuti davvero chi legge.

## Output visibile al pubblico

Una dashboard, un report o una pagina che spiega cosa emerge dai dati.

## Obiettivo

Preparare un output pubblico che consumi i mart prodotti dal progetto.

## Checklist

- [ ] Identificare il mart sorgente e i KPI che alimentano l'output
- [ ] Documentare limiti, assunzioni e ultimo aggiornamento in `dashboard/README.md`
- [ ] Verificare coerenza fra dashboard e `docs/data_dictionary.md`
- [ ] Esplicitare cosa emerge e cosa non emerge dall'output
- [ ] Collegare l'output nel `README.md`

## Output atteso

Dashboard, report o pagina pubblica leggibile e coerente con i mart del progetto.

## Supporto operativo

- notebook consigliato: `notebooks/05_dashboard_export.ipynb`

## File da toccare

- `dashboard/README.md`
- `README.md`
- `docs/data_dictionary.md`

## Acceptance criteria

- l'output usa solo mart documentati
- KPI e limiti sono spiegati in modo leggibile
- il collegamento con il dataset rilasciato e tracciabile
- l'issue non blocca la release del dataset se l'output pubblico non e previsto
