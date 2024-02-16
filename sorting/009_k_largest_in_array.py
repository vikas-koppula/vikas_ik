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
            #     return
            piv_idx = random.randint(st, end)
            piv = nums[piv_idx]
            # swap pivot with the first element of the array
            nums[st], nums[piv_idx] = nums[piv_idx], nums[st]
            sm:int = st
            for big in range(st+1, end+1):
                if nums[big] < piv:
                    sm += 1
                    nums[sm], nums[big] = nums[big], nums[sm]
            nums[st], nums[sm] = nums[sm], nums[st]

            # Pivot right now is on the sm index
            # Check if pivot is on the target position
            if sm == target_idx:
                return nums[sm]
            elif sm < target_idx:
                return helper(nums, sm + 1, end, k)
            elif sm > target_idx:
                return helper(nums, st, sm - 1, k - len(nums) - sm)

        ans: int = helper(nums, 0, len(nums)-1, k)
        return ans


nums = [3,2,1,5,6,4]
k = 2
sol = Solution()
print("Quick Select")
print("----------------------")
print("nums_1:", nums)
print("sorted nums_1:", sol.findKthLargest(nums, k))
