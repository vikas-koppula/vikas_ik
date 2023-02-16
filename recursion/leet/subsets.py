"""
Given an integer array nums of unique elements, return all possible  subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Input: nums = [0]
Output: [[],[0]]
"""
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result: List[List[int]] = list()

    def helper(nums: List[int], i: int, slate: List[int]):
        if i == len(nums):
            result.append(slate[:])
            return

        # Exclusion
        helper(nums, i + 1, slate)

        # Inclusion
        slate.append(nums[i])
        helper(nums, i+1, slate)
        slate.pop()

    helper(nums, 0, [])
    return result


test = [1, 2, 3]
print('Answer:', subsets(test))
