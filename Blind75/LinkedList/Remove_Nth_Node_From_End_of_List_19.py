"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Brute Force Sol:
Create a dummy node and assign it's next value as head - (this will be useful when there is only 1 node in the list).
Write a separate function to find the length of list.
Find the node which is before the node that needs to be deleted. node = length - n.
Loop again and Stop at that node, assign p.next = p.next.next - this will eliminate the middle node.

Solution within one pass:
Create a dummy node (root) and assign it's next value as head.
Consider two pointers, slow and fast with initially pointing at root.
keep iterating fast until you reach nth node, then start iterating slow pointer from the head.
At this point, slow pointer with be at the node, before the node which needs to be deleted.
assign slow.next = slow.next.next and return root.next
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        length = self.findLength(root)
        node = length - n
        count = 0
        root = ListNode()
        root.next = head
        p = root
        while count < node:
            p = p.next
            count += 1
        p.next = p.next.next
        return root.next

    def findLength(self, head):
        p = head
        count = 0
        while p:
            count += 1
            p = p.next
        return count


# One Pass Solution:
class sol(object):
    def removeNthFromEnd(self, head, n):
        if not head:
            return None
        root = ListNode("sentinal", head)
        count = 1
        slow = root
        fast = root
        while fast.next:
            fast = fast.next
            if count > n:
                slow = slow.next
            count += 1
        slow.next = slow.next.next
        return root.next

