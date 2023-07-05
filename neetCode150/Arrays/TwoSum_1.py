"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Sol: in nested for loop check for target and return indices
"""


# 1. Brute Force
class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Time Complexity O(n sq)


# 2. Transform and conquer ---- Here were are just returning yes/no when two elements can add upto the target

class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sortedNums = sorted(nums);
        length = len(sortedNums)
        start = 0
        end = length - 1
        while start < end:
            if (sortedNums[start] + sortedNums[end]) == target:
                return True
            elif (sortedNums[start] + sortedNums[end]) < target:
                start += 1
            else:
                end -= 1

        return False
# Time Complexity O(n log n)


# 3. When we can use extra space. -- Use hashmap (dictionary) to store value and it's index.
# Search for target-val key in dictionary and return val index, target-val index from dictionary

class Solution3(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = dict()
        length = len(nums)
        for i in range(0,length):
            if target-nums[i] in dic:
                return dic[target-nums[i]],i
            else:
                dic[nums[i]] = i


obj = Solution3()
print(obj.twoSum([2, 8, 9, 3, 4, 1, 7], 6))
print(obj.twoSum([3, 2, 4], 6))
print(obj.twoSum([3, 2, 4], 8))
