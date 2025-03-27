"""
285. Inorder Successor in BST
Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST.
If the given node has no in-order successor in the tree, return null.
The successor of a node p is the node with the smallest key greater than p.val.

Example 1:
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

Example 2:
Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
"""
from util.display_tree import display
from util.treenode import TreeNode, build_tree
from typing import Optional

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        curr = root
        if curr is None:
            return curr
        succ = None
        # Strategy here is that we are going to start search from the root and use the properties of the BST.
        # curr val <= the target => the successor will only be in the right subtree. hence iterate. Ignore left subtree
        # Curr val > the target => this is a potential successor. Will still need to iterate on the left subtree to find
        # if there is a closer successor. Can ignore the right subtree
        while curr is not None:
            if curr.val > p.val:
                succ = curr.val
                curr = curr.left
            # Import to include equal to condition, otherwise will not find the successor if the target == root val
            elif curr.val <= p.val:
                curr = curr.right
        return succ

sol = Solution()

print('.........Test_Case_1...........')
input = '[2,1,3]'
p = 1
display(build_tree(input))
root = build_tree(input)
print('inorderSuccessor: ', sol.inorderSuccessor(root, TreeNode(p, None, None)))

print('.........Test_Case_2...........')
input = '[5,3,6,2,4,null,null,1]'
p = 6
display(build_tree(input))
root = build_tree(input)
print('inorderSuccessor: ', sol.inorderSuccessor(root, TreeNode(p, None, None)))

print('.........Test_Case_3...........')
input = '[2,null,3]'
p = 2
display(build_tree(input))
root = build_tree(input)
print('inorderSuccessor: ', sol.inorderSuccessor(root, TreeNode(p, None, None)))
