"""
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
"""
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result: List[str] = list()
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7':'pqrs', '8': 'tuv', '9': 'wxyz'}

        def helper(arr: str, i:int, slate: List[str]) -> None:
            if len(digits) == 0:
                return
            if i == len(digits):
                result.append("".join(slate))
                return

            for let in mapping[digits[i]]:
                slate.append(let)
                helper(arr, i+1, slate)
                slate.pop()

        helper(digits, 0, [])
        return result


sol = Solution()
print('\n.........Test_Case_1...........')
digits = "23"
print("digits:", digits)
print('Output: ', sol.letterCombinations(digits))
print('\n.........Test_Case_2...........')
digits = ""
print("digits:", digits)
print('Output: ', sol.letterCombinations(digits))
print('\n.........Test_Case_3...........')
digits = "2"
print("digits:", digits)
print('Output: ', sol.letterCombinations(digits))
print('\n.........Test_Case_4...........')
digits = "3"
print("digits:", digits)
print('Output: ', sol.letterCombinations(digits))
