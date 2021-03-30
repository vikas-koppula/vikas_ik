"""
Given a set of integers and a target value k, find a non-empty subset that sums up to k.
Example One
Input: [2 4 8], k = 6
Output: True
Because 2+4=6.
Example Two
Input: [2 4 6], k = 5
Output: False
Because no subset of numbers from the input sums up to 5.
"""


def check_if_sum_possible(arr: list, k: int):
    result: list = []
    if len(arr) == 1:
        return k == arr[0]

    def helper(i: int, slate: list):
        # Need to check sum before checking if leaf is reached
        if sum(slate) == k:
            result.append(sum(slate[:]))
            return
        # Base condition: The leaf node is reached
        if i == len(arr):
            result.clear()
            return
        else:
            # exclude
            helper(i+1, slate)
            # include
            slate.append(arr[i])
            helper(i+1, slate)
            slate.pop()
    helper(i=0, slate=[])
    print('result:', result)
    if result == [0]:
        return False
    return bool(result)


test_arr = [10, 20]
test_k = 0
print('Answer:', check_if_sum_possible(test_arr, test_k))
