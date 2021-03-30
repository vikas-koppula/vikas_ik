

def letter_case_permutation(test_str: str):
    result: list = []

    def helper(s: str, i: int, slate: list):
        # Each left node is going to accumulate of this result list.
        # Will reach left node at the last letter
        if i == len(s):
            result.append("".join(slate))
            return
        # If digit then only one recursive call is made, as there can only be one worker below
        if s[i].isdigit():
            helper(s, i+1, slate.append(s[i]))
        else:
            # Add small letter and send one node down
            slate.append(s[i].lower())
            helper(s, i+1, slate)
            slate.pop()
            slate.append(s[i].upper())
            helper(s, i+1, slate)
            slate.pop()
    helper(test_str, 0, [])
    return result


test_str_1 = "ab"
print("test_str_1=a1b2")
print('answer:', letter_case_permutation(test_str_1))
