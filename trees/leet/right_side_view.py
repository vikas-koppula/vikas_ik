"""
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Input: root = [1,null,3]
Output: [1,3]
"""

from collections import deque
from util.display_tree import display
from util.treenode import TreeNode
from typing import List


def right_side_view(root: TreeNode):

    if root is None:
        return []

    dq = deque()
    result: List[int] = list()
    dq.append(root)

    while bool(dq):
        tmp: int = 0
        for _ in range(len(dq)):
            node: TreeNode = dq.popleft()
            tmp = node.val
            if node.left is not None:
                dq.append(node.left)
            if node.right is not None:
                dq.append(node.right)
        result.append(tmp)
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

    levels = right_side_view(top_node)
    print(levels)


if __name__ == "__main__":
    test()
