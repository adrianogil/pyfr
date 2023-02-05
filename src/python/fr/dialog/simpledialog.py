import random


def process_dialog_graph(current_graph):
    if type(current_graph) is list:
        next_line = random.choice(current_graph)
        print(next_line)
        return
    possible_next_line = list(current_graph.keys())
    next_line = random.choice(possible_next_line)
    print(next_line)
    current_graph = current_graph[next_line]

    if not current_graph:
        return

    if type(current_graph) is list:
        next_line = random.choice(current_graph)
        print(next_line)
        return
    possible_next_line = list(current_graph.keys())

    # Get user input
    user_input = input("> ")
    user_input = user_input.strip()
    if user_input in ["exit"]:
        return
    if user_input not in possible_next_line:
        print("Désolé, je n'ai pas compris.")
        return
    process_dialog_graph(current_graph[user_input])


def generate_simple_dialog():

    dialog_graph_quoi_faire_response = {
        "Je travaille.": ["C'est cool!", "C'est dur!"],
        "Je travaille": ["C'est cool!", "C'est dur!"],
        "Je suis en vacances.": ["C'est super!", "C'est chouette!"],
        "Je vais à la plage!": ["C'est cool!", "C'est chouette!"],
        "Je fais du tourisme.": ["C'est cool!", "C'est chouette!"],
        "Rien.": ["C'est cool!", "C'est chouette!"]
    }

    dialog_cavabien_response = {
        "Ça va bien, merci!": {
            "C'est super! Qu'est-ce que tu fais ce week-end?": dialog_graph_quoi_faire_response,
            "C'est super!": None,
            "Cool": None
        }, 
        "Ça va! Quoi tu fais maintenant?": dialog_graph_quoi_faire_response
    }

    dialog_cava = {
        "Ça va!": {
            "Content de l'entendre. Et quois tu fait maintenant?": dialog_graph_quoi_faire_response
        },
        "Ça va": {
            "Content de l'entendre. Et quois tu fait maintenant?": dialog_graph_quoi_faire_response
        },
        "Ça va bien!": {
            "Content de l'entendre. Et quois tu fait maintenant?": dialog_graph_quoi_faire_response
        },
        "Ça va bien": {
            "Content de l'entendre. Et quois tu fait maintenant?": dialog_graph_quoi_faire_response
        },
        "Ça va bien, et toi?": dialog_cavabien_response,
        "Ça va! Et toi?": dialog_cavabien_response
    }

    dialog_graph_entry = {
        "Salut! Ça va?": dialog_cava,
        "Salut!": {
            "Salut": {
                "Ça va?": dialog_cava
            },
            "Salut!": {
                "Ça va?": dialog_cava
            }
        }
    }

    # responses = {
    #      [],
    #     "Ça va bien, merci!": [, ],
    #     "Ça va. Quoi tu fais maintenant?": ["Je travaille.", "Je suis en vacances."],
    #     "C'est super! Qu'est-ce que tu fais ce week-end?": ["Je vais à la plage!", "Je fais du tourisme."],
    #     "Content de l'entendre. Et toi?": ["Je travaille sur un projet.", "Je suis en vacances."],
    #     ,
    # }
    process_dialog_graph(dialog_graph_entry)



if __name__ == '__main__':
    generate_simple_dialog()
