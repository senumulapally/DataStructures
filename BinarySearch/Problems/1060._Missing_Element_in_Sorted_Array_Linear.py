"""
Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an
integer k, return the kth missing number starting from the leftmost number of the array.
"""


class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        high = len(nums)
        arr = []
        for i in range(0, high):
            if nums[0]+i != nums[i]:
                for j in range(nums[i - 1] + 1, nums[i]):
                    arr.append(j)
        m = len(arr)
        last = max(arr[m - 1], nums[high-1])
        if k > m:
            while m < k:
                last += 1
                arr.append(last)
                m += 1
        return arr[k-1]


obj1 = Solution()
assert obj1.missingElement([4, 7, 9, 10], 1) == 5
assert obj1.missingElement([4, 7, 9, 10], 3) == 8
assert obj1.missingElement([1, 2, 4], 3) == 6
