"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to
right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        dq = deque()
        result: List[List[int]] = list()
        dq.append(root)
        flag: bool = False
        while bool(dq):
            flag = not flag
            tmp: List[int] = list()
            for _ in range(len(dq)):
                node = dq.popleft()
                tmp.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            if bool(flag):
                tmp.reverse()
            result.append(tmp)
        return result


sol = Solution()
print('.........Test_Case_1...........')
input = [3,9,20,None,None,15,7]
display(build_tree(input))
root = build_tree(input)
print('Level Order:\n', sol.zigzagLevelOrder(root))
print('.........Test_Case_2...........')
input = [1]
display(build_tree(input))
root = build_tree(input)
print('Level Order:\n', sol.zigzagLevelOrder(root))
