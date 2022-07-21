"""
You are given a sorted array consisting of only integers where every element appears exactly twice,
except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.
"""


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums) - 1:
            if nums[i] ^ nums[i + 1]:  # If the element is not same as the next one breaking the loop.
                break
            else:  # Else, incrementing the index by 2
                i += 2
        return nums[i]


obj1 = Solution()
assert obj1.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
assert obj1.singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 4, 8]) == 8
assert obj1.singleNonDuplicate([1, 2, 2, 3, 3, 4, 4, 8, 8]) == 1
assert obj1.singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 8, 8]) == 4
assert obj1.singleNonDuplicate([8]) == 8
assert obj1.singleNonDuplicate([1, 1, 2]) == 2
