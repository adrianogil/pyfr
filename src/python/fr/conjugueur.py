import argparse
import sys


pronouns = ['Je', "Tu", "Il", "Elle", "On", "Nous", "Vous", "Ils", "Elles"]
supported_verbs = (
    "aimer",
    "aller",
    "avoir",
    "manger",
    "parler",
    "pouvoir",
    "être",
)
supported_modes_tenses = {
    "indicatif": ["présent", "passé composé", "imparfait", "plus-que-parfait"],
}
irregular_present_forms = {
    "être": {
        "je": "suis",
        "tu": "es",
        "il": "est",
        "elle": "est",
        "on": "est",
        "nous": "sommes",
        "vous": "êtes",
        "ils": "sont",
        "elles": "sont",
    },
    "aller": {
        "je": "vais",
        "tu": "vas",
        "il": "va",
        "elle": "va",
        "on": "va",
        "nous": "allons",
        "vous": "allez",
        "ils": "vont",
        "elles": "vont",
    },
}


def est_cest_voyelle(lettre):
    lettre = lettre.lower()
    return lettre in ['a', 'á', 'à', 'e', 'é', 'è', 'i', 'o', 'u']


def format_verbe(pronoun, verb):
    if pronoun.lower() == "je" and est_cest_voyelle(verb[0]):
        pronoun = pronoun[:-1]
        return pronoun + "'" + verb
    else:
        return pronoun + " " + verb


def print_verbe(pronoun, verb):
    print(format_verbe(pronoun, verb))


def normalize_pronoun(pronoun):
    for supported_pronoun in pronouns:
        if pronoun.lower() == supported_pronoun.lower():
            return supported_pronoun

    raise ValueError("Unsupported pronoun: %s" % (pronoun,))


def normalize_verb(verb):
    if verb is None or verb.strip() == "":
        raise ValueError("Verb is required")

    normalized_verb = verb.strip().lower()
    if normalized_verb not in supported_verbs:
        raise ValueError("Unsupported verb: %s" % (normalized_verb,))

    return normalized_verb


def validate_conjugation_args(pronoun, verb, mode, temps):
    normalize_pronoun(pronoun)
    normalize_verb(verb)

    if mode not in supported_modes_tenses:
        raise ValueError("Unsupported mode: %s" % (mode,))

    if temps not in supported_modes_tenses[mode]:
        raise ValueError("Unsupported tense for %s: %s" % (mode, temps))


def get_participe(verb):
    if verb == "avoir":
        return "eu"

    return verb[:-2] + "é"


def get_verb_radical(pronoun, verb, mode, temps):
    # Regular verbs - Indicatif présent
    if mode == "indicatif":
        if temps == "présent":
            if verb == "avoir":
                return "%s"
            elif verb == "pouvoir":
                return "%s"
            elif verb == "manger" and pronoun == "nous":
                return "mange%s"
            return verb[:-2] + "%s"
        elif temps == "passé composé":
            avoir_auxiliar = get_verb_desinence(pronoun, "avoir", "indicatif", "présent")

            return avoir_auxiliar + " " + get_participe(verb) + "%s"
        elif temps == "plus-que-parfait":
            avoir_auxiliar = get_verb_desinence(pronoun, "avoir", "indicatif", "imparfait")

            return avoir_auxiliar + " " + get_participe(verb) + "%s"
        elif temps == "imparfait":
            return get_verb_radical("nous", verb, "indicatif", "présent")

    return ""


def get_verb_desinence(pronoun, verb, mode, temps):
    desinence = {}

    if mode == 'indicatif':
        if temps == 'présent':
            if verb == 'avoir':
                desinence['je'] = 'ai'
                desinence['tu'] = 'as'
                desinence['il'] = 'a'
                desinence['elle'] = 'a'
                desinence['on'] = 'a'
                desinence['nous'] = 'avons'
                desinence['vous'] = 'avez'
                desinence['ils'] = 'ont'
                desinence['elles'] = 'ont'
            elif verb == 'pouvoir':
                desinence['je'] = 'peux'
                desinence['tu'] = 'peux'
                desinence['il'] = 'peut'
                desinence['elle'] = 'peut'
                desinence['on'] = 'peut'
                desinence['nous'] = 'pouvons'
                desinence['vous'] = 'pouvez'
                desinence['ils'] = 'peuvent'
                desinence['elles'] = 'peuvent'
            else:
                desinence['je'] = 'e'
                desinence['tu'] = 'es'
                desinence['il'] = 'e'
                desinence['elle'] = 'e'
                desinence['on'] = 'e'
                desinence['nous'] = 'ons'
                desinence['vous'] = 'ez'
                desinence['ils'] = 'ent'
                desinence['elles'] = 'ent'
        elif temps in ['passé composé', 'plus-que-parfait']:
            return ""
        elif temps == "imparfait":
            if verb == 'avoir':
                desinence['je'] = 'avais'
                desinence['tu'] = 'avais'
                desinence['il'] = 'avait'
                desinence['elle'] = 'avait'
                desinence['on'] = 'avait'
                desinence['nous'] = 'avions'
                desinence['vous'] = 'aviez'
                desinence['ils'] = 'avaient'
                desinence['elles'] = 'avaient'
            else:
                desinence['je'] = 'ais'
                desinence['tu'] = 'ais'
                desinence['il'] = 'ait'
                desinence['elle'] = 'ait'
                desinence['on'] = 'ait'
                desinence['nous'] = 'aions'
                desinence['vous'] = 'aiez'
                desinence['ils'] = 'aient'
                desinence['elles'] = 'aient'

    return desinence[pronoun.lower()]


def conjugueur(pronoun, verb, mode, temps):
    print(conjugate(pronoun, verb, mode, temps))


def conjugate(pronoun, verb, mode="indicatif", temps="présent"):
    validate_conjugation_args(pronoun, verb, mode, temps)
    normalized_pronoun = normalize_pronoun(pronoun)
    verb = normalize_verb(verb)

    irregular_form = get_irregular_form(normalized_pronoun.lower(), verb, mode, temps)
    if irregular_form is not None:
        return format_verbe(normalized_pronoun, irregular_form)

    verb_radical = get_verb_radical(normalized_pronoun.lower(), verb, mode, temps)
    desinence_verbale = get_verb_desinence(normalized_pronoun.lower(), verb, mode, temps)
    return format_verbe(normalized_pronoun, verb_radical % (desinence_verbale))


def get_irregular_form(pronoun, verb, mode, temps):
    if mode == "indicatif" and temps == "présent":
        verb_forms = irregular_present_forms.get(verb)
        if verb_forms is not None:
            return verb_forms[pronoun]

    return None


def iter_conjugations(target_verb, mode=None, temps=None, pronoun=None):
    modes = [mode] if mode else supported_modes_tenses.keys()

    for current_mode in modes:
        tenses = [temps] if temps else supported_modes_tenses[current_mode]
        yield current_mode.capitalize()

        for current_tense in tenses:
            yield current_tense.capitalize()
            current_pronouns = [normalize_pronoun(pronoun)] if pronoun else pronouns
            for current_pronoun in current_pronouns:
                yield conjugate(current_pronoun, target_verb, current_mode, current_tense)
            yield ""


def format_conjugations(target_verb, mode=None, temps=None, pronoun=None):
    return "\n".join(iter_conjugations(target_verb, mode, temps, pronoun)).rstrip()


def conjuguer_verb(target_verb):
    print(format_conjugations(target_verb))


def build_parser():
    parser = argparse.ArgumentParser(description="Conjugate a French verb")
    parser.add_argument(
        "verb",
        help="supported verb to conjugate: %s" % (", ".join(supported_verbs),),
    )
    parser.add_argument(
        "-m",
        "--mode",
        choices=sorted(supported_modes_tenses.keys()),
        default="indicatif",
        help="verb mode to use",
    )
    parser.add_argument(
        "-t",
        "--temps",
        "--tense",
        choices=sorted({tense for tenses in supported_modes_tenses.values() for tense in tenses}),
        help="tense to print; defaults to all supported tenses",
    )
    parser.add_argument(
        "-p",
        "--pronoun",
        help="pronoun to print; defaults to all supported pronouns",
    )

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        output = format_conjugations(args.verb, args.mode, args.temps, args.pronoun)
    except ValueError as exception:
        parser.error(str(exception))
        return 2

    print(output)
    return 0


if __name__ == '__main__':
    sys.exit(main())
