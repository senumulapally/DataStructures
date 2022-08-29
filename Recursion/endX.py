"""
Given a string, compute recursively a new string where all the lowercase 'x'
chars have been moved to the end of the string.

endX("xxre") → "rexx"
endX("xxhixx") → "hixxxx"
endX("xhixhix") → "hihixxx"
"""


def endX(chars):
    n = len(chars)
    if n == 0:
        return ""
    if chars[0] == 'x':
        chars.pop()
        newChar = chars + 'x'
    else:
        newChar = chars
    return newChar


print(endX("xxre"))
print(endX("xxhixx"))
print(endX("xhixhix"))