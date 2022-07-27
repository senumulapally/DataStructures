"""
Given an array of distinct integers arr, where arr is sorted in ascending order,
return the smallest index i that satisfies arr[i] == i. If there is no such index, return -1.
"""


class Solution:
    def fixedPoint(self, arr):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] < mid:
                low = mid + 1

            else:
                high = mid - 1

        if low == len(arr) or arr[low] != low:
            return -1

        return low


obj1 = Solution()
assert obj1.fixedPoint([-10, -5, -2, 0, 4, 5, 6, 7, 8, 9, 10]) == 4
assert obj1.fixedPoint([-10, -5, 0, 3, 7]) == 3
assert obj1.fixedPoint([0, 2, 5, 8, 17]) == 0
assert obj1.fixedPoint([-10, -5, 3, 4, 7, 9]) == -1
