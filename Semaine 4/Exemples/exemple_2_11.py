import matplotlib.pyplot as plt

plt.figure(figsize=(2, 2))
plt.bar(1, 15, color="m")
plt.bar([2, 3, 4], [10, 25, -15], width=1, color="#323796", edgecolor="k")
plt.xlim(0, 5)
plt.ylim(-20, 30)
plt.grid()
plt.gca().set_axisbelow(True)
plt.show()
