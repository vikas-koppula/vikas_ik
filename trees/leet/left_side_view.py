"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you
can see ordered from top to bottom.
"""

from collections import deque
from display_tree import display
from treenode import TreeNode
from typing import List


def left_view_dfs(root: TreeNode) -> List[int]:
    if root is None:
        return []

    def left_node_per_lvl(node: TreeNode, curr_lvl: int, max_lvl: list, left_nodes: List[int]):
        if node is None:
            return
        curr_lvl += 1
        if curr_lvl > max_lvl[0]:
            left_nodes.append(node.val)
            max_lvl[0] = curr_lvl
        left_node_per_lvl(node.left, curr_lvl, max_lvl, left_nodes)
        left_node_per_lvl(node.right, curr_lvl, max_lvl, left_nodes)

    max_level = [0]
    left_nodes_collector = []
    left_node_per_lvl(root, 0, max_lvl=max_level, left_nodes=left_nodes_collector)
    return left_nodes_collector



"""       5
         / \
        /   \
       3     7
        \   / \
         4 6   8
              /
             9 
"""

def test():
    top_left_right = TreeNode(None, None, 4)
    top_left = TreeNode(None, top_left_right, 3)

    top_right_right_left = TreeNode(None, None, 9)
    top_right_right = TreeNode(top_right_right_left, None, 8)
    top_right_left = TreeNode(None, None, 6)
    top_right = TreeNode(top_right_left, top_right_right, 7)
    top_node =  TreeNode(top_left, top_right, 5)
    display(top_node)
    print("-------------------")
    print("left view of tree")

    # left_most_nodes = left_most_value_at_level(top_node)
    # print(left_most_nodes)

    print("-------------------")
    print("left view of tree using DFS")
    left_most_nodes = left_view_dfs(top_node)
    print(left_most_nodes)

    print("-------------------")
    print("right view of tree")

    # right_most_nodes = right_most_value_at_level(top_node)
    # print(right_most_nodes)


if __name__ == "__main__":
    test()