# 📊 Project Template – DataCivicLab

Questo repository è il **template ufficiale** per tutti i progetti del **DataCivicLab**.

Serve come base comune per:
- strutturare correttamente un progetto
- lavorare in modo collaborativo e replicabile
- mantenere coerenza metodologica tra progetti diversi

👉 Ogni nuovo progetto del Lab nasce **copiando questo repository** e compilando i placeholder.

---

## 🎯 Domanda civica del progetto
**Domanda (1 frase):** _[Scrivi qui la domanda civica, chiara e misurabile]_

**Perché è rilevante (2–4 righe):** _[Impatto civico, decisioni pubbliche, perché ora]_

---

## 🧭 Metodo DataCivicLab (flusso standard)

```text
Domanda civica
   ↓
Ricerca dataset
   ↓
Raw → Clean → Mart
   ↓
Analisi & KPI
   ↓
Dashboard / Output
   ↓
Documentazione civica
```

---

## 📦 Dati: Drive come storage (regola d’oro)

⚠️ **I dati non vengono versionati su GitHub.**

```text
GitHub = codice, metodo, documentazione
Drive  = dati (raw, clean, mart)
```

**Cartella Drive del progetto:** _[link Drive]_

---

## 📁 Struttura del repository

```text
project/
├─ README.md               → orientamento rapido
├─ WORKFLOW.md             → come si lavora (Discussion → Issue → PR)
├─ data/                   → documentazione sui dati (no file)
│  ├─ raw/                 → fonti + link Drive
│  ├─ clean/               → schema + regole pulizia
│  └─ mart/                → schema finale + KPI base
├─ notebooks/              → pipeline (raw→clean→mart)
├─ dashboards/             → link e descrizione dashboard
├─ queries/                → query SQL riusabili (opzionale)
└─ docs/                   → note civiche, checklist e DoD
```

---

## Ruoli
- Project Lead:
- Data:
- Metodo:
- Viz:
- QA:
- Docs:

---

## ✅ Output attesi (pubblici)

- **Dashboard**: _[link + breve descrizione KPI]_
- **Docs civiche**: _[cosa deve capire un non tecnico]_

---

## 🔁 Come si contribuisce (super breve)

1. **Discussion** per idee / contesto
2. **Issue** per task concreti
3. **Branch** per lavorare
4. **Pull Request** per revisione e merge

Dettagli in `WORKFLOW.md`.

---

🧠 DataCivicLab – dati, metodo e comunità per capire (e migliorare) il Paese.
