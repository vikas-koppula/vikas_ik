"""
703. Kth Largest Element in a Stream
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Implement KthLargest class:
-   KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
-   int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element
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
"""
import heapq
class KthLargest(object):
    def __init__(self, k, nums):
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap)

        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

    def __add__(self, val) -> int:
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap, val)
            return self.minheap[0]
        elif val <= self.minheap[0]:
            return self.minheap[0]
        else:
            heapq.heappush(self.minheap, val)
            heapq.heappop(self.minheap)
            return self.minheap[0]
