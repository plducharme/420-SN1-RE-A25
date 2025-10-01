
quitter = False
while not quitter:

    valeur = int(input("Entrer un nombre positif, -1 pour quitter: "))

    if valeur == -1:
        print("Quitter")
        quitter = True
    elif valeur < 0:
        print("Nombre invalide")
        while valeur < 0:
            valeur = int(input("Veuillez ressaisir le nombre:"))
    print("Valeur saisie:", valeur)

