"""
Given a binary tree, determine if it is
height-balanced- A height-balanced binary tree is a binary tree in which the depth of the
two subtrees of every node never differs by more than one.

Sol:
write a recursive function to go through the nodes and return a tuple of depth and
if the node is balanced or not for each node. Finally, return [1] frm the tuple
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.depth(root)[1]

    def depth(self, root):
        if root is None:
            return 0, True

        leftDepth, res1 =  self.depth(root.left)
        rightDepth, res2 = self.depth(root.right)

        depth = max(1+leftDepth,1+rightDepth)
        if abs(leftDepth - rightDepth)>1 or not (res1 and res2) :
            result =  False
        else:
            result = True
        return depth, result


