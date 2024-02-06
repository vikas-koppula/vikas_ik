# Merge two sorted linked lists and return it as a sorted list.
# The list should be made by splicing together the nodes of the first two lists.
# Example 1:
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]


def arrays_union(arr1: list, arr2: list):
    idx_1 = 0
    idx_2 = 0
    aux_arr = []
    while idx_1 <= len(arr1)-1 and idx_2 <= len(arr2)-1:
        if arr1[idx_1] < arr2[idx_2]:
            aux_arr.append(arr1[idx_1])
            idx_1 += 1
        elif arr2[idx_2] < arr1[idx_1]:
            aux_arr.append(arr2[idx_2])
            idx_2 += 1
        else:
            aux_arr.append(arr1[idx_1])
            idx_1 += 1
            idx_2 += 1
    while idx_1 <= len(arr1)-1:
        aux_arr.append(arr1[idx_1])
        idx_1 += 1
    while idx_2 <= len(arr2)-1:
        aux_arr.append(arr2[idx_2])
        idx_2 += 1
    return aux_arr


arr1 = [1, 2, 4]
arr2 = [1, 3, 4]
ans = arrays_union(arr1, arr2)
print('union of two arrays:', ans)
