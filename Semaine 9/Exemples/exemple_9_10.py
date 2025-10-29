# Fonctions sur les listes
nombres_premiers = [2, 3, 5]
suivants = [7, 11]
print(nombres_premiers)
print(suivants)

# extend() ajoute une liste à la fin de la liste sur laquelle le extend est appelé
nombres_premiers.extend(suivants)
print(nombres_premiers)

# insert(index, valeur) insert la valeur à l'index spécifié dans la liste et décale les éléments vers la droite
print()
ma_liste = [10, 20, 30, 40, 50]
print(ma_liste)
ma_liste.insert(2, 99)
print(ma_liste)

# remove(valeur) retire la première occurence de la valeur de la liste
print()
ma_liste.remove(99)
print(ma_liste)

