"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to
find the number of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.
"""
import logging
from collections import deque
from typing import List, Set, Deque


def num_conn_comp(n: int, edges: List[list]):

    # Initialize a visited list to keep track of the vertex visited so far
    visited = [-1] * n
    # First build an adj list
    adj_list: List[Set[int]] = [set() for i in range(5)]
    for src, dest in edges:
        adj_list[src].add(dest)
        adj_list[dest].add(src)
    print("adj_list:", adj_list)
    num_connected: int = 0

    def bfs_traversal(node: int):
        # Mark this node as visited, this will be the source node of the traversal
        visited[node] = 1
        dq: Deque = deque()
        dq.appendleft(node)
        # While there are elements in the queue, visit the neighbors
        while bool(dq):
            x = dq.pop()
            # Mark this source traversal node as visited
            visited[x] = 1
            # Look up neighbors from the adj list and add them to the queue
            for node in adj_list[x]:
                # We shouldn't add already visited nodes to the queue to avoid circular infinite traversal
                if visited[node] != 1:
                    dq.appendleft(node)
        return

    # Outer loop
    for x in range(n):
        # Start bfs traversal if the node hasn't been visited yet
        # If there is only one connected graph, then the bfs traversal will be invoked just once
        if visited[x] != 1:
            bfs_traversal(x)
            num_connected += 1
    return num_connected


def test():
    # Case 1
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    """
    0          3
    |          |
    1 --- 2    4
    """
    case_1 = num_conn_comp(n=5, edges=edges)
    print("case 1 num connected components:", case_1)

    # Case 2
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    """
    0           4
    |           |
    1 --- 2 --- 3
    """
    case_2 = num_conn_comp(n=5, edges=edges)
    print("case 2 num connected components:", case_2)


if __name__ == "__main__":
    test()
