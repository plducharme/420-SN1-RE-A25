import math


def hypothenuse(adjacent, oppose):
    resultat = math.sqrt(adjacent**2 + oppose**2)
    return resultat


print(hypothenuse(.0, 4.0))
# Donne une erreur

try:
    print(float("a"))
except ValueError as e:
    print("Erreur gérée")

print(resultat)