"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Sol: Using quick sort/select pattern, select a pivot element and by the end of loop the pivot element goes to its index.
 If the index is equal to required index, return the value.
 else if the index is smaller than the required index, recursively call the helper method with second partition
 else call the method recursively with first partition until the pivot element ends up at required index
"""

import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) < 0 or k < 0 or k > len(nums):
            return None
        reqIndex = len(nums) - k
        return self.kthLargestHelper(nums, reqIndex, 0, len(nums)-1)

    def kthLargestHelper(self, nums, reqIndex, start, end):
        if start > end:
            return
        elif start == end:
            return nums[start]
        randIndex = random.randint(start, end)
        nums[start], nums[randIndex] = nums[randIndex], nums[start]
        pivot = nums[start]
        smaller = start
        for bigger in range(start + 1, end + 1):
            if nums[bigger] < pivot:
                smaller += 1
                nums[bigger], nums[smaller] = nums[smaller], nums[bigger]

        nums[start], nums[smaller] = nums[smaller], nums[start]
        if reqIndex == smaller:
            return nums[smaller]
        elif reqIndex < smaller:
            return self.kthLargestHelper(nums, reqIndex, start, smaller - 1)
        else:
            return self.kthLargestHelper(nums, reqIndex, smaller + 1, end)

# Worst case for a quick select/sort is O(n sq)
# but, avg case is O(n) - (Assuming that each time we are eliminating 5% of numbers [1*n +0.95n + 0.95 sq * n + ....]
# which gives n(1/1-f) here f is 0.95 which gives n(20) - so Ticme complexity is O(n)

obj = Solution()
print(obj.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(obj.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))


# Bruteforce: Is to sort and then find the kth largest element
# It takes O(n log n) for sorting and O (1) for getting the kth largest element

class Solution2(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        x = len(nums) - k
        return nums[x]

# obj = Solution2()
# print(obj.findKthLargest([3,2,1,5,6,4],2))
