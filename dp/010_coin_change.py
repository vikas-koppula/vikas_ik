"""
322. Coin Change
You are given an integer array coins representing coins of different denominations and an integer amount representing
a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of
money cannot be made up by any combination of the coins, return -1. You may assume that you have an infinite number of
each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
"""
from typing import List, Dict


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem: Dict[int:int] = dict()
        # Base cases
        mem[0] = 0

        def mem_lookup(x: int):
            if x < 0:
                return amount+1
            else:
                return mem[x]

        for amt in range(1, amount+1):
            mem[amt] = min( [mem_lookup(amt-coin) for coin in coins]) + 1
        if mem[amount] > amount:
            return -1
        else:
            return mem[amount]


sol = Solution()

print('\n.........Test_Case_1...........')
coins = [1,2,5]
amount = 11
print('coinChange:', sol.coinChange(coins, amount))

print('\n.........Test_Case_2...........')
coins = [2]
amount = 3
print('coinChange:', sol.coinChange(coins, amount))

print('\n.........Test_Case_3...........')
coins = [1]
amount = 0
print('coinChange:', sol.coinChange(coins, amount))
