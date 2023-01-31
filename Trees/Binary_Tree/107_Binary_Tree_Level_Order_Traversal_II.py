"""
Given the root of a binary tree, return the bottom-up level order traversal of its nodes'
values. (i.e., from left to right, level by level from leaf to root).

Sol: 
1. Add root node to deq. While deq is not null,
2. Length of deq will be the length of level
3. keep popping the left node in deq and add to the level array.
4. after each level append the level array to the left of output deq.
5. once deq is empty, return output deq.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return None
        deq = deque([root, ]);
        output = deque([]);
        while deq:
            level_arr = []
            levelLen = len(deq)
            for i in range(0, levelLen):
                node = deq.popleft();
                level_arr.append(node.val)
                if node.left is not None:
                    deq.append(node.left)
                if node.right is not None:
                    deq.append(node.right)

            output.appendleft(level_arr);

        return output;