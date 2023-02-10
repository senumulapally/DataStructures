"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be
set to NULL. Initially, all next pointers are set to NULL.

Sol: Consider PrevNode as None before every for loop. Within the loop assign PrevNode.
Next as current Node and at the end of loop assign prevNode = Node. Return root.
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        deq = deque([root,])
        while deq:
            levelLen = len(deq)
            prevNode = None
            for _ in range(0,levelLen):
                node = deq.popleft()
                if node.left is not None:
                    deq.append(node.left)
                if node.right is not None:
                    deq.append(node.right)
                if prevNode is not None:
                    prevNode.next =  node
                prevNode = node
        return root

