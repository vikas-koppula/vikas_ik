#from util.display_tree import display

class TreeNode:
    def __init__(self, left, right, val):
        self.left: TreeNode = left
        self.right: TreeNode = right
        self.val = val

    def set_left(self, left) -> None:
        self.left = left

    def set_right(self, right) -> None:
        self.right = right


# class TreeNode:
#     def __init__(self, left, right, val):
#         self.val = val
#         self.left = self.right = None


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


def build_tree(input):
    if len(input) == 0:
        return input
    root = TreeNode(None, None, input[0])
    tree_lookup = {1: root}
    for i in range(1, len(input[1:]) + 1):
        node_num = i + 1
        parent_idx = int(node_num / 2)
        parent: TreeNode = tree_lookup[parent_idx]
        curr: TreeNode = TreeNode(None, None, input[i])
        tree_lookup[node_num] = curr
        if node_num % 2 == 0 and curr.val is not None:
            parent.set_left(curr)
        if node_num % 2 == 1 and curr.val is not None:
            parent.set_right(curr)
    return root


# Driver Code
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, 0, n)
    inOrder(root)