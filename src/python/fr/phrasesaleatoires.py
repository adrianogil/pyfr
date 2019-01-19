from simplegrammar.grammar import SimpleGrammar


phrase_aleatoire = SimpleGrammar() \
.set_text("#phrase_aleatoire#")\
    .add_tag("phrase_aleatoire", [
        "#des_que_je_peux#",
        "#presentation_de_quelquun#",
        "#des_nos_jours#",
    ])\
    .add_tag("des_que_je_peux", [
        "#chose_je_fait_tout_les_temps# dès que je peux."
    ])\
    .add_tag("chose_je_fait_tout_les_temps", [
        "Je t'apporte #chose_a_tapporter#",
        "Je vais au cinéma",
        "J'áchete #chose_a_acheter#"
    ])\
    .add_tag("chose_a_acheter", [
        "une voiture",
        "un jouet",
        "un ordinateur"
    ])\
    .add_tag("chose_a_tapporter", [
        "la bouillie",
        "une fleur",
    ])\
    .add_tag("presentation_de_quelquun", [
        "D'abord #je_suis_mon_nom#."
    ])\
    .add_tag("je_suis_mon_nom", [
        "Je suis #nom_personne#"
    ])\
    .add_tag("nom_personne", [
        "Adriano",
        "Albert",
        "Jussara",
        "Eliamara",
        "Roberto",
        "Geovana"
    ])\
    .add_tag("des_nos_jours", [
        "Des nos jours, #chose_etrange_des_nos_jours# est devenu un vrai luxe.",
        "Des nos jours, #chose_etrange_des_nos_jours# est devenu un vrai luxe qui n'est pas donné à tout le monde.",
        "Des nos jours, la technologie en matière de téléphonie permet à un appelant d'empêcher l'affichage de son identité et de son numéro de téléphone."
    ])\
    .add_tag("chose_etrange_des_nos_jours", [
        "regarder le ciel bleu et respirer de l'air frais",
    ])\


print(str(phrase_aleatoire))
