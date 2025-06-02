"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Generate the mem structure to store the subproblem results
        # Imp: Start for loop from 1 to generate the lists of different sizes based on the row number
        # Use the pattern of the previous problem. Num rows is going to be one greater than the last row index
        numRows = rowIndex+1
        mem: List[List[int]] = [[0] * i for i in range(1, numRows+1)]
        # Base cases are going to be along the left and right walls of the triangle
        for i in range(numRows):
            mem[i][0] = 1
            mem[i][-1] = 1
        # Recursive case: Need to fill just the inner cells of the triangle. Can start at row 2. Will need to use the
        # row number to figure out the right edge of the row. Hence the inner cell's cols will be from 1 to row-1
        # Warning: Easy to make a mistake with the range boundaries of the for loops
        for row in range(2,numRows):
            for col in range(1,row):
                # Imp: Structure of the triangle is such that a cell will depend on col-1 and col of the previous cell
                mem[row][col] = mem[row-1][col-1] + mem[row-1][col]
        return mem[rowIndex]

sol = Solution()
print('\n.........Test_Case_1...........')
rowIndex = 3
print('climbStairs:', sol.getRow(rowIndex))

print('\n.........Test_Case_2...........')
rowIndex = 0
print('climbStairs:', sol.getRow(rowIndex))

print('\n.........Test_Case_2...........')
rowIndex = 1
print('climbStairs:', sol.getRow(rowIndex))
