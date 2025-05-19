"""
746. Min Cost Climbing Stairs
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost,
you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Important: Need to add the cost 0 of the dest to the cost array. This helps with the coding.
        cost.append(0)
        n = len(cost) # Dest step is in the n-1 position. Min cost of dest step will be in the nth position in Mem
        # Memory structure to store subproblem results.
        mem = dict()
        # Base cases. Ground step with cost of 0. 1st step will be the cost of itself
        mem[0] = 0
        mem[1] = cost[0]
        # Recursive case.
        for i in range(2, n+1):
            mem[i] = cost[i-1] + min(mem[i-1], mem[i-2])
        return mem[n]

sol = Solution()
print('\n.........Test_Case_1...........')
cost = [10,15,20]
print('climbStairs:', sol.minCostClimbingStairs(cost))

print('\n.........Test_Case_2...........')
cost = [1,100,1,1,1,100,1,1,100,1]
print('climbStairs:', sol.minCostClimbingStairs(cost))
