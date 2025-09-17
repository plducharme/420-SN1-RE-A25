import matplotlib.pyplot as plt

plt.figure(figsize=(0.7, 0.7))
# Génère le carré en rouge
plt.fill([0, 1, 1, 0], [0, 0, 1, 1], color="r")
# Coordonnées des points blancs
points_x = [0.25, 0.25, 0.25, 0.75, 0.75, 0.75]
points_y = [0.25, 0.5, 0.75, 0.25, 0.5, 0.75]
# Les derniers arguments sont équivalents à "ow"
plt.plot(points_x, points_y, marker="o", color="w", linestyle="")
# Enlève les axes du graphique
plt.axis("off")
plt.show()
