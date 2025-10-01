import matplotlib.pyplot as plt
import pandas

x = 0
y = 0

# plt.figure(figsize=(3, 3))

while y <= 100000:
    plt.plot(x, y, ".g")
    x = x + 1
    y = x ** 4 - x ** 3

plt.grid()
plt.show()
