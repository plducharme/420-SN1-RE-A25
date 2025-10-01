chaine_saisie = input("Entrez la température en F: ")
temperature_F = float(chaine_saisie)
temperature_C = (temperature_F - 32) * 5 / 9
print(temperature_F, "\u00B0F =", round(temperature_C, 1), "\u00B0C")



