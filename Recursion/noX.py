"""
Given a string, compute recursively a new string where all the 'x' chars have been removed.

noX("xaxb") → "ab"
noX("abc") → "abc"
noX("xx") → ""
"""


def noX(chars):
    n = len(chars)
    if n == 0:
        return ""
    if chars[0] == 'x':
        return noX(chars[1:n])
    else:
        return chars[0] + noX(chars[1:n])


print(noX("xaxb"))
print(noX("xxx"))
print(noX("xx"))
print(noX("abc"))
