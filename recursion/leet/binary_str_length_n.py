"""
Enumerate all possible binary strings of length 3
Input: nums = [0,1]
Output:  [[0,0,0],  [1,1,1], [0,0,1], [0,1,0], [1,0,0], [0,1,1], [1,0,1], [1,1,0]]
"""
from typing import List


def binary_str_len_n(str_len: int) -> List[List[int]]:
    result: List[List[int]] = list()

    def helper(str_len: int, slate: List[int]):
        if len(slate) == str_len:
            result.append(slate[:])
            return

        for i in [0,1]:
            slate.append(i)
            helper(str_len, slate)
            slate.pop()

    helper(str_len, [])
    return result


print('Test Case 1:', binary_str_len_n(3))
