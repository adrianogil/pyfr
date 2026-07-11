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
