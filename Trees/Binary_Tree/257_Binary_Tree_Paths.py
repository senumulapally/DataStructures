"""
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.

DFS sol: Similar to Pre-order traversal. But keep adding root.val to a string and append it to an aray at leaf node.
BFS sol:


cases:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Input: root = [1]
Output: ["1"]
"""
import CreateBinaryTree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1(object):
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
        self.treePaths(root.left, paths, currPath)
        self.treePaths(root.right, paths, currPath)

        return paths


# BFS - returning list of paths

class Solution2(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return None
        deq = deque([(root, []), ]);
        output = deque([]);
        while deq:
            node, slate = deq.popleft();
            slate = slate + [node];
            if node.left is not None:
                deq.append(node.left, slate)
            if node.right is not None:
                deq.append(node.right, slate)
            if node.left is None and node.right is None:
                output.append(slate);

        return output;




# DFS- 2 - returning list of paths

class Solution3(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        output = []
        return self.dfs(root, output, [])

    def dfs(self, node, output, slate):
        if node is None:
            return None
        slate.append(node.val)
        if node.left is None and node.right is None:
            output.append(slate.copy());
        if node.left is not None:
            self.dfs(node.left, output, slate)
        if node.right is not None:
            self.dfs(node.right,output, slate)
        slate.pop()
        return output;


bst = CreateBinaryTree.createBinarySearchTree()

# Inserting elements manually
bst.manual_insert(50, None)  # Root node
# print(bst.display())
bst.manual_insert(30, 50, True)  # Insert 30 as the left child of 50
# print(bst.display())
bst.manual_insert(20, 30, True)  # Insert 20 as the left child of 30
# bst.display()
bst.manual_insert(40, 30, False)  # Insert 40 as the right child of 30
bst.manual_insert(70, 50, False)  # Insert 70 as the right child of 50
bst.manual_insert(23, 70, False)
bst.manual_insert(81, 70, True)
root = bst.getRoot()

obj = Solution3()
print(obj.binaryTreePaths(root))