# Déclaration d'un tuple, on utilise les parenthèses
mon_tuple = (1, 2, 3, 4)

print(mon_tuple)

# Pour déclarer un tuple vide, on met deux parenthèse
tuple_vide = ()
print(tuple_vide)

# Pour déclarer un tuple avec un seul élément, on doit ajouter la virgule sans mettre de deuxième élément
tuple_unique = (42, )
print(tuple_unique)

# Autre façon de déclarer un tuple
mon_tuple2 = 1, 2, 3, 4
print(mon_tuple2)

# Python utilise cela à l'interne pour les assignations et les retour de fonctions
import math


def hypothenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return a, b, c


retour_fct = hypothenuse(3, 4)
print(retour_fct)

# Les éléments sont "dépaquetés"
adjacent, oppose, hypo = hypothenuse(3, 4)
print(adjacent, oppose, hypo)

# De la même façon
mon_tuple3 = (5, 6, 7, 8)
e1, e2, e3, e4 = mon_tuple3
print(e1, e2, e3, e4)
