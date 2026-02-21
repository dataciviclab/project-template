---
title: "M1-03 — RAW ingestion (download, snapshot, metadata)"
labels: ["pipeline", "raw", "m1"]
assignees: []
---
## 🎯 Obiettivo
Acquisire RAW in modo ripetibile e tracciabile.

## ✅ Task
- [ ] Definire path RAW standard (Drive/FS) + naming files
- [ ] Script/notebook per download o import (no trasformazioni)
- [ ] Salvare metadata: url, timestamp, checksum/size, note versione
- [ ] Gestire encoding e separatore (senza “pulire” i dati)
- [ ] Log minimo (righe, colonne, errori)

## 📦 Output atteso
RAW disponibile + manifest/metadata (anche solo JSON/MD).