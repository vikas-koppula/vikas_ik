"""
46. Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:
Input: nums = [1]
Output: [[1]]
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = list()

        def helper(arr: List[int], i:int, slate: List[int]) -> None:
            # Base case: Leaf node. One permutation reached
            if i == len(arr):
                result.append(slate[:])
                return
            # Loop is used to iterate through the possible elements that can be placed at the position i
            for tmp in range(i, len(arr)):
                # Swap i and tmp to set the tmp element at i
                arr[i], arr[tmp] = arr[tmp], arr[i]
                # IMPORTANT: Need to append using i and not tmp. Appending using tmp will lead to dups due to the swap
                slate.append(arr[i])
                helper(arr, i+1, slate)
                slate.pop()
                arr[i], arr[tmp] = arr[tmp], arr[i]

        helper(nums, 0, [])
        return result

    # Dont use array copy based solution
    def permute_no_swap(self, input_arr: list):

        result: List[List[int]] = list()

        def helper(arr: list, slate: List[int]):
            if len(slate) == len(input_arr) or len(arr) == 0:
                result.append(slate[:])
                return
            for i in range(0, len(arr)):
                slate.append(arr[i])
                helper(arr[0:i] + arr[i+1:len(arr)], slate)
                slate.pop()

        helper(input_arr, [])
        return result


sol = Solution()

print('.........Test_Case_1...........')
nums = [1, 2, 3]
print("nums:", nums)
print('Permutations:\n', sol.permute(nums))
print('.........Test_Case_2...........')
nums = [0, 1]
print("nums:", nums)
print('Permutations:\n', sol.permute(nums))
print('.........Test_Case_3...........')
nums = [1]
print("nums:", nums)
print('Permutations:\n', sol.permute(nums))
print('.........Test_Case_4...........')
nums = []
print("nums:", nums)
print('Permutations:\n', sol.permute(nums))
