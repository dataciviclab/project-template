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


## Confine con il toolkit

Questo repository contiene il contratto del dataset:

* configurazione in `dataset.yml`
* trasformazioni SQL in `sql/`
* test di contratto e documentazione locale
* notebook leggeri per ispezione degli output

Il motore della pipeline vive nel repository **Toolkit DataCivicLab**.
Questa repo non replica la logica di esecuzione del toolkit: definisce input, regole e output attesi per questo dataset.

In pratica:

* bug o feature della CLI, runner, validazioni runtime e metadata di run → repo `toolkit`
* bug o modifiche a fonti, mapping, SQL, mart, docs e notebook di dataset → questa repo


## 🧭 Roadmap

La roadmap è gestita con **issue + milestone**.


## 🔁 Clonabilità

Questo repository è un modello per progetti dataset DataCivicLab.

`dataset.yml` in root è un esempio eseguibile completo, utile per smoke e onboarding.
Chi clona questo template deve adattarlo al dataset reale, non copiarlo come contratto finale immutabile.

Per adattarlo a un nuovo dataset:

1. aggiorna la domanda civica e gli esempi di insight
2. sostituisci fonti, copertura e unità di analisi
3. definisci metriche e tabelle finali
4. documenta le decisioni specifiche del dataset

La struttura resta invariata.


## 🧪 Esecuzione tecnica (per contributor)

```bash
pip install dataciviclab-toolkit
toolkit run all --config dataset.yml
toolkit validate all --config dataset.yml
```

Se lavori con un checkout locale del toolkit, installalo in editable e poi esegui i comandi da questa repo.

Per dettagli tecnici su CLI, configurazione supportata, validazioni runtime e run metadata,
vedi il repository **Toolkit DataCivicLab**.

I notebook del template usano `toolkit inspect paths --config dataset.yml --year <year> --json` per localizzare gli output reali della pipeline.
Il workflow principale del template resta centrato su `run all`, `validate all`, `status` e notebook locali; i flow avanzati del toolkit restano documentati nel repo toolkit.
Per i contratti stabili del toolkit, vedi in particolare:

* `docs/notebook-contract.md`
* `docs/feature-stability.md`
* `docs/advanced-workflows.md`


## Archivio Pubblico

Se il progetto pubblica artifact in un archivio pubblico DataCivicLab su Drive, il flusso consigliato e:

1. eseguire e validare la pipeline in locale
2. verificare gli output sotto `root/data/...`
3. pubblicare solo gli artifact pubblici con uno script separato

Il publish su Drive e una operazione `maintainer-only`, da eseguire in fase di release o merge, non nel workflow base dei contributor.

Esempio:

```bash
py scripts/publish_to_drive.py --config dataset.yml --drive-root "G:\\DataCivicLab" --dry-run
py scripts/publish_to_drive.py --config dataset.yml --drive-root "G:\\DataCivicLab" --year 2022
```

Per default lo script pubblica:

* payload RAW
* metadata, manifest e validation di `raw`, `clean`, `mart`
* parquet CLEAN
* parquet MART
* ultimo run record

La destinazione su Drive mantiene lo stesso path relativo degli output del toolkit sotto `root`.

Esempio:

* locale: `root/data/mart/<dataset>/<year>/mart_ok.parquet`
* Drive: `<drive-root>/data/mart/<dataset>/<year>/mart_ok.parquet`


## 🌍 DataCivicLab

Parte del progetto DataCivicLab.
Costruiamo infrastruttura open per analisi pubbliche riproducibili.
