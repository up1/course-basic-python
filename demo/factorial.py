import sys

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))

# Max of recursion in python
print(sys.getrecursionlimit())
sys.setrecursionlimit(15000)
print(sys.getrecursionlimit())
print(factorial(5000))
