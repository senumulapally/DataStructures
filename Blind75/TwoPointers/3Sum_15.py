"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Sol: Loop nums. Skip (i) the looping for duplicates. Make sur eit is executed only once.
Write a nested while loop and consider two pointers from both ends  and keep moving until you find a target value.
Append values to result. Also skip left pointer if there are duplicate similar to i.
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        for i in range(0, len(nums)):
            if i>0 and nums[i-1]==nums[i]:  #skipping if we found the duplicate of i
                continue
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                    if (nums[l] + nums[r]) > target:
                        r -= 1
                    elif (nums[l] + nums[r]) < target:
                        l += 1
                    else:
                        threeSum = [nums[i], nums[l], nums[r]]
                        result.append(threeSum)
                        r -= 1
                        l += 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
        return result


obj = Solution()
# print(obj.threeSum([-2, 0, 0, 2, 2]))
print(obj.threeSum([-1,0,1,2,-1,-4]))
# print(obj.threeSum([0,1,1]))
# print(obj.threeSum([0,0,0]))