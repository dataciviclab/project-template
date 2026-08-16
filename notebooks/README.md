# Notebook

I notebook di questo repo servono a LEGGERE gli output reali della pipeline,
non a ricostruire i path del runtime a mano.

Regola di contratto (verificata da `tests/test_contract.py`):

- i notebook usano `toolkit inspect paths --config <dataset.yml> --year <year> --json`
  come unica fonte di verità per i path di RAW/CLEAN/MART
- non ricostruiscono a mano `out/data/raw|clean|mart|_runs`
- un notebook per layer/fase di solito basta:
  `01_inspect_raw`, `02_inspect_clean`, `03_explore_mart`

Quando aggiungi un dataset, apri i notebook che ti servono con il `--config`
del dataset (multi-dataset): ogni notebook dichiara quale config usa.
