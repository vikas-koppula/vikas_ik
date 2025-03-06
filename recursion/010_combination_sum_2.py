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

        # Count the number of adjacent duplicates
        def char_count(idx: int) -> int:
            count: int = 1
            next_idx = idx + 1
            while next_idx < len(nums) and nums[idx] == nums[next_idx]:
                count += 1
                next_idx += 1
            return count

        def helper(i: int, slate: List[int]):
            # Backtracking case
            if sum(slate) == target:
                result.append(slate[:])
                return

            # Sum exceed exit condition
            if sum(slate) > target:
                return

            # Leaf / Exit condition
            if i == len(nums):
                return

            # Get count of repetitions
            count: int = char_count(i)

            # Exclude condition
            # IMPORTANT: need to increment i by count and not just +1
            helper(i + count, slate)

            # Include based on char count
            for cnt in range(1, count + 1):
                # Needed to include once, twice and more, based on the number of duplicates. Includes depend on current value of cnt
                [slate.append(x) for x in cnt * [nums[i]]]
                # IMPORTANT: need to increment i by count and not cnt. Using cnt will result in duplicate sets
                helper(i + count, slate)
                # Pop once, twice and more, based on the number of duplicates
                [slate.pop() for _ in cnt * [nums[i]]]

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
print('\n.........Test_Case_3...........')
candidates = [5]
target = 5
print("candidates:", candidates)
print("target:", target)
print('Combination Sum: ', sol.combinationSum2(candidates, target))
