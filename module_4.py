import numpy as np

x = np.zeros((2, 2))
print(x)
y = x[0]
y += 1

print(np.shares_memory(y, x))
print(np.shape(x))