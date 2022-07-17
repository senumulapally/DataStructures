"""
Given an array of elements with duplicate values,
If the target value is present in the array, the first position of the element should be returned.
Else, the possible correct position of the element should be returned
"""

class Solution(object):
    def insertAtFirstElementIndex(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0  # Initiating start-pointer
        end = len(nums) - 1  # Initiating end-pointer
        while start <= end:
            mid = start + (end-start)//2  # Calculating Mid-pointer
            if target <= nums[mid]:  # If the target number is less than or equal to the mid-point value,
                # end-pointer will be updated to the previous value of mid.
                end = mid - 1
            else:  # Even if there is a condition where the target value is at the mid-point the loop will continue
                # till the start-pointer reaches the first position of duplicate target values
                start = mid + 1

        return start  # Hence, returning start-pointer


object1 = Solution()
assert object1.insertAtFirstElementIndex([1, 3, 5, 5, 6], 5) == 2
assert object1.insertAtFirstElementIndex([1, 3, 3, 5, 5, 6], 5) == 3
assert object1.insertAtFirstElementIndex([1, 3, 3, 5, 5, 6], 1) == 0
assert object1.insertAtFirstElementIndex([1, 3, 3, 5, 5, 6], 2) == 1
assert object1.insertAtFirstElementIndex([1, 3, 3, 5, 5, 6], 6) == 5
assert object1.insertAtFirstElementIndex([1, 1, 3, 3, 5, 5, 6], 1) == 0
assert object1.insertAtFirstElementIndex([1, 1, 3, 3, 5, 5, 6], 7) == 7
assert object1.insertAtFirstElementIndex([3, 3, 5, 5, 6], 1) == 0
