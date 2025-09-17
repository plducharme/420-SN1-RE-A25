import matplotlib.pyplot as plt

plt.figure(figsize=(3, 2))
plt.xlim(0, 5)
plt.ylim(0, 50)
plt.fill([1, 2, 2], [30, 30, 40], color="r")
plt.fill([1, 2, 2, 1], [10, 10, 20, 20], color="y", edgecolor="b", linestyle="--")
plt.fill([1, 4, 4], [40, 40, 10], color="None", edgecolor="k", linestyle=":")
plt.show()

