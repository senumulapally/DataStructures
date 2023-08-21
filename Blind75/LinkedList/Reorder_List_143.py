"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Sol:
1) Find the mid-point and reverse the next half of list.
2) Then insert list2 into list2 alternatively
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head
        list1 = head
        list2 = self.findMidPoint(head)
        while list1.next and list2.next:
            temp1 = list1.next
            list1.next = list2
            list2 = list2.next
            list1.next.next = temp1
            list1 = list1.next.next
        if list2:
            list1.next = list2


    def findMidPoint(self, head):
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            if fast.next:
                fast = fast.next.next
        prev.next = None
        return self.reverseList(slow)

    def reverseList(self, head):
        curr = headclass Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head
        list1 = head
        list2 = self.findMidPoint(head)
        while list1.next and list2.next:
            temp1 = list1.next
            list1.next = list2
            list2 = list2.next
            list1.next.next = temp1
            list1 = list1.next.next
        if list2:
            list1.next = list2


    def findMidPoint(self, head):
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            if fast.next:
                fast = fast.next.next
        prev.next = None
        return self.reverseList(slow)

    def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev



