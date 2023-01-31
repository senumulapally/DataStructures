"""
Given the root of a binary search tree (BST) with duplicates, return all the mode(s)
(i.e., the most frequently occurred element) in it.
If the tree has more than one mode, return them in any order.
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

Sol:
 """

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

##Not working##

class Solution(object):
    modeNums = list()

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        modeNums = []
        prevNum = None
        maxCount = 0
        count = 1
        return self.modeNum(root, prevNum, maxCount, count, modeNums)

    def modeNum(self, node, prevNum, maxCount, count, modeNums):
        if node == None:
            return
        self.modeNum(node.left, prevNum, maxCount, count, modeNums)

        if prevNum != None:
            if prevNum == node.val:
                count += 1
            else:
                count = 1

        if count > maxCount:
            maxCount = count
            modeNums = []
            modeNums.append(node.val)
        elif count == maxCount:
            modeNums.append(node.val)
        prevNum = node.val
        self.modeNum(node.right, prevNum, maxCount, count, modeNums)
        return modeNums
