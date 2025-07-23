"""
72. Edit Distance
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        mem: List[List[int]] = [[0 for i in range(n+1)] for j in range(m+1)]
        # Base cases will be along the first row and column respectively
        for i in range(n+1):
            mem[0][i] = i
        for j in range(m+1):
            mem[j][0] = j

        for row in range(1, m+1):
            for col in range(1, n+1):
                mem[row][col] = min(
                    mem[row-1][col-1] if word1[row-1] == word2[col-1] else mem[row-1][col-1] + 1,
                    mem[row][col - 1] + 1,
                    mem[row - 1][col] + 1,
                )
        return mem[m][n]


sol = Solution()
print('\n.........Test_Case_1...........')
word1 = "horse"
word2 = "ros"
print('minDistance:', sol.minDistance(word1, word2))

print('\n.........Test_Case_2...........')
word1 = "intention"
word2 = "execution"
print('minDistance:', sol.minDistance(word1, word2))
