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
        if list1 is None and list2 is None:
            return None
        if list1 is None and list2 is not None:
            return list2
        if list2 is None and list1 is not None:
            return list1

        sortedNode = ListNode()
        if list1.val <= list2.val:
            sortedNode = list1
            list1 = list1.next
        else:
            sortedNode = list2
            list2 = list2.next
        HeadNode = sortedNode

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                sortedNode.next = list1
                list1 = list1.next
            else:
                sortedNode.next = list2
                list2 = list2.next

            sortedNode = sortedNode.next

        if list1 is None:
            sortedNode.next = list2
        else:
            sortedNode.next = list1

        return HeadNode


obj1 = Solution()
# Create list before calling the method with lists
# Else, this code doesn't work
assert obj1.mergeTwoLists([1, 2, 4], [1, 3, 4]) == [1, 1, 2, 3, 4, 4]
assert obj1.mergeTwoLists([], []) == []
assert obj1.mergeTwoLists([], [0]) == [0]
