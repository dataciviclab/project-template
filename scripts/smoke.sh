#!/usr/bin/env sh

set -eu

DATASET_FILE="${DATASET_FILE:-dataset.yml}"
TOOLKIT_BIN="${TOOLKIT_BIN:-toolkit}"
DCL_ROOT="${DCL_ROOT:-$(pwd)}"

export DCL_ROOT

detect_python() {
  if command -v python >/dev/null 2>&1; then
    echo python
    return 0
  fi
  if command -v python3 >/dev/null 2>&1; then
    echo python3
    return 0
  fi
  return 1
}

detect_toolkit_module() {
  if [ -z "${PYTHON_BIN:-}" ]; then
    return 1
  fi
  if "${PYTHON_BIN}" -c "import importlib.util, sys; sys.exit(0 if importlib.util.find_spec('toolkit') else 1)" >/dev/null 2>&1; then
    echo toolkit
    return 0
  fi
  if "${PYTHON_BIN}" -c "import importlib.util, sys; sys.exit(0 if importlib.util.find_spec('dataciviclab_toolkit') else 1)" >/dev/null 2>&1; then
    echo dataciviclab_toolkit
    return 0
  fi
  return 1
}

detect_year() {
  if [ -n "${YEAR:-}" ]; then
    echo "${YEAR}"
    return 0
  fi
  if [ -n "${1:-}" ]; then
    echo "${1}"
    return 0
  fi
  if [ -f "${DATASET_FILE}" ]; then
    parsed_year="$(sed -n 's/^[[:space:]]*years:[[:space:]]*\[\([0-9][0-9][0-9][0-9]\).*/\1/p' "${DATASET_FILE}" | head -n 1)"
    if [ -n "${parsed_year}" ]; then
      echo "${parsed_year}"
      return 0
    fi
  fi
  echo 2023
}

run_toolkit() {
  if [ -n "${TOOLKIT_COMMAND:-}" ]; then
    "${TOOLKIT_COMMAND}" "$@"
    return 0
  fi
  if [ -n "${TOOLKIT_MODULE:-}" ]; then
    "${PYTHON_BIN}" -m "${TOOLKIT_MODULE}" "$@"
    return 0
  fi
  echo "Toolkit non disponibile: imposta TOOLKIT_BIN oppure installa un modulo Python 'toolkit' o 'dataciviclab_toolkit'." >&2
  exit 2
}

PYTHON_BIN="$(detect_python || true)"
TOOLKIT_COMMAND=""
TOOLKIT_MODULE=""

if command -v "${TOOLKIT_BIN}" >/dev/null 2>&1; then
  TOOLKIT_COMMAND="${TOOLKIT_BIN}"
else
  TOOLKIT_MODULE="$(detect_toolkit_module || true)"
fi

if [ -z "${TOOLKIT_COMMAND}" ] && [ -z "${TOOLKIT_MODULE}" ]; then
  echo "Toolkit non trovato. Provati: comando '${TOOLKIT_BIN}', modulo 'toolkit', modulo 'dataciviclab_toolkit'." >&2
  exit 2
fi

YEAR="$(detect_year "${1:-}")"

echo "DCL_ROOT=${DCL_ROOT}"
echo "DATASET_FILE=${DATASET_FILE}"
echo "TOOLKIT_BIN=${TOOLKIT_BIN}"
echo "TOOLKIT_COMMAND=${TOOLKIT_COMMAND:-<none>}"
echo "TOOLKIT_MODULE=${TOOLKIT_MODULE:-<none>}"
echo "YEAR=${YEAR}"

run_toolkit run raw --config "${DATASET_FILE}" --year "${YEAR}"
run_toolkit run clean --config "${DATASET_FILE}" --year "${YEAR}"
run_toolkit run mart --config "${DATASET_FILE}" --year "${YEAR}"
run_toolkit validate --config "${DATASET_FILE}" --year "${YEAR}"
