liste_a = [1, 2, 3, 4]
# Première façon de copier une liste
liste_copy = liste_a.copy()
print(liste_copy)
# deuxième façon
liste_c2 = liste_a[:]
print(liste_c2)
liste_a[0] = 42
print(liste_copy, liste_c2)

# Troisième façon à éviter
liste_d = []
for x in liste_a:
    liste_d.append(x)
print(liste_d)

