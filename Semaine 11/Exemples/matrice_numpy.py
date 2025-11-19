import numpy as np
ma_matrice = [[10, 20, 30],
              [40, 50, 60]]

matrice_np = np.array(ma_matrice)
print(matrice_np)

# multiplication par un scalaire
print(matrice_np * 2)

# produit matriciel
matrice_1 = [[1, 2,],
             [3, 4],
             [5, 6]]

matrice_2 = [[1, 2, 3, 4],
             [5, 6, 7, 8]]

resultat = np.dot(matrice_1, matrice_2)
print(resultat)

# Pour faire une matrice 2 par 3 remplie de zéros
matrice_zeros = np.zeros((2, 3))
print(matrice_zeros)

# Pour faire une matrice 2 par 3 remplie de 1
matrice_uns = np.ones((2, 3))
print(matrice_uns)


