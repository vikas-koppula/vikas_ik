"""
90. Subsets II
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

# Subsets 2: Include and exclude. The order doesn't matter. No duplicate subsets. Include multiple times based on dups.
class Solution:
    def subsetsWithDup(self, orig_nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = list()
        # Sort is needed in order to count the adjacent duplicates
        nums = sorted(orig_nums)

        # Count the number of adjacent duplicates
        def char_count(idx: int) -> int:
            count: int = 1
            next_idx = idx + 1
            while next_idx < len(nums) and nums[idx] == nums[next_idx]:
                count += 1
                next_idx += 1
            return count

        def helper(i: int, slate: List[int]):
            # Exit condition
            if i == len(nums):
                result.append(slate[:])
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

print('.........Test_Case_1...........')
nums = [1, 2, 2]
print("nums:", nums)
print('Subsets 2:\n', sol.subsetsWithDup(nums))
print('.........Test_Case_2...........')
nums = [0]
print("nums:", nums)
print('Subsets 2:\n', sol.subsetsWithDup(nums))
print('.........Test_Case_3...........')
nums = [4, 4, 4, 1, 4]
print("nums:", nums)
print('Subsets 2:\n', sol.subsetsWithDup(nums))
