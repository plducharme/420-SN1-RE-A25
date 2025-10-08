a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]

if len(a) != len(b):
    print("Impossible de calculer le produit scalaire")
else:
    a_point_b = 0
    for i in range(len(a)):
        a_point_b = a_point_b + a[i]*b[i]
    print(f"Le produit scalaire est {a_point_b}")