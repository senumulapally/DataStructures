"""
Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""


def validMountainArray(arr):
    low = 0
    high = len(arr) - 1
    pos = -1
    neg = -1
    while low < high:
        mid = low + (high - low)//2
        if arr[i + 1] - arr[i] > 0:
            pos = 0
        elif arr[i + 1] - arr[i] < 0:
            neg = 0
        else:
            return False
        if arr[i + 1] - arr[i] > 0 and neg == 0:
            return False
        i += 1

    if pos == -1 or neg == -1:
        return False

    return True


print(validMountainArray([2, 1]))
print(validMountainArray([3, 5, 5]))
print(validMountainArray([0, 3, 2, 1]))
print(validMountainArray([1]))
print(validMountainArray([0, 1, 0]))
