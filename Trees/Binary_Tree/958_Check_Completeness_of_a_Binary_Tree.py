"""
Given the root of a binary tree, determine if it is a complete binary tree.
In a complete binary tree, every level, except possibly the last, is completely filled,
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes
inclusive at the last level h.

Sol1: add id of the node to the deque as well like [(root,1)] (ids are 1,2,3,4 numbering of nodes starting from 1).
left node's ID will be (2*id) and right nodes id will be (2*id + 1). and check at the beginning of the for loop after
popping the node, if the expectedDI is equal to ID of node (If yes, increment expectedID). Else, return False.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



#Sol1
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        deq = deque([(root,1)])
        expectedId = 1
        while deq:
            levelLen = len(deq)
            for _ in range(0,levelLen):
                node,id = deq.popleft()
                if id == expectedId:
                    expectedId += 1
                else:
                    return False
                if node.left is not None:
                    deq.append((node.left, 2*id))
                if node.right is not None:
                    deq.append((node.right, 2*id + 1))

        return True

#Sol2

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        deq = deque([root,])
        flag = True
        while deq:
            levelLen = len(deq)
            for _ in range(0,levelLen):
                node = deq.popleft()
                if node.left is not None or node.right is not None:
                    if flag == False:
                        return False
                if node.left is not None:
                    deq.append(node.left)
                else:
                    flag = False
                if node.right is not None:
                    deq.append(node.right)
                    if flag == False:
                        return False
                else:
                    flag = False
        return True