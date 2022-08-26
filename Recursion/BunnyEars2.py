"""
We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the normal 2 ears.
The even bunnies (2, 4, ..) we'll say have 3 ears, because they each have a raised foot.
Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

bunnyEars2(0) → 0
bunnyEars2(1) → 2
bunnyEars2(2) → 5
"""


def bunnyEars(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return 3 + bunnyEars(n - 1)
    else:
        return 2 + bunnyEars(n - 1)


print(bunnyEars(4))
print(bunnyEars(3))
print(bunnyEars(2))
print(bunnyEars(1))
print(bunnyEars(0))