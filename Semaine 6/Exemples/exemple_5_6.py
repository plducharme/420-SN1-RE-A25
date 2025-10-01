def somme_une_demie_exposant_n(tolerance: float):
    terme = 1 / 2
    numero_terme = 1
    somme = 0

    while abs(somme - 1) > tolerance:
        somme = somme + terme
        numero_terme = numero_terme + 1
        terme = (1/2)**numero_terme
    return somme


print(somme_une_demie_exposant_n(0.1))
print(somme_une_demie_exposant_n(0.01))
print(somme_une_demie_exposant_n(0.001))

