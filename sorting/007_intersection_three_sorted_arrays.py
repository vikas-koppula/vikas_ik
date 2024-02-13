"""
1213.Intersection of Three Sorted Arrays
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order,
return a sorted array of only the integers that appeared in all three arrays.

Example 1:
Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.

Example 2:
Input: arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = [521,682,1337,1395,1764]
Output: []
"""
from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        idx1 = idx2 = idx3 = 0
        result: list = list()
        while idx1 <= len(arr1) - 1 and idx2 <= len(arr2) - 1 and idx3 <= len(arr3) - 1:
            if arr1[idx1] == arr2[idx2] == arr3[idx3]:
                if len(result) == 0 or result[-1] != arr1[idx1]:
                    result.append(arr1[idx1])
                idx1 += 1
                idx2 += 1
                idx3 += 1
            else:
                if arr1[idx1] < arr2[idx2]:
                    idx1 += 1
                elif arr2[idx2] < arr3[idx3]:
                    idx2 += 1
                else:
                    idx3 += 1
        return result


sol = Solution()

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]
print('\n.........Test_Case_1...........')
print("arr1:", sorted(arr1))
print("arr2:", sorted(arr2))
print("arr3:", sorted(arr3))
print('Intersection of two arrays:', sol.arraysIntersection(arr1, arr2, arr3))

arr1 = [197, 418, 523, 876, 1356]
arr2 = [501, 880, 1593, 1710, 1870]
arr3 = [521, 682, 1337, 1395, 1764]
print('\n.........Test_Case_2...........')
print("arr1:", sorted(arr1))
print("arr2:", sorted(arr2))
print("arr3:", sorted(arr3))
print('Intersection of two arrays:', sol.arraysIntersection(arr1, arr2, arr3))
