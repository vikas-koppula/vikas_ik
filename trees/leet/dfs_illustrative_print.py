"""
Simple dfs print for illustrative purposes
"""

from display_tree import display
from treenode import TreeNode
from typing import List


def dfs_print(root: TreeNode):

    def helper(node: TreeNode):
        if node is None:
            print("At null node, simply return")
            return
        print("..................................................")
        print("At node:", node.val)
        print("going left")
        helper(node.left)
        print("completed processing at left node of:", node.val)
        print("going right")
        helper(node.right)
        print("completed processing at right node of:", node.val)

        print("Completed processing at both left and right recursive calls for the node:", node.val)
    helper(root)


"""       5
         / \
        2   7

"""


def test():
    top_left = TreeNode(None, None, 2)
    top_right = TreeNode(None, None, 7)
    top_node = TreeNode(top_left, top_right, 5)
    display(top_node)
    print("-------------------")
    dfs_print(top_node)


if __name__ == "__main__":
    test()
