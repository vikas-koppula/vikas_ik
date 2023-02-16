"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values
in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
"""
from display_tree import display
from treenode import TreeNode
from typing import List


def paths_with_sum(root: TreeNode, target_sum: int) -> List[List[int]]:
    paths: List[List[int]] = []
    path: List[int] = []

    def check_path_sum(node: TreeNode, target: int, path: List[int]):
        if node is None:
            return

        path.append(node.val)
        if node.left is None and node.right is None:
            if sum(path) == target:
                # Very important to take a copy and put that in paths. Otherwise the value of path keep changing
                paths.append(path.copy())
        # No return statement after append, otherwise the pop will not be reached
        check_path_sum(node.left, target, path)
        check_path_sum(node.right, target, path)
        # Pop will remove the current node from the path before moving up the recursive tree
        path.pop()

    check_path_sum(node=root, target=target_sum, path=[])
    return paths


"""       5
         / \
        2   7
       / \   \
      1   3   -2
"""


def test():
    top_left_left = TreeNode(None, None, 1)
    top_left_right = TreeNode(None, None, 3)
    top_left = TreeNode(top_left_left, top_left_right, 2)

    top_right_right = TreeNode(None, None, -2)
    top_right = TreeNode(None, top_right_right, 7)
    top_node =  TreeNode(top_left, top_right, 5)
    display(top_node)
    print("-------------------")
    paths = paths_with_sum(top_node, 10)
    print(paths)


if __name__ == "__main__":
    test()
