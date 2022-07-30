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
        end = len(arr) - 1
        d = (arr[end] - arr[start]) // (end + 1)
        while start <= end:
            mid = start + ((end - start) // 2)
            term = arr[0] + mid * d  # Calculating the possible midterm
            if arr[mid] == term:
                start = mid + 1
            else:
                end = mid - 1

        return arr[end] + d


obj1 = Solution()
assert obj1.missingNumber([5, 7, 11, 13]) == 9
assert obj1.missingNumber([15, 13, 12]) == 14
assert obj1.missingNumber([1, 2, 3, 5]) == 4
assert obj1.missingNumber([7, 10, 16, 19]) == 13
assert obj1.missingNumber([7, 10, 13, 16, 19, 22, 28]) == 25
assert obj1.missingNumber([7, 13, 16, 19, 22, 25, 28]) == 10
assert obj1.missingNumber([28, 25, 22, 19, 16, 13, 7]) == 10
assert obj1.missingNumber([5, 3, 2, 1]) == 4
assert obj1.missingNumber([1, 1, 1, 1, 1, 1]) == 1
