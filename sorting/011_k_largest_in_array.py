"""
215.Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_idx = len(nums) - k

        def helper(nums: List[int], st: int, end:int, k: int):
            # if st >= end:
            #     return None
            # Random select the pivot p_idx 12 is a problem
            p_idx = random.randint(st, end)
            pivot = nums[p_idx]
            # Set the l and curr to the start of the array. Will walk to the right
            l, curr = st, st
            # Set r to the end of the array. Will walk to the left
            r = end
            # Let curr walk to the right, swap as needed, increment and decrement l, curr and r as needed. (sort colors)
            while curr <= r:
                if nums[curr] < pivot:
                    nums[curr], nums[l] = nums[l], nums[curr]
                    curr += 1
                    l += 1
                elif nums[curr] > pivot:
                    nums[curr], nums[r] = nums[r], nums[curr]
                    r -= 1
                else:
                    curr += 1
            # If target_idx is to the right of the pivot wall, then recurse on the segment right of the pivot wall
            if target_idx >= r+1:
                return helper(nums, r+1, end, k)
            # If target_idx is to the left of the pivot wall, then recurse on the segment left of the pivot wall
            elif target_idx <= l-1:
                return helper(nums, st, l-1, k)
            # If target_idx is in range of the pivot wall, then return the pivot as the required value
            # l and r mark the left and right most points of the pivot wall
            elif target_idx in range(l, r+1):
                return nums[l]
        ans: int = helper(nums, 0, len(nums)-1, k)
        return ans


sol = Solution()
print("Quick Select")
print("----------------------")
nums_1 = [3,2,1,5,6,4]
k = 2
print("nums_1:", nums_1)
print("sorted nums_1:", sorted(nums_1))
print("k:", k)
print("Ans:", sol.findKthLargest(nums_1, k))
print("----------------------")
nums_2 = [3,2,3,1,2,4,5,5,6]
k = 4
print("nums_2:", nums_2)
print("sorted nums_2:", sorted(nums_2))
print("k:", k)
print("Ans:", sol.findKthLargest(nums_2, k))
print("----------------------")
#nums_3 = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
nums_3 = [7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
k = 1
print("nums_3:", nums_3)
print("sorted nums_3:", sorted(nums_3))
print("k:", k)
print("Ans:", sol.findKthLargest(nums_3, k))
print("----------------------")
nums_4 = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
k = 2
print("nums_4:", nums_4)
print("sorted nums_4:", sorted(nums_4))
print("k:", k)
print("Ans:", sol.findKthLargest(nums_4, k))
