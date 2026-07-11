import pytest

from fr import conjugueur


def test_conjugate_formats_elision_before_vowel():
    assert conjugueur.conjugate("je", "aimer") == "J'aime"


def test_conjugate_keeps_manger_e_for_nous_present():
    assert conjugueur.conjugate("nous", "manger") == "Nous mangeons"


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


def test_main_rejects_unsupported_pronoun(capsys):
    with pytest.raises(SystemExit) as exception:
        conjugueur.main(["parler", "--pronoun", "moi"])

    assert exception.value.code == 2
    assert "Unsupported pronoun: moi" in capsys.readouterr().err
