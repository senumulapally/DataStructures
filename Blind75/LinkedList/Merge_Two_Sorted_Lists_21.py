"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing
together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Sol:
1) Consider two pointers head and sorted.
Head will hold the start point of merged lists
and sorted will point the last node of sorted list and keeps updating in each loop
2) if l1<=l2: sorted.next will be l1 and move sorted to next
3) if l2<l1: sorted.next will be l2 and move sorted to next
4) if any of l1 or l2 is remaining, assign it to sorted.next and return the head

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        head = ListNode()
        sorted = head
        while list1 and list2:
            if list1.val <= list2.val:
                sorted.next = list1
                list1 = list1.next
            else:
                sorted.next = list2
                list2 = list2.next
            sorted = sorted.next

        if list2:
            sorted.next = list2
        elif list1:
            sorted.next = list1

        return head.next

