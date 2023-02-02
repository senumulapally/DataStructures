# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Sol:
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0;
        deq = deque([root,])
        maxDepth = 0
        level = 0
        while deq:
            levelLen = len(deq)
            level += 1
            for _ in range(0,levelLen):
                node = dep.popleft()
                if node.left is not None:
                    deq.append(node.left)
                if node.right is not None:
                    deq.append(node.right)
                if node.left is None and node.right is None:
                    maxDepth = max(level, maxDepth)

        return maxDepth
