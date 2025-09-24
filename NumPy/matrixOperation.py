import numpy as np

array1 = np.arange(1, 10).reshape(3, 3)
array2 = np.arange(1, 10).reshape(3, 3)

print("3x3 matrix:")
print(array1)

print("Iterate every element in the array:")
for x in np.nditer(array1):
    print(x, end = " ")
print("\n")
print("multiplication: ")
result = np.multiply(array1, array2)
print(f"{result}\n")

trace = np.trace(array1)
print(f"trace array1: {trace}\n")

transpose = np.transpose(array2)
print("array2 transpose:")
print(transpose)


