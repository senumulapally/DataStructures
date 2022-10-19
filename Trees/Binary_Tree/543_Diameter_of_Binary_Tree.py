"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
"""

"""
Sol: Consider recursive dfs  Post order traversal as it starts from the bottom. 
Return the height (Max of left,right heights of nod) & diameter(Max of L_R heights, previous max diameter) at each node.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.getDiameter(root, 0)[1]

    def getDiameter(self, root, diameter):
        if root is None:
            return 0, diameter

        LHeight, diameter = self.getDiameter(root.left, diameter)
        RHeight, diameter = self.getDiameter(root.right, diameter)

        maxDia = LHeight + RHeight
        diameter = max(diameter, maxDia)

        return max(LHeight, RHeight) + 1, diameter;