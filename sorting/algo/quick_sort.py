import random


def quicksort(arr:list):
    def quicksort_helper(arr, st_idx: int, end_idx: int):
        pivot_idx: int = random.choice(arr[st_idx: end_idx + 1])
        pivot_elem: int = arr[pivot_idx]
        arr[st_idx], arr[pivot_idx] = arr[pivot_idx], arr[st_idx]
        # now pivot element is at the st_idx position
        green_idx: int = st_idx + 1
        orange_idx: int = st_idx + 1
        while green_idx <= end_idx:
            if arr[green_idx] >= pivot_elem:
                green_idx += 1
            elif arr[green_idx] < pivot_elem:
                # swap green with orange to have a contiguous orange and green blocks
                arr[orange_idx], arr[green_idx] = arr[green_idx], arr[orange_idx]
                orange_idx += 1
                green_idx += 1


test_arr = [3, 1, 41, 59, 26, 53]
print(test_arr)
print('....................')
quicksort(test_arr)
print(test_arr)