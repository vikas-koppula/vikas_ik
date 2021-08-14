from pprint import pprint


# Assume that array has been solved for n-1 elements. We just need to solve for the last element
# n here is the index of the element that is to be placed in its correct position ()
def insertion_sort(arr):
    def place_idx(arr: list, idx: int):
        # When trying to place the first element, do nothing. Trivial case
        if idx == 0:
            return
        # Make a recursive call to have all elements before the last, fully sorted
        place_idx(arr, idx-1)
        # Array is fully sorted till the last element. Following will place the last element in its correct index
        last = arr[idx]
        # Assume that the array before the idx element is already sorted. Hence we use a while to place the idx element
        # i is the index before idx, hence the 2nd from the right
        i = idx - 1
        while i >= 0 and arr[i] > last:
            # shift to the right
            arr[i+1] = arr[i]
            i = i - 1
        # After the while loop completes there is a space where the target element has to be placed
        arr[i+1] = last
    place_idx(arr, len(arr)-1)


test_arr = [3, 1, 41, 59, 26, 53, 59]
pprint(test_arr)
print('....................')
# insertion_sort_r(test_arr, len(test_arr))
# # Let's see the list after we run the sort
#
# print('....................')
# pprint(test_arr)
insertion_sort(test_arr)
pprint(test_arr)
