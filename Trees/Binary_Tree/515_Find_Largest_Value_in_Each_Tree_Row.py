"""
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

sol: Assgn the max value as minimum integer value before every level and calculate max value at each level in loop.
Append the maxValue to the output array at the end of while loop and return output array.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return None
        deq = deque([root,])
        output = []
        while deq:
            levelLen = len(deq)
            maxVal = -sys.maxsize - 1
            for i in range(0,levelLen):
                node = deq.popleft()
                maxVal = max(maxVal,node.val)
                if node.left is not None:
                    deq.append(node.left)
                if node.right is not None:
                    deq.append(node.right)
            output.append(maxVal)
        return output