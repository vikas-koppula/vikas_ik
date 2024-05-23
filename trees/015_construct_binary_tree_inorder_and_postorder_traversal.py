"""
106. Construct Binary Tree from Inorder and Postorder Traversal
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree
and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]
"""
from util.treenode import TreeNode, build_tree
from typing import List, Optional, Dict
from util.display_tree import display


class Solution:
    def buildTree(self, postorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Build hmap from the inorder to get the location of the elements
        inord_map: Dict[int:int] = {val: idx for idx, val in enumerate(inorder)}

        def helper(pst_or: List[int], p_st: int, p_end: int, in_or: List[int], i_st: int, i_end: int) -> (
                Optional)[TreeNode]:
            if p_st > p_end:
                return None
            # Leaf node hence create Treenode with no left and right children
            if p_st == p_end:
                return TreeNode(None, None, pst_or[p_end])
            pst_root = pst_or[p_end]
            in_idx = inord_map[pst_root]
            # Find no of elements to the left and right of the root node from inorder
            # Note: Will be relative to the start and end indexes
            num_l = in_idx - i_st
            num_r = i_end - in_idx
            # We can use num_l and num_r to now find the left and right subtree limits for both pre and in
            root_node: TreeNode = TreeNode(None, None, pst_or[p_end])
            root_node.set_left(
                helper(pst_or, p_st, p_st + num_l - 1, in_or, i_st, in_idx - 1)
            )
            root_node.set_right(
                helper(pst_or, p_end - num_r, p_end - 1, in_or, in_idx + 1, i_end)
            )
            return root_node

        return helper(postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1)


sol = Solution()
print('.........Test_Case_1...........')
postorder = [9, 15, 7, 20, 3]
inorder = [9, 3, 15, 20, 7]
root = sol.buildTree(postorder, inorder)
display(root)
