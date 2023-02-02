"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Sol: Write a recursive function to calculate depths. Here, we need to return the min depth amon left and right depths.
But when Left or Right depth is 1 we need to return max among left and right depths.

2/1/2023
Sol2: similar to level order traversal, but return the level first time you encounter a leaf node.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        left = 1 + self.minDepth(root.left)
        right = 1 + self.minDepth(root.right)

        if left == 1 or right == 1:
            depth = max(left, right)
        else:
            depth = min(left, right)

        return depth

### OR

    def minDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        deq = deque([root,])
        level = 0
        while deq:
            levelLen = len(deq)
            level += 1
            for _ in range(0,levelLen):
                node = deq.popleft()
                if node.left is not None:
                    deq.append(node.left)
                if node.right is not None:
                    deq.append(node.right)
                if node.left is None and node.right is None:
                    return level
