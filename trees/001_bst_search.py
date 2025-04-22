"""
700. Search in a Binary Search Tree
You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
If such a node does not exist, return null.

Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []
"""

from util.display_tree import display
from util.treenode import TreeNode, build_tree
from typing import Optional


class Solution:
    def searchBST_iterative(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr: TreeNode = root
        # Edge case: If the root is null, then return the root
        if curr is None:
            return root
        # Starting with the root node, check if the target is less than or greater than the current val.
        # Iterate to the left node or right node till the curr becomes null.
        while curr is not None:
            if curr.val == val:
                return curr
            elif val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right
        # If the node couldn't be found, then return null
        return None

    def searchBST_rec(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr: TreeNode = root
        # Edge case: If the root is null, then return the root
        if curr is None:
            return root
        # Starting with the root node, check if the target is less than or greater than the current val.
        # Iterate to the left node or right node till the curr becomes null.
        if val == curr.val:
            return curr
        elif val < curr.val:
            return self.searchBST_rec(curr.left, val)
        elif val > curr.val:
            return self.searchBST_rec(curr.right, val)

        return None


sol = Solution()

print('.........Test_Case_1...........')
input = '[4,2,7,1,3]'
val = 2
display(build_tree(input))
root = build_tree(input)
print('Search: ', sol.searchBST_iterative(root, val))

print('.........Test_Case_2...........')
input = '[4,2,7,1,3]'
val = 2
display(build_tree(input))
root = build_tree(input)
print('Search: ', sol.searchBST_rec(root, val))
