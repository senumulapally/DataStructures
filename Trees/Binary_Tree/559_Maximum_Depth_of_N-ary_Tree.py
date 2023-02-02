"""
Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

Sol:similar to N-array traversal. But keep tracking the leaf node length
(maxDepth when the length of children at a node is 0) and return the maxDepth.
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        deq = deque([root,])
        maxDepth = 0
        level = 0
        while deq:
            levelLen = len(deq)
            level += 1
            for _ in range(0,levelLen):
                node = deq.popleft()
                for child in node.children:
                    if child is not None:
                        deq.append(child)
                if len(node.children) is 0:
                    maxDepth = max(maxDeoth, level)
        return maxDepth
