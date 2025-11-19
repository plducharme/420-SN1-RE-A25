import csv

ma_matrice = [[0.1, 2.3, 4.5], [6.7, 8.9, 10]]

# Code du livre, problème d'ajout de lignes supplémentaires
# with open("sauvegarde.csv", mode="w") as fichier:
#     ecrivain = csv.writer(fichier)
#     ecrivain.writerows(ma_matrice)

# Code corrigé
with open("sauvegarde.csv", mode="w") as fichier:
    ecrivain = csv.writer(fichier)
    for ligne in ma_matrice:
        ecrivain.writerow(ligne)


