# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be
# unique and you may return the result in any order
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted


def arrays_intersection(nums1: list, nums2: list):
    sorted_1 = sorted(nums1)
    sorted_2 = sorted(nums2)
    idx_1, idx_2 = 0, 0
    result = []

    while idx_1 <= len(nums1)-1 and idx_2 <= len(nums2)-1:
        if sorted_1[idx_1] < sorted_2[idx_2]:
            idx_1 += 1
        elif sorted_2[idx_2] < sorted_1[idx_1]:
            idx_2 += 1
        else:
            if len(result) == 0 or result[-1] != sorted_1[idx_1]:
                result.append(sorted_1[idx_1])
            idx_1 += 1
            idx_2 += 1
    return result


arr1 = [4, 9, 5]
arr2 = [6, 9, 8, 4]
ans = arrays_intersection(arr1, arr2)
print('Intersection of two arrays:', ans)


arr1 = [4, 7, 9, 5, 7]
arr2 = [7, 6, 9, 7, 8, 4]
ans = arrays_intersection(arr1, arr2)
print('Intersection of two arrays:', ans)