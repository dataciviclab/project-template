# CLI toolkit del Lab. La memoria DuckDB è controllata da safe_connect
# (lab-connectors) via env DUCKDB_MEMORY_LIMIT (default 2GB); nei runner CI
# con RAM ridotta il pipeline imposta limiti conservativi.
TOOLKIT = toolkit

# --- Dataset del repo -------------------------------------------------------
# Convenzione (ADR-001, modello multi-dataset):
#   datasets/  = dataset principali (una dir per dataset, ognuna con dataset.yml)
#   support/   = anagrafiche/support dataset usati dai principali
# Ogni dir è un "dataset" a sé: il comando toolkit riceve il --config.
# I path relativi in dataset.yml sono risolti rispetto alla dir del file.

DATASETS := $(shell find datasets -name dataset.yml 2>/dev/null | sort)
SUPPORT  := $(shell find support -name dataset.yml 2>/dev/null | sort)

# --- Support seeds (eseguire prima dei dataset principali) ------------------

.PHONY: seeds
seeds:
	@for f in $(SUPPORT); do \
		echo "=== $$f ==="; \
		$(TOOLKIT) run --config "$$f" || exit 1; \
	done

# --- Dataset principali ------------------------------------------------------

.PHONY: run
run:
	@for f in $(DATASETS); do \
		echo "=== $$f ==="; \
		$(TOOLKIT) run --config "$$f" || exit 1; \
	done

.PHONY: run-all
run-all: seeds run

# --- Validazione config -------------------------------------------------------

.PHONY: check
check:
	@for f in $(SUPPORT) $(DATASETS); do \
		echo "→ $$f"; \
		$(TOOLKIT) run preflight --config "$$f" > /dev/null 2>&1 || exit 1; \
	done
	@echo "✅ All configs valid"

# --- Pulizia -----------------------------------------------------------------

.PHONY: clean
clean:
	rm -rf out/data/_runs out/data/probe out/data/raw out/data/clean out/data/mart out/data/cross .tmp/

.PHONY: clean-runs
clean-runs:
	rm -rf out/data/_runs/

# --- Registry (artifact catalogo — dry-run di default) -----------------------

.PHONY: registry registry-write
registry:
	$(TOOLKIT) registry build

registry-write:
	$(TOOLKIT) registry build --write

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:' Makefile | sort
