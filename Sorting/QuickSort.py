"""
Quick sort - selects a random element and moves all the numbers less than pivot element to left
and greater than the pivot element to its right.

Solution:
1- Select a random index and swap the value with the starting index
2- maintain 2 pointers smaller, bigger to make partitions easy
3 - We can move 'bigger' pointer by one element each from start+1 (as start is pivot element) to end
4 - whenever a smaller value than pivot is encountered, increment the 'smaller' pointer by 1 and
5 - swap smaller index value with bigger index value
(with which all the smaller values are moved to the left and automatically bigger values are moved to the left)
6 - at the end, bring the pivot element back to its index
7 - and recursively call the helper function once with elements on the left side of pivot
(at this point pivot element is at 'smaller' pointer) and once with elements on the right side of pivot

# Lomutos partitioning both pointers start from beginning
Hoare's partitioning one pointer is at start and another starts at end position
"""

import random
def quickSort(nums):
    if len(nums) <= 1:
        return nums
    return quickSortHelper(nums, 0, len(nums)-1)

def quickSortHelper(nums, start, end):
    if start >= end:
        return
    randIndex= random.randint(start, end)
    nums[start], nums[randIndex] = nums[randIndex], nums[start]
    pivot = nums[start]
    smaller = start
    bigger = start
    for bigger in range(start+1,end+1):
        if nums[bigger] < pivot:
            smaller += 1
            nums[smaller], nums[bigger] = nums[bigger], nums[smaller]

    nums[start], nums[smaller] = nums[smaller], nums[start]
    quickSortHelper(nums, start, smaller-1)
    quickSortHelper(nums, smaller + 1, end)
    return nums

print(quickSort([3,7,1,6,2,9]))


# Time Complexity -
# Worst Case - O(n square)
# Best and Average Case - O(n log n)



# Time Complexity for Heap Sort is O(n log n)