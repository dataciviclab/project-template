# Seed Issues

Questa cartella contiene seed issue leggere per repo dataset basate su `project-template`.

Non vanno usate come pacchetto standard da aprire tutto insieme.
Servono come libreria di partenza da cui derivare 2-4 issue piccole, ancorate a un problema reale del progetto.

Regole pratiche:

- aprire solo issue che corrispondono a un blocco o a un prossimo passo reale
- preferire issue piccole e chiudibili in poco tempo
- evitare issue generiche tipo "fare QA completa" o "fare dashboard" se il progetto non e pronto
- adattare sempre titolo, checklist e acceptance criteria al dataset concreto

Seed consigliate come base:

- `00_kickoff.md`
- `01_sources.md`
- `02_raw.md`
- `03_clean.md`
- `04_mart.md`
- `05_release.md`
- `06_maintenance.md`

Le altre fasi del lifecycle restano importanti, ma di solito funzionano meglio:

- dentro il README o le note metodologiche
- come parte di issue piu piccole
- nel repo hub `dataciviclab` invece che nella repo tecnica del dataset
