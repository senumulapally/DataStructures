"""
Given an integer array nums and an integer k, return true if there are two distinct indices
i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Sol:
"""
from collections import deque
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        l = 0
        n = len(nums)
        dic = dict()
        dic[nums[l]] = 1
        for h in range(1,n):
            dic[nums[h]] = 1 + dic.get(nums[h], 0)
            if h-l > k:
                dic[nums[l]] -= 1
                l += 1
            if dic[nums[h]] == 2:
                if abs(h-l) <= k:
                    return True
        return False


obj = Solution()
print(obj.containsNearbyDuplicate([1,2,3,1], 3))
print(obj.containsNearbyDuplicate([1,0,1,1], 1))
print(obj.containsNearbyDuplicate([1,2,3,4,2,3], 3))
print(obj.containsNearbyDuplicate([1,2,3,1,2,3], 2))



