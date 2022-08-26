"""
Given n of 1 or more, return the factorial of n, which is n * (n-1) * (n-2) ... 1.
Compute the result recursively (without loops).
factorial(1) → 1
factorial(2) → 2
factorial(3) → 6
"""


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(3))
print(factorial(4))
print(factorial(2))
print(factorial(1))
print(factorial(0))