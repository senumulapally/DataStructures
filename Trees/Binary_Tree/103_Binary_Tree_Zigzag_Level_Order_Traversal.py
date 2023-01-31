"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Sol:
1. Similar to Binary tree level order traversal
2. but here, the level array should be deque
3. and for alternate levels starting from level 0, we need to appendleft(node.val) to the level array.
4. Increment the level value at the end of loop
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return None
        deq = deque([root,])
        output = []
        level = 0
        while deq:
            levelarr = deque([])
            levelLen = len(deq)
            for i in range(0,levelLen):
                node = deq.popleft()
                if level%2 == 0:
                    levelarr.append(node.val)
                else:
                    levelarr.appendleft(node.val)
                if node.left is not None:
                    deq.append(node.left)
                if node.right is not None:
                    deq.append(node.right)
            output.append(levelarr)
            level += 1
        return output
