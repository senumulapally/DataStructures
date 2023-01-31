"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
Answers within 10-5 of the actual answer will be accepted.

sol: Similar to Level order traversal, but instead of adding values to Levelarray we add them and at the end of loop we divide it with length of level. We need to use float() for any either dividend or divisor to get the answer in float values.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
            return None
        deq = deque([root,])
        output = []
        while deq:
            levellen = len(deq)
            sum = 0
            for i in range(0,levellen):
                node = deq.popleft()
                sum = sum + node.val
                if node.left is not None:
                    deq.append(node.left)
                if node.right is not None:
                    deq.append(node.right)
            output.append(sum/float(levellen))
        return output