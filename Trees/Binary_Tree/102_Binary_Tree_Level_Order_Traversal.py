# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
example testcases:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        deq = deque([root,])
        output = []
        level = 0
        while deq:
            level_len = len(deq)
            level_arr= []
            node = root
            for i in range(0,level_len):
                node = deq.popleft()
                if node.left:
                    deq.append(node.left.val)
                    level_arr.append(node.left.val)
                if node.right:
                    deq.append(node.right.val)
                    level_arr.append(node.right.val)
            













