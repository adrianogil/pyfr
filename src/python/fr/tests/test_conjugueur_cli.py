import pytest

from fr import conjugueur


PRESENT_TENSE_TABLES = {
    "parler": (
        "Je parle",
        "Tu parles",
        "Il parle",
        "Elle parle",
        "On parle",
        "Nous parlons",
        "Vous parlez",
        "Ils parlent",
        "Elles parlent",
    ),
    "aimer": (
        "J'aime",
        "Tu aimes",
        "Il aime",
        "Elle aime",
        "On aime",
        "Nous aimons",
        "Vous aimez",
        "Ils aiment",
        "Elles aiment",
    ),
    "manger": (
        "Je mange",
        "Tu manges",
        "Il mange",
        "Elle mange",
        "On mange",
        "Nous mangeons",
        "Vous mangez",
        "Ils mangent",
        "Elles mangent",
    ),
    "avoir": (
        "J'ai",
        "Tu as",
        "Il a",
        "Elle a",
        "On a",
        "Nous avons",
        "Vous avez",
        "Ils ont",
        "Elles ont",
    ),
    "être": (
        "Je suis",
        "Tu es",
        "Il est",
        "Elle est",
        "On est",
        "Nous sommes",
        "Vous êtes",
        "Ils sont",
        "Elles sont",
    ),
    "aller": (
        "Je vais",
        "Tu vas",
        "Il va",
        "Elle va",
        "On va",
        "Nous allons",
        "Vous allez",
        "Ils vont",
        "Elles vont",
    ),
    "pouvoir": (
        "Je peux",
        "Tu peux",
        "Il peut",
        "Elle peut",
        "On peut",
        "Nous pouvons",
        "Vous pouvez",
        "Ils peuvent",
        "Elles peuvent",
    ),
}


@pytest.mark.parametrize("verb", PRESENT_TENSE_TABLES)
def test_conjugate_supports_complete_present_tense_table(verb):
    actual_forms = tuple(
        conjugueur.conjugate(pronoun, verb)
        for pronoun in conjugueur.pronouns
    )

    assert actual_forms == PRESENT_TENSE_TABLES[verb]


def test_format_conjugations_can_filter_by_tense_and_pronoun():
    assert conjugueur.format_conjugations("parler", temps="présent", pronoun="Je") == (
        "Indicatif\n"
        "Présent\n"
        "Je parle"
    )


def test_main_prints_filtered_conjugation(capsys):
    exit_code = conjugueur.main(["manger", "--temps", "présent", "--pronoun", "nous"])

    assert exit_code == 0
    assert capsys.readouterr().out == "Indicatif\nPrésent\nNous mangeons\n"


def test_main_prints_filtered_irregular_conjugation(capsys):
    exit_code = conjugueur.main(["aller", "--temps", "présent", "--pronoun", "je"])

    assert exit_code == 0
    assert capsys.readouterr().out == "Indicatif\nPrésent\nJe vais\n"


def test_main_rejects_unsupported_pronoun(capsys):
    with pytest.raises(SystemExit) as exception:
        conjugueur.main(["parler", "--pronoun", "moi"])

    assert exception.value.code == 2
    assert "Unsupported pronoun: moi" in capsys.readouterr().err
