# /notebooks - notebook standard per il dataset

Questa cartella contiene notebook leggeri e clonabili per tutto il lifecycle operativo del dataset.
Usano solo Python standard, `duckdb`, path relativi e il file `../dataset.yml` come riferimento di progetto.

I notebook non reimplementano il motore della pipeline.
Assumono che il toolkit produca output leggibili e servono a ispezionare RAW, CLEAN o MART dal punto di vista del dataset.

## Notebook inclusi

- `00_quickstart.ipynb` - setup, command preview, run opzionale e localizzazione output reali del toolkit
- `01_inspect_raw.ipynb` - ispezione del layer RAW tramite `manifest.json`, file primario e sample di output
- `02_inspect_clean.ipynb` - ispezione del parquet CLEAN con schema e sanity checks minimi
- `03_explore_mart.ipynb` - esplorazione del mart selezionato nella config
- `04_quality_checks.ipynb` - controlli ripetibili su chiavi, missingness e range del mart selezionato
- `05_dashboard_export.ipynb` - export opzionali derivati dal mart selezionato nella config

## Regole

- non salvare output pesanti nel repo
- se serve esportare file, usa `../_tmp/`
- mantieni i notebook generici: preferisci leggere `dataset.yml` e usa i parametri iniziali per scegliere anno/tabella
- per dettagli tecnici della pipeline, vedi il repository Toolkit DataCivicLab
