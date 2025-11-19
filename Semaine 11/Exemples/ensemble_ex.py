liste_1 = [1, 2, 3, 4, 5, 6]
liste_2 = [3, 4, 42, 54, 99]

# Une des utilités des ensembles est d'enlever les doublons dans des listes
liste_3 = liste_1 + liste_2
print(f"liste_3: {liste_3}")

# Pour ce faire on construit un ensemble à partir des listes, ce qui va enlever les doublons
ensemble = set(liste_3)
print(f"ensemble: {ensemble}")

liste_sans_doublons = list(ensemble)
print(f"liste_sans_doublons: {liste_sans_doublons}")


# de façon similaire et concise
print(list(set(liste_1 + liste_2)))
