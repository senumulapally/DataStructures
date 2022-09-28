# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
In recursive function DFS, If the root node has left node, the dfs method is called with left
node as root node and similarly is the case with right node.
As we are writing the code for Inorder traversal, the root value is appended to output
in between left and right node recursive calls
"""
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        return self.dfs(root, output)

    def dfs(self, root, output):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return None
        self.dfs(root.left, output)
        output.append(root.val)
        self.dfs(root.right, output)
        return output