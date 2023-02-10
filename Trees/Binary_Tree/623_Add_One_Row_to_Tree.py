"""
Given the root of a binary tree and two integers val and depth, add a row of nodes with value
val at the given depth depth. Note that the root node is at depth 1.

The adding rule is:
Given the integer depth, for each not null tree node cur at the depth depth - 1,
create two tree nodes with value val as cur's left subtree root and right subtree root.
cur's original left subtree should be the left subtree of the new left subtree root.
cur's original right subtree should be the right subtree of the new right subtree root.
If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with
value val as the new root of the whole original tree, and the original tree is the new root's left subtree.

Sol: If depth is 1, create a new root with given value and assign the current root as it's left node.
Else, whenever depth is -1 store lft and roght nodes, and create new left and right nodes with given values,
and assign previous left/right nodes to newly created nodes.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def addOneRow(self, root, val, depth):
        """
                :type root: TreeNode
                :type val: int
                :type depth: int
                :rtype: TreeNode
                """
        if depth == 1:
            rootRef = root
            root = TreeNode(val)
            root.left = rootRef

        deq = deque([root, ])
        level = 0
        while deq:
            levelLen = len(deq)
            level += 1
            # prevNode = None
            for _ in range(0, levelLen):
                node = deq.popleft()
                if node.left is not None:
                    deq.append(node.left)
                if node.right is not None:
                    deq.append(node.right)
                if depth - 1 == level:
                    nodeLeft = node.left
                    nodeRight = node.right
                    node.left = TreeNode(val)
                    node.right = TreeNode(val)
                    node.left.left = nodeLeft
                    node.right.right = nodeRight
        return root
