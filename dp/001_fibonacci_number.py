"""
509. Fibonacci Number
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is
the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
"""
class Solution:
    def fib(self, n: int) -> int:
        # Memory structure to store subproblem results
        memo = dict()
        # Base conditions to build on
        memo[0] = 0
        memo[1] = 1
        # Iterative for loop
        for x in range(n+1):
            if x > 1:
                memo[x] = memo[x-1] + memo[x-2]
        return memo[n]


sol = Solution()
print('\n.........Test_Case_1...........')
n = 4
print('Fib:', sol.fib(n))
