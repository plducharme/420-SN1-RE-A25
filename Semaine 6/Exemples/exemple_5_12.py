def afficher_pgcd_v1(a, b):
    essai = min(a, b)
    nb_iter = 0

    while a % essai != 0 or b % essai != 0:
        essai = essai - 1
        nb_iter += 1
    print("PGCD =", essai, "en", nb_iter)


afficher_pgcd_v1(9, 15)
afficher_pgcd_v1(65, 40)
afficher_pgcd_v1(100, 400)
afficher_pgcd_v1(999, 996)



