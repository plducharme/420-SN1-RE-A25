import matplotlib.pyplot as plt

# Définir les options du graphiques (tel la grandeur)
plt.figure(figsize=(2, 2))
# les arguments sont, les x, les y et ensuite on peut personnaliser le style de graphique
# marker : forme des points https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html#sphx-glr-gallery-lines-bars-and-markers-marker-reference-py
# color : couleur de la ligne https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def
# linestyle : style de la ligne {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
plt.plot(120, 35, "h")
plt.plot([100, 140], [20, 40], linestyle="-", color="b")
coordonnees_x = [25, 76, 65, 89]
coordonnees_y = [35, 55, 42, 66]
plt.plot(coordonnees_x, coordonnees_y, color="r")
plt.grid()
plt.show()
