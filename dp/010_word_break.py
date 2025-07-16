"""
139. Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence
of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # This is a DP problem in which the last subproblem is actually dependent on all the subproblems before it not
        # just the previous 2 like the problems we have seen so far

        # f(1): Represents the case if the first char in the string is a valid word in the dict
        # f(2): Represents the case if the first 2 chars in the string are a valid word in the dict or if they can be
        # successfully broken down into valid words in the dict
        # Setup up the mem structure. Will be of length n+1 to include always true for the f(0) case
        # Important: f(0) case is needed here for the code to work properly
        mem = [0 for _ in s]
        mem.append(0)
        # Make f(0) case always return true
        mem[0] = 1
        # First look at the last letter, if it is in dict then check if all the chars before it can be split into words
        # in the dict. Then look at the last two letters, see if those are in the dict, if they are then check if all
        # chars before the last two words can be split into valid words in the dict
        # We write the code in such a way that this analysis starts from left to right of the string.
        # That way we can populate the cells for f(0), f(1) etc and look those up when calculating gradually to f(n)
        for i in range(1, len(s)+1):
            for llen in range (1, i+1):
                last_word = s[i-llen:i]
                before_word_fn = mem[i-llen]
                if s[i-llen:i] in wordDict and bool(mem[i-llen]):
                    mem[i] = 1
                    # IMP: Break is needed here as once we know that the substring till this position i can be broken
                    # down to valid strings, then we can just move on to the next i.
                    break
        return bool(mem[-1])

sol = Solution()
print('\n.........Test_Case_1...........')
s = "applepenapple"
wordDict = ["apple","pen"]
print('wordBreak:', sol.wordBreak(s, wordDict))

print('\n.........Test_Case_2...........')
s = "leetcode"
wordDict = ["leet","code"]
print('wordBreak:', sol.wordBreak(s, wordDict))

print('\n.........Test_Case_3...........')
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print('wordBreak:', sol.wordBreak(s, wordDict))
