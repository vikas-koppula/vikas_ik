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
from util.treenode import TreeNode, build_tree
from typing import List, Optional

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int: