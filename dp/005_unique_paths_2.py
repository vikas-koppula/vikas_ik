"""
63. Unique Paths II
You are given an m x n integer array grid. There is a robot initially located in the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or
right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot
include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # Generate a 2d array to store the subproblem results. Initialize every cell to 0
        mem:List[List[int]] = [[0 for i in range(n)] for j in range(m)]
        # Populate the base cases in the 2d grid
        # First check if there is an obstacle along the 1st col and row. If there is then break.
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            else:
                mem[i][0] = 1
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            else:
                mem[0][i] = 1
        # Recursive case
        for row in range(1,m):
            for col in range(1,n):
                # First check if there is an obstacle in our own cell. If there is then just store a 0 to the mem
                if obstacleGrid[row][col] == 1:
                    mem[row][col] = 0
                else:
                    mem[row][col] = mem[row-1][col] + mem[row][col-1]
        return mem[m-1][n-1]

sol = Solution()
print('\n.........Test_Case_1...........')
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print('climbStairs:', sol.uniquePathsWithObstacles(obstacleGrid))

print('\n.........Test_Case_2...........')
obstacleGrid = [[0,1],[0,0]]
print('climbStairs:', sol.uniquePathsWithObstacles(obstacleGrid))
