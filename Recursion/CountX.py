"""
Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.
countX("xxhixx") → 4
countX("xhixhix") → 3
countX("hi") → 0
"""


def countX(chars):
    n = len(chars)
    if n == 0:
        return 0
    else:
        if chars[n - 1] == 'x':
            return 1 + countX(chars[0:n - 1])
        else:
            return 0 + countX(chars[0:n - 1])


print(countX("xxhixx"))
print(countX("xhixhix"))
print(countX("hi"))
