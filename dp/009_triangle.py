"""
120. Triangle
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current
row, you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10
"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Create a cache structure in a triangle shape to store the subproblem results
        cache: List[List[int]] =  [[0]*i for i in range(1, len(triangle)+1)]
        # Base Cases: Apex node which is the value of the cell itself. Left & right wall which is just going to be the
        # sum along the left and right walls as there is only one adjacent node from the row above
        cache[0][0] = triangle[0][0]
        for i in range(1,len(triangle)):
            cache[i][0] = triangle[i][0] + cache[i-1][0]
            cache[i][-1] = triangle[i][-1] + cache[i - 1][-1]
        # Recursive case: The optimal substructure here is going to be to the prefix cell. That optimal substructure
        # will not tell us if that is the shortest path of the row itself, but it will tell us the shortest path instead
        # to the cell. To get the min path to the row, we need to compute the cost for all bottom cells and then get min
        for row in range(2, len(triangle)):
            for col in range(1, row):
                cache[row][col] = triangle[row][col] + min(cache[row-1][col-1], cache[row-1][col])
        # Now that we have computed the min cost to each cell in the bottom row. We do a min to get the least path sum
        return min(cache[len(cache)-1])


sol = Solution()
print('\n.........Test_Case_1...........')
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print('minimumTotal:', sol.minimumTotal(triangle))

print('\n.........Test_Case_2...........')
triangle = [[-10]]
print('minimumTotal:', sol.minimumTotal(triangle))
