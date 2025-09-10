import numpy as np

hypotenuse = int(input("hypothénuse: "))
angle_deg = int(input("angle en degré: "))

angle_radian = np.radians(angle_deg)
cote_oppose = hypotenuse * np.sin(angle_radian)
cote_adjacent = hypotenuse * np.cos(angle_radian)

# Version format()
print("Longueur opposée: ", format(cote_oppose, ".3g"))
# Version format string (fstring)
print(f"Longueur adjacente: {cote_adjacent:.3g}")


