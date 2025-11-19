
def produit_matriciel(matrice_a, matrice_b):
    matrice_produit = []
    nombre_lignes_a = len(matrice_a)
    nombre_colonnes_a = len(matrice_a[0])
    nombre_lignes_b = len(matrice_b)
    nombre_colonnes_b = len(matrice_b[0])

    if nombre_colonnes_a == nombre_lignes_b:
        for i in range(nombre_lignes_a):
            ligne_resultante = []
            for j in range(nombre_colonnes_b):
                element = 0
                for k in range(nombre_colonnes_a):
                    element += (matrice_a[i][k] * matrice_b[k][j])
                ligne_resultante.append(element)
            matrice_produit.append(ligne_resultante)
    else:
        print("Opération impossible, grandeur de matrices incompatible")
    return matrice_produit


matrice_1 = [[1, 2,],
             [3, 4],
             [5, 6]]

matrice_2 = [[1, 2, 3, 4],
             [5, 6, 7, 8]]

resultat = produit_matriciel(matrice_1, matrice_2)

print(resultat)