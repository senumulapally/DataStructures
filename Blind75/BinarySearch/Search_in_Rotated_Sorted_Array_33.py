"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot
index k (1 <= k < nums.length) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Sol: We need to first find the smallest element (pivot element)
and then do Binary Search to find the target on arrays on both sides of the pivot.
If the first part finds target, return the index, else if it returns -1, search the right part of pivot.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        start = 0
        end = length-1
        pivot = -1
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] < nums [end]:
                end = mid
            elif nums[mid] > nums [end]:
                start = mid + 1
            else:
                pivot = start
                break

        result = self.BinarySearch(0, pivot, nums, target)
        if result != -1:
            return result
        return self.BinarySearch( pivot, length-1,  nums, target);


    def BinarySearch(self, start, end, nums, target):
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
        return -1


obj = Solution()
print(obj.search([4, 5, 6, 7, 8, 0, 1, 2], 8))
print(obj.search([0, 1, 2, 4, 5, 6, 7, 8], 8))
print(obj.search([0, 1, 2, 4, 5, 6, 7, 8], 0))
print(obj.search([0, 1, 2, 4, 5, 6, 7, 8], 10))
