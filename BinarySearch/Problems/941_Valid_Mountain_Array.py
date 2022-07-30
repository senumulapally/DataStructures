"""
Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""


def validMountainArray(arr):
    i = 0
    high = len(arr) - 1
    pos = -1
    neg = -1
    while i < high:
        if arr[i + 1] - arr[i] > 0:  # If increment in two consecutive numbers pos = 0
            pos = 0
        elif arr[i + 1] - arr[i] < 0: # If decrement in two consecutive numbers neg = 0
            neg = 0
        else:  # When both are equal returning False
            return False
        if arr[i + 1] - arr[i] > 0 and neg == 0:  # Once the negative is already 0 and then the values start
            # increasing, returning false
            return False
        i += 1

    if pos == -1 or neg == -1:  # if either one of them is missing, returning false
        return False

    return True  # returning true when all the above conditions are satisfied.


print(validMountainArray([2, 1]))
print(validMountainArray([3, 5, 5]))
print(validMountainArray([0, 3, 2, 1]))
print(validMountainArray([1]))
print(validMountainArray([0, 1, 0]))
print(validMountainArray([-1, -2, 0]))