def sauvegarder_fibonnacci(limite: int, nom_fichier: str):

    with open(nom_fichier, mode="w") as fichier:
        precedent = 0
        courant = 1
        suivant = 1

        fichier.write(str(precedent) + "\n")
        fichier.write(str(suivant) + "\n")

        while suivant <= limite:
            fichier.write(f"{suivant}\n")
            precedent = courant
            courant = suivant
            suivant = precedent + courant


sauvegarder_fibonnacci(100, "fibo.txt")
sauvegarder_fibonnacci(150, "fibo2.txt")

