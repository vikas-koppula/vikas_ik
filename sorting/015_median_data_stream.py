"""
295. Find Median from Data Stream
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value,
and the median is the mean of the two middle values.
For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:
MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

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
"""
import heapq

class MedianFinder(object):
    def __init__(self):
        self.minHeap, self.maxHeap = [], []

    def addNum(self, num: int):
        # Check if the new val is <= to the max heap root. If yes, the place in the max heap, else in the min heap.
        # This means that if the maxheap is empty, then the element will be placed in the min heap by default
        if bool(self.maxHeap) and num <= -1 * self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -1 * num)
        else:
            heapq.heappush(self.minHeap, num)
        # Adding the val might have unbalanced the heaps. Need to make sure than the heaps are not bigger than each other by
        # one additional element
        if len(self.maxHeap) > len(self.minHeap) + 1:
            # Need to move an element from the maxheap to the min heap
            extra = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, extra)
        elif len(self.minHeap) > len(self.maxHeap) + 1:
            # Need to move an element from the minheap to the maxheap
            extra = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * extra)

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        else:
            return ((-1* self.maxHeap[0]) + self.minHeap[0]) / 2
