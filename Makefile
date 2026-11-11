# CLI toolkit del Lab. Le dipendenze vivono in pyproject.toml:
#   pip install -e ".[dev,pipeline,dashboard]"
# La memoria DuckDB è controllata da safe_connect (lab-connectors) via env
# DUCKDB_MEMORY_LIMIT; nei runner CI con RAM ridotta il pipeline imposta limiti
# conservativi.
TOOLKIT = toolkit

# Slug della repo: prefisso GCS e registry. Default = nome della dir, come fa
# la pipeline con github.event.repository.name: se cloni il template e la dir
# ha il nome definitivo non serve toccare nulla.
REPO_SLUG ?= $(notdir $(CURDIR))

# --- Layer del repo (ADR-001, modello multi-dataset) ------------------------
#   datasets/  dataset principali (una dir per dataset, ognuna con dataset.yml)
#   compose/   dataset derivati che leggono più dataset o support (gira dopo)
#   support/   anagrafiche condivise usate dagli altri layer (gira prima)
# Ogni dir è un "dataset" a sé: il comando toolkit riceve il --config.
# I path relativi in dataset.yml sono risolti rispetto alla dir del file.

DATASETS := $(shell find datasets -name dataset.yml 2>/dev/null | sort)
COMPOSE  := $(shell find compose -name dataset.yml 2>/dev/null | sort)
SUPPORT  := $(shell find support -name dataset.yml 2>/dev/null | sort)

# --- Esecuzione -------------------------------------------------------------

# support seeds: anagrafiche prima di tutto
.PHONY: seeds
seeds:
	@for f in $(SUPPORT); do \
		echo "=== $$f ==="; \
		$(TOOLKIT) run --config "$$f" || exit 1; \
	done

.PHONY: run
run:
	@for f in $(DATASETS); do \
		echo "=== $$f ==="; \
		$(TOOLKIT) run --config "$$f" || exit 1; \
	done

.PHONY: compose
compose:
	@for f in $(COMPOSE); do \
		echo "=== $$f (compose) ==="; \
		$(TOOLKIT) run --config "$$f" || exit 1; \
	done

# Ordine: support → dataset → compose
.PHONY: run-all
run-all: seeds run compose

# Batch selettivo: batch.txt (un dataset.yml per riga) è generato dal workflow
# pipeline quando detect-paths è impostato, oppure da `make batch-all` in locale.
.PHONY: run-batch
run-batch:
	@test -s batch.txt || (echo "❌ batch.txt vuoto — genera con: make batch-all"; exit 1)
	$(TOOLKIT) run --batch batch.txt

.PHONY: batch-all
batch-all:
	@find datasets compose support -name dataset.yml 2>/dev/null | sort > batch.txt
	@echo "📦 $(shell wc -l < batch.txt | tr -d ' ') dataset in batch.txt"

# make run-<slug> / make status-<slug> — slug = nome della dir del dataset
run-%:
	@config=$$(find datasets compose -maxdepth 2 -name dataset.yml -path "*/$*/dataset.yml" | head -1); \
	[ -n "$$config" ] || { echo "❌ Dataset '$*' non trovato"; exit 1; }; \
	echo "=== $* ==="; \
	$(TOOLKIT) run --config "$$config"

status-%:
	@config=$$(find datasets compose -maxdepth 2 -name dataset.yml -path "*/$*/dataset.yml" | head -1); \
	[ -n "$$config" ] || { echo "❌ Dataset '$*' non trovato"; exit 1; }; \
	$(TOOLKIT) inspect runs --config "$$config"

# --- Validazione config -----------------------------------------------------

# Preflight: valida config e verifica la raggiungibilità delle fonti (rete).
# Non si ferma al primo errore: riporta tutti i config rotti e poi esce 1.
.PHONY: check
check:
	@fail=0; \
	for f in $(SUPPORT) $(DATASETS) $(COMPOSE); do \
		echo "→ $$f"; \
		if $(TOOLKIT) run preflight --config "$$f" > /dev/null 2>&1; then \
			echo "  ✅ OK"; \
		else \
			echo "  ❌ FAIL"; \
			fail=1; \
		fi; \
	done; \
	if [ $$fail -eq 0 ]; then echo "✅ All configs valid"; else echo "❌ Alcuni config non validi"; exit 1; fi

# --- Test -------------------------------------------------------------------

.PHONY: test
test:
	pytest tests/ dashboard/tests/ -v

# --- Registry (artifact catalogo — dry-run di default) ----------------------

.PHONY: registry registry-write
registry:
	$(TOOLKIT) registry build --prefix $(REPO_SLUG)

registry-write:
	$(TOOLKIT) registry build --prefix $(REPO_SLUG) --write

# --- Dashboard (richiede: pip install -e ".[dashboard]") --------------------

.PHONY: dashboard
dashboard:
	cd dashboard && streamlit run app.py --server.headless=true

# --- Pulizia -----------------------------------------------------------------

.PHONY: clean
clean:
	rm -rf out/data/_runs out/data/probe out/data/raw out/data/clean out/data/mart out/data/cross .tmp/ batch.txt

.PHONY: clean-runs
clean-runs:
	rm -rf out/data/_runs/

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:' Makefile | sort
