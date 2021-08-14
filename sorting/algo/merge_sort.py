def mergesort(input_array: list):
    def mergesort_helper(arr: list, start: int, end: int):

        if start >= end:
            return
        # Divide the arr into two parts
        mid: int = int((start + end) / 2)
        # Recursive call to the helper to sort the halfs
        mergesort_helper(arr, start, mid)
        mergesort_helper(arr, mid + 1, end)
        # i will now represent the first index of the left array
        # j will represent the first index of the right array
        i = start
        j = mid + 1
        aux_arr: list = list()
        # define an aux array which is used to hold the merged and sorted elements
        # the length would be (end - start) / 2
        while i <= mid and j <= end:
            if arr[i] <= arr[j]:
                aux_arr.append(arr[i])
                i += 1
            else:
                aux_arr.append(arr[j])
                j += 1
        # Either the left or the right array still has elements to be placed. Hence iterate and fill the aux array
        while i <= mid:
            aux_arr.append(arr[i])
            i += 1
        while j <= end:
            aux_arr.append(arr[j])
            j += 1
        # copy back the to the original array
        print('aux array:', aux_arr)
        # NOTE: end + 1 is needed as slicing uses the num of elements and not the indexes. Hence last element would be
        # index of the last element + 1 as indexes start from 0
        arr[start:end + 1] = aux_arr
        aux_arr = list()

    mergesort_helper(input_array, 0, len(input_array) - 1)
    print('Input array after sorting')
    print(input_array)


test_arr = [3, 1, 41, 59, 26, 53]
print(test_arr)
print('....................')
mergesort(test_arr)
print(test_arr)
