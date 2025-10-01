def afficher_pyramide(nb_etages):

    for numero_etage in range(1, nb_etages + 1):
        blocs = 2 * numero_etage - 1
        marge = nb_etages - numero_etage
        print(marge * " " + blocs * "o")


afficher_pyramide(5)

