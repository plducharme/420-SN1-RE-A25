import csv

with open("sauvegarde.csv", mode="r") as fichier:
    ma_matrice_reconstituee = []
    for ligne_lue in csv.reader(fichier):
        ligne_convertie = []
        for element in ligne_lue:
            ligne_convertie.append(float(element))
        ma_matrice_reconstituee.append(ligne_convertie)


print(ma_matrice_reconstituee)
for ligne in ma_matrice_reconstituee:
    print(ligne)

