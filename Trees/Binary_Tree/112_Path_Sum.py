"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path
such that adding up all the values along the path equals targetSum. A leaf is a node with no children.

Sol: Be a good manager. Do some work and pass on remaining work to the subordinates. Calculate the sum in current loop
and ask subordinates to add up their root value to yours. Once the left node is reached, compare sum with target value.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        return self.sumPath(root, 0, targetSum)

    def sumPath(self, root, currentSum, targetSum):
        if root is None:
            return False
        currentSum = currentSum + root.val
        if root.left is None and root.right is None:
            if currentSum == targetSum:
                return True
            else:
                return False

        left = self.sumPath(root.left, currentSum, targetSum)
        right = self.sumPath(root.right, currentSum, targetSum)

        return left or right
