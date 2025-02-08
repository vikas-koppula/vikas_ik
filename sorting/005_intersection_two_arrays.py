"""
349.Intersection of Two Arrays
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique, and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
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
                # Important: Checking for dups at the time of inserting to the result is much easier to handle
                # Trying to check previous element for dups is kinda tricky and needs lots of conditions
                if len(result) == 0 or result[-1] != arr1[idx1]:
                    result.append(arr1[idx1])
                idx1 += 1
                idx2 += 1
        return result


sol = Solution()
arr1 = [4, 9, 5]
arr2 = [6, 9, 8, 4]
print('\n.........Test_Case_1...........')
print("arr1:", arr1)
print("arr2:", arr2)
print('Intersection of two arrays:', sol.intersection(arr1, arr2))


arr1 = [4, 7, 9, 5, 7]
arr2 = [7, 6, 9, 7, 8, 4]
print('\n.........Test_Case_1...........')
print("arr1:", arr1)
print("arr2:", arr2)
print('Intersection of two arrays:', sol.intersection(arr1, arr2))
