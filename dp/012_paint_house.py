"""
256. Paint House
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of
painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses
have the same color.
The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.
For example, costs[0][0] is the cost of painting house 0 with the color red;
costs[1][2] is the cost of painting house 1 with color green, and so on...
Return the minimum cost to paint all houses.

Example 1:
Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.

Example 2:
Input: costs = [[7,6,2]]
Output: 2
"""

from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        m = len(costs)
        n = len(costs[0])
        # There is no optimal substructure just like the triangle problem
        # There is an optimal substructure if we include the color of the house
        # Thus the mem now maintains the costs so far for each color of the house
        mem:List[List[int]] = [[0 for i in range(n)] for j in range(m)]
        # Base case will be house 1. Cheapest way to color house 1 blue, will be its own cost for blue.
        mem[0] = costs[0]
        for house in range(1, len(costs)):
            mem[house][0] = costs[house][0] + min(mem[house-1][1], mem[house-1][2])
            mem[house][1] = costs[house][1] + min(mem[house-1][0], mem[house-1][2])
            mem[house][2] = costs[house][2] + min(mem[house-1][0], mem[house-1][1])
        return min(mem[-1])

sol = Solution()
print('\n.........Test_Case_1...........')
costs = [[17,2,17],[16,16,5],[14,3,19]]
print('minCost:', sol.minCost(costs))

print('\n.........Test_Case_2...........')
costs =  [[7,6,2]]
print('minCost:', sol.minCost(costs))
