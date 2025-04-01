"""
450. Delete Node in a BST
Given a root node reference of a BST and a key, delete the node with the given key in the BST.
Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
1) Search for a node to remove.
2) If the node is found, delete the node.

Example 1:
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:
Input: root = [], key = 0
Output: []
"""
from util.display_tree import display
from util.treenode import TreeNode, build_tree
from typing import Optional

class Solution:

    def successor(self, root: TreeNode) -> int:
        curr: TreeNode = root.right
        while curr.left:
            curr = curr.left
        return curr.val

    def predecessor(self, root: TreeNode) -> int:
        curr: TreeNode = root.left
        while curr.right:
            curr = curr.right
        return curr.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        # Standard edge case check on a null node
        if root is None:
            return root

        # Navigate the left or right subtree to get to the node to be deleted
        # Propagate the delete function down the subtrees.
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Found the node to be deleted. Now we have 3 conditions.
            # 1. Leaf node. Then just make the node null and return the null to the calling function
            if root.left is None and root.right is None:
                root = None
            # 2. Node has a right subtree: Find the successor. Copy the successor val to node and then del the successor
            # Note: The node can have a left subtree. If it also has a right subtree, then we need to replace deleted
            # node with the successor, which would be in the right subtree. We can just leave the left subtree as is.
            elif root.right is not None:
                # Copy the value of the successor to the root node to be deleted
                root.val = self.successor(root)
                # We now need to delete the successor. Look for the successor in the right subtree and delete it
                # Leaf left subtree as is, if it does exist
                # root.val works here because of the overwrite the line before.
                # root.val is now the value of the successor we are trying to delete
                root.right = self.deleteNode(root.right, root.val)
            # 3. Node has a left subtree: Find the predecessor, but only look down the tree. Dont look up the tree.
            # Copy the predecessor val to node and then del the predecessor
            elif root.left is not None:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root

sol = Solution()

print('.........Test_Case_1...........')
input = '[5,3,6,2,4,null,7]'
key = 3
display(build_tree(input))
root = build_tree(input)
print('inorderSuccessor: ', sol.deleteNode(root, key))
