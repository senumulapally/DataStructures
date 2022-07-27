"""
Given an array of distinct integers arr, where arr is sorted in ascending order,
return the smallest index i that satisfies arr[i] == i. If there is no such index, return -1.
"""


class Solution(object):
    def fixedPoint(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        start = 0
        end = len(arr) - 1
        retVal = -1  # Initially considering return value as -1
        while start <= end:
            mid = start + ((end - start) // 2)
            if arr[mid] == mid:
                retVal = mid  # Updating return value to mid
                end = mid - 1  # As we need to return the lowest value, checking if there are any other
                # values which are less than current index match with their index.
                # So, updating end to previous value of mid
            elif arr[mid] < mid:
                start = mid + 1
            else:
                end = mid - 1
        return retVal


obj1 = Solution()
assert obj1.fixedPoint([-10, -5, -2, 0, 4, 5, 6, 7, 8, 9, 10]) == 4
assert obj1.fixedPoint([-10, -5, 0, 3, 7]) == 3
assert obj1.fixedPoint([0, 2, 5, 8, 17]) == 0
assert obj1.fixedPoint([-10, -5, 3, 4, 7, 9]) == -1
