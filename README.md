# [Nome dataset] - DataCivicLab

Questo progetto analizza **[fenomeno pubblico]** per rispondere a una domanda semplice:
**cosa sta succedendo, dove e con quali differenze nel tempo?**

E pensato per chi vuole orientarsi in fretta:
capire cosa mostrano i dati, dove sono solidi, quali limiti hanno e quali domande aiutano ad approfondire.

- **Stato:** [alpha | beta | stable]
- **Copertura:** [anni], [territorio]
- **Unita di analisi:** [Comune / ASL / Provincia / ...]

## 🎯 La domanda civica

**[Scrivi qui la domanda chiave in una frase chiara.]**

Esempi:

- Come varia [fenomeno] tra territori?
- Dove si osservano miglioramenti o peggioramenti?
- Il mio territorio e sopra o sotto la media?

Questa repo dovrebbe avere **una domanda civica principale**.

Dallo stesso dataset possono nascere anche altre domande utili, ma vanno tenute distinte:

- la domanda principale orienta README, notebook e output pubblici
- le domande secondarie o complementari possono emergere in Discussions e trasformarsi in issue operative

In questo modo il repository resta leggibile e non diventa un contenitore indistinto di analisi.

## 🔎 Cosa puoi capire con questi dati

- come cambia il fenomeno nel tempo
- quali territori mostrano differenze significative
- se il tuo territorio e sopra o sotto la media
- se emergono anomalie o salti improvvisi
- quali aree meritano un approfondimento mirato

Non e solo un dataset: e una base per confronto e monitoraggio.

## 📦 Output disponibili

Le tabelle finali sono pronte per dashboard, grafici e analisi.

- `mart.[tabella_1]` - confronti territoriali o temporali
- `mart.[tabella_2]` - indicatori sintetici, ranking o riepiloghi

Definizioni dettagliate di colonne e metriche:
`docs/data_dictionary.md`

## ✅ Perche fidarsi

La fiducia si costruisce su trasparenza e metodo.

- fonti ufficiali o verificabili (`docs/sources.md`)
- trasformazioni documentate (`docs/decisions.md`)
- controlli automatici prima della pubblicazione
- standard condivisi del DataCivicLab

Ogni scelta che cambia il significato dei dati viene esplicitata.

## 💬 Partecipa

Questo repository distingue chiaramente:

- **Discussions** -> domande civiche, interpretazioni, proposte di metriche
- **Issues** -> bug, problemi tecnici, miglioramenti della pipeline

Flusso consigliato:

`domanda civica -> Discussion -> Issue -> analisi / notebook / output`

Se non sei tecnico, parti da una **Discussion** in questa repo:
spiega il contesto, il territorio o l'anno che ti interessa e cosa vuoi capire.

Se la domanda richiede lavoro concreto, va trasformata in una **Issue** nella repo giusta:

- issue dataset-specifiche in questa repo
- issue di runtime o pipeline nel `toolkit`
- issue di governance o processo nelle repo di ecosistema

## 📚 Documentazione del dataset

- `docs/overview.md` - contesto, copertura, limiti
- `docs/sources.md` - fonti ufficiali
- `docs/data_dictionary.md` - colonne e metriche
- `docs/decisions.md` - scelte progettuali
- `docs/contributing.md` - come contribuire

## 🧩 Cos'e questa repo

Questo repository e il template operativo da cui nascono i repo dataset DataCivicLab.

Qui trovi il minimo necessario per far partire un progetto concreto:

- `dataset.yml` come contratto del dataset
- `sql/` per CLEAN e MART
- `docs/` per documentazione locale del dataset
- `tests/` per i contract tests minimi
- `notebooks/` per leggere gli output reali della pipeline

Un repo nato da questo template non serve solo a "ospitare dati".
Serve a rispondere in modo verificabile a una domanda civica centrale, lasciando spazio anche a domande complementari ben tracciate.

## 🛠️ Confine con il toolkit

Il motore della pipeline vive nel repository `toolkit`.
Questa repo non replica la logica di esecuzione del motore: definisce input, regole e output attesi per questo dataset.

In pratica:

- bug o feature di CLI, runner, validazioni runtime e run metadata -> repo `toolkit`
- bug o modifiche a fonti, mapping, SQL, mart, docs e notebook di dataset -> questa repo

## 🔁 Da dove partire

Se stai clonando il template per un nuovo progetto:

1. aggiorna la domanda civica e gli esempi di insight
2. sostituisci fonti, copertura e unita di analisi
3. definisci metriche e tabelle finali
4. documenta le decisioni specifiche del dataset
5. esegui `py -m pytest tests/test_contract.py`

La struttura resta invariata. Non serve capire tutto subito: qui trovi la base pratica da cui partire.

## 🧪 Esecuzione tecnica

```bash
pip install dataciviclab-toolkit
toolkit run all --config dataset.yml
toolkit validate all --config dataset.yml
toolkit status --dataset <dataset> --year <year> --latest --config dataset.yml
```

I notebook del template usano anche:

```bash
toolkit inspect paths --config dataset.yml --year <year> --json
```

Nota di contratto:

- i path relativi in `dataset.yml` sono risolti rispetto alla directory del file `dataset.yml`, non rispetto al `cwd`
- i notebook non devono ricostruire a mano `root/data/raw|clean|mart|_runs`
- `metadata.json` e il payload ricco del layer
- `manifest.json` e il summary stabile del layer
- `data/_runs/.../<run_id>.json` e il run record letto da `status`

Per dettagli piu profondi su CLI, contratti stabili, workflow advanced e feature stability, il posto giusto e `toolkit`.

## 🧭 Dove andare per il resto

Questa repo resta focalizzata sul progetto dataset.

Per il resto:

- contesto del Lab, mappa delle repo e catalogo dataset: `dataciviclab`
- policy comuni, onboarding GitHub, issue/PR template e community health: `.github`
- motore tecnico della pipeline e documentazione del runtime: `toolkit`

I riferimenti rapidi sono raccolti in `docs/lab_links.md`.

## Seed issue del template

Questo template include anche una piccola libreria di seed issue in `.github/seed-issues/`.

Non vanno aperte tutte in blocco:

- servono come base da adattare al dataset reale
- conviene usarne poche, solo quando corrispondono a un blocco o a un prossimo passo concreto
- il workflow `seed-issues.yml` crea issue solo dai file numerati `NN_nome.md`

## 🌍 Archivio pubblico

Se il progetto pubblica artifact in un archivio pubblico DataCivicLab su Drive, il flusso consigliato e:

1. eseguire e validare la pipeline in locale
2. verificare gli output sotto `root/data/...`
3. pubblicare solo gli artifact pubblici con uno script separato

Questo passaggio e `maintainer-only`.

Esempio:

```bash
py scripts/publish_to_drive.py --config dataset.yml --drive-root "G:\\DataCivicLab" --dry-run
py scripts/publish_to_drive.py --config dataset.yml --drive-root "G:\\DataCivicLab" --year 2022
```

La destinazione su Drive mantiene lo stesso path relativo degli output del toolkit sotto `root`.

## Ritmo operativo consigliato

Quando un repo dataset entra in ritmo, conviene mantenere una sequenza semplice:

1. una domanda civica principale sempre visibile nel README
2. domande complementari che emergono e si chiariscono in Discussions
3. issue piccole per trasformare le domande mature in lavoro concreto
4. output condivisibili pubblicati con continuita

L'output non deve essere sempre una dashboard completa.
Puo essere anche:

- una risposta breve con una tabella
- un notebook che chiude una domanda precisa
- un aggiornamento intermedio su limiti, dati mancanti o primi pattern

Questo aiuta a mantenere il repository vivo senza trasformarlo in un backlog confuso.
