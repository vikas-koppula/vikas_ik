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

        def num_char_count(arr: List[int], idx: int):
            next_idx = idx + 1
            while next_idx < len(arr) and arr[idx] == arr[next_idx]:
                next_idx += 1
            return next_idx - idx

        def helper(arr: List[int], i: int, slate: List[int]):
            # Backtracking Case 1
            slate_sum = sum(slate)
            if slate_sum == target:
                result.append(slate[:])
                return
            # Backtracking Case 2
            elif slate_sum > target:
                return
            # Base case: This is needed without which recursion goes to infinity, because of all exclude cases
            if i == len(nums):
                return

            # Rest follows as is from subsets 2 problem
            char_count = num_char_count(nums, i)

            # Exclusion
            helper(arr, i + char_count, slate)

            # Inclusion from 1 to num of dup chars. Eg: 1,2,2,3. Will need case for one 2 and two 2s
            for cnt in range(1, char_count + 1):
                # slate = slate + (cnt*arr[i])
                [slate.append(x) for x in cnt * [arr[i]]]
                helper(arr, i + char_count, slate)
                # [slate.pop() for _ in range(1, cnt+1)]
                [slate.pop() for _ in cnt * [arr[i]]]

        helper(nums, 0, [])
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
