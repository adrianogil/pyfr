import sys


pronouns = ['Je', "Tu", "Il", "Elle", "On", "Nous", "Vous", "Ils", "Elles"]


def est_cest_voyelle(lettre):
    lettre = lettre.lower()
    return lettre in ['a', 'á', 'à', 'e', 'é', 'è', 'i', 'o', 'u']


def print_verbe(pronoun, verb):
    if pronoun.lower() == "je" and est_cest_voyelle(verb[0]):
        pronoun = pronoun[:-1]
        print(pronoun + "'" + verb)
    else:
        print(pronoun + " " + verb)


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
                desinence['je'] = 'peut'
                desinence['tu'] = 'peut'
                desinence['il'] = 'a'
                desinence['elle'] = 'a'
                desinence['on'] = 'a'
                desinence['nous'] = 'avons'
                desinence['vous'] = 'avez'
                desinence['ils'] = 'ont'
                desinence['elles'] = 'ont'
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
    verb_radical = get_verb_radical(pronoun.lower(), verb, mode, temps)
    desinence_verbale = get_verb_desinence(pronoun.lower(), verb, mode, temps)
    print_verbe(pronoun, verb_radical % (desinence_verbale))


def conjuguer_verb(target_verb):
    modes = ["indicatif"]
    temps = {"indicatif": ["présent", "passé composé", "imparfait", "plus-que-parfait"]}

    for m in modes:
        print(m.capitalize())
        for t in temps[m]:
            print(t.capitalize())
            for p in pronouns:
                conjugueur(p, target_verb, m, t)
            print("")


if __name__ == '__main__':
    target_verb = sys.argv[1]
    conjuguer_verb(target_verb)
