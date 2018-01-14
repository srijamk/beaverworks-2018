import numpy as np
from numpy import pi

a = np.arange(10).reshape(2, 5);
print(a)
print()
print(a.shape)
print()
print(a.ndim)  # Number of dimensions
print()
print(a.itemsize)
print()
print(type(a))
print()
print(a.dtype)

b = np.array([1, 2, 3])
print(b)
b = np.array([(1, 2, 3), (3, 4, 5)])
print(b)
b = np.array([(1, 2, 3), (3, 4, 5)], dtype=complex)
print(b)
b = np.empty(3, dtype=int)
print(b)
b = np.zeros((3, 4))
print(b)
b = np.ones((3, 4))
print(b)
b = np.arange(10, 30, 2)
print(b)

x = np.linspace(0, 2*pi, 100)
f = np.sin(x)
print(f)  # sin function!

