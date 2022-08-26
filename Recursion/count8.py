"""
Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 8 as a digit,
except that an 8 with another 8 immediately to its left counts double, so 8818 yields 4. Note that mod (%) by
10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

count8(8) → 1
count8(818) → 2
count8(8818) → 4
"""


def count8(n, flag=False):
    if n == 0:
        return 0
    else:
        if flag and n % 10 == 8:
            return 2 + count8(n // 10, True)
        elif flag == False and n % 10 == 8:
            return 1 + count8(n // 10, True)
        else:
            return 0 + count8(n // 10)


print(count8(818))
print(count8(8))
print(count8(0))
print(count8(12345))
print(count8(888))
print(count8(8818))
