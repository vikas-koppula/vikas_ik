

def letter_case_permutation(test_str: str):
    result: list = []

    def helper(s: str, i: int, slate: list):
        # DFS approach. Each node is going to add a char to the slate and then either have one child or two child nodes
        # Leaf node will have a str of the required length. Hence next recursive call will exit with the condition below
        if i == len(s):
            result.append("".join(slate))
            return
        # If digit then only one recursive call is made, as there can only be one worker below
        if s[i].isdigit():
            slate.append(s[i])
            helper(s, i+1, slate)
            slate.pop()
        else:
            # Add small letter and send one node down
            slate.append(s[i].lower())
            helper(s, i+1, slate)
            slate.pop()
            # Add upper letter and send one node down
            slate.append(s[i].upper())
            helper(s, i+1, slate)
            slate.pop()
    helper(test_str, 0, [])
    return result


test_str_1 = "a1b2"
print("test_str_1=a1b2")
print('answer:', letter_case_permutation(test_str_1))
