"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

sol:
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums = sorted(nums)
        dic = {}
        output = []
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        print(dic)
       # for key,value in dic:


obj = Solution()
obj.topKFrequent([1,3,1,2,1,3,4],2)