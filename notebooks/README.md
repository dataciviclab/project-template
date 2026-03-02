# /notebooks - notebook standard per il dataset

Questa cartella contiene notebook leggeri e clonabili per tutto il lifecycle operativo del dataset.
Usano Python standard, `duckdb` e il contratto stabile `toolkit inspect paths --json` per scoprire gli output reali del progetto.

I notebook non reimplementano il motore della pipeline.
Usano `toolkit inspect paths --json` come fonte primaria per localizzare RAW, CLEAN, MART e run record, e servono a ispezionare gli output dal punto di vista del dataset.
Il comando puo essere disponibile come `toolkit ...` oppure come fallback `py -m toolkit.cli.app ...`.
Per i dettagli stabili lato toolkit, vedi `docs/notebook-contract.md` e `docs/feature-stability.md` nel repo toolkit.

Contratto minimo degli output:

- `metadata.json` = payload ricco del layer
- `manifest.json` = summary stabile del layer con puntatori a metadata e validation
- `data/_runs/.../<run_id>.json` = stato del run letto da `status` e `resume`

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
- non ricostruire a mano i path degli output del toolkit: usa sempre i path restituiti da `inspect paths --json`
- per dettagli tecnici della pipeline, vedi il repository Toolkit DataCivicLab
