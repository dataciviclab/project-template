#!/usr/bin/env bash
# scaffold-dashboard.sh — Genera la struttura dashboard Streamlit per un repo DataCivicLab.
#
# Usage:
#   bash scaffold-dashboard.sh <repo-path> <prefix> <slug> <title> <year_start> <year_end>
#
# Example:
#   bash scaffold-dashboard.sh /path/to/my-repo my-prefix my_slug "My Dashboard" 2020 2026
set -euo pipefail

REPO="${1:?Usage: scaffold-dashboard.sh <repo-path> <prefix> <slug> <title> <year_start> <year_end>}"
PREFIX="${2:?Missing prefix}"
SLUG="${3:?Missing slug}"
TITLE="${4:?Missing title}"
YEAR_START="${5:?Missing year_start}"
YEAR_END="${6:?Missing year_end}"

TEMPLATE_DIR="$(cd "$(dirname "$0")" && pwd)"
DASH_DIR="${REPO}/dashboard"

echo "📁 Creating dashboard in ${DASH_DIR}..."

# Create directory structure
mkdir -p "${DASH_DIR}"/{pages,tests,.streamlit}

# Copy deploy files (verbatim)
cp "${TEMPLATE_DIR}/.streamlit/config.toml" "${DASH_DIR}/.streamlit/config.toml"
cp "${TEMPLATE_DIR}/Dockerfile" "${DASH_DIR}/Dockerfile"
cp "${TEMPLATE_DIR}/requirements.txt" "${DASH_DIR}/requirements.txt"
cp "${TEMPLATE_DIR}/tests/test_smoke.py" "${DASH_DIR}/tests/test_smoke.py"

# Generate app.py
sed -e "s|{{TITLE}}|${TITLE}|g" \
    -e "s|{{DESCRIPTION}}|Dashboard per ${TITLE}|g" \
    -e "s|{{ICON}}|📊|g" \
    -e "s|{{FONTI}}|Fonte dati|g" \
    -e "s|{{REPO}}|$(basename "${REPO}")|g" \
    "${TEMPLATE_DIR}/app.py" > "${DASH_DIR}/app.py"

# Generate sources.py
sed -e "s|{{PREFIX}}|${PREFIX}|g" \
    -e "s|{{SLUG}}|${SLUG}|g" \
    -e "s|{{YEAR_START}}|${YEAR_START}|g" \
    -e "s|{{YEAR_END}}|${YEAR_END}|g" \
    "${TEMPLATE_DIR}/sources.py" > "${DASH_DIR}/sources.py"

# Copy page templates
cp "${TEMPLATE_DIR}/pages/01_Panoramica.py" "${DASH_DIR}/pages/01_Panoramica.py"
cp "${TEMPLATE_DIR}/pages/05_SQL.py" "${DASH_DIR}/pages/05_SQL.py"

# Generate pages with substitutions
for f in "${DASH_DIR}/pages/"*.py; do
    sed -i -e "s|{{TITLE}}|${TITLE}|g" \
           -e "s|{{PREFIX}}|${PREFIX}|g" \
           -e "s|{{SLUG}}|${SLUG}|g" \
           -e "s|{{YEAR_END}}|${YEAR_END}|g" \
           -e "s|{{FONTI}}|Fonte dati|g" \
           "$f"
done

echo "✅ Dashboard scaffolded in ${DASH_DIR}"
echo ""
echo "Files created:"
find "${DASH_DIR}" -type f | sort | sed "s|${REPO}/||"
echo ""
echo "Next steps:"
echo "  1. Edit pages/ to add your visualizations"
echo "  2. Update app.py navigation to match your pages"
echo "  3. Add @st.cache_data to data loading functions in sources.py"
