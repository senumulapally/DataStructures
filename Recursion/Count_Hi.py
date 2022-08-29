"""
Given a string, compute recursively (no loops) the number of times lowercase "hi" appears in the string.
countHi("xxhixx") → 1
countHi("xhixhix") → 2
countHi("hi") → 1
"""

def countHi(chars):
    n = len(chars)
    if n == 0 or n == 1:
        return 0
    else:
        if chars[0] == 'h' and chars[1] == 'i':
            return 1 + countHi(chars[2:n])
        else:
            return 0 + countHi(chars[1:n])


print(countHi("xxhixx"))
print(countHi("xhixhix"))
print(countHi("hi"))
print(countHi("h"))
print(countHi("xhx"))