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

The tested present-tense verb allowlist contains `aimer`, `aller`, `avoir`,
`manger`, `parler`, `pouvoir`, and `être`. Other verbs are rejected instead of
being treated as regular `-er` verbs and returning potentially incorrect forms.

## French vocabulary

`fr.vocabulaire.VERBES` mirrors verbs from the structured French vocabulary
notes, plus the legacy `croire` note. The random phrase grammar uses this
collection for its “verbe du jour” output. Inclusion in this vocabulary bank
does not imply conjugator support.
