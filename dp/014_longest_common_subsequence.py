"""
1143. Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none)
deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""
from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        mem: List[List[int]] = [[0 for i in range(n + 1)] for j in range(m + 1)]
        # Base cases are going to be along the first row and column. Number of common chars with an empty string.
        # We have already made the first row and column as 0.
        for row in range(1, m+1):
            for col in range(1, n+1):
                mem[row][col] = max(
                    mem[row - 1][col - 1] + 1 if text1[row - 1] == text2[col - 1] else 0 ,
                    mem[row][col - 1],
                    mem[row - 1][col],
                )
        return mem[m][n]

sol = Solution()
print('\n.........Test_Case_1...........')
text1 = "abcde"
text2 = "ace"
print('longestCommonSubsequence:', sol.longestCommonSubsequence(text1, text2))

print('\n.........Test_Case_2...........')
text1 = "abc"
text2 = "abc"
print('longestCommonSubsequence:', sol.longestCommonSubsequence(text1, text2))

print('\n.........Test_Case_3...........')
text1 = "abc"
text2 = "def"
print('longestCommonSubsequence:', sol.longestCommonSubsequence(text1, text2))

print('\n.........Test_Case_4...........')
text1 = "bl"
text2 = "yby"
print('longestCommonSubsequence:', sol.longestCommonSubsequence(text1, text2))
