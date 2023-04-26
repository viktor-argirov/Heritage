import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        couleurs = ["Coeur", "Carreau", "Pique", "Trèfle"]
        valeurs = {"As": 11, "Roi": 10, "Dame": 10, "Valet": 10,
                   "10": 10, "9": 9, "8": 8, "7": 7, "6": 6,
                   "5": 5, "4": 4, "3": 3, "2": 2}
        self.paquet = []
        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))
        random.shuffle(self.paquet)

    def distribuer(self):
        main_joueur = [self.paquet.pop(), self.paquet.pop()]
        main_croupier = [self.paquet.pop(), self.paquet.pop()]
        return main_joueur, main_croupier

    def valeur_main(self, main):
        valeur = 0
        as_present = False
        for carte in main:
            if carte.valeur == "As":
                as_present = True
            valeur =valeurs[carte.valeur]
        if as_present and valeur > 21:
            valeur -= 10
        return valeur

jeu = Jeu()

main_joueur, main_croupier = jeu.distribuer()

print("Votre main :")
for carte in main_joueur:
    print(carte.valeur, "de", carte.couleur)
print("Carte visible du croupier :")
print(main_croupier[0].valeur, "de", main_croupier[0].couleur)

while True:
    choix = input("Prendre une carte (P) ou passer (S) ? ")
    if choix.upper() == "P":
        main_joueur.append(jeu.paquet.pop())
        print("Votre main :")
        for carte in main_joueur:
            print(carte.valeur, "de", carte.couleur)
        if jeu.valeur_main(main_joueur) > 21:
            print("Vous avez dépassé 21, vous avez perdu.")
            break
    elif choix.upper() == "S":
        break
    else:
        print("Choix invalide, veuillez réessayer.")

while jeu.valeur_main(main_croupier) < 17:
    main_croupier.append(jeu.paquet.pop())

print("Main du croupier :")
for carte in main_croupier:
    print(carte.valeur, "de", carte.couleur)
