"""
Bubble Sort: We scan the array from right to left. we keep comparing two adjacent elements
and swap the elements so that min element is towards left. At the end of first iteration, smallest element
would be at index-0. At the end of second iteration, second smallest num would be at index-1 and so on..

Sol: Iterate a for loop from 0-n, then a nested loop iterating from n-i.
from right to left, compare adj two elements. whenever a greater number is encountered in a smaller
index swap it with adjacent greater number. At the end of loops, return the list.
"""

def bubbleSort(nums):
    length = len(nums)
    for i in range(0,length):
        for j in range(length-1,i, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j - 1] = nums[j-1], nums[j]
    return nums

print(bubbleSort([3, 7, 1, 6, 2, 9]))
print(bubbleSort([1, 3, 1, 4, 7, 2, 1, 0]))

# Time Complexity:  O(N square)