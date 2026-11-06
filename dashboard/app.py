#!/usr/bin/env python3
"""
{{TITLE}} · Dashboard Streamlit
{{DESCRIPTION}}
"""

import streamlit as st
from lab_connectors.branding import apply_branding

st.set_page_config(
    page_title="{{TITLE}} · Dashboard",
    page_icon="{{ICON}}",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_branding(
    repo_name="{{REPO}}",
    repo_url="https://github.com/dataciviclab/{{REPO}}",
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

st.sidebar.caption("Dati: {{FONTI}}")
st.sidebar.caption(
    "Codice: [dataciviclab/{{REPO}}](https://github.com/dataciviclab/{{REPO}})"
)

pg.run()
