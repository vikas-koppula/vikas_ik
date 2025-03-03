"""
40. Combination Sum II
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in
candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[ [1,1,6], [1,2,5], [1,7], [2,6] ]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output:
[ [1,2,2], [5] ]
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result: List[List[int]] = list()
        nums = sorted(candidates)
        def helper(i: int, slate: List[int]):
            # Leaf / Exit condition
            if i == len(nums):
                return
            # Sum exceed exit condition
            if sum(slate) > target:
                return
            # Backtracking case
            if sum(slate) == target:
                result.append(slate[:])
                return
            # Exclude
            helper(i + 1, slate)
            # Include
            slate.append(nums[i])
            helper(i+1, slate)
            slate.pop()

        helper(0, [])
        return result


sol = Solution()
print('\n.........Test_Case_1...........')
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print("candidates:", candidates)
print("target:", target)
print('Combination Sum: ', sol.combinationSum2(candidates, target))

print('\n.........Test_Case_2...........')
candidates = [2, 5, 2, 1, 2]
target = 5
print("candidates:", candidates)
print("target:", target)
print('Combination Sum: ', sol.combinationSum2(candidates, target))
