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
  if "${PYTHON_BIN}" -c "import importlib.util, sys; sys.exit(0 if importlib.util.find_spec('toolkit.cli.app') else 1)" >/dev/null 2>&1; then
    echo toolkit.cli.app
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

detect_dataset() {
  if [ -n "${DATASET_NAME:-}" ]; then
    echo "${DATASET_NAME}"
    return 0
  fi
  if [ -f "${DATASET_FILE}" ]; then
    parsed_dataset="$(sed -n 's/^[[:space:]]*name:[[:space:]]*"\{0,1\}\([^"]*\)"\{0,1\}[[:space:]]*$/\1/p' "${DATASET_FILE}" | head -n 1)"
    if [ -n "${parsed_dataset}" ]; then
      echo "${parsed_dataset}"
      return 0
    fi
  fi
  echo "dataset_unknown"
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
  echo "Toolkit non disponibile: imposta TOOLKIT_BIN oppure installa il modulo Python del toolkit." >&2
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
  echo "Toolkit non trovato. Provati: comando '${TOOLKIT_BIN}', modulo 'toolkit.cli.app'." >&2
  exit 2
fi

YEAR="$(detect_year "${1:-}")"
DATASET_NAME="$(detect_dataset)"

echo "DCL_ROOT=${DCL_ROOT}"
echo "DATASET_FILE=${DATASET_FILE}"
echo "TOOLKIT_BIN=${TOOLKIT_BIN}"
echo "TOOLKIT_COMMAND=${TOOLKIT_COMMAND:-<none>}"
echo "TOOLKIT_MODULE=${TOOLKIT_MODULE:-<none>}"
echo "DATASET_NAME=${DATASET_NAME}"
echo "YEAR=${YEAR}"

run_toolkit run all --config "${DATASET_FILE}"
run_toolkit validate all --config "${DATASET_FILE}"
run_toolkit status --dataset "${DATASET_NAME}" --year "${YEAR}" --latest --config "${DATASET_FILE}"
run_toolkit inspect paths --config "${DATASET_FILE}" --year "${YEAR}" --json
