"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Sol:
1) Add first element from every list to the heap along with the index using for loop
2) Create a while loop to execute while the len(heap) != 0
3) Within the while loop keep popping the min element and add it to the result linked list
4) adjust the pointer of the added LL to the next node
5) add the next node from the popped LL to the heap
6) return the head of output LL
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        minHeap = []
        k = len(lists)
        for l in range(k):
            if lists[l] is not None:
                heapq.heappush(minHeap, (lists[l].val, i))
                # lists[l] = lists[l].next
        head = ListNode(0)
        result = head
        while len(minHeap) != 0:
            (val, index) = heapq.heappop(minHeap)
            result.next = lists[index]
            result = result.next
            lists[index] = lists[index].next
            if lists[index] is not None:
                heapq.heappush(minHeap, (lists[index].val, index))

        head = head.next
        return head


# Merge K sorted lists/arrays
# Using a dictionary to store the index/currentPointer of each sublist
def mergeSortedLists(lists):
    minHeap = []
    k = len(lists)
    dic = dict([])
    for i in range(k):
        if len(lists[i]) > 0:
            heapq.heappush(minHeap, (lists[i][0], i))
            dic[i] = 0

    result = []
    while len(minHeap) != 0:
        val, index = heapq.heappop(minHeap)
        result.append(lists[index][dic[index]])
        dic[index] += 1
        if len(lists[index]) > dic[index]:
            heapq.heappush(minHeap, (lists[index][dic[index]], index))

    return result


print(mergeSortedLists([[1, 5], [2, 4], [3, 6]]))
print(mergeSortedLists([[1, 5], [2, 4], []]))
print(mergeSortedLists([[1, 5], [1, 5], []]))
print(mergeSortedLists([[], [], []]))
