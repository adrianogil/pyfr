import sys


target_verb = sys.argv[1]

pronouns = ['Je', "Tu", "Il", "Elle", "Nous", "Vous", "Ils", "Elles"]


def est_cest_voyelle(lettre):
    lettre = lettre.lower()
    return lettre == 'a' or \
           lettre ==  'á' or \
           lettre ==  'à' or \
           lettre ==  'e' or \
           lettre ==  'é' or \
           lettre ==  'è' or \
           lettre ==  'i' or \
           lettre ==  'o' or \
           lettre ==  'u'


def print_verbe(pronoun, verb):
    if pronoun.lower() == "je" and est_cest_voyelle(verb[0]):
        pronoun = pronoun[:-1]
        print(pronoun + "'" + verb)
    else:
        print(pronoun + " " + verb)

def get_verb_radical(pronoun, verb, mode, temps):
    # Regular verbs - Indicatif présent
    return verb[:-2]

def get_verb_desinence(pronoun, verb, mode, temps):
    desinence = {}

    if mode == 'indicatif':
        if temps == 'présent':
            desinence['je'] = 'e'
            desinence['tu'] = 'es'
            desinence['il'] = 'e'
            desinence['elle'] = 'e'
            desinence['nous'] = 'ons'
            desinence['vous'] = 'ez'
            desinence['ils'] = 'ent'
            desinence['elles'] = 'ent'

    return desinence[pronoun.lower()]


def conjugueur(pronoun, verb, mode, temps):
    verb_radical = get_verb_radical(pronoun, verb, mode, temps)
    desinence_verbale = get_verb_desinence(pronoun, verb, mode, temps)
    print_verbe(pronoun, verb_radical + desinence_verbale)

for p in pronouns:
    conjugueur(p, target_verb, "indicatif", "présent")
