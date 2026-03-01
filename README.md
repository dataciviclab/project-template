# 📊 [Nome dataset] — DataCivicLab

Questo progetto analizza **[fenomeno pubblico]** per rispondere a una domanda semplice:
**cosa sta succedendo, dove e con quali differenze nel tempo?**

È pensato per chi vuole orientarsi in fretta:
capire cosa mostrano i dati, dove sono solidi, quali limiti hanno e quali domande aiutano ad approfondire.

* **Stato:** [alpha | beta | stable]
* **Copertura:** [anni], [territorio]
* **Unità di analisi:** [Comune / ASL / Provincia / …]

## 🎯 La domanda civica

**[Scrivi qui la domanda chiave in una frase chiara.]**

Esempio:

* Come varia [fenomeno] tra territori?
* Dove si osservano miglioramenti o peggioramenti?
* Il mio territorio è sopra o sotto la media?

## 🔎 Cosa puoi capire con questi dati

* come cambia il fenomeno nel tempo
* quali territori mostrano differenze significative
* se il tuo territorio è sopra o sotto la media
* se emergono anomalie o salti improvvisi
* quali aree meritano un approfondimento mirato

Non è solo un dataset: è una base per confronto e monitoraggio.

## 📦 Output disponibili

Le tabelle finali sono pronte per dashboard, grafici e analisi.

* `mart.[tabella_1]` — confronti territoriali o temporali
* `mart.[tabella_2]` — indicatori sintetici, ranking o riepiloghi

Definizioni dettagliate di colonne e metriche:
👉 `docs/data_dictionary.md`


## ✅ Perché fidarsi

La fiducia si costruisce su trasparenza e metodo.

* fonti ufficiali o verificabili (`docs/sources.md`)
* trasformazioni documentate (`docs/decisions.md`)
* controlli automatici prima della pubblicazione
* standard condivisi del DataCivicLab

Ogni scelta che cambia il significato dei dati viene esplicitata.


## 💬 Partecipa

Questo repository distingue chiaramente:

* **Discussions** → domande civiche, interpretazioni, proposte di metriche
* **Issues** → bug, problemi tecnici, miglioramenti della pipeline

Se non sei tecnico, parti da una **Discussion**:
spiega il contesto, il territorio o l’anno che ti interessa e cosa vuoi capire.


## 📚 Documentazione del dataset

* `docs/overview.md` — contesto, copertura, limiti
* `docs/sources.md` — fonti ufficiali
* `docs/data_dictionary.md` — colonne e metriche
* `docs/decisions.md` — scelte progettuali
* `docs/contributing.md` — come contribuire


## 🧭 Roadmap

La roadmap è gestita con **issue + milestone**.


## 🔁 Clonabilità

Questo repository è un modello per progetti dataset DataCivicLab.

Per adattarlo a un nuovo dataset:

1. aggiorna la domanda civica e gli esempi di insight
2. sostituisci fonti, copertura e unità di analisi
3. definisci metriche e tabelle finali
4. documenta le decisioni specifiche del dataset

La struttura resta invariata.


## 🧪 Esecuzione tecnica (per contributor)

```bash
pip install dataciviclab-toolkit
toolkit run --dataset dataset.yml
```

Per dettagli tecnici (CLI, configurazione, validazioni, run metadata)
vedi il repository **Toolkit DataCivicLab**.


## 🌍 DataCivicLab

Parte del progetto DataCivicLab.
Costruiamo infrastruttura open per analisi pubbliche riproducibili.
