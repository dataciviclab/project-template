# Workflow

Come contribuire in modo semplice a un progetto dataset DataCivicLab.

## Percorsi

- feedback o idee: usa le Discussions della repo se vuoi lasciare una traccia ragionata
- avanzamento operativo: usa issue, project board o milestone della repo
- insight o visual: parti da `sql/` o `dashboard/` se il progetto li prevede

## Dove andare

- setup e contributo rapido: [docs/contributing.md](docs/contributing.md)
- contesto DataCivicLab, policy comuni e motore tecnico: [docs/lab_links.md](docs/lab_links.md)
- indice docs locali: [docs/README.md](docs/README.md)

## Confine tecnico

- questa repo contiene config dataset, SQL, docs, test di contratto e notebook
- il motore di esecuzione della pipeline sta nel repo toolkit
- se il problema riguarda run, CLI o comportamento interno del motore, aprilo nel toolkit
- se il problema riguarda fonti, mapping, mart o documentazione del dataset, aprilo qui

## Flusso minimo

1. apri una domanda, un feedback o una correzione
2. scegli una issue o aprine una nuova
3. lavora su branch dedicato
4. apri una PR piccola e leggibile

GitHub resta il posto dove deve restare la traccia utile.

## Flusso tecnico minimo

1. valida la config con `py -m pytest tests/test_contract.py`
2. esegui `toolkit run all --config dataset.yml`
3. esegui `toolkit validate all --config dataset.yml`
4. usa i notebook per ispezionare RAW, CLEAN, MART e QA

## Maintainers

1. revisiona PR e stato del dataset
2. verifica `status` e output finali
3. se il progetto ha un archivio pubblico, pubblica gli artifact con `py scripts/publish_to_drive.py`
