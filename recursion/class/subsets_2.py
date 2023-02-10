"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Input: nums = [0]
Output: [[],[0]]
Input: nums =[4,4,4,1,4]
Output: [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
"""
from typing import List


def subsets_2(orig_nums: List[int]) -> List[List[int]]:
    result: List[List[int]] = list()
    nums = sorted(orig_nums)

    def num_char_count(arr: List[int], idx: int):
        next_idx = idx + 1
        while next_idx < len(arr) and arr[idx] == arr[next_idx]:
            next_idx += 1
        return next_idx - idx

    def helper(arr: List[int], i: int, slate: List[int]):
        if i == len(nums):
            result.append(slate[:])
            return

        char_count = num_char_count(nums, i)

        # Exclusion
        helper(arr, i+char_count, slate)

        # Inclusion from 1 to num of dup chars. Eg: 1,2,2,3. Will need case for one 2 and two 2s
        for cnt in range(1, char_count+1):
            # slate = slate + (cnt*arr[i])
            [slate.append(x) for x in cnt*[arr[i]]]
            helper(arr, i + char_count, slate)
            # [slate.pop() for _ in range(1, cnt+1)]
            [slate.pop() for _ in cnt*[arr[i]]]
        char_count = num_char_count(nums, i)
    helper(nums, 0, [])
    return result


test = [1, 2, 2]
print('Answer:', subsets_2(test))
