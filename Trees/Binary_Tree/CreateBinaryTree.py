from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class createBinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if data < node.val:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(data, node.right)

    def search(self, data):
        return self.traversal(data, self.root)

    def traversal(self, data, node):
        if node is None or node.val == data:
            return node
        result = self.traversal(data, node.left)
        if result is None:  # If not found in the left subtree, search the right subtree
            result = self.traversal(data, node.right)
        return result


    def manual_insert(self, data, parent, isLeft=False):
        if parent is None:
            self.root = TreeNode(data)
        else:
            node = self.search(parent)
            if isLeft:
                node.left = TreeNode(data)
            else:
                node.right = TreeNode(data)

    def display(self):
        if self.root is None:
            return None
        deq = deque([self.root])
        output = []

        while deq:
            levelLen = len(deq)
            for i in range(0, levelLen):
                node = deq.popleft()
                output.append(node.val)
                if node.left is not None:
                    deq.append(node.left)
                if node.right is not None:
                    deq.append(node.right)

        return output


##################################################################################################################

bst = createBinarySearchTree()

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
bst.manual_insert(None, 70, True)
print(bst.display())
