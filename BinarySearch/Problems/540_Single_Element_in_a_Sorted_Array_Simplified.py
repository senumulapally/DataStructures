"""
You are given a sorted array consisting of only integers where every element appears exactly twice,
except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.
"""


class Solution:

    def singleNonDuplicate(self, nums):
        low = 0
        high = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

         while low <= high:
            mid = low + (high - low) // 2

            if mid % 2 == 0:
                if mid == len(nums) - 1:
                    return nums[mid]

                if nums[mid] == nums[mid + 1]:
                    low = mid + 2
                else:
                    high = mid - 1
            else:
                if nums[mid] == nums[mid - 1]:
                    low = mid + 1
                else:
                    high = mid - 1

        return nums[low]


obj1 = Solution()
assert obj1.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2  # Test Case 1
assert obj1.singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 4, 8]) == 8  # Test Case 2
assert obj1.singleNonDuplicate([1, 2, 2, 3, 3, 4, 4, 8, 8]) == 1  # Test Case 3
assert obj1.singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 8, 8]) == 4  # Test Case 4
assert obj1.singleNonDuplicate([8]) == 8  # Test Case 5
assert obj1.singleNonDuplicate([1, 1, 2]) == 2  # Test Case 6
