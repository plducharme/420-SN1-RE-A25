import sys
import random
# En extra, taille mémoire en octets
liste_quelconque = ["une string", 42, 666, 9876]
print(sys.getsizeof(liste_quelconque))

random.seed(42)
# resultats[0] est le total de lancer de 1 obtenu, ...
resultats = [0, 0, 0, 0, 0, 0]

for i in range(6000):
    lancer = random.randint(1, 6)
    resultats[lancer - 1] += 1  # équivalent de resultats[lancer - 1] = resultats[lancer - 1] + 1

print(resultats)


