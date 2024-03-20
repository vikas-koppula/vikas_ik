"""
47. Permutations II
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order
Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
from typing import List, Set


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = list()

        def helper(arr:List[int], i:int, slate:List[int]) -> None:
            element_set: Set[int] = set()
            if i == len(arr):
                result.append(slate[:])
                return
            for tmp in range(i, len(arr)):
                if arr[tmp] in element_set:
                    continue
                else:
                    element_set.add(arr[tmp])
                arr[i], arr[tmp] = arr[tmp], arr[i]
                slate.append(arr[i])
                helper(arr, i+1, slate)
                slate.pop()
                arr[i], arr[tmp] = arr[tmp], arr[i]

        helper(nums, 0, [])
        return result


sol = Solution()

print('.........Test_Case_1...........')
nums = [1,1,2]
print("nums:", nums)
print('Permutations:\n', sol.permuteUnique(nums))
print('.........Test_Case_2...........')
nums = [1,2,3]
print("nums:", nums)
print('Permutations:\n', sol.permuteUnique(nums))
