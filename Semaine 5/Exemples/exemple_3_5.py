print("Première instructions")


def afficher_equivalent_celsius(temperature_F: float):
    temperature_C = (temperature_F - 32) * 5 / 9
    print(temperature_F, "\u00B0F =", round(temperature_C, 1), "\u00B0C")


print("Deuxième instructions")
afficher_equivalent_celsius(42.0)
afficher_equivalent_celsius(89)
afficher_equivalent_celsius(72.5)



