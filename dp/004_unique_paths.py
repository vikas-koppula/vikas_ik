"""
62. Unique Paths
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to
reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""
from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Generate a 2d array to store the subproblem results
        mem:List[List[int]] = [[0 for i in range(n)] for j in range(m)]
        # Populate the base cases in the 2d grid
        # First base case is nC0, which is always 1. This is along the first column of all the rows
        # There is only one way for the robot to travel along the first column
        for i in range(m):
            mem[i][0] = 1
        # 2nd base case is along the first row of the grid. There is only one way to reach those nodes.
        for i in range(n):
            mem[0][i] = 1
        # Recursive case
        for row in range(1,m):
            for col in range(1,n):
                mem[row][col] = mem[row-1][col] + mem[row][col-1]
        return mem[m-1][n-1]


sol = Solution()
print('\n.........Test_Case_1...........')
m = 3
n = 7
print('climbStairs:', sol.uniquePaths(m,n))

print('\n.........Test_Case_2...........')
m = 3
n = 2
print('climbStairs:', sol.uniquePaths(m,n))
