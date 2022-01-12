from collections import deque
from display_tree import display
from node import Node
from typing import List


def level_order_traversal(root: Node) -> List[List[Node]]:
    levels: list = []
    dq = deque()  # FIFO through popleft
    dq.append(root)
    # While there are nodes in the queue, iterate over them
    while dq:
        # size is used to determine how many nodes there are for a particular level and set boundaries
        size = len(dq)
        level: list = []
        # if there are 3 nodes in the level, then 2nd while loop will execute 3 times, once for each node
        #
        while size > 0:
            node: Node = dq.popleft()
            # Decrement to exit at level boundary
            size -= 1
            # add left child if exists to dq
            if node.left:
                dq.append(node.left)
            # add right child if exists to dq
            if node.right:
                dq.append(node.right)
            level.append(node.val)
        levels.append(level)
    return levels


# bottom-up level order
def reverse_level_order_traversal(root: Node) -> List[List[Node]]:
    if root is None:
        return []
    q = deque() # FIFO queue
    q.append(root)
    levels = []
    while q:
        size = len(q)
        level = []
        while size > 0:
            size -= 1
            node = q.popleft()
            level.append(node.val)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        levels.append(level)
    levels.reverse()
    return levels


"""       5
         / \
        /   \
       3     7
        \   / \
         4 6   8
              /
             9 
"""


def test():
    top_left_right = Node(None, None, 4)
    top_left = Node(None, top_left_right, 3)

    top_right_right_left = Node(None, None, 9)
    top_right_right = Node(top_right_right_left, None, 8)
    top_right_left = Node(None, None, 6)
    top_right = Node(top_right_left, top_right_right, 7)
    top_node =  Node(top_left, top_right, 5)
    display(top_node)
    print("-------------------")
    print("top down levels")

    levels = level_order_traversal(top_node)
    print(levels)

    print("-------------------")
    print("bottom up levels")

    levels = reverse_level_order_traversal(top_node)
    print(levels)


if __name__ == "__main__":
    test()
