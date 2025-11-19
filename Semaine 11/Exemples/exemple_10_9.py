import copy

liste_imbriquee = [10, [20, 30]]
# Si on modifie liste_jumelle, liste_imbriquee sera modifiée
liste_jumelle = liste_imbriquee

# Une nouvelle copy est faire par copy(), sauf que la sous-liste est celle référencée par la sous-liste dans
# liste_imbriquee
copie_superficielle = liste_imbriquee.copy()

# deepcopy fait aussi une nouvelle copie des sous-listes dans la liste
copie_profonde = copy.deepcopy(liste_imbriquee)

liste_imbriquee[0] = 11
liste_imbriquee[1][0] = 21

print(liste_imbriquee)
print(liste_jumelle)

print(copie_superficielle)
print(copie_profonde)
