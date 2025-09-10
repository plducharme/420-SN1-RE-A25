import numpy as np

n_1 = float(input("coefficient milieu incident: "))
n_2 = float(input("coefficient milieu réfracté: "))
theta_1_deg = float(input("angle d'incidence: "))

theta_2_rad = np.arcsin(n_1 * np.sin(np.radians(theta_1_deg)) / n_2)
theta_2_deg = np.degrees(theta_2_rad)

print(f"Angle refraction: {theta_2_deg}\u00b0")

