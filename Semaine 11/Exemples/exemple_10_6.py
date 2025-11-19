# Multiplication scalaire d'une matrice
def scalaire_fois_matrice(scalaire, matrice_fournie):
    matrice_resultante = []
    for ligne in matrice_fournie:
        ligne_resultante = []
        for element in ligne:
            ligne_resultante.append(scalaire * element)
        matrice_resultante.append(ligne_resultante)
    return matrice_resultante


ma_matrice = [[10, 20, 30],
              [40, 50, 60]]

matrice_fois_2 = scalaire_fois_matrice(2, ma_matrice)
print(matrice_fois_2)


