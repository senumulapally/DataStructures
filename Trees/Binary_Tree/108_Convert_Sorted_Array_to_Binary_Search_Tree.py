"""
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs
by more than one.
"""
"""
Sol: Write recursive function for finding the mid value in the given list and assigning to the root value.
Then calling itself for left anf right values with corresponding parts of the list. End the recursion when start>end
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        start = 0
        numsLen = len(nums)
        end = numsLen - 1
        return self.midValues(start, end, nums)

    def midValues(self, start, end, nums):
        if start > end:
            return None
        mid = start + (end - start) // 2
        root = TreeNode()
        root.val = nums[mid]
        root.left = self.midValues(start, mid - 1, nums)
        root.right = self.midValues(mid + 1, end, nums)
        return root
