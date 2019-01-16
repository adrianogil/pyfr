import sys


target_verb = sys.argv[1]

pronouns = ['Je', "Tu", "Il", "Nous", "Vous", "Ils"]


def conjugueur_regular_verbs(verb):
    ''' Regular verbs
    '''
    verb_radical = verb[:-2]

    print("Indicatif\n")

    print("Présent\n")
    regular_present = [
        'e',
        'es',
        'e',
        'ons',
        'ez',
        'ent'
    ]

    for i in xrange(0, 6):
        print(pronouns[i] + " " + verb_radical + regular_present[i])


conjugueur_regular_verbs(target_verb)
