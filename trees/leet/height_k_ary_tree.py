"""
Given a k-ary tree, find the height of that tree: number of edges in the longest path from the root to any node.
A k-ary tree is a rooted tree in which each node has no more than k children.
"""

from display_tree import display
from typing import List


class TreeNode:
    def __init__(self):
        self.children = []


def height_k_tree(root: TreeNode):

    max_height: List[int] = [0]

    def height_dfs(node: TreeNode, max: List[int], height_so_far: int):
        if node is None:
            return

        height_so_far += 1
        # Check if leaf node
        if len(node.children) == 0 :
            if height_so_far > max_height[0]:
                # this path is deepest for far
                max_height[0] = height_so_far
            return

        for treeNode in node.children:
            height_dfs(treeNode, max_height, height_so_far)
            height_so_far -= 1

    height_dfs(root, max_height, 0)
    return max_height
