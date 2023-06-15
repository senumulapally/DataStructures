"""
Insertion Sort (Decrease and conquer): Insert value in it's correct place in a sorted array.


Recursive:
Make recursive calls till the size of list reaches to 1.
and keep swaping jth term with j-1th term till j-1<j and j+1>j

Iterative:

"""

def insertionSortRecursive(nums, size):  #recursive
    if size <= 1:
        return
    insertionSortTD(nums, size - 1)
    j = size - 1  # index of last element
    while j >= 1 and nums[j] < nums[j - 1]:
        nums[j], nums[j - 1] = nums[j - 1], nums[j]
        j = j - 1
    return nums

def insertionSortRecursive2(nums, size): #recursive
    if size <= 1:
        return
    insertionSortTD2(nums, size - 1)
    nth = nums[size-1] # value of last element
    j = size - 2  # index of last but one element
    while j >= 0 and nums[j] > nth:
        nums[j + 1] = nums[j]
        j = j - 1
    nums[j+1] = nth
    return nums


def insertionSortIterative(nums, size): #Iterative
    if size <= 1:
        return
    for i in range(1,size):
        ith = nums[i]
        j = i-1
        while j >= 0 and nums[j] > ith:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j+1] = ith
    return nums

print(insertionSortIterative([ 7, 3, 1, 6, 2, 9], 6))
print(insertionSortIterative([1, 3, 1, 4, 7, 2, 1, 0], 8))

#Time Complexity
"""
# Iterative and Recursive
Worst Case - O(n sq) - reverse sorted
Avg Case - O(n sq)
best Case - O(n) - sorted
"""