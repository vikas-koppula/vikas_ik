"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
You may return the answer in any order.
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


def combinations(n: int, k: int):
    result: list = []

    def helper(i: int, slate: list):

        # backtrack (filter) which stops the recursion at the node where slate reaches 2 elements
        if len(slate) == k:
            result.append(slate[:])
            return
        # Base case: Important: This is needed without which recursion goes to infinity, because of all exclude cases
        if i == n+1:
            return

        # exclude
        helper(i+1, slate)
        # include
        slate.append(i)
        helper(i+1, slate)
        slate.pop()

    helper(i=1, slate=[])
    return result


n1 = 4
k1 = 2
print('Answer:', combinations(n1, k1))
