"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path
such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.
"""

from util.display_tree import display
from util.treenode import TreeNode
from typing import List


def path_sum(root: TreeNode, target: int) -> bool:

    def check_node_path_sum(node: TreeNode, sum_so_far: int, target_sum: int, has_path_sum: List[bool]):
        if node is None:
            return
        # If left node then check if target sum == current cumulative sum
        sum_so_far += node.val
        if node.left is None and node.right is None:
            if target_sum == sum_so_far:
                has_path_sum[0] = True
                return
        check_node_path_sum(node.left, sum_so_far, target_sum, has_path_sum)
        if has_path_sum[0] is False:
            check_node_path_sum(node.right, sum_so_far, target_sum, has_path_sum)

    has_path_sum: List[bool] = [False]
    check_node_path_sum(root, 0, target, has_path_sum)
    return has_path_sum[0]

"""       5
         / \
        2   7
       / \
      1   3
"""

def test():
    top_left_left = TreeNode(None, None, 1)
    top_left_right = TreeNode(None, None, 3)
    top_left = TreeNode(top_left_left, top_left_right, 2)

    top_right = TreeNode(None, None, 7)
    top_node =  TreeNode(top_left, top_right, 5)
    display(top_node)
    # print("-------------------")
    # has_path_with_sum = has_path_sum(top_node, 10)
    # print(has_path_with_sum)
    # has_path_with_sum = has_path_sum(top_node, 16)
    # print(has_path_with_sum)
    print("-------------------")
    has_path_with_sum = path_sum(top_node, 10)
    print(has_path_with_sum)
    # has_path_with_sum = path_sum(top_node, 15)
    # print(has_path_with_sum)


if __name__ == "__main__":
    test()
