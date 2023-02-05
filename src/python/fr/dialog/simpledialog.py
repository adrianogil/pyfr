import random


def generate_simple_dialog():
    responses = {
        "Salut! Ça va?": ["Ça va!", "Ça va bien, et toi?"],
        "Ça va! Et toi?": ["Ça va bien, merci!", "Ça va. Quoi tu fais maintenant?"],
        "Ça va bien, merci!": ["C'est super! Qu'est-ce que tu fais ce week-end?", "Content de l'entendre. Et quois tu fait maintenant?"],
        "Ça va. Quoi tu fais maintenant?": ["Je travaille.", "Je suis en vacances."],
        "C'est super! Qu'est-ce que tu fais ce week-end?": ["Je vais à la plage!", "Je fais du tourisme."],
        "Content de l'entendre. Et toi?": ["Je travaille sur un projet.", "Je suis en vacances."],
        "Je travaille.": ["C'est cool!", "C'est dur!"],
        "Je suis en vacances.": ["C'est super!", "C'est chouette!"],
        "Je vais à la plage!": ["C'est cool!", "C'est chouette!"],
        "Je fais du tourisme.": ["C'est cool!", "C'est chouette!"],
        "Rien.": ["C'est cool!", "C'est chouette!"],
    }

    def get_user_response(question):
        if question in responses:
            return random.choice(responses[question])
        else:
            return "Désolé, je n'ai pas compris. Pourrais-tu reformuler?"

    print("Bonjour! Comment ça va?")
    while True:
        user_input = input("> ")
        if user_input in ["exit"]:
            return
        response = get_user_response(user_input)
        print(response)


if __name__ == '__main__':
    generate_simple_dialog()
