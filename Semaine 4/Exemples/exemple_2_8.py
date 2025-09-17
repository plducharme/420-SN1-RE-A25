import matplotlib.pyplot as plt

plt.figure(figsize=(2, 2))
plt.plot(120, 35, marker="o")
plt.plot([100, 140], [20, 40], linestyle="--")
plt.axis("equal")
plt.xlim(100, 200)
plt.ylim(10, 60)
plt.grid()
plt.show()
