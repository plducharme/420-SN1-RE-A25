# "in" est l'opérateur d'appartenance, il permet de vérifier si un élément est dans une séquence (e.g. liste, tuple, dict, etc..)
ma_liste = ["Alice", "Bob", "Charlie", "David"]
print("Alice" in ma_liste)
print("Johnny" in ma_liste)

# pratique pour le remove(), si un élément n'existe pas et que l'on essaie de faire un remove(), une erreur est levée
if "David" in ma_liste:
    ma_liste.remove("David")
print(ma_liste)