from simplegrammar import SimpleGrammar


fr_grammar = {
    "text": ["#phrase_aleatoire#"],
    "phrase_aleatoire": [
        "#des_que_je_peux#",
        "#presentation_de_quelquun#",
        "#des_nos_jours#",
        "#je_me_suis_tout_daccord#"
    ],
    "je_me_suis_tout_daccord": ["Je suis tout à fait d'accord avec #chose_que_je_suis_daccord_avec#",
                                "Je suis entièrement d'accord avec #chose_que_je_suis_daccord_avec#",
                                "Je suis d'accord avec #chose_que_je_suis_daccord_avec#"],
    "chose_que_je_suis_daccord_avec": ["la politique dingue du Brèsil"],
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
    "je_suis_mon_nom": ["Je suis #nom_personne#"],
    "nom_personne": [
        "Adriano",
        "Albert",
        "Jussara",
        "Eliamara",
        "Roberto",
        "Geovana"
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
