import sys

print(sys.getsizeof(range(1)))
print(sys.getsizeof(list(range(1))))

print(sys.getsizeof(range(1000)))
print(sys.getsizeof(list(range(1000))))

print(sys.getsizeof(range(20000)))
print(sys.getsizeof(list(range(20000))))