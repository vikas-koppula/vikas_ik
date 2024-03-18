def subsets(test_ints: list):
    result: list = []

    def helper(ints: list, i: int, slate: list):
        # Base case: At leaf node, then append the aggregated to the result array
        if i == len(ints):
            result.append(slate[:])
            return
        else:
            # We first need to determine how many similar elements are present.
            # In order to avoid duplicate subsets, we have to have a branch for them (1,2,2)=> (1,2,22)
            counter = 1  # choosing counter = 0 doesnt work well in the while condition
            while i + counter <= len(ints) - 1 and ints[i] == ints[i + counter]:
                counter += 1
            #
            for j in range(0, counter + 1):
                slate.extend([ints[i]] * j)  # extend the slate by appending the ith element j times
                helper(ints, i+counter, slate)  # call the helper for each branch of the node
                slate = slate[:-j or None]  # replace pop with this to remove j num of elements that were appended in this iteration earlier

    helper(test_ints, 0, [])
    return result


test = [1, 2, 2]
print('Answer:', subsets(test))
