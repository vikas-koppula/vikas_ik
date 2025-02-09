"""
905. Sort Array By Parity
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:
Input: nums = [0]
Output: [0]
"""
from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        od, ev = 0, 0
        for od in range(0, len(nums)):
            if nums[od] % 2 == 0:
                nums[ev], nums[od] = nums[od], nums[ev]
                ev += 1
        return nums


sol = Solution()
print("----------------------")
test_arr = [1, 2, 3, 4]
print(test_arr)
print('Sorted:', sol.sortArrayByParity(test_arr))
print("----------------------")
test_arr = [2, 3, 4, 5]
print(test_arr)
print('Sorted:', sol.sortArrayByParity(test_arr))
print("----------------------")
test_arr = [0]
print(test_arr)
print('Sorted:', sol.sortArrayByParity(test_arr))
