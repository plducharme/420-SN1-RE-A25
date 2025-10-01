nombre_1 = float(input("nombre 1:"))
nombre_2 = float(input("nombre 2:"))
nombre_3 = float(input("nombre 3:"))

print("Strictement croissant?", nombre_1 < nombre_2 and nombre_2 < nombre_3)
# expression simplifiée
print("Strictement croissant?", nombre_1 < nombre_2 < nombre_3)
