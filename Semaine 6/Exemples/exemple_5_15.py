def afficher_pgcd_v2(a, b):

    nb_iter = 0
    while a != b:
        temporaire = a
        a = max(temporaire, b)
        b = min(temporaire, b)
        a = a - b
        nb_iter += 1
    print("PGCD =", a, "en", nb_iter)


afficher_pgcd_v2(9, 15)
afficher_pgcd_v2(65, 40)
afficher_pgcd_v2(100, 400)
afficher_pgcd_v2(999, 996)