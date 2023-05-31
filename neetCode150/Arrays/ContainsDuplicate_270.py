"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Sol: compare len(set(nums)) length and len(nums)
"""

# Mysol:

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums)) == len(nums):
            return False
        else:
            return True

# Sol2:

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)