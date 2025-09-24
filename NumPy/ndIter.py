import numpy as np

array = np.arange(1, 10).reshape(3, 3)

print("3x3 matrix:")
print(array)

print("Iterate every element in the array:")
for x in np.nditer(array):
    print(x, end = " ")
