import random
import matplotlib.pyplot as plt
import pylab as pl

random.seed(42)

nombre_points = 8000
x_interieur = []
y_interieur = []
x_exterieur = []
y_exterieur = []

for i in range(nombre_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        x_interieur.append(x)
        y_interieur.append(y)
    else:
        x_exterieur.append(x)
        y_exterieur.append(y)

estimation_pi = 4 * len(x_interieur) / nombre_points
print(f"Estimatoin de pi: {estimation_pi}")

plt.figure()
pl.plot(x_interieur, y_interieur, ",y")
plt.plot(x_exterieur, y_exterieur, ",r")
plt.grid()
plt.show()

