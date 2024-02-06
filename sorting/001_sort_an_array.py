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
        # print('pivot_idx:', pivot_idx)
        # print('pivot:', pivot)
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


def merge_sort_impl(arr: list[int]):
    aux_arr = [0] * len(arr)

    def helper(st: int, end: int):
        # Leaf condition. Return as is, dont do anything
        if st >= end:
            return

        mid = (st + end) // 2
        helper(st, mid)
        helper(mid+1, end)
        # Merge part starts now after the two halves were sorted by their managers.
        # Copy the left part to the aux array. Copy to the correct positions in the aux array
        aux_arr[st: mid+1] = arr[st: mid+1]
        # Copy the right part to the aux array. Copy to the correct positions in the aux array
        aux_arr[mid+1: end+1] = arr[mid+1: end+1]
        left_idx = st
        right_idx = mid+1
        orig_idx = st
        while left_idx <= mid and right_idx <= end:
            if aux_arr[left_idx] <= aux_arr[right_idx]:
                arr[orig_idx] = aux_arr[left_idx]
                left_idx += 1
                orig_idx += 1
            else:
                arr[orig_idx] = aux_arr[right_idx]
                right_idx += 1
                orig_idx += 1
        # Important copy remaining to the orig array. Now when you compare you need to use < and not <=
        while left_idx <= mid:
            arr[orig_idx] = aux_arr[left_idx]
            left_idx += 1
            orig_idx += 1
        while right_idx <= end:
            arr[orig_idx] = aux_arr[right_idx]
            right_idx += 1
            orig_idx += 1

    helper(0, len(arr)-1 )
    return arr


nums_1 = [5, 2, 3, 1]
nums_2 = [5, 1, 1, 2, 0, 0]
# print("Quick Sort")
# print("----------------------")
# print("nums_1:", nums_1)
# print("sorted nums_1:", quick_sort_impl(nums_1))
# print("nums_2:", nums_2)
# print("sorted nums_2:", quick_sort_impl(nums_2))

print("Merge Sort")
print("----------------------")
print("nums_1:", nums_1)
print("sorted nums_1:", merge_sort_impl(nums_1))
print("nums_2:", nums_2)
print("sorted nums_2:", merge_sort_impl(nums_2))