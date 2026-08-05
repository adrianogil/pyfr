import pytest

from fr import negation


@pytest.mark.parametrize(
    ("pronoun", "verb", "expected"),
    [
        ("je", "parler", "Je ne parle pas"),
        ("je", "aimer", "Je n'aime pas"),
        ("il", "avoir", "Il n'a pas"),
        ("nous", "aller", "Nous n'allons pas"),
        ("vous", "être", "Vous n'êtes pas"),
        ("elles", "pouvoir", "Elles ne peuvent pas"),
    ],
)
def test_negate_present_handles_regular_irregular_and_elided_forms(
    pronoun,
    verb,
    expected,
):
    assert negation.negate_present(pronoun, verb) == expected


def test_build_negation_example_pairs_affirmative_and_negative():
    assert negation.build_negation_example("manger", "nous") == (
        negation.NegationExample(
            affirmative="Nous mangeons",
            negative="Nous ne mangeons pas",
        )
    )


def test_seeded_negation_example_is_reproducible():
    assert negation.build_negation_example(seed=41) == (
        negation.build_negation_example(seed=41)
    )


def test_negation_rejects_unsupported_pronoun():
    with pytest.raises(ValueError, match="Unsupported pronoun: moi"):
        negation.build_negation_example("parler", "moi")


def test_cli_prints_beginner_example(capsys):
    exit_code = negation.main(["aller", "--pronoun", "je"])

    assert exit_code == 0
    assert capsys.readouterr().out == (
        "Affirmatif : Je vais\n"
        "Négatif : Je ne vais pas\n"
    )
