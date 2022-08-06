"""
LeetCode 785
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array
graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u],
there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the
graph connects a node in set A and a node in set B
"""
from collections import deque
from typing import List, Set, Deque


def is_bipartite_graph(adj_list: List[List[int]]):

    visited: List[int] = [-1] * len(adj_list)
    num_connected: int = 0
    parent_list: List[int] = [-1] * len(adj_list)
    length_list: List[int] = [0] * len(adj_list)

    def bfs_traversal(source: int):
        visited[source] = 1
        dq: Deque = deque()
        dq.appendleft(source)

        while bool(dq):
            popped_node = dq.pop()
            print("Popped node:", str(popped_node))
            for nbh in adj_list[popped_node]:
                print("nbh = ", str(nbh))
                if visited[nbh] == -1:
                    visited[nbh] = 1
                    dq.appendleft(nbh)
                    print(str(nbh) + " is a tree node, to" + str(popped_node))
                    parent_list[nbh] = popped_node
                    length_list[nbh] = length_list[popped_node] + 1
                    print("length nbh:" + str(length_list[nbh]) + " length popped:" + str(length_list[popped_node]))
                elif parent_list[popped_node] == nbh:
                    print("nbh is parent of the popped node")
                else:
                    # This is a cross edge
                    print("This is a cross edge, check even cycle or odd cycle")
                    if length_list[nbh] == length_list[popped_node]:
                        print("length nbh:" + str(length_list[nbh]) + " length popped:" + str(length_list[popped_node]))
                        print("This is an odd cycle, hence graph cannot be bipartite")
                        return False
                    else:
                        print("length nbh:" + str(length_list[nbh]) + " length popped:" + str(length_list[popped_node]))
                        print("This is an even cycle, hence graph can be bipartite")
        # return true indicates that no odd cycle was detected
        return True
    for node in range(len(adj_list)):
        if visited[node] == -1:
            is_bipartite: bool = bfs_traversal(node)
            # If any of the connected components are not bipartite, then the whole graph is not bipartite
            if is_bipartite is False:
                print("Return False as graph is not bipartite with source node:", node)
                return False
    return True


def test():
    # Case 1
    adj_list = [[1, 2], [0], [0]]
    """
    1
    |
    0 -- 2
    """
    case_1 = is_bipartite_graph(adj_list=adj_list)
    print("case 1 is bipartite:", case_1)
    print('...............................................................................')
    # Case 2
    adj_list = [[1, 2], [0], [1]]
    """
    1
    |  \
    0 -- 2
    """
    case_2 = is_bipartite_graph(adj_list=adj_list)
    print("case 2 is bipartite:", case_2)
    print('...............................................................................')
    # Case 3
    adj_list = [[1, 3], [0, 2], [1, 3], [0, 2]]
    """
    0----1
    |    |
    3----2
    """
    case_3 = is_bipartite_graph(adj_list=adj_list)
    print("case 3 is bipartite:", case_3)
    print('...............................................................................')
    # Case 4
    adj_list = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    """
    0----1
    |  \ |
    3----2
    """
    case_4 = is_bipartite_graph(adj_list=adj_list)
    print("case 4 is bipartite:", case_4)


if __name__ == "__main__":
    test()
