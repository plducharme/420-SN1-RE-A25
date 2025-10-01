nombre = float(input("Nombre: "))

if nombre > 0:
    resultat = "positif"
else:
    if nombre < 0:
        resultat = "négatif"
    else:
        resultat = "nul"
print("Ce nombre est", resultat)
