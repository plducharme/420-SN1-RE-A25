ma_liste = [1, -2, 3, -4, 5]
print(f"ma_liste originale {ma_liste}")

# sorted retourne une nouvelle liste contenant les éléments triés
liste_triee = sorted(ma_liste)
print(f"ma_liste après le sorted(): {ma_liste}")
print(f"liste_triee: {liste_triee}")

# C'est différent de la fonction sort() des listes... sort() modifie la liste pour la trier
ma_liste.sort()

print(f"ma_liste après le sort(): {ma_liste}")
