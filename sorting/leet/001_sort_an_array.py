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


    def helper(orig_arr: list[int], start_idx: int, end_idx: int):
        pivot_idx = random.randint(start_idx, end_idx)
        pivot = orig_arr[pivot_idx]
        orig_arr[start_idx], orig_arr[pivot_idx] = orig_arr[pivot_idx], orig_arr[start_idx]
        small: int = pivot_idx
        for big in range(start_idx+1, end_idx+1):
            if orig_arr[big] < pivot:
                small+=1
                orig_arr[small], orig_arr[big] = orig_arr[big], orig_arr[small]
            else:
                big+=1
        orig_arr[start_idx], orig_arr[small] = orig_arr[small], orig_arr[start_idx]

        helper(orig_arr, start_idx, small-1)
        helper(orig_arr, small+1, end_idx)

    helper(arr, 0, len(arr)-1)
    return arr



nums = [5,2,3,1]
print("quick sort", )