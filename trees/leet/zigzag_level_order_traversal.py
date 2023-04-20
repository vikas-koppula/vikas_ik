"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Input: root = [1]
Output: [[1]]
"""

from collections import deque
from util.display_tree import display
from util.treenode import TreeNode
from typing import List


def zigzag_lvl_order_traversal(root: TreeNode):
    if root is None:
        return []

    dq = deque()
    result: List[List[int]] = list()
    dq.append(root)
    flag: bool = False
    while bool(dq):
        tmp: List[int] = list()
        for _ in range(len(dq)):
            node: TreeNode = dq.popleft()
            tmp.append(node.val)

            if node.left is not None:
                dq.append(node.left)
            if node.right is not None:
                dq.append(node.right)

        if bool(flag):
            tmp.reverse()
        result.append(tmp)
        flag = not flag
    return result

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
    print("top down levels")

    levels = zigzag_lvl_order_traversal(top_node)
    print(levels)


if __name__ == "__main__":
    test()
