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

        def MissingElementsCount(val1, val2):
            return abs(val2 - val1)

        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            count = MissingElementsCount(nums[0] + mid, nums[mid])
            if count < k:
                low = mid + 1
            else:
                high = mid - 1

        missingVals = MissingElementsCount(nums[0] + high, nums[high])
        return nums[high] + (k - missingVals)


obj1 = Solution()
assert obj1.missingElement([4, 7, 9, 10], 1) == 5  # TestCase 1
assert obj1.missingElement([4, 7, 9, 10], 3) == 8  # TestCase 2
assert obj1.missingElement([1, 2, 4], 3) == 6  # TestCase 3
assert obj1.missingElement([746421, 1033196, 1647541, 4775111, 7769817, 8030384], 10) == 746431  # TestCase 4
assert obj1.missingElement([1, 2, 10], 3) == 5  # TestCase 5
assert obj1.missingElement([1], 3) == 4  # TestCase 6
