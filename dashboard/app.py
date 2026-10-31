#!/usr/bin/env python3
"""
{{TITLE}} · Dashboard Streamlit
{{DESCRIPTION}}
"""

import streamlit as st

st.set_page_config(
    page_title="{{TITLE}} · Dashboard",
    page_icon="{{ICON}}",
    layout="wide",
    initial_sidebar_state="expanded",
)

pages = {
    "": [
        st.Page("pages/01_Panoramica.py", title="Panoramica", icon="📊", default=True),
    ],
    "Analisi": [
        st.Page("pages/02_Analisi.py", title="Analisi", icon="📈"),
    ],
    "Strumenti": [
        st.Page("pages/05_SQL.py", title="Query SQL", icon="🧪"),
    ],
}

pg = st.navigation(pages, position="sidebar")

st.sidebar.markdown("---")
st.sidebar.caption("Dati: {{FONTI}}")
st.sidebar.caption(
    "Codice: [dataciviclab/{{REPO}}](https://github.com/dataciviclab/{{REPO}})"
)
st.sidebar.caption("[DataCivicLab](https://dataciviclab.org/) · CC BY 4.0")

pg.run()
