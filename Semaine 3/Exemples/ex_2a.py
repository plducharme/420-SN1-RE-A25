# Utilisation de random
import random

random.seed(42)
lancer1 = random.randint(1, 6)
lancer2 = random.randint(1, 6)
lancer3 = random.randint(1, 6)

# Première façon d'afficher
print("Le premier lancer:\t", lancer1)
# Deuxième façon, la plus utilisée et la plus flexible
print(f"Le deuxième lancer:\t{lancer2}\nLe troisième lancer:\t{lancer3}")




