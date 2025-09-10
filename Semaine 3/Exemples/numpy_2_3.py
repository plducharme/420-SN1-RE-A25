import numpy as np

a = 1
b = 3
c = -10

discriminant = b**2 - 4*a*c
x_1 = (-b - np.sqrt(discriminant)) / (2*a)
x_2 = (-b + np.sqrt(discriminant)) / (2*a)
print(f"Solution 1: {x_1}\tSolution 2: {x_2}")
