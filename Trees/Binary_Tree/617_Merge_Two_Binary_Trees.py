"""
You are given two binary trees root1 and root2.
Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others
are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap,
then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of
the new tree.Return the merged tree.
Note: The merging process must start from the root nodes of both trees.
"""

"""
Sol: Write a recursive dfs method tho move from one node to another. If both root1 and root2 have values, add them. 
Else return the one which has value.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        return self.dfsMerge(root1, root2)

    def dfsMerge(self, root1, root2):
        if root1 is None and root2 is None:
            return None
        elif root1 is None:
            return root2
        elif root2 is None:
            return root1

        node = TreeNode()
        node.val = root1.val + root2.val
        node.left = self.dfsMerge(root1.left, root2.left)
        node.right = self.dfsMerge(root1.right, root2.right)

        return node