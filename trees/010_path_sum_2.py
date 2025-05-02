"""
113. Path Sum II
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values
in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []
"""
from util.display_tree import display
from util.treenode import TreeNode, build_tree
from typing import List, Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        target_paths: List[List[int]] = list()

        def helper(node: TreeNode, slate: List[int], target: int):
            if node is None:
                return False
            # Base case
            if node.left is None and node.right is None:
                if node.val == target:
                    slate.append(node.val)
                    target_paths.append(slate[:])
                    slate.pop()
                return

            # Recursive Case
            if node.left:
                slate.append(node.val)
                helper(node.left, slate, target-node.val)
                slate.pop()
            if node.right:
                slate.append(node.val)
                helper(node.right, slate, target-node.val)
                slate.pop()

        helper(root, [], targetSum)
        return target_paths


sol = Solution()


# print('.........Test_Case_1...........')
# input = [5,4,8,11,None,13,4,7,2,None,None,5,1]
# display(build_tree(input))


print('.........Test_Case_1...........')
input = '[5,4,8,11,None,13,4,7,2,None,None,5,1]'
display(build_tree(input))
root = build_tree(input)
targetSum = 22
print('pathSum', sol.pathSum(root, targetSum))
