"""
912. Sort an Array
Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest
space complexity possible.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3),
while the positions of other numbers are changed (for example, 1 and 5).

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
"""
import random


def quick_sort_impl(arr: list[int]):

    def helper(orig_arr: list[int], start_idx: int, end_idx: int) -> None:
        # Return if partition is empty (start idx or end idx chosen as pivot) or if partition has just one element
        if start_idx >= end_idx:
            return

        pivot_idx = random.randint(start_idx, end_idx)
        pivot = orig_arr[pivot_idx]
        # Swap the first element with the pivot element, thus the pivot is the first position
        orig_arr[start_idx], orig_arr[pivot_idx] = orig_arr[pivot_idx], orig_arr[start_idx]
        small: int = start_idx
        # Walk the big pointer from left to right, and create orange(small) and green(big) sections
        for big in range(start_idx+1, end_idx+1):
            if orig_arr[big] < pivot:
                # Move forward the small pointer. It will land on the big nums space
                small += 1
                # Swap the identified small num with the big num that the small idx landed on in the previous line
                orig_arr[small], orig_arr[big] = orig_arr[big], orig_arr[small]
        # Swap the pivot in the start idx with the last idx of the orange partition
        # Pivot is now in its correct and final sorted position
        orig_arr[start_idx], orig_arr[small] = orig_arr[small], orig_arr[start_idx]
        # Call helper recursive call on the orange(small) and green(big) sections
        helper(orig_arr, start_idx, small-1)
        helper(orig_arr, small+1, end_idx)

    helper(arr, 0, len(arr)-1)
    return arr

from typing import List, Set, Deque

class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        aux = [0] * len(nums)
        def helper(st: int, end:int):
            # Leaf condition. Return as is, dont do anything
            if st >= end:
                return
            # Determine the left and right arrays. Recursively call the helper on the left and right parts
            # Each helper will return with its index range sorted
            mid = (st + end) // 2
            helper(st, mid)
            helper(mid+1, end)
            # Copy the sorted left and right parts to the respective indexes of the aux array.
            aux[st: mid+1] = nums[st: mid+1]
            aux[mid+1: end+1] = nums[mid+1: end+1]
            # Merge starts now. 3 pointers are needed. One for the left, one for the right
            # and one that points to the orig array
            l = st
            orig = st
            r = mid+1
            # Merge the left and right parts to the orig array
            while l <= mid and r <= end:
                if aux[l] <= aux[r]:
                    nums[orig] = aux[l]
                    l+=1
                    orig+=1
                else:
                    nums[orig] = aux[r]
                    r+=1
                    orig+=1
            # Fill in the remaining slots of the original array with the remaining sorted items from the aux arrays
            while l <= mid:
                nums[orig] = aux[l]
                l+=1
                orig+=1
            while r <= end:
                nums[orig] = aux[r]
                r+=1
                orig+=1
        helper(0, len(nums)-1)
        return nums

nums_1 = [5, 2, 3, 1]
nums_2 = [5, 1, 1, 2, 0, 0]
sol = Solution()
print("Nums 1:", nums_1)
print("sol:", sol.sortArray(nums_1))

print("Nums 2:", nums_2)
print("sol:", sol.sortArray(nums_2))
