"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Write a function to recursively send right and left roots and compare the values.
Return true when right at left nodes reaches None values at the same time, Else return false
"""
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root.left, root.right)

    def isMirror(self, root1, root2):
        if root1 is None and root2 is None:
            return True;
        if root1 is not None and root2 is not None:
            if root1.val == root2.val:
                return (self.isMirror(root1.left, root2.right)) and (self.isMirror(root1.right, root2.left))
        return False

"""
Sol: Create a deque which stores both (root1,root2) values and pass root,root from the main function. 
In for loop keep popping left most values from queue and check if values root1.left and root2.right are not None. 
if either of them is None return False. similarly compare root1.right & root2.left. 
At last compare root1.val and root2.val and return False if both are not equal.
"""
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isMirror(root, root)

    def isMirror(self, root1, root2):
        deq = deque([(root1,root2)])
        while deq:
            levelLen = len(deq)
            for _ in range(0,levelLen):
                node1,node2 = deq.popleft()
                if node1.left is not None and node2.right is not None:
                    deq.append((node1.left,node2.right))
                elif node1.left is not None or node2.right is not None:
                    return False
                if node1.right is not None and node2.left is not None:
                    deq.append((node1.right,node2.left))
                elif node1.right is not None or node2.left is not None:
                    return False
                if node1.val != node2.val:
                    return False
        return True

