import math
import numpy as np

# print ("Hi")

# Lame solution to creating array of integers 0 - 9
x = []
start = 0
while start <= 9:
    x.append(start)
    start = start + 1
print(x)
###

# Awesome solution
x = []
while len(x) <= 9:
    x.append(len(x))
print(x)

x = [1, 2, 3, 4, 5]

print(x[-3:])
print(x[2:])

print(x[-3:2])
print(x[2:2])

print(x[-6:4])  # If first num in range is -, first num has index 0
print(x[0:4])

num = 4
print(num ** 0.5)

# -b + square (b^2-4ac) / 2


def solve_quad(a, b, c):

    return (-b + math.sqrt(b*b - 4*a*c)) / (2*a), (-b - math.sqrt(b*b - 4*a*c)) / (2*a)


print(solve_quad(1, 3, 2))

a = np.array([3.14, 1, 2, 3])
print(a.dtype.name)
print(type(a[2]))

b = np.zeros((4, 6), dtype=int)
print(b)
c = np.ones((2, 3), dtype=int)
print(c)
b[2:4, 2:5] = c
print(b)

rand_num = np.random.rand(10000)
print(rand_num)

print(np.average(rand_num))

run_mean = np.add.accumulate(rand_num)
run_mean = run_mean / np.arange(1, 10001)
print(run_mean)