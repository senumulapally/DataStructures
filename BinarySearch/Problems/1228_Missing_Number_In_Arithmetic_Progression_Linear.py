"""
In some array arr, the values were in arithmetic progression:
the values arr[i + 1] - arr[i] are all equal for every 0 <= i < arr.length - 1.
A value from arr was removed that was not the first or last value in the array.
Given arr, return the removed value.
"""


class Solution(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        start = 0
        end = len(arr)-1
        apSum = (end+2) * (arr[start]+arr[end])//2
        arrSum = sum(arr)
        return apSum-arrSum


obj1 = Solution()
assert obj1.missingNumber([5,7,11,13]) == 9
assert obj1.missingNumber([15,13,12]) == 14