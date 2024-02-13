"""
350.Intersection of Two Arrays II
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays. You may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr1 = sorted(nums1)
        arr2 = sorted(nums2)
        idx1: int = 0
        idx2: int = 0
        result: list = list()
        while idx1 <= len(arr1)-1 and idx2 <= len(arr2)-1:
            if arr2[idx2] > arr1[idx1]:
                idx1 += 1
            elif arr2[idx2] < arr1[idx1]:
                idx2 += 1
            elif arr2[idx2] == arr1[idx1]:
                result.append(arr1[idx1])
                idx1 += 1
                idx2 += 1
        return result


sol = Solution()
arr1 = [1, 2, 2, 1]
arr2 = [2, 2]
print('\n.........Test_Case_1...........')
print("arr1:", sorted(arr1))
print("arr2:", sorted(arr2))
print('Intersection of two arrays:', sol.intersect(arr1, arr2))

arr1 = [4, 9, 5]
arr2 = [9, 4, 9, 8, 4]
print('\n.........Test_Case_1...........')
print("arr1:", sorted(arr1))
print("arr2:", sorted(arr2))
print('Intersection of two arrays:', sol.intersect(arr1, arr2))
