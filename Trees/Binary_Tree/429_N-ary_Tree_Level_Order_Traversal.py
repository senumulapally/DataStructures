"""
Given an n-ary tree, return the level order traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

Sol:
1. Add root node to deq. While deq is not null,
2. Length of deq will be the length of level and write a loop from range(0,length of deq)
3. keep popping the left node in deq and add the node value to the level array.
3. Build a for loop and keep adding the children if not null to the deq
4. after each level append the level array to output array.
5. once deq is empty, return output array
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return None
        deq = deque([root,])
        output = []
        while deq:
            levelLen = len(deq)
            levelarr = []
            for i in range(0,levelLen):
                node = deq.popleft()
                levelarr.append(node.val)
                for child in node.children:
                    deq.append(child)
            output.append(levelarr)

        return output