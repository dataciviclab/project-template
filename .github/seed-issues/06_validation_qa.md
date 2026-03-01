---
title: "[QA] Chiudere validazioni, contract tests e smoke opzionale"
labels: ["QA", "DATA"]
assignees: []
---
## Perche questa fase conta

E il momento in cui si verifica se il progetto regge davvero.
Serve a evitare output convincenti ma fragili o poco affidabili.

## Output visibile al pubblico

Un dataset piu affidabile, con controlli espliciti e anomalie residue tracciate.

## Obiettivo

Chiudere il gate tecnico di qualita con contract tests verdi, validazioni dataset e smoke opzionale documentato.

## Checklist

- [ ] Eseguire `pytest tests/test_contract.py`
- [ ] Verificare che la CI `contract` sia verde
- [ ] Verificare che la CI `smoke` sia documentata e attivabile con `RUN_SMOKE=1`
- [ ] Rieseguire `toolkit validate --config dataset.yml --year <year>` se disponibile
- [ ] Controllare outlier, rowcount sanity, duplicates e coerenza dei KPI
- [ ] Aprire issue residue per anomalie non bloccanti

## Output atteso

Gate QA superato, con standard minimo del Lab rispettato e stato di qualita esplicito.

## File da toccare

- `tests/test_contract.py`
- `.github/workflows/ci.yml`
- `README.md`
- `docs/decisions.md`

## Acceptance criteria

- i contract tests passano
- il job `contract` in CI e sempre eseguibile senza dipendere da toolkit su PyPI
- il job `smoke` resta opzionale e documentato
- le anomalie residue sono documentate o trasformate in issue
