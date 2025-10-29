import csv
import pandas as pd
import math

with open("donnees_excel.csv", mode="r") as fichier:
    donnees = csv.reader(fichier, delimiter=";")

    for ligne in donnees:
        print(ligne)


# lecture en utilisant pandas
print()
dataframe = pd.read_csv("donnees_excel.csv", delimiter=";")
print(dataframe)

# ex: moyenne de l'examen 1
print(dataframe["exam1"].mean())


