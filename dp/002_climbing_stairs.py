"""
70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # Memory structure to store subproblem results
        mem = dict()
        # Base cases: Only one way to get to the first step; Two ways to get to the 2nd step
        mem[1] = 1
        mem[2] = 2
        # Iterative for loop. Will start from 3 as the recursive equation will not work for < 3
        for i in range(3,n+1):
            mem[i] = mem[i-1] + mem[i-2]
        return mem[n]


sol = Solution()
print('\n.........Test_Case_1...........')
n = 2
print('climbStairs:', sol.climbStairs(n))

print('\n.........Test_Case_2...........')
n = 3
print('climbStairs:', sol.climbStairs(n))
