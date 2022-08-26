"""
Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2.
(no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the
rightmost digit (126 / 10 is 12).

count7(717) → 2
count7(7) → 1
count7(123) → 0
"""


def count7(n):
    if n == 0:
        return 0
    else:
        if n % 10 == 7:
            return 1 + count7(n // 10)
        else:
            return 0 + count7(n // 10)


print(count7(717))
print(count7(7))
print(count7(0))
print(count7(12345))
print(count7(777))
print(count7(17745))
