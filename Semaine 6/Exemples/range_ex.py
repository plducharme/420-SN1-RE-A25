
# range(debut, fin, pas)
# debut: début de la séquence (optionnel, par défaut = 0)
# fin: fin non-incluse de la séquence
# pas: de combien on incrémente pour le prochain élément de la séquence (optionnel, par défaut 1)

for i in range(5):
    print(i)

print("*" * 80)

for i in range(2, 15):
    print(i)

print("*" * 80)

# Avec un pas de 3
for i in range(3, 100, 3):
    print(i)

print("*" * 80)
# On peut utiliser des valeurs négatives aussi
for i in range(-1, -65, -2):
    print(i)
