def subsets(test_ints: list):
    result: list = []

    def helper(ints: list, i: int, slate: list):
        if i == len(ints):
            result.append(slate[:])
            return
        else:
            # slate.append(ints[i])
            helper(ints, i+1, slate)
            # slate.pop()
            slate.append(ints[i])
            helper(ints, i + 1, slate)
            slate.pop()

    helper(test_ints, 0, [])
    return result


test = [1, 2, 2]
print('Answer:', subsets(test))
