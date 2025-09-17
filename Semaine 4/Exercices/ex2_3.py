import random

valeur_1 = random.uniform(0, 1)
valeur_2 = random.uniform(0, 1)
valeur_3 = random.uniform(0, 1)

# produit = valeur_1 * valeur_2 * valeur_3
print(f"Le produit de {valeur_1} * {valeur_2} * {valeur_3} est {valeur_1 * valeur_2 * valeur_3}")

# Autre façon que l'on va voir plus tard
total = 0.0
for i in range(0, 3):
    total += random.uniform(0, 1)
print(f"Total: {total}")
