# Tri à bulles non-optimisé
def tri_a_bulles_non_optimise(liste_elements):
    liste_a_traiter = liste_elements.copy()
    n = len(liste_a_traiter)
    for numero_passage in range(1, n):
        for i in range(n - numero_passage):
            if liste_a_traiter[i] > liste_a_traiter[i+1]:
                temporaire = liste_a_traiter[i]
                liste_a_traiter[i] = liste_a_traiter[i+1]
                liste_a_traiter[i+1] = temporaire
    return liste_a_traiter


liste = [30, 40, 50, 10, 20]
resultat = tri_a_bulles_non_optimise(liste)
print(resultat)
