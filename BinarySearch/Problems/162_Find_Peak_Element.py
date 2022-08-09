"""
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater
than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.
"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        length = len(nums)
        while low <= high:
            mid = low + (high - low)//2
            if (mid == 0 and length == 1) or (mid == length - 1):
                return mid
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid] > nums[mid+1]:
                high = mid - 1
            else:
                low = mid + 1


obj1 = Solution()
print(obj1.findPeakElement([1,2,3,1]))
print(obj1.findPeakElement([1,2,1,3,5,6,4]))
print(obj1.findPeakElement([1,2,3,5,6]))
print(obj1.findPeakElement([1,2,1]))
print(obj1.findPeakElement([2]))
