"""
64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mem:List[List[int]] = [[0 for i in range(n)] for j in range(m)]
        mem[0][0] = grid[0][0]
        for x in range(1,m):
            mem[x][0] = grid[x][0] + mem[x-1][0]
        for x in range(1,n):
            mem[0][x] = grid[0][x] + mem[0][x-1]

        for row in range(1,m):
            for col in range(1,n):
                mem[row][col] = grid[row][col] + min(mem[row-1][col], mem[row][col-1])
        return mem[m-1][n-1]

sol = Solution()
print('\n.........Test_Case_1...........')
grid = [[1,3,1],[1,5,1],[4,2,1]]
print('min_path_sum:', sol.minPathSum(grid))

print('\n.........Test_Case_2...........')
grid = [[1,2,3],[4,5,6]]
print('min_path_sum:', sol.minPathSum(grid))
