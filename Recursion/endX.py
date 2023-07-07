"""
Given a string, compute recursively a new string where all the lowercase 'x'
chars have been moved to the end of the string.

endX("xxre") → "rexx"
endX("xxhixx") → "hixxxx"
endX("xhixhix") → "hihixxx"

Sol: in each recursive call we are sending the chars with one less letter chars[1:] removing chars[0].
if chars[0] is x, recursively call by returning endx(chars[1:]) + x this adds x at the end
to the chars[1:] by removing from the beginning
if chars[0] is not x, recursive call by returning chars[0] + endx(chars[1:]). this keeps chars[0] as is while returning
"""

def endX(chars):
    if len(chars) <= 1:
        return chars

    if chars[0] == 'x':
        return endX(chars[1:]) + 'x'
    else:
        return chars[0] + endX(chars[1:])


print(endX("xxre"))
print(endX("xxhixx"))
print(endX("xhixhix"))
print(endX("xxxxxxxi"))
print(endX("ixxxxxxx"))