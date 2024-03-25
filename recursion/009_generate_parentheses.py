"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result: List[str] = list()

        def helper(num_l: int, num_r: int, slate: List[str]) -> None:
            if num_r > num_l:
                return
            elif num_l > n:
                return
            elif num_l == n and num_r == n:
                result.append("".join(slate))
                return
            # Append (
            slate.append("(")
            helper(num_l+1, num_r, slate)
            slate.pop()
            # Append )
            slate.append(")")
            helper(num_l, num_r+1, slate)
            slate.pop()

        helper(0, 0, [])
        return result


sol = Solution()
print('\n.........Test_Case_1...........')
n = 3
print("n:", n)
print("permutations:", sol.generateParenthesis(n))
