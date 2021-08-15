# Given an array of integers nums and an integer target, return indices of the two nums such that they add up to target
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].


def twosum_twopointer(arr: list, target_sum: int) -> list:
    # First sort the array by building a build heap, which takes O(n) time
    sorted_arr = sorted(arr)
    # Initialize the two pointers. One starts from the left and the other from the right
    left_idx = 0
    right_idx = len(arr) - 1
    ans = list()
    # If both the indexes arrive at the same index, then sum isn't available
    while left_idx < right_idx:
        iter_sum = sorted_arr[left_idx] + sorted_arr[right_idx]
        # If the iter sum is less than the target, then we need to move the right pointer to the smaller numbers (left)
        if iter_sum > target_sum:
            right_idx = right_idx - 1
        # If the iter sum is greater than the target, then we need to move the left pointer to the bigger nums (right)
        elif iter_sum < target_sum:
            left_idx = left_idx + 1
        # Found the sum, hence add the two indexes to the aux list. Increment the left idx by one to continue the
        # search for more pairs. Note: The right index can stay the same
        else:
            ans.append((left_idx, right_idx))
            left_idx = left_idx + 1
    return ans


test_arr = [5, 9, 1, 2, 8, 20, 15, 3, 11]
target_sum = 14
# The answer will be two pairs (3,11) and (5,9)
print(test_arr)
print("sorted:", sorted(test_arr))
print('....................')
ans = twosum_twopointer(test_arr, target_sum)
print("two sum tuple index:", ans)
