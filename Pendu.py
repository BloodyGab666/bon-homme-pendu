import random

# Liste des mots du pendu.
liste_mots = [
    "armoire", "boucle", "buisson", "bureau",
    "chaise", "carton", "couteau", "fichier",
    "garage", "glace", "journal", "kiwi", "lampe",
    "liste", "montagne", "remise", "sandale", "taxi",
    "vampire", "volant",
]

# Nom joueur.
nom = input("Entrer votre pseudonyme : ")

# score total
score_total = 0

while True:
    # Regle jeu
    print("Vous avez 8 chances pour trouver les lettres du mot.\nBONNE CHANCE!")

    # Nombre de tentative
    nb_tenta = 8

    # Choix aléatoire d'un mot de la liste.
    mot_alea = random.choice(liste_mots)

    # Liste lettre devinées
    let_dev = []

    # score
    score = 0

    while nb_tenta > 0:
        mot_affiche = ""
        for lettre in mot_alea:
            if lettre in let_dev:
                mot_affiche += lettre + " "
            else:
                mot_affiche += "* "
        print("Mot actuel :", mot_affiche)

        # Devinée les lettres.
        let_trou = input("Choisir une lettre : ").lower()

        # Vérification de la lettre.
        if let_trou in mot_alea:
            print("Bien jouer !")
            let_dev.append(let_trou)
        else:
            print("La lettre n'est pas dans le mot.")
            nb_tenta -= 1

        # Vérification si toutes les lettres ont été devinées
        if all(lettre in let_dev for lettre in mot_alea):
            score = nb_tenta
            print("Félicitations ! Vous avez trouvé le mot :", mot_alea)
            print("Score de", nom, "pour cette parti est =", score)
            break

    # Si le joueur a épuisé toutes ses tentatives
    if nb_tenta == 0:
        print("Désolé, vous avez épuisé toutes vos tentatives. Le mot était :", mot_alea)

    # Ajout du score de la partie au score total
    score_total += score
    print("Score total de", nom, "=", score_total)

    play_again = input("Voulez-vous faire une autre partie (o/n) ? ").lower()
    if play_again != "o":
        break
