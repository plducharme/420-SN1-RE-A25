import matplotlib.pyplot as plt

for x in range(-50, 51, 10):
    plt.plot(x, x**2, ".g")

plt.title("x = x**2")
plt.grid()
plt.show()
