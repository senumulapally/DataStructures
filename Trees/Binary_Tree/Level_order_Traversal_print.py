"""print the values in the tree in level order

Sol: 
1) First add the root to the deque
2) keep popping the left most value from the deque 
3) and keep appending node.left and node.right values to the deq if not a leaf node.
4) run the while loop until the deq is empty
"""

## For printing in Level order
class Solution(object):
    def levelOrderPrint(self, root):
        deq = deque([root,])
        while deq:
            node = deq.popleft()
            print(node.val)
            if node.left is not None:
                deq.append(node.left)
            if node.right is not None:
                deq.append(node.right)


## For printing an array in Level order

class Solution(object):
    def levelOrderArray(self, root):
        deq = deque([root,])
        output = []
        while deq:
            node = deq.popleft()
            output.append(node.val)
            if node.left is not None:
                deq.append(node.left)
            if node.right is not None:
                deq.append(node.right)
        return output;