# Function to insert nodes in level order
def insertLevelOrder(arr, i, n):
    root = None
    # Base case for recursion
    if i < n:
        root = TreeNode(None, None, arr[i])

        # insert left child
        root.left = insertLevelOrder(arr, 2 * i + 1, n)

        # insert right child
        root.right = insertLevelOrder(arr, 2 * i + 2, n)

    return root


# Function to print tree nodes in
# InOrder fashion
def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.val, end=" ")
        inOrder(root.right)


def build_tree(leet_code_input: str, should_print_tree_code_to_console=False):
    """
    Credit to LeetCode user 'bqrkhn' for this function

    Given the typical leet code input string for
    a tree, where the tree is defined level by
    level such that input[i] has nodes defined
    for a level as input[i+1:nodes_in_level],
    this builds that tree!

    Explicitly, it prints out the code for the tree structure if
    should_print_tree_code_to_console=True,
    and returns the root of the constructed tree regardless
    """
    leet_code_input = leet_code_input[1:-1].split(',')
    if len(leet_code_input) == 0:
        return
    nodes = [('root', leet_code_input[0])]
    for index, current_node in enumerate(leet_code_input[1:]):
        if current_node != 'null':
            if index & 1:
                nodes.append((nodes[index // 2][0] + '.right', current_node))
            else:
                nodes.append((nodes[index // 2][0] + '.left', current_node))
    root = TreeNode(int(nodes[0][1]))
    for node in nodes:
        execution_statement: str = node[0] + ' = TreeNode(' + node[1] + ')'
        if should_print_tree_code_to_console:
            print(execution_statement)
        exec(execution_statement)
    return root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right


# Driver Code
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, 0, n)
    inOrder(root)