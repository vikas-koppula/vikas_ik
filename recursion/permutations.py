"""
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


def permutations(input_arr):
    result: list = []

    def helper(arr: list, i: int, slate: list):
        # Base case: Leaf node. One permutation reached
        if i == len(arr):
            result.append(slate[:])
            return
        # A loop is needed to iterate and swap the first element of the array after i
        for tmp in range(i, len(arr)):
            arr[i], arr[tmp] = arr[tmp], arr[i]
            slate.append(arr[i])  # Append the ith element after the swap (swap doesnt happen when tmp = 0)
            helper(arr, i+1, slate)  # Recursive call to handle below nodes
            # Important: This has to be here and not before the recursive call.
            # We need to put back the array in its original state for the next iteration
            arr[i], arr[tmp] = arr[tmp], arr[i]
            slate.pop()

    helper(input_arr, i=0, slate=[])
    return result


test = [1, 2, 3]
print('Answer:', permutations(test))
