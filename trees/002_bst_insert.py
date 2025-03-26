"""
701. Insert into a Binary Search Tree
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of
the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
You can return any of them.

Example 1:
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]

Example 1:
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
"""

from util.display_tree import display
from util.treenode import TreeNode, build_tree
from typing import Optional

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Create a new Treenode for the insert
        ins_node: TreeNode = TreeNode(val,None, None)
        curr: TreeNode = root
        # Edge case: If the root is null, then return the node to be inserted as the root
        if root is None:
            return ins_node
        # Starting with the root node, check if the target is less than or greater than the current val.
        # Iterate to the left node or right node till the curr becomes null.
        # For this problem we need to maintain the prev node and curr is expected to go null
        prev = None
        while curr is not None:
            if val < curr.val:
                prev = curr
                curr = curr.left
            else:
                prev  = curr
                curr = curr.right
        # While loop has exited, we have reached a null node as the prev node didnt have a left or right child
        # We need to now use prev to assign the new node to the prev node
        if val < prev.val:
            prev.left = ins_node
        else:
            prev.right = ins_node
        return root




sol = Solution()

print('.........Test_Case_1...........')
input = '[4,2,7,1,3]'
val = 5
display(build_tree(input))
root = build_tree(input)
print('Search: ', sol.insertIntoBST(root, val))

print('.........Test_Case_2...........')
input = '[8,null,55,39,null,11,null,null,23,null,null]'
val = 17
display(build_tree(input))
root = build_tree(input)
print('Search: ', sol.insertIntoBST(root, val))

print('.........Test_Case_3...........')
input = '[5,null,14,10,77,null,null,null,95,null,null]'
val = 4
display(build_tree(input))
root = build_tree(input)
print('Search: ', sol.insertIntoBST(root, val))
