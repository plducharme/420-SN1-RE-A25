# Par défaut, la comparaison d'objets en Python se fait par référence. Cela signifie que deux objets sont égaux si et
# seulement s'ils pointent vers la même adresse mémoire. En d'autres mots, ils seront égaux s'ils sont le même objet.
class ObjetNormal:
    def __init__(self, x: int):
        self.x = x


# Création de deux objets
obj1 = ObjetNormal(5)
obj2 = ObjetNormal(5)

if obj1 == obj2:
    print("Les objets sont égaux")
else:
    print("Les objets ne sont pas égaux")

# Les objets ne sont pas égaux, même si les valeurs des attributs sont les mêmes. Cela est dû au fait que les objets
# sont comparés par référence, et non par valeur.

# Pour comparer des objets par valeur, il suffit de redéfinir les méthodes des opérateurs de comparaison dans la classe
# de l'objet. Les méthodes à redéfinir sont:
# __eq__ pour l'opérateur ==
# __ne__ pour l'opérateur !=
# __lt__ pour l'opérateur <
# __le__ pour l'opérateur <=
# __gt__ pour l'opérateur >
# __ge__ pour l'opérateur >=
# Ces méthodes doivent retourner un booléen. Par exemple, pour comparer deux objets par la valeur de leur attribut x:


class ObjetAvecComparaison:
    def __init__(self, x: int):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x

    def __ne__(self, other):
        return self.x != other.x

    def __lt__(self, other):
        return self.x < other.x

    def __le__(self, other):
        return self.x <= other.x

    def __gt__(self, other):
        return self.x > other.x

    def __ge__(self, other):
        return self.x >= other.x


# Création de deux objets
objet_comparable1 = ObjetAvecComparaison(5)
objet_comparable2 = ObjetAvecComparaison(5)

# À noter que la comparaison suivante utilise la méthode __eq__ redéfinie dans la classe ObjetAvecComparaison
if objet_comparable1 == objet_comparable2:
    print("Les objets comparable sont égaux")
else:
    print("Les objets comparables ne sont pas égaux")

# De la même manière, les autres opérateurs de comparaison utilisent les méthodes redéfinies dans la classe
objet_comparable3 = ObjetAvecComparaison(10)
objet_comparable4 = ObjetAvecComparaison(8)
# Cette comparaison utilise la méthode __gt__ redéfinie dans la classe ObjetAvecComparaison
if objet_comparable3 > objet_comparable4:
    print("objet_comparable3 est plus grand que objet_comparable4")
# Cette comparaison utilise la méthode __lt__ redéfinie dans la classe ObjetAvecComparaison
if objet_comparable4 < objet_comparable3:
    print("objet_comparable4 est plus petit que objet_comparable3")
# Ansi de suite pour les autres opérateurs de comparaison