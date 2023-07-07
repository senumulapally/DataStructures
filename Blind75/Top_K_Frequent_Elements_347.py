"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Sol1:Create an empty array of arrays with the size of len(nums)+1. Create a dictionary of nums and their frequencies.
For each number while looping dictionary, append the keys to freq list at in value's index. i.e.,
if 1 is repeated 3 times 1 will be appended at 3rd index's array of freq array.
while looping from end to start, keep appending encountered values to result array until the size reaches k.

sol2: Similar to quick select. But apply the quick select on key values of dictionary.
Here, dictionary consists of numbers present in nums and their frequency.
To the helper method, send the dictionary, array if keys from dic, k, start and end
continue with the quick select on array of keys but compare the values with frequency of each number
and adjust the sequence accordingly until the desired kth element is reached.
"""
#Solution 1:

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        freq = [[] for i in range(len(nums)+1)]
        dic = {}
        for num in nums:
            dic[num] = 1 + dic.get(num,0)  # get is used to handle the numbers which are being added for the first time
        for key,val in dic.items():
            freq[val].append(key)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


obj = Solution()
print(obj.topKFrequent([1, 3, 1, 2, 1, 3, 4], 2))
print(obj.topKFrequent([1, 1, 1, 1, 2], 2))
print(obj.topKFrequent([1, 3, 1, 2, 1, 3, 4, 9, 8, 5, 5, 5, 5], 2))
print(obj.topKFrequent([1], 1))


#Solution 2:
import random


class Solution1(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums = sorted(nums)
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        lis = list(dic)
        if len(lis) <= k:
            return lis
        kIndex = len(lis) - k
        return self.topKfreqHelper(lis, kIndex, dic, 0, len(lis) - 1)

    def topKfreqHelper(self, nums, k, dic, start, end):
        if start > end:
            return
        randIndex = random.randint(start, end)
        pivot = dic[nums[randIndex]]
        nums[start], nums[randIndex] = nums[randIndex], nums[start]
        smaller = start
        for bigger in range(start + 1, end + 1):
            if dic[nums[bigger]] < pivot:
                smaller += 1
                nums[smaller], nums[bigger] = nums[bigger], nums[smaller]

        nums[smaller], nums[start] = nums[start], nums[smaller]

        if smaller == k:
            return nums[k:]
        elif smaller > k:
            return self.topKfreqHelper(nums, k, dic, start, smaller - 1)
        else:
            return self.topKfreqHelper(nums, k, dic, smaller + 1, end)

#Time Complexity O(n log n)


# obj = Solution()
# print(obj.topKFrequent([1, 3, 1, 2, 1, 3, 4], 2))
# print(obj.topKFrequent([1, 1, 1, 1], 2))
# print(obj.topKFrequent([1, 3, 1, 2, 1, 3, 4, 9, 8, 5, 5, 5, 5], 2))
