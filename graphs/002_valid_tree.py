"""
LeetCode 261
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to
check whether these edges make up a valid tree.
Example 1
Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
                            0
                          / | \
                         1  2  3
                         |
                         4
Output: true

Example 2
Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
                             0----1----2
                                  | \  |
                                  |  \ |
                                  4    3
Output: false

"""
from collections import deque
from typing import List, Set, Deque


def valid_graph(n: int, edges: List[list]):
    # A graph is valid if there are no unconnected components and if there are no cycles (cross edges)
    # Initialize a visited list to keep track of the vertex visited so far
    visited = [-1] * n
    # First build an adj list
    adj_list: List[Set[int]] = [set() for i in range(5)]
    for src, dest in edges:
        adj_list[src].add(dest)
        adj_list[dest].add(src)
    print("adj_list:", adj_list)
    num_connected: int = 0
    # While traversing we need to populate the parent child relation of the nodes. An already visited node is not a
    # cross edge if that node is the parent of the current node.
    parent_list: List[int] = [-1] * n

    def dfs_cycle_check(root: int):
        visited[root] = 1

        print("Current Node:", str(root))
        for nbr in adj_list[root]:
            if visited[nbr] != 1:
                parent_list[nbr] = root
                dfs_cycle_check(nbr)
            elif parent_list[root] == nbr:
                print("Do nothing," + str(nbr) + " is the parent of current node" + str(root))
            else:
                print("Cross edge. " + str(nbr) + " already visited before current node:" + str(root))
                return False
        return True

    def bfs_traversal(src_vertex: int):
        # Mark this node as visited, this will be the source node of the traversal
        visited[src_vertex] = 1
        dq: Deque = deque()
        dq.appendleft(src_vertex)
        # While there are elements in the queue, visit the neighbors
        while bool(dq):
            x = dq.pop()
            print("Current Node:", str(x))
            # Look up neighbors from the adj list and add them to the queue
            for nbr in adj_list[x]:
                # We shouldn't add already visited nodes to the queue to avoid circular infinite traversal
                if visited[nbr] != 1:
                    # Mark this neighbor node as visited
                    visited[nbr] = 1
                    dq.appendleft(nbr)
                    # Mark the neighbors parent as the current node, x
                    parent_list[nbr] = x
                elif parent_list[x] == nbr:
                    print("Do nothing," + str(nbr) + " is the parent of current node" + str(x))
                else:
                    # Return false to indicate that the graph has a cycle
                    print("Cross edge. " + str(nbr) + " already visited before current node:" + str(x))
                    return False
        return True

    # Outer loop
    for node in range(n):
        # Start bfs traversal if the node hasn't been visited yet
        # If there is only one connected graph, then the bfs traversal will be invoked just once
        if visited[node] != 1:
            # BFS Traversal
            graph_no_cycle = dfs_cycle_check(node)
            if graph_no_cycle is False:
                return False
            num_connected += 1
    print("No Cycles, num of connected components:", str(num_connected))
    return True if num_connected == 1 else False


def test():
    # Case 1
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

    case_1 = valid_graph(n=5, edges=edges)
    print("case 1 valid graph:", case_1)

    # Case 2
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

    case_2 = valid_graph(n=5, edges=edges)
    print("case 2 valid graph:", case_2)


if __name__ == "__main__":
    test()
