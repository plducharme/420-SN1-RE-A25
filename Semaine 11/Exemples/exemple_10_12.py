import csv

ma_matrice = [[0.1, 2.3, 4.5], [6.7, 8.9, 10]]

# Code du livre, tous les lignes à la fois. Corrigé pour enlever le problème de lignes supplémentaires
with open("sauvegarde.csv", mode="w", encoding="utf8", newline="") as fichier:
    ecrivain = csv.writer(fichier)
    ecrivain.writerows(ma_matrice)

# Code corrigé, version ligne par ligne
with open("sauvegarde.csv", mode="w", encoding="utf8", newline="") as fichier:
    ecrivain = csv.writer(fichier)
    for ligne in ma_matrice:
        ecrivain.writerow(ligne)


