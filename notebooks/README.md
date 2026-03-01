# /notebooks - notebook standard per il dataset

Questa cartella contiene notebook leggeri e clonabili per avvio rapido, esplorazione dei mart e controlli di qualita.
Usano solo Python standard, `duckdb`, path relativi e il file `../dataset.yml` come riferimento di progetto.

## Notebook inclusi

- `00_quickstart.ipynb` - esegue la pipeline e controlla che esistano tabelle mart leggibili
- `01_explore_mart.ipynb` - esplorazione public-first dei dati finali
- `02_quality_checks.ipynb` - controlli ripetibili su duplicati, missingness e range
- `03_dashboard_export.ipynb` - export opzionali in `../_tmp/`, disattivati di default

## Regole

- non salvare output pesanti nel repo
- se serve esportare file, usa `../_tmp/`
- mantieni i notebook generici: aggiorna nomi tabella e chiavi senza introdurre logica dataset-specifica
- per dettagli tecnici della pipeline, vedi il repository Toolkit DataCivicLab
