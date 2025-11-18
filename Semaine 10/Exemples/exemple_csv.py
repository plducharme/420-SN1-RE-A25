import csv

with open("eee_listeespeces_csv.csv", mode="r", encoding="utf-8-sig") as fichier:
    # lis le fichier sous forme de csv
    donnees = csv.reader(fichier)

    for i, ligne in enumerate(donnees):
        # Saute par dessus la première ligne
        if i == 0:
            continue
        print(f"Regne: {ligne[0]}\tNom Latin: {ligne[3]}")

