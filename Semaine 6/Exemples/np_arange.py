import numpy as np

# arange est similaire à range, mais peut générer des float
for i in np.arange(5):
    print(i)

print("*" * 80)

for i in np.arange(2, 12):
    print(i)

print("*" * 80)

for i in np.arange(3, 100, 3):
    print(i)

print("*" * 80)

for i in np.arange(0.25, 2.26, 0.25):
    print(i)
