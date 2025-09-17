import matplotlib.pyplot as plt

points_x = [2, 4, 6]
points_y = [2, 6, 3]
points_x_carre = [4, 16, 36]
points_y_carre = [4, 36, 9]
# Pyplot supporte le fait de tracer plusieurs courbes en même temps
plt.plot(points_x, points_y, "gv--", points_x_carre, points_y_carre, "rH--")
# Ajouter des titres aux axes
plt.xlabel("Axe des x")
plt.ylabel("Le super axe des y")
# Ajouter un titre
plt.title("Exemple de graphique")
plt.legend(["points x,y", "x,y au carré"])
plt.show()



