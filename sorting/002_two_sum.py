# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two nums such that they add up to target
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
from typing import List, Tuple

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Transform to tuple as we need to maintain the original positions of the elements
        nums_tuple = [(x,i) for i,x in enumerate(nums, 0)]
        sorted_tuple = sorted(nums_tuple, key=lambda x:x[0])
        l = 0
        r = len(nums)-1
        # Exit while loop if both the left and right index arrive at the same item in the array
        while l < r:
            if sorted_tuple[l][0] + sorted_tuple[r][0] == target:
                return [sorted_tuple[l][1], sorted_tuple[r][1]]
            elif sorted_tuple[l][0] + sorted_tuple[r][0] < target:
                l+=1
            elif sorted_tuple[l][0] + sorted_tuple[r][0] > target:
                r-=1
        # Return null array as the target hasnt been found
        return []


nums_1 = [2, 7, 11, 15]
target = 9
sol = Solution()
print("Nums 1:", nums_1)
print("sol:", sol.twoSum(nums_1, target))
