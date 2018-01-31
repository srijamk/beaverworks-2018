import numpy as np

x = np.zeros((2, 2))
print(x)
y = x[0]
y += 1

print(np.shares_memory(y, x))
print(np.shape(x))

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20]
])

print(matrix)
print(matrix.shape)
print()

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(np.dot(a, b))

a = np.arange(3).reshape(3, 1)
b = np.arange(3).reshape(1, 3)
print(np.dot(a, b))
