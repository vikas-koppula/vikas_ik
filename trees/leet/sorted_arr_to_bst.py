"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced binary search tree.
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
"""

from util.display_tree import display, insertLevelOrder
from util.treenode import TreeNode
from typing import List, Optional


def sorted_arr_to_bst(nums: List[int]) -> Optional[TreeNode]:
    def helper(nums: List[int], start: int, end: int):
        # Leaf node children case
        if start > end:
            return None
        # Leaf node case
        if start == end:
            return TreeNode(left=None, right=None, val=nums[start])
        # Recursive case
        mid = int((start + end)/2)

        lh_treenode = helper(nums, start, mid-1)
        rh_treenode = helper(nums, mid+1, end)
        curr_treenode = TreeNode(val=nums[mid], left=lh_treenode, right=rh_treenode)
        return curr_treenode

    root_node: TreeNode = helper(nums, 0, len(nums)-1)
    return root_node


def test():
    nums = [-10, -3, 0, 5, 9]

    bst = sorted_arr_to_bst(nums)

    display(bst)
    print("-------------------")


if __name__ == "__main__":
    test()
