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


def findIndex(arr, target, isRightIndex):
    low = 0
    high = len(arr) - 1
    returnVal = -1
    while low <= high:
        mid = low + (high - low) // 2
        if isRightIndex:
            if arr[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
            returnVal = high
        else:
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
            returnVal = low

    if arr[returnVal] != target:
        return -1
    return returnVal


print(occurrences([4, 4, 8, 8, 8, 15, 16, 23, 23, 42], 8))
print(occurrences([3, 5, 5, 5, 5, 7, 8, 8], 6))
print(occurrences([3, 5, 5, 5, 5, 7, 8, 8], 5))
print(occurrences([3, 5, 7, 8, 8], 5))

"""
Boundary Pattern:
the key for boundary pattern is the following. Diving the array into either two parts or 3 parts.
If we divide the array into 3 parts if you will have equality, less than and equal condition. 
If we divide into two parts, we will skip equality condition and just have < and >= or <= and > depending on the prblm. 
The idea is when start and end cross over they stop at some key places.

More info in the Fixed_Point_Simplified.py
"""