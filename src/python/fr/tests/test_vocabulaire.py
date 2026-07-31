import importlib
import sys
from types import SimpleNamespace

from fr import vocabulaire


EXPECTED_VERBES = {
    "aller",
    "alphabétiser",
    "aimer",
    "apaiser",
    "arracher",
    "avoir",
    "balloter",
    "buter",
    "cambrioler",
    "conquérir",
    "consacrer",
    "contrer",
    "copier",
    "croire",
    "domestiquer",
    "débrider",
    "décourager",
    "décélérer",
    "délivrer",
    "démissionner",
    "dénaturer",
    "effectuer",
    "empoigner",
    "enfermer",
    "envier",
    "exercer",
    "être",
    "flatter",
    "fournir",
    "frimer",
    "gagner",
    "gâcher",
    "intimider",
    "manger",
    "menacer",
    "miroiter",
    "musarder",
    "mériter",
    "parler",
    "patauger",
    "perquisitionner",
    "plonger",
    "pouvoir",
    "rallier",
    "relier",
    "remettre",
    "remédier",
    "renouer",
    "reproduire",
    "réfléchir",
    "siroter",
    "soupçonner",
    "surmonter",
    "triompher",
    "venger",
}


def test_verbes_match_french_vocabulary_notes():
    assert set(vocabulaire.VERBES) == EXPECTED_VERBES


def test_verbes_are_unique():
    assert len(vocabulaire.VERBES) == len(set(vocabulaire.VERBES))


def test_random_phrase_grammar_uses_vocabulary_verbs(monkeypatch):
    class FakeSimpleGrammar:
        def parse(self, grammar):
            return ""

    monkeypatch.setitem(
        sys.modules,
        "simplegrammar",
        SimpleNamespace(SimpleGrammar=FakeSimpleGrammar),
    )
    phrasesaleatoires = importlib.import_module("fr.phrasesaleatoires")

    assert phrasesaleatoires.fr_grammar["verbe_vocabulaire"] == list(
        vocabulaire.VERBES
    )
    assert "#verbe_du_jour#" in phrasesaleatoires.fr_grammar["phrase_aleatoire"]
