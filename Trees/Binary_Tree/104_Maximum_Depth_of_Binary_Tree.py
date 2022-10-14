# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Calculate max depth recursively by adding 1 each time and return 0 when the root is None
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0;
        depth = max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
        return depth;
