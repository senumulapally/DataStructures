"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Sol: Convert nums to set(nums)
loop the nums and write a condition to check if num-1 exists in nums
if not continue with the loop and check if num+1 exists in the loop keep incrementing the
num to find the no.of consecutive values available. and update the maxLength value each time.
"""
#Simplified
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLength = 0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                count = 1
                j = num
                while j+1 in nums:
                    count+= 1
                    j += 1
                maxLength = max(maxLength, count)
        return maxLength

obj = Solution()
print(obj.longestConsecutive([100,4,200,1,3,2]))
print(obj.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(obj.longestConsecutive([0,-1]))

class Solution1(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLength = 0
        count = 1
        nums = set(nums)
        for num in nums:
            if num-1 in nums and count == 1:
                continue
            flag = 1
            j = num
            while flag:
                if j+1 in nums:
                    count+= 1
                    j = j + 1
                else:
                    count = 1
                    flag = 0
                maxLength = max(maxLength, count)
        return maxLength
