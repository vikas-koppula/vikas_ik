"""
250. Count Univalue Subtrees
Given the root of a binary tree, return the number of uni-value subtrees
A uni-value subtree means all nodes of the subtree have the same value.
Example 1:
Input: root = [5,1,5,5,5,null,5]
Output: 4

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [5,5,5,5,5,null,5]
Output: 6
"""
from util.display_tree import display
from util.treenode import TreeNode, build_tree
from typing import List, Optional


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if root is None:
            return 0
        unival_cnt: List[int] = [0]

        def helper(node: TreeNode) -> bool:
            # Base Case
            if node.left is None and node.right is None:
                unival_cnt[0] = unival_cnt[0]+1
                return True
            # Recursive Case
            # Be careful not to do early stop as the dfs has to reach the leaf node to count all unival trees
            # Else True because if the node doesnt have a left or right subtree,
            # then the unival check is only on the other subtree
            lh = helper(node.left) if bool(node.left) else True
            rh = helper(node.right) if bool(node.right) else True
            # If either the lh or rh subtrees are not unival, then the node itself is not unival
            if lh is False or rh is False:
                return False
            # Now both lh and rh are unival subtrees. Return true if node.val is the same as the subtrees
            lh_node_eq = node.val == node.left.val if bool(node.left) else True
            rh_node_eq = node.val == node.right.val if bool(node.right) else True
            if bool(lh_node_eq) and bool(rh_node_eq):
                unival_cnt[0] = unival_cnt[0] + 1
            return lh_node_eq & rh_node_eq

        helper(root)
        return unival_cnt[0]

    def count_unival_subtrees_2(root: TreeNode) -> int:
        global_count: List[int] = [0]
        if root is None:
            return 0

        def helper(node: TreeNode):
            # Leaf Node is always unival, hence return 1
            if node.left is None and node.right is None:
                global_count[0] = global_count[0] + 1
                return True
            # Recursive node case. Need if node itself is a unival subtree
            # and how many unival subtrees under it are there
            am_unival = True
            # LH
            if node.left is not None:
                is_lh_unival = helper(node.left)
                if not is_lh_unival or node.left.val != node.val:
                    am_unival = False
            # RH
            if node.right is not None:
                is_rh_unival = helper(node.right)
                if not is_rh_unival or node.right.val != node.val:
                    am_unival = False

            if am_unival:
                global_count[0] = global_count[0] + 1

            return am_unival
        is_root_unival = helper(root)
        return global_count[0]


    def count_unival_subtrees_3(root: TreeNode) -> int:
        result: list[int] = [0]
        if root is None:
            return 0

        def helper(node: TreeNode) -> bool:
            lh = True
            rh = True
            # Base case leaf node
            if node.left is not None and node.right is not None:
                result[0] = result[0] + 1
                return True
            if bool(node.left):
                if node.left is True and node.val == node.left.val:
                    lh = True
                else:
                    lh = False
            if bool(node.right):
                if helper(node.right) is True and node.right.val == node.val:
                    rh = True
                else:
                    rh = False

            if lh & rh is True:
                result[0] = result[0] + 1

            return lh & rh

        helper(root)
        return result[0]




sol = Solution()
print('.........Test_Case_1...........')
input = '[5, 1, 5, 5, 5, None, 5]'
display(build_tree(input))
root = build_tree(input)
print('Count Univalue Subtrees:\n', sol.countUnivalSubtrees(root))
