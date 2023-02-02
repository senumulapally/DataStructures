"""
A binary tree is uni-valued if every node in the tree has the same value.
Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

sol:
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return None
        deq = deque([root,])
        value = root.val
        while deq:
            node = deq.popleft()
            if node.left is not None:
                deq.append(node.left)
            if node.right is not None:
                deq.append(node.right)
            if node.val != value:
                return False
        return True