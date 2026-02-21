---
title: "M1-04 — RAW → CLEAN (standard colonne, parsing, validazioni base)"
labels: ["pipeline", "clean", "m1"]
assignees: []
---
## 🎯 Obiettivo
Produrre CLEAN coerente multi-anno e pronto per analisi.

## ✅ Task
- [ ] Standardizzare nomi colonne (snake_case) + dizionario
- [ ] Parsing numeri IT (., , , %, -, null)
- [ ] Tipi coerenti (string/int/float/date) e regole di casting
- [ ] Gestire valori speciali (n.d., 0, vuoti) con policy esplicita
- [ ] Validazioni base: righe attese, colonne obbligatorie, duplicati chiave

## 📦 Output atteso
File CLEAN (parquet/csv) + mini data dictionary.