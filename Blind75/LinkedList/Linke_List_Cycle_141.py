"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again
by continuously following the next pointer. Internally, pos is used to denote the index of the node that
tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Brute Force: Consider map and keep adding addresses of lnode to the map.
if the address already exists, return False. If the end of node is obtained, return True
We can append address using id(node)

Actual Sol:
Consider two pointers, slow and fast
slow take one step at a time, while fast takes two
keep comparing slow and fast. return true when slow == false
if end of list is reached, return true (i.e, when fast is none or fast.next is None)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Actual Sol:

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow = fast = head
        while fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
            elif not fast:
                return False
        return False

#Brute force: Takes extra space
class Sol(object):
    def hasCycle(self, head):
        map = []
        p = head
        while p:
            if id(p) not in map:
                map.append(id(p))
            else:
                return True
            p = p.next
        return False



