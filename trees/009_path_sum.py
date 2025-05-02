"""
112. Path Sum
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
adding up all the values along the path equals targetSum.
A leaf is a node with no children
Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
"""
from util.display_tree import display
from util.treenode import TreeNode, build_tree
from typing import List, Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # This is the global box. This is needed for a top down DFS
        check: list = [False]

        def helper(node: TreeNode, target: int):
            # Edge case
            if node is None:
                return False
            # Base case: First check if we are in the leaf node, then only check the sum
            if node.left is None and node.right is None:
                if node.val == target:
                    check[0] = True
                return # Return nothing as this is top down DFS

            # Recursive Case
            if node.left and check[0] is False:
                helper(node.left, target - node.val)
            if node.right and check[0] is False:
                helper(node.right, target - node.val)
            return
        helper(root, targetSum)
        return check[0]


sol = Solution()
print('.........Test_Case_1...........')
input = '[5,4,8,11,None,13,4,7,2,None,None,None,1]'
targetSum = 22
display(build_tree(input))
root = build_tree(input)
print('Path sum:\n', sol.hasPathSum(root, targetSum))
