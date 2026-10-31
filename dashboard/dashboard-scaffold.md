# Dashboard Streamlit — Scaffold Standard

## Quando usare
Ogni volta che si crea una nuova dashboard Streamlit in un repo DataCivicLab.

## Template
`lab-ops/operations/dashboard-template/` contiene tutti i file copiabili.

## Checklist (obbligatoria per ogni dashboard)

1. **Deploy files** — `requirements.txt`, `.streamlit/config.toml`, `Dockerfile`
2. **sources.py** — usa `lab_connectors.formatters` (no duplicazione `fmt_*`), `@st.cache_data(ttl=3600)` su ogni funzione dati, anni derivati dal registry
3. **SQL page** — `render_sql_query()` da `lab_connectors.duckdb.sql_page`, registry path con 3 parent da `pages/`
4. **Tests** — almeno `tests/test_smoke.py` con `py_compile` su tutte le pagine
5. **No `sys.path.insert`** — il pattern `from sources import ...` funziona senza hack
6. **No URL hardcoded** — tutto passa da `lab_connectors.duckdb.queries`

## Template files

```
dashboard/
├── app.py                    # navigazione (st.Page + st.navigation)
├── sources.py                # PREFIX, SLUG, YEARS, load_mart, query (cached)
├── pages/
│   ├── 01_Panoramica.py      # KPI + overview
│   └── 05_SQL.py             # render_sql_query (sempre presente)
├── tests/
│   └── test_smoke.py         # py_compile su tutte le pagine
├── .streamlit/
│   └── config.toml           # theme dark
├── Dockerfile                # python:3.12-slim
└── requirements.txt          # streamlit, plotly, altair, pandas, lab-connectors
```

## sources.py — pattern standard

```python
from lab_connectors.duckdb.queries import load_mart_table, query_clean
from lab_connectors.formatters import fmt_eur, fmt_num, fmt_pct

PREFIX = "my-prefix/"
SLUG = "my_slug"
YEARS = [2020, 2021, 2022, 2023, 2024]

@st.cache_data(ttl=3600, show_spinner=False)
def load_mart(table: str, year: int = 2024):
    return load_mart_table(SLUG, table, year, prefix=PREFIX)

@st.cache_data(ttl=3600, show_spinner=False)
def query(sql: str, years: tuple[int, ...] = tuple(YEARS)):
    return query_clean(SLUG, sql, list(years), prefix=PREFIX)
```

## SQL page — pattern standard

```python
from pathlib import Path
from lab_connectors.duckdb.sql_page import render_sql_query
from lab_connectors.registry import load_registry

registry = load_registry(Path(__file__).parent.parent.parent / "registry" / "registry.json")
render_sql_query(registry=registry, prefix="my-prefix/", default_slug="my_slug")
```

## Gli errori più comuni (evitare)

| Errore | Fix |
|---|---|
| `requirements.txt` mancante | Copiare dal template |
| `fmt_*` definiti localmente | Usare `lab_connectors.formatters` — e re-export da `sources.py` |
| `use_container_width=True` | Deprecato → usare `width='stretch'` |
| URL GCS hardcoded in SQL | Usare `load_clean` + merge Python |
| `@st.cache_data` mancante | Wrappare ogni query |
| `sys.path.insert` in ogni pagina | Non serve — `from sources import` funziona |
| Registry path sbagliato | Da `pages/`: 3 parent. Da `dashboard/`: 2 parent |
| Anni hardcoded senza check | Se registry ha un solo dataset, usa `years_from_registry()` |
| Path parquet hardcoded in sources.py | Mai farlo — usare `load_mart_flat`/`load_mart_table` da lab_connectors |
| SQL page con read_parquet manuale | Usare `render_sql_query()` da lab_connectors — gestisce GCS + registry |
