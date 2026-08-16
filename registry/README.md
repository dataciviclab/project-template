# Registry

Questa cartella contiene gli artifact registry (catalogo) del repo,
generati dal builder `toolkit registry build`.

- il file `registry/registry.json` è prodotto dalla pipeline e aggiornato via
  la composite action `registry-update-pr` (draft PR dopo ogni run)
- i registry sono parte del contratto pubblico: documentano dataset, mart e
  signals con schema, periodo, location e stato del run
- non si modifica `registry.json` a mano: lo si rigenera con
  `make registry-write` (dry-run: `make registry`)

Consumer cross-repo leggono questi artifact: la documentazione del contratto
vive nel toolkit (`toolkit_registry_show`) e nel catalogo del Lab.
