"""Fonti dati per la dashboard {{TITLE}}.

Wrappa lab_connectors.duckdb.queries con @st.cache_data.
"""

from __future__ import annotations

from pathlib import Path

import streamlit as st

from lab_connectors.duckdb.queries import (
    detect_local_root,
    load_mart_table as _load_mart_table,
    query_clean as _query_clean,
)

ROOT = Path(__file__).parent.parent
PREFIX = "{{PREFIX}}/"
SLUG = "{{SLUG}}"
YEARS = list(range({{YEAR_START}}, {{YEAR_END}} + 1))
LOCAL_ROOT = detect_local_root(repo_root=ROOT)


@st.cache_data(ttl=3600, show_spinner=False)
def load_mart(table: str, year: int = {{YEAR_END}}):
    """Carica un singolo mart table da GCS (cached 1h)."""
    return _load_mart_table(SLUG, table, year, prefix=PREFIX, local_root=LOCAL_ROOT)


@st.cache_data(ttl=3600, show_spinner=False)
def query(sql: str, years: tuple[int, ...] = tuple(YEARS)):
    """Esegue SQL sul clean layer (cached 1h)."""
    return _query_clean(SLUG, sql, list(years), prefix=PREFIX, local_root=LOCAL_ROOT)
