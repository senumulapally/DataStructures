"""
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

sol: From leverarray, pop the right most value after every for loop and append it to output.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
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
            levelArr = deque([])
            for i in range(0,levelLen):
                node = deq.popleft()
                levelArr.append(node.val)
                if node.left is not None:
                    deq.append(node.left)
                if node.right is not None:
                    deq.append(node.right)

            output.append(levelArr.pop())
        return output
