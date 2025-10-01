import math


def hypothenuse_v3(adjacent, oppose):
    global resultat
    resultat = math.sqrt(adjacent**2 + oppose**2)
    return resultat


resultat = 42
print(hypothenuse_v3(3, 4))
# sera 5.0
print(resultat)
