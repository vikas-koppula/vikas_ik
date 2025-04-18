"""
199. Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you
can see ordered from top to bottom.
Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []
"""
from collections import deque
from util.display_tree import display
from util.treenode import TreeNode, build_tree
from typing import List, Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = list()
        dq = deque()
        if root is None:
            return []
        dq.append(root)
        while bool(dq):
            lvl_cnt = len(dq)
            rigth_most: int = 0
            for _ in range(lvl_cnt):
                node: TreeNode = dq.popleft()
                rigth_most = node.val
                if node.left is not None:
                    dq.append(node.left)
                if node.right is not None:
                    dq.append(node.right)
            # At the end of each level traversal, append the last popped node to the result for this level
            result.append(rigth_most)
        return result


sol = Solution()

print('.........Test_Case_1...........')
input = [1,2,3,None,5,None,4]
display(build_tree(input))
root = build_tree(input)
print('Level Order:\n', sol.rightSideView(root))
print('.........Test_Case_2...........')
input = [1,None,3]
display(build_tree(input))
root = build_tree(input)
print('Level Order:\n', sol.rightSideView(root))
