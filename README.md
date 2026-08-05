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

## Beginner negation CLI

Generate a matching affirmative and `ne ... pas` example:

```
PYTHONPATH=src/python python -m fr.negation parler --pronoun je
PYTHONPATH=src/python python -m fr.negation --seed 17
```

The generator reuses the supported present-tense conjugations and handles
elision in forms such as `Je n'aime pas`, `Il n'a pas`, and
`Nous n'allons pas`.

## French vocabulary

`fr.vocabulaire.VERBES` mirrors verbs from the structured French vocabulary
notes, plus the legacy `croire` note. The random phrase grammar uses this
collection for its “verbe du jour” output. Inclusion in this vocabulary bank
does not imply conjugator support.
