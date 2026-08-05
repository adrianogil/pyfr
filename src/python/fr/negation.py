"""Generate beginner French present-tense negation examples."""

import argparse
from dataclasses import dataclass
from random import Random

from fr import conjugueur


BEGINNER_VERBS = conjugueur.supported_verbs
VOWELS = frozenset("aàâäáeéèêëiîïíoôöóuùûüúyÿ")


@dataclass(frozen=True)
class NegationExample:
    """An affirmative sentence paired with its ``ne ... pas`` form."""

    affirmative: str
    negative: str


def negate_present(pronoun, verb):
    """Conjugate and negate one supported verb in the present tense."""

    normalized_pronoun = conjugueur.normalize_pronoun(pronoun)
    affirmative = conjugueur.conjugate(normalized_pronoun, verb)

    if affirmative.startswith("J'"):
        verb_form = affirmative[2:]
    else:
        prefix = normalized_pronoun + " "
        if not affirmative.startswith(prefix):
            raise ValueError("Could not identify conjugated verb form")
        verb_form = affirmative[len(prefix):]

    particle = "n'" if verb_form[0].lower() in VOWELS else "ne "
    return "{0} {1}{2} pas".format(
        normalized_pronoun,
        particle,
        verb_form,
    )


def build_negation_example(verb=None, pronoun=None, seed=None):
    """Build a reproducible affirmative/negative beginner example."""

    random_generator = Random(seed)
    selected_verb = (
        conjugueur.normalize_verb(verb)
        if verb is not None
        else random_generator.choice(BEGINNER_VERBS)
    )
    selected_pronoun = (
        conjugueur.normalize_pronoun(pronoun)
        if pronoun is not None
        else random_generator.choice(conjugueur.pronouns)
    )
    return NegationExample(
        affirmative=conjugueur.conjugate(selected_pronoun, selected_verb),
        negative=negate_present(selected_pronoun, selected_verb),
    )


def format_negation_example(example):
    return "Affirmatif : {0}\nNégatif : {1}".format(
        example.affirmative,
        example.negative,
    )


def build_parser():
    parser = argparse.ArgumentParser(
        description="Generate a beginner French ne ... pas example",
    )
    parser.add_argument(
        "verb",
        nargs="?",
        choices=BEGINNER_VERBS,
        help="supported verb; omit to choose one",
    )
    parser.add_argument(
        "--pronoun",
        help="subject pronoun; omit to choose one",
    )
    parser.add_argument(
        "--seed",
        type=int,
        help="seed for a reproducible random example",
    )
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        example = build_negation_example(
            verb=args.verb,
            pronoun=args.pronoun,
            seed=args.seed,
        )
    except ValueError as error:
        parser.error(str(error))
    print(format_negation_example(example))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
