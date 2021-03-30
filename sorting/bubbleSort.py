from pprint import pprint


# Scan the a array from right to left and bubble up the min to the left by repeated exchanges
# While scanning from right to left if A[i-1] > A[i], swap them
# In the 1st iteration, the 1st element will be the smallest.
# In the ith iteration, the ith element will be the ith smallest. i-1 elements to the left are already sorted

def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in reversed(range(i+1, len(arr))):
            if arr[j-1] > arr[j]:
                # perform a swap if element before i is greater than element at i
                arr[j-1], arr[j] = arr[j], arr[j-1]


test_arr = [3, 1, 41, 59, 26, 53, 59]
pprint(test_arr)
print('....................')
bubble_sort(test_arr)
# Let's see the list after we run the sort

print('....................')
pprint(test_arr)
