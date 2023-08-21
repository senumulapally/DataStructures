"""Given the root of a binary tree, invert the tree, and return its root."""

"""Sol: Write a recursive function to swap the left and right nodes for root value and 
recursively call the function for left and right nodes until 'None' is reached."""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.recursive(root)
        return root

    def recursive(self, root):
        if root is None:
            return None

        root.left, root.right = root.right, root.left
        self.recursive(root.left)
        self.recursive(root.right)

