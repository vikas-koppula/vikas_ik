"""
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to
right, level by level from leaf to root).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
"""
from collections import deque
from util.display_tree import display
from util.treenode import TreeNode, build_tree
from typing import List, Optional


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: List[List[int]] = list()
        dq = deque()
        if root is None:
            return []
        dq.append(root)
        while bool(dq):
            lvl_cnt = len(dq)
            tmp: List[int] = list()
            for _ in range(lvl_cnt):
                node: TreeNode = dq.popleft()
                tmp.append(node.val)
                if node.left is not None:
                    dq.append(node.left)
                if node.right is not None:
                    dq.append(node.right)
            result.append(tmp[:])
        result.reverse()
        return result


sol = Solution()

print('.........Test_Case_1...........')
input = [3,9,20,None,None,15,7]
display(build_tree(input))
root = build_tree(input)
print('Level Order:\n', sol.levelOrderBottom(root))
print('.........Test_Case_2...........')
input = [1]
display(build_tree(input))
root = build_tree(input)
print('Level Order:\n', sol.levelOrderBottom(root))
