"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Sol: consider maxSum as minimum Integer value (-sys.maxsize - 1) and levelsum as 0.
For each level check if maxSum < levelsum and update the maxsum and minLevel values accordingly.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        deq = deque([root, ])
        level = 0
        maxSum = -sys.maxsize - 1
        minLevel = 0
        while deq:
            levelLen = len(deq)
            level += 1
            levelSum = 0
            for _ in range(0, levelLen):
                node = deq.popleft()
                levelSum = levelSum + node.val
                if node.left is not None:
                    deq.append(node.left)
                if node.right is not None:
                    deq.append(node.right)
            if maxSum < levelSum:
                maxSum = levelSum
                minLevel = level

        return minLevel
