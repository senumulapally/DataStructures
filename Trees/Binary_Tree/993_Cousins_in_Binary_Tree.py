"""
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y,
return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
Two nodes of a binary tree are cousins if they have the same depth with different parents.
Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

Sol: Keep tracking x depth, y depth , xparent , yparent values at each level and at the end compare
if xparent!=yparent and xdepth=ydepth, return true. Else False.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if root is None:
            return False
        if x == root.val or y == root.val:
            return False
        deq = deque([root, ])
        depth = 0
        xDepth = 0
        yDepth = 0
        xParentVal = -sys.maxsize - 1
        yParentVal = -sys.maxsize - 1
        while deq:
            levelLen = len(deq)
            for _ in range(0,levelLen):
                node = deq.popleft()
                if node.left is not None:
                    if node.left.val == x:
                        xDepth = depth
                        xParentVal = node.val
                    if node.left.val == y:
                        yDepth = depth
                        yParentVal = node.val
                    deq.append(node.left)
                if node.right is not None:
                    if node.right.val == x:
                        xDepth = depth
                        xParentVal = node.val
                    if node.right.val == y:
                        yDepth = depth
                        yParentVal = node.val
                    deq.append(node.right)
            depth += 1

        if xParentVal != yParentVal and xDepth == yDepth:
            return True
        else:
            return False
