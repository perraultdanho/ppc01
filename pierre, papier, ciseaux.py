import tkinter as tk
import random

# Initialiser la fenêtre de jeu
window = tk.Tk()
window.title("Jeu Pierre, Papier, Ciseaux")
window.geometry("400x300")  # Définir les dimensions de la fenêtre
window.config(bg="lightblue")  # Définir la couleur d'arrière-plan

# Créer une étiquette pour le titre du jeu
title_label = tk.Label(window, text="Pierre, Papier, Ciseaux", font=("Helvetica", 16), bg="lightblue")
title_label.pack(pady=20)

# Créer une étiquette pour inviter l'utilisateur à faire un choix
prompt_label = tk.Label(window, text="Choisissez Pierre, Papier ou Ciseaux :", font=("Helvetica", 12), bg="lightblue")
prompt_label.pack()

# Créer un champ de saisie pour que l'utilisateur entre son choix
user_choice = tk.Entry(window, font=("Helvetica", 12))
user_choice.pack(pady=10)

# Fonction pour générer le choix de l'ordinateur
def generate_computer_choice():
    choices = ["pierre", "papier", "ciseaux"]
    comp_pick = random.choice(choices)
    return comp_pick

# Fonction pour afficher le choix de l'ordinateur et le résultat
def play_game():
    user_pick = user_choice.get().lower()
    comp_pick = generate_computer_choice()
    
    result_text = f"Votre choix : {user_pick}\nChoix de l'ordinateur : {comp_pick}\n"

    # Déterminer le résultat du jeu
    if user_pick == comp_pick:
        result_text += "Match nul !"
    elif (user_pick == "pierre" and comp_pick == "ciseaux") or \
         (user_pick == "papier" and comp_pick == "pierre") or \
         (user_pick == "ciseaux" and comp_pick == "papier"):
        result_text += "Vous avez gagné !"
    else:
        result_text += "L'ordinateur a gagné !"
    
    # Afficher le résultat
    result_label.config(text=result_text)

# Créer un bouton pour lancer le jeu
play_button = tk.Button(window, text="Jouer", font=("Helvetica", 12), command=play_game)
play_button.pack(pady=20)

# Créer un label pour afficher les résultats
result_label = tk.Label(window, text="", font=("Helvetica", 12), bg="lightblue")
result_label.pack()

# Lancer la boucle principale de l'application
window.mainloop()
