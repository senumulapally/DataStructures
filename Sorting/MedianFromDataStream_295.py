"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value,
 and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:
MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far.
Answers within 10**-5 of the actual answer will be accepted.

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0


Sol: Create two separate heaps,
One max heap for the first half numbers, so that the max element is stored at the top.
One min heap for the second half numbers, so that the min element is stored at the top.
When we have even number of elements: Median will the avg of two top elements of both the heaps
When we have odd No of elements: Median will be the top element of the heap which have len more than the other heap by 1

Adding the elements: Whenever an element greater than median comes, add it to the min heap
Whenever an element less than median comes, add it to the max heap

When we get two consecutive elements which are greater than median, while adding the second element to min heap,
We need to pop the top element from min heap and add to the max heap. Vice versa with the min heap.

At all times we need to make sure that it is either len(minHeap) == len(maxHeap)
or either of the length is greater than the other by one
"""

import heapq


class MedianFinder(object):

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.median = 0.0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num <= self.median:
            # Insert value into max heap
            heapq.heappush(self.maxHeap, -num)
            # Re-balancing the heaps. If maxHeap has 2 nums more than minHeap,
            # pop from maxHeap and insert it in minHeap to re-balance
            if len(self.maxHeap) - len(self.minHeap) == 2:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        else:
            # Insert value into min heap
            heapq.heappush(self.minHeap, num)
            # Re-balancing the heaps. If minHeap has 2 nums more than maxHeap,
            # pop from minHeap and insert it in maxHeap to re-balance
            if len(self.minHeap) - len(self.maxHeap) == 2:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

        self.findMedian();

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxHeap) < len(self.minHeap):
            self.median = self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            self.median = - self.maxHeap[0]
        else:  # Both are of same length median will be the avg of both top elements
            self.median = (- self.maxHeap[0] + self.minHeap[0]) / 2.0
        return self.median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
