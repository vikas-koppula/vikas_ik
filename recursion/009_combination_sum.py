"""
39. Combination Sum
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of,
candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency
of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less than 150
combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result: List[List[int]] = list()

        def helper(arr: List[int], i: int, slate: List[int]):
            # Backtracking case 1
            if sum(slate) == target:
                result.append(slate[:])
                return
            # Backtracking case 2
            if sum(slate) > target:
                return
            # Base/leaf case
            if i == len(candidates):
                return
            cnt = 1
            # Exclude
            helper(arr, i + 1, slate)
            # Include n times as long as sum(slate+ n appends) < target
            while True:
                [slate.append(x) for x in cnt*[arr[i]]]
                sum_slate = sum(slate)
                helper(arr, i+1, slate)
                [slate.pop() for _ in cnt * [arr[i]]]
                cnt += 1
                if sum_slate >= target:
                    break

        helper(candidates, 0, [])
        return result


sol = Solution()
print('\n.........Test_Case_1...........')
candidates = [2, 3, 6, 7]
target = 7
print("candidates:", candidates)
print("target:", target)
print('Combination Sum: ', sol.combinationSum(candidates, target))
