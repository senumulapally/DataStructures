"""
Given a string, compute recursively a new string where identical chars that are adjacent in the
original string are separated from each other by a "*".

pairStar("hello") → "hel*lo"
pairStar("xxyy") → "x*xy*y"
pairStar("aaaa") → "a*a*a*a"
"""

def pairStar(chars):
    n = len(chars)
    if n == 0 or n == 1:
        return chars
    if chars[0] == chars[1]:
        return chars[0] + "*" + pairStar(chars[1:n])
    else:
        return chars[0] + pairStar(chars[1:n])

print(pairStar("hello"))
print(pairStar("xxyy"))
print(pairStar("aaaa"))