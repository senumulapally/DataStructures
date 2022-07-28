"""
Given a sorted array of n elements, possibly with duplicates, find the number of occurrences of the target element.

Example 1:
Input: arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42], target = 8
Output: 3

Example 2:
Input: arr = [3, 5, 5, 5, 5, 7, 8, 8], target = 6
Output: 0

Example 3:
Input: arr = [3, 5, 5, 5, 5, 7, 8, 8], target = 5
Output: 4
"""


def occurrences(arr, target):
    rightIndex = findIndex(arr, target, True)
    if rightIndex == -1:
        return 0
    else:
        leftIndex = findIndex(arr, target, False)
        return rightIndex - leftIndex + 1


def findIndex(arr, target, isRightElement):
    low = 0
    high = len(arr) - 1
    index = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            index = mid
            if isRightElement:
                low = mid + 1
            else:
                high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return index


assert occurrences([4, 4, 8, 8, 8, 15, 16, 23, 23, 42], 8) == 3
assert occurrences([3, 5, 5, 5, 5, 7, 8, 8], 6) == 0
assert occurrences([3, 5, 5, 5, 5, 7, 8, 8], 5) == 4
