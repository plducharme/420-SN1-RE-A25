# Faire attention si on multiple des sous-listes, elles référencent les mêmes éléments
matrice_2_par_3 = [[0] * 3] * 2
print(matrice_2_par_3)

# Si on essaie de changer la première valeur de la première sous-liste, celle de la deuxième sous-liste sera aussi
# modifiée
matrice_2_par_3[0][0] = 1
print(matrice_2_par_3)
