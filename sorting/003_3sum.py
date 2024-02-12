"""
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print("sorted nums:", nums)
        ans: List[List[int]] = []
        # Iterate from left, leaving the two right most positions for l and r
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lft = i+1
            rgt = len(nums)-1
            while lft < rgt:
                total = nums[i] + nums[lft] + nums[rgt]
                if total < 0:
                    # Total less than zero indicates that we need to increase the total, thereby move lft pointer
                    lft += 1
                elif total > 0:
                    # Total greater than zero, indicates that we need to decrease the total, hence move rgt pointer
                    rgt -= 1
                elif total == 0:
                    answer = [nums[i], nums[lft], nums[rgt]]
                    ans.append(answer)
                    while lft < rgt and nums[lft] == answer[1]:
                        lft += 1
                    while lft < rgt and nums[rgt] == answer[2]:
                        rgt -= 1
        return ans


sol = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print("nums:", nums)
print("sol:", sol.threeSum(nums))
