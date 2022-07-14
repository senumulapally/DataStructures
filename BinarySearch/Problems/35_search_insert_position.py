"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while start < end:
            '''
            While loop is written for start < end,
            as we want to terminate the loop once the start-pointer is equal to end-pointer.
            Start-pointer equals the end-pointer when the index of target value is reached.
            '''
            mid = start + (end-start)//2  # Calculating Mid-pointer
            if nums[mid] < target:  # Checking if mid-pointer value is less than that of target
                start = mid+1  # Updating start-pointer to the next index of mid-pointer
            else:
                end = mid  # If the Mid-pointer value is >= target value updating the end pointer to mid-pointer.
        if nums[start] < target:  # If the target value is to be positioned at the end
            start += 1  # Incrementing start-pointer value by 1
        return start  # Returning start pointer


object1 = Solution()
assert object1.searchInsert([1, 3, 5, 6], 5) == 2  # Running Test Case 1
assert object1.searchInsert([1, 3, 5, 6], 2) == 1  # Running Test Case 2
assert object1.searchInsert([1, 3, 5, 6], 7) == 4  # Running Test Case 3
assert object1.searchInsert([1, 3, 5, 6], 0) == 0  # Running Test Case 4
assert object1.searchInsert([1, 3, 5, 6], 1) == 0  # Running Test Case 5
