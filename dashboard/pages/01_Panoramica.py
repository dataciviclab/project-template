"""Panoramica — Visione d'insieme."""

import streamlit as st
from lab_connectors.formatters import fmt_num
from sources import query, YEARS

st.title("📊 {{TITLE}}")

# ── KPI ─────────────────────────────────────────────────────────────
year = st.selectbox("Anno", YEARS, index=len(YEARS) - 1)

df = query("SELECT COUNT(*) AS n FROM clean_input", years=(year,))

if df.empty:
    st.warning("Nessun dato disponibile.")
    st.stop()

k1, k2, k3, k4 = st.columns(4)
k1.metric("Righe", fmt_num(df["n"].iloc[0]))

st.caption("Dati: {{FONTI}} · CC BY 4.0")
