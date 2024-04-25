"""
108. Convert Sorted Array to Binary Search Tree
Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced binary search tree.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
"""
from util.display_tree import display
from util.treenode import TreeNode, build_tree
from typing import List, Optional


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(arr: List[int], s: int, e: int) -> TreeNode:
            if s > e:
                return None
            if s == e:
                return TreeNode(None, None, arr[s])
            mid = s + int((e-s)/2)
            root = TreeNode(None, None, arr[mid])
            root.left = helper(arr, s, mid-1)
            root.right = helper(arr, mid+1, e)
            return root
        return helper(nums, 0, len(nums)-1)


sol = Solution()
print('.........Test_Case_1...........')
input = [-10, -3, 0, 5, 9]
root = sol.sortedArrayToBST(input)
display(root)
print('sortedArrayToBST:\n', sol.sortedArrayToBST(input))
