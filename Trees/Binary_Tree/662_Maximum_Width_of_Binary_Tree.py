"""
Given the root of a binary tree, return the maximum width of the given tree.
The maximum width of a tree is the maximum width among all levels.
The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes),
 where the null nodes between the end-nodes that would be present in a complete binary tree extending down
 to that level are also counted into the length calculation.
 It is guaranteed that the answer will in the range of a 32-bit signed integer.

Sol: add id of the node to the deque as well like [(root,1)] (ids are 1,2,3,4 numbering of nodes starting from 1).
left node's ID will be (2*id) and right nodes id will be (2*id + 1). store firstID whenever the loop is starting
(i.e., firstID value is None) and keep updating lastID untill loop ends.
Width of the level can be calculated by (last-first+1)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        deq = deque([(root,1)])
        maxWidth = 1
        while deq:
            levelLen = len(deq)
            first = None
            last = None
            for _ in range(0, levelLen):
                node,id = deq.popleft()
                if node.left is not None:
                    deq.append((node.left, 2 * id))
                if node.right is not None:
                     deq.append((node.right, 2 * id + 1))
                last = id
                if first is None:
                    first = id
            maxWidth = max((last - first + 1), maxWidth)
        return maxWidth