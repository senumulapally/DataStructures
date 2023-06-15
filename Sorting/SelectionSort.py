"""
Selection sort - scan the whole list from 0-n and swap the min element with 0th element.
for the second scan, consider the list from 1-n and swap the min element with 1st element and so on..

Solution:
1- write a nested for loop. first loop is from 0-n indexes and second loop will be from i-n indexes
2 - each time find the min value from i-n indexes and swap the min value with i'th index value.
3 - at the end for both loops we'll get a sorted list
"""

def selectionSort(nums):
    length = len(nums)
    for ind in range(length):
        minIndex = ind
        for j in range(ind + 1, length):
            if nums[j] < nums[minIndex]:
                minIndex = j
        nums[minIndex], nums[ind] = nums[ind], nums[minIndex]
    return nums


print(selectionSort([3, 7, 1, 6, 2, 9]))
print(selectionSort([1, 3, 1, 4, 7, 2, 1, 0]))


# Time Complexity:  O(N square)