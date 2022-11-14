"""
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.

sol: Similar to Pre-order traversal. But keep adding root.val to a string and append it to an aray at leaf node.

cases:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Input: root = [1]
Output: ["1"]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        return self.treePaths(root, paths, "")

    def treePaths(self, root, paths, currPath):
        if root is None:
            return None

        currPath = currPath + str(root.val)
        if root.left is None and root.right is None:
            paths.append(currPath)
            return paths

        currPath = currPath + "->"
        left = self.treePaths(root.left, paths, currPath)
        right = self.treePaths(root.right, paths, currPath)

        return paths
