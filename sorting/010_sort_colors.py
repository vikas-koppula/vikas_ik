"""
75. Sort Colors
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color
are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
"""
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> List[int]:
        pivot = 1
        # l are nums less than the pivot which here is the number 1. L will start at beginning of the array
        l: int = 0
        # curr are nums equal to the pivot. curr will start at beginning of the array
        curr: int = 0
        # y are nums greater than the pivot. R will move to the left from the last position in the array.
        r: int = len(nums) - 1
        # Curr walks to the right (just like big) and ends the loop when, it crosses the r index
        # if curr < pivot, swap curr and l and then move curr and l indexes to the right
        # if curr > pivot, swap curr and r and then only move r to the left
        # if curr == pivot, move the curr index to the right. No swap here.
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
        return nums

sol = Solution()
print("----------------------")
nums = [2,0,2,1,1,0]
print("nums:", nums)
print('Sorted:', sol.sortColors(nums))
print("----------------------")
nums = [2,0,1]
print("nums:", nums)
print('Sorted:', sol.sortColors(nums))
print("----------------------")
