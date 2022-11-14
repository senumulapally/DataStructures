"""
Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

sol:
write a pre-order traversal recursive function to add the sum whenever a left leaf is encountered.

Cases:
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Input: root = [1]
Output: 0
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.leftSum(root,0)

    def leftSum(self, root, sumL):
        if root is None:
            return sumL

        if root.left and root.left.left is None and root.left.right is None:
            sumL = sumL + root.left.val

        sumL = self.leftSum(root.right, sumL)
        sumL = self.leftSum(root.left, sumL)
        return sumL