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


"""
Boundary Pattern:
in the above problem for fixed point, i modelled it as the following. 
1. The first part will contain all the elements whose value at the index is less than index. (array[mid] < mid)
2.  The second half is elements whose index is greater than or equal to index.

Note that when wee run this while loop, it will stop at the boundary when start > end because 
of our while loop (while start <= end)
So when the while loop stops, end will point to last element of first part and 
start will point to first element of second part. 
Our answer is the first element in second part because we modelled our second part as >= mid
"""