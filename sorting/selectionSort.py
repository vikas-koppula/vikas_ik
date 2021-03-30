from pprint import pprint


def selection_sort(arr):
    for i in range(len(arr)):
        # initially assume that the first element is the smallest
        # By the time we get to ith iteration, all elements left of i are sorted in ascending order
        min_idx = i
        # Traverse rest of the array till end
        for j in range(i+1, len(arr)):
            # If we find a smaller element than arr[min_idx], then update the index of the min element
            # We need to find out the smallest element by the end of this loop
            if arr[min_idx] > arr[j]:
                # This is the index of the least num
                min_idx = j
        # Swap the min element with arr[i]
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [3, 1, 41, 59, 26, 53, 59]
pprint(arr)
selection_sort(arr)
# Let's see the list after we run the Selection Sort
pprint(arr)
