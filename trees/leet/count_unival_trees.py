"""
250. Count Univalue Subtrees
Given the root of a binary tree, return the number of uni-value
subtrees
A uni-value subtree means all nodes of the subtree have the same value.

Input: root = [5,1,5,5,5,null,5]
Output: 4
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [5,5,5,5,5,null,5]
Output: 6
"""
from util.display_tree import display, insertLevelOrder
from util.treenode import TreeNode
from typing import List, Optional

def count_unival_subtrees(root: TreeNode) -> int:
    def helper(node: TreeNode):
        # Leaf Node is always unival, hence return 1
        if node.left is None and node.right is None:
            return 1, True
        # Recursive node case. Need if node itself is a unival subtree and how many unival subtrees under it are there
        # LH
        if node.left is not None:
            num_lh_subtrees, is_lh_unival = helper(node.left)

        # RH
        if node.right is not None:
            num_rh_subtrees, is_rh_unival = helper(node.right)
        if is_lh_unival is True & num_rh_subtrees is True & node.val == node.left.val & node.val == node.right.val:
            sum_node_unival_subtrees = num_lh_subtrees + num_rh_subtrees + 1
            is_node_unival = True
        else:
            sum_node_unival_subtrees = num_lh_subtrees + num_rh_subtrees
            is_node_unival = False

        return sum_node_unival_subtrees, is_node_unival
    cnt_unival_trees, _ = helper(root)
    return cnt_unival_trees


def test():
    top_left_left = TreeNode(None, None, 1)
    top_left_right = TreeNode(None, None, 3)
    top_left = TreeNode(top_left_left, top_left_right, 2)

    top_right = TreeNode(None, None, 7)
    top_node = TreeNode(top_left, top_right, 5)
    display(top_node)
    print("-------------------")
    count_unival = count_unival_subtrees(top_node)
    print("count_unival: ", count_unival)


def test_2():
    top_node = TreeNode(val=5, left=TreeNode(val=1, left=TreeNode(val=5, left=None, right=None),
                                             right=TreeNode(val=5, left=None, right=None)),
                        right=TreeNode(val=5, left=None, right=TreeNode(val=5, left=None, right=None)))
    display(top_node)
    print("-------------------")
    count_unival = count_unival_subtrees(top_node)
    print("count_unival: ", count_unival)


if __name__ == "__main__":
    test_2()
