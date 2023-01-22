import random


def quicksort(arr: list):

    def helper(arr, st_idx: int, end_idx: int):
        if st_idx >= end_idx:
            return
        # pivot_idx: int = random.choice(arr[st_idx: end_idx + 1])
        pivot_idx: int = random.choice(range(st_idx, end_idx+1))
        pivot_elem: int = arr[pivot_idx]
        print('pivot_idx:', pivot_idx)
        print('pivot_elem:', pivot_elem)
        # Swap the first element with the pivot element, thus the pivot is the first position
        arr[st_idx], arr[pivot_idx] = arr[pivot_idx], arr[st_idx]
        # Walk the green pointer from left to right, and create orange and green sections
        orange_idx = st_idx
        for green_idx in range(st_idx + 1, end_idx + 1):
            if arr[green_idx] < pivot_elem:
                # Move orange pointer to next green element and then swap with the green pointer's element
                orange_idx += 1
                arr[green_idx], arr[orange_idx] = arr[orange_idx], arr[green_idx]
        # Swap the pivot in the start position with the last element of the orange partition
        # Pivot is now in its correct and final sorted position
        arr[st_idx], arr[orange_idx] = arr[orange_idx], arr[st_idx]
        # Call helper recursive call on the orange and green sections
        helper(arr, st_idx, orange_idx-1)
        helper(arr, orange_idx+1, end_idx)
        # Original array is now fully sorted in place
    helper(arr, 0, len(arr)-1)
    return arr


test_arr = [5, 7, 6, 3, 1, 2, 4]
print(test_arr)
print('....................')
quicksort(test_arr)
print(test_arr)
