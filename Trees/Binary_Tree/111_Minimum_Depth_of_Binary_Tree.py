"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Sol: Write a recursive function to calculate depths. Here, we need to return the min depth amon left and right depths.
But when Left or Right depth is 1 we need to return max among left and right depths.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        left = 1 + self.minDepth(root.left)
        right = 1 + self.minDepth(root.right)

        if left == 1 or right == 1:
            depth = max(left, right)
        else:
            depth = min(left, right)

        return depth
