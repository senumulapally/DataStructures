"""
Given 2 sorted lists, find the intersection of two lists

eg1: [1,2,3,4] and [3,4,5,6] -> intersection is [3,4]
"""


# There are no duplicates in the same list
def intersection(lis1, lis2):
    len1 = len(lis1)
    len2 = len(lis2)
    p1, p2 = 0, 0
    res = []
    while p1 < len1 and p2 < len2:
        if lis1[p1] < lis2[p2]:
            p1 += 1
        elif lis1[p1] > lis2[p2]:
            p2 += 1
        else:
            res.append(lis1[p1])
            p1 += 1
            p2 += 1
    return res


print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))
#TimeComplexity - O(n)
#if not sorted O(n log n)

# There are duplicates in the same list but the output should be free of duplicates
def intersectionDup(lis1, lis2):
    len1 = len(lis1)
    len2 = len(lis2)
    p1, p2 = 0, 0
    res = []
    while p1 < len1 and p2 < len2:
        if p1 <= len1-2 and p2 <= len2-2:
            while lis1[p1] == lis1[p1+1]:
                p1 += 1
            while lis2[p2] == lis2[p2+1]:
                p2 += 1
        if lis1[p1] < lis2[p2]:
            p1 += 1
        elif lis1[p1] > lis2[p2]:
            p2 += 1
        else:
            res.append(lis1[p1])
            p1 += 1
            p2 += 1
    return res


print(intersectionDup([0, 0, 1, 2, 2, 3, 3, 4, 5, 5, 6], [0, 0, 0, 3, 4, 5, 6, 6, 6]))
#or we can use set of result list and return it if we can take extra space