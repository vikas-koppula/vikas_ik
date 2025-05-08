"""
543. Diameter of Binary Tree
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may
not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
"""
from util.display_tree import display
from util.treenode import TreeNode, build_tree
from typing import List, Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter: List[int] = [0]

        def helper(node: TreeNode):
            if node.left is None and node.right is None:
                return 0

            # LH
            left_len = 1 + helper(node.left) if bool(node.left) else 0
            # RH
            right_len = 1 + helper(node.right) if bool(node.right) else 0
            print('node:', node.val)
            print('...............')
            print('left_len', left_len)
            print('right_len:', right_len)
            max_ht_of_node = max(left_len, right_len)
            dia_of_node = left_len + right_len
            if dia_of_node > max_diameter[0]:
                max_diameter[0] = dia_of_node
            return max_ht_of_node

        helper(root)
        return max_diameter[0]


sol = Solution()
print('.........Test_Case_1...........')
input = '[1, 2, 3, 4, 5]'
display(build_tree(input))
root = build_tree(input)
print('Diameter:\n', sol.diameterOfBinaryTree(root))
