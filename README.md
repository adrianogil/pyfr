# pyfr
Text generation in French

## French conjugation CLI

Conjugate all supported forms for a verb:

```
PYTHONPATH=src/python python -m fr.conjugueur parler
```

Filter by tense and pronoun:

```
PYTHONPATH=src/python python -m fr.conjugueur manger --temps présent --pronoun nous
```

## French vocabulary

`fr.vocabulaire.VERBES` mirrors verbs from the structured French vocabulary
notes, plus the legacy `croire` note. The random phrase grammar uses this
collection for its “verbe du jour” output.
