# il existe déjà un tri dans python avec sorted()
liste_a_trier = [23, 1, 43, 22]
liste_triee = sorted(liste_a_trier)
print(liste_triee)
print(sorted(liste_triee, reverse=True))
print(liste_a_trier)
# Trier une liste en la modifiant
liste_triee.sort()
print(liste_triee)

def tri_a_bulle_optimise(liste_elements: list):
    liste_a_traiter = liste_elements.copy()
    n = len(liste_a_traiter)
    numero_passage = 1
    interversion = True

    while interversion and numero_passage <= n - 1:
        interversion = False
        for i in range(n - numero_passage):
            if liste_a_traiter[i] > liste_a_traiter[i+1]:
                temporaire = liste_a_traiter[i]
                liste_a_traiter[i] = liste_a_traiter[i+1]
                liste_a_traiter[i+1] = temporaire
                interversion = True
        numero_passage += 1
        print(numero_passage-1, liste_a_traiter)
    return liste_a_traiter


liste = [10, 30, 20, 50, 40]
print("Tri à bulles")
tri_a_bulle_optimise(liste)