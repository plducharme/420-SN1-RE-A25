
def fonction_courbe(x):
    return 2*x**3 + 18 * x - 20


def pente(x_p, delta_x):
    pente_en_x_p = (fonction_courbe(x_p + delta_x) - fonction_courbe(x_p)) / delta_x
    return pente_en_x_p


print(pente(2, 1))
print(pente(2, 0.1))