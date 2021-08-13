from pprint import pprint


# Assume that array has been solved for n-1 elements. We just need to solve for the last element
# n here is the number of elements in the array (size)
def insertion_sort_r(arr, n):
    # if the size of the array is 1, then its already sorted, so nothing to do
    if n <= 1:
        return
    # Sort first n-1 elements
    insertion_sort_r(arr, n-1)
    # Now insert the nth element into its place
    last = arr[n-1]
    # We now need to compare the last element to all the remaining elements to the right to correctly place it
    # 2nd last element. Highest element after n-1 operations
    j = n-2
    # Shift right all the elements of arr[0...n-1] that are greater than arr[n]
    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]
        j = j - 1
    # After the while loop completes there is a space
    arr[j + 1] = last


test_arr = [3, 1, 41, 59, 26, 53, 59]
pprint(test_arr)
print('....................')
insertion_sort_r(test_arr, len(test_arr))
# Let's see the list after we run the sort

print('....................')
pprint(test_arr)
