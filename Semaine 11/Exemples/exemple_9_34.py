code_oaci = {"A": "Alpha", "B": "Bravo", "C": "Charlie"}

print(code_oaci["A"])

# Parcourir les tuples de clés-valeurs
for k, v in code_oaci.items():
    print(k, v)

# Parcourir la liste des clés
for k in code_oaci.keys():
    print(k)

# Parcourir la liste des valeurs
for v in code_oaci.values():
    print(v)
