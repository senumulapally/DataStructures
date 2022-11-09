"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

sol: Keep moving by one node at a time and compare values of each node in both trees using DFS.
return true when values are equal and when both roots are None else return False.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.sameTree(p, q)

    def sameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        if p.val == q.val:
            res1 = self.sameTree(p.left,q.left)
            res2 = self.sameTree(p.right,q.right)
        else:
            return False

        if res1 and res2:
            return True
        else:
            return False


