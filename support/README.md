# Support dataset

Questa cartella ospita gli anagrafiche / support dataset usati dai dataset
principali in `datasets/`. Esempio di support dataset: lista comuni, elenco
codici gestionali, dizionari di classificazione.

## Regole

- un support dataset è una directory con `dataset.yml` + `sql/`, come i dataset
  principali, ma con `category: support` (o il tag equivalente nel repo)
- si esegue con `make seeds` (prima dei dataset principali)
- si dichiara nei `mart` o nei `clean` dei dataset che lo consumano
- quando un support dataset è condiviso tra più repo del Lab, si valuta di
  spostarlo in un repo dedicato o in `dataset-incubator` (issue upstream)
