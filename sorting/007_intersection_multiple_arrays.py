"""
2248. Intersection of Multiple Arrays
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of
integers that are present in each array of nums sorted in ascending order.

Example 1:
Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation:
The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].

Example 2:
Input: nums = [[1,2,3],[4,5,6]]
Output: []
Explanation:
There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].
"""
from typing import List
from functools import reduce

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
            arr1 = sorted(nums1)
            arr2 = sorted(nums2)
            idx1: int = 0
            idx2: int = 0
            result: list = list()
            while idx1 <= len(arr1) - 1 and idx2 <= len(arr2) - 1:
                if arr2[idx2] > arr1[idx1]:
                    idx1 += 1
                elif arr2[idx2] < arr1[idx1]:
                    idx2 += 1
                elif arr2[idx2] == arr1[idx1]:
                    # No additional checks needed unlike the last problem as dups are allowed
                    result.append(arr1[idx1])
                    idx1 += 1
                    idx2 += 1
            return result

        if len(nums) == 1:
            return sorted(nums[0])
        intersection = reduce(intersect, nums)
        return intersection

sol = Solution()

print('\n.........Test_Case_1...........')
test1 = [[1, 2], [2, 3,4]]
print("test 1:", test1)
print('Intersection of multiple arrays:', sol.intersection(test1))
