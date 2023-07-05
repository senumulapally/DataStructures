"""Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted
order, not the kth distinct element.

Implement KthLargest class:
KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element
in the stream.

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8


Sol: We are using minHeap in this problem.
 Loop the nums and keep adding elements to the heap until the size reached k.
Once the size is reached k, execute heappushpop() to pop the min element and insert new element

In the add method, check if the max size of k is reached,
if not:  push the element to the heap else: push pop the element
at the end heap will be of size k with k large elements and minimum of those k elements will be at [0].
So return the arr[0]

Note: for max heap use heapq._heapify_max()
for popping from maxheap -> heapq._heappop_max(maxheap)
"""

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.array = []
        self.maxSize = k
        for num in nums:
            if len(self.array) != self.maxSize:
                heapq.heappush(self.array, num)
            elif len(self.array) == self.maxSize:
                heapq.heappushpop(self.array, num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.array) != self.maxSize:
            heapq.heappush(self.array, val)
        elif len(self.array) == self.maxSize:
            heapq.heappushpop(self.array, val)
        return self.array[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)