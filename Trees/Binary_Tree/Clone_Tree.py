"""
Given a binary tree(represented by its root not as usual), clone it and return the root of cloned tree.

Input:
One argument named root. denoting the root node of a tree

Output:
Return the root node of cloned tree

Sol:
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def clone_a_binary_tree(self, root):
        newRoot = TreeNode(node.val)
        deq = deque([root, newRoot])
        while deq:
            levelLen = len(deq)
            for _ in range(0,levelLen):
                node, newNode = deq.popleft()
                if node.left is not None:
                    newNode.left = TreeNode(node.left.val)
                    deq.append(node.left, newNode.left)
                if node.right is not None:
                    newNode.right = TreeNode(node.right.val)
                    deq.append(node.right, newNode.right)
        return newRoot

