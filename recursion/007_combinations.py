"""
77. Combinations
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
"""
from typing import List
# Ordering doesn't matter. Thus, we need to use the subsets framework (exclude include).
# Backtracking case: Return on length of slate == k
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result: List[List[int]] = list()
        def helper(i: int, slate: List[int]):
            # Base case: Important: Needed, without which recursion goes to infinity, because of all exclude cases
            if i == n+1:
                return
            # backtrack (filter) which stops the recursion at the node where slate reaches 2 elements
            # Backtrack condition has to be based on length and not i == k+1, as i will increment for exclusion cases
            if len(slate) == k:
                result.append(slate[:])
                return
            # exclude
            helper(i+1, slate)
            # include
            slate.append(i+1)
            helper(i+1, slate)
            slate.pop()

        helper(0, [])
        return result

sol = Solution()

print('\n.........Test_Case_1...........')
n = 4
k = 2
print('Combinations: ', sol.combine(n, k))

print('\n.........Test_Case_2...........')
n = 1
k = 1
print('Combinations: ', sol.combine(n, k))
