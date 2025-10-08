import numpy as np


def moyenne(liste_elements: list) -> float:
    somme = 0

    for element in liste_elements:
        somme += element
    return somme/len(liste_elements)


liste_valeurs = [10, 20, 30, 40]
print(moyenne(liste_valeurs))
# Avec numpy
print(np.mean(liste_valeurs))

