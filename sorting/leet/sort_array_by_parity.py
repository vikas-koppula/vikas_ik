"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Input: nums = [0]
Output: [0]
"""
from typing import List


def sort_array_by_parity(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    odd: int = 0
    even: int = 0
    while odd <= len(nums)-1:
        if nums[odd] % 2 == 0:
            # Swap even with odd
            nums[even], nums[odd] = nums[odd], nums[even]
            even += 1
        odd += 1
    return nums


test_arr = [1, 2, 3, 4]
print(test_arr)
print('Sorted:', sort_array_by_parity(test_arr))
test_arr = [2, 3, 4, 5]
print(test_arr)
print('Sorted:', sort_array_by_parity(test_arr))
test_arr = [0]
print(test_arr)
print('Sorted:', sort_array_by_parity(test_arr))
