# Given an array of integers nums and an integer target, return indices of the two nums such that they add up to target
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
from typing import List, Tuple


def twoSum(nums: List[int], target: int) -> List[int]:
    new_nums: List[Tuple[int, int]] = list()
    for i in range(0, len(nums)):
        new_nums.append((nums[i], i))
    sorted_new_nums = sorted(new_nums, key=lambda x: x[0])
    left: int = 0
    right: int = len(nums)-1
    while left < right:
        if sorted_new_nums[left][0] + sorted_new_nums[right][0] == target:
            return [sorted_new_nums[left][1], sorted_new_nums[right][1]]
        elif sorted_new_nums[left][0] + sorted_new_nums[right][0] > target:
            right -= 1
        elif sorted_new_nums[left][0] + sorted_new_nums[right][0] < target:
            left += 1
    return []


nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))
