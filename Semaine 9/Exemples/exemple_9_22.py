dizaines = [n * 10 for n in range(1, 8)]
print(dizaines)

# L'opérateur d'indexation [debut : fin non_incluse : pas], comme pour les str, permet de retourner une sous-liste.
# C'est du tranchage (slicing), une nouvelle liste est retournée, la liste originale n'est pas moddifiée
# debut est l'index du début, par défaut 0, fin non_incluse est l'index de fin, -1 par défaut,
# pas est le pas (de combien on avance, 1 par défaut)
print(dizaines[1:4])
print(dizaines[:])
print(dizaines[4:])


print(dizaines[0:-1:2])
# équivalent
print(dizaines[::2])
