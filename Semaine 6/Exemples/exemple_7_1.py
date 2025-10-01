def afficher_table_multi(n):
    for i in range(1, n + 1):
        for j in range(1, n+1):
            print(i, "X", j, "=", i*j)
        print("----------")


afficher_table_multi(3)

