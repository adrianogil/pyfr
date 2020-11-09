from simplegrammar import SimpleGrammar


fr_grammar = {
    "text": ["#phrase_aleatoire#"],
    "phrase_aleatoire": [
        "#des_que_je_peux#",
        "#presentation_de_quelquun#",
        "#des_nos_jours#",
        "#je_me_suis_tout_daccord#",
        "#exprimer_desaccord#",
    ],
    "commence_pour_expliquer": [
        "En effet",
        "De fait",
        "Par exemple",
        "Cela dit que",
        "Cependant",
        "Pourtant",
        "Néanmoins"
    ],
    "je_me_suis_tout_daccord": [
        "#commence_pour_expliquer# je suis tout à fait d'accord avec #chose_que_je_suis_daccord_avec#",
        "#commence_pour_expliquer# je suis entièrement d'accord avec #chose_que_je_suis_daccord_avec#",
        "#commence_pour_expliquer# je suis d'accord avec #chose_que_je_suis_daccord_avec#",
        "Je suis tout à fait d'accord avec #chose_que_je_suis_daccord_avec#",
        "Je suis entièrement d'accord avec #chose_que_je_suis_daccord_avec#",
        "Je suis d'accord avec #chose_que_je_suis_daccord_avec#"
    ],
    "de_chose_que_je_ne_suis_pas_daccord": [
        "voter pour Donald Trump"
    ],
    "que_chose_que_je_ne_suis_pas_daccord": [
        "Bolsonaro continue à faire ses mauvaises choses"
    ],
    "exprimer_desaccord": [
        "C'est inacceptable",
        "C'est ridicule",
        "Je suis contre l'idée de #de_chose_que_je_ne_suis_pas_daccord#",
        "On a tort de penser que #que_chose_que_je_ne_suis_pas_daccord#",
        "On a tort de croire que #que_chose_que_je_ne_suis_pas_daccord#",
        "C'est tout à fait faux de dire que #que_chose_que_je_ne_suis_pas_daccord#",
        "C'est absolument faux de dire que #que_chose_que_je_ne_suis_pas_daccord#",
        "C'est inexact d'affirmer que #que_chose_que_je_ne_suis_pas_daccord#"
    ],
    "chose_que_je_suis_daccord_avec": [
        "la politique dingue du Brèsil",
        "sauvegarder l'Amazonie d'intérêts étrangeres"
    ],
    "des_que_je_peux": ["#chose_je_fait_tout_les_temps# dès que je peux."],
    "chose_je_fait_tout_les_temps": [
        "Je t'apporte #chose_a_tapporter#",
        "Je vais au cinéma",
        "J'áchete #chose_a_acheter#"
    ],
    "chose_a_acheter": [
        "une voiture",
        "un jouet",
        "un ordinateur"
    ],
    "chose_a_tapporter": [
        "la bouillie",
        "une fleur",
    ],
    "presentation_de_quelquun": ["D'abord #je_suis_mon_nom#."],
    "je_suis_mon_nom": [
        "Je suis #nom_personne#",
        "Je m'appele #nom_personne#"
    ],
    "nom_personne": [
        "Adriano",
        "Albert",
        "Jussara",
        "Eliamara",
        "Roberto",
        "Geovana",
        "Marie",
        "Sophie"
    ],
    "des_nos_jours": [
        "Des nos jours, #chose_etrange_des_nos_jours# est devenu un vrai luxe.",
        "Des nos jours, #chose_etrange_des_nos_jours# est devenu un vrai luxe qui n'est pas donné à tout le monde.",
        "Des nos jours, la technologie en matière de téléphonie permet à un appelant d'empêcher l'affichage de son identité et de son numéro de téléphone."
    ],
    "chose_etrange_des_nos_jours": ["regarder le ciel bleu et respirer de l'air frais"]
}


phrase_aleatoire = SimpleGrammar()
print(phrase_aleatoire.parse(fr_grammar))
