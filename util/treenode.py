#from util.display_tree import display


class TreeNode:
    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val


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


# Driver Code
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, 0, n)
    inOrder(root)