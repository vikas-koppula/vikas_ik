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
from typing import List, Deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        # Distance or level list is needed to detemine the distance of a vertex from the root node
        #level_list: List[int] = [0] * n
        parent_list: List[int] = [-1] * n
        # Adjacency list isnt needed as it has been provided already

        def bfs_check(root: int):

            level_list: List[int] = [0] * n
            # Set the root vertex as level 0
            level_list[root] = 0
            # Root vertex cannot have a parent, hence set it to itself. Otherwise code doesnt work, as it will be
            # considered as not visited, which isn't accurate
            parent_list[root] = root
            dq: Deque = deque()
            dq.appendleft(root)

            while bool(dq):
                node = dq.pop()
                for nbr in graph[node]:
                    # Parent not being set for the nbr indicates that the nbr is being visited for the first time
                    if parent_list[nbr] == -1:
                        parent_list[nbr] = node
                        level_list[nbr] = level_list[node] + 1
                        dq.appendleft(nbr)
                    elif parent_list[node] == nbr:
                        None
                    else:
                        # Cycle exists
                        # Bipartite if an odd cycle
                        if level_list[nbr] == level_list[node]:
                            return False
            return True
        # Outer loop is important as we need to make sure that if there are multiple connected components,
        # then all those graphs are still bipartite
        for x in range(n):
            if parent_list[x] == -1:
                if bfs_check(x) is False:
                    return False
        return True

sol = Solution()
graph_1 = [[1,2,3],[0,2],[0,1,3],[0,2]]
graph_2 = [[1,3],[0,2],[1,3],[0,2]]
graph_3 = [[3],[2,4],[1],[0,4],[1,3]]

print("graph 1:", graph_1)
print("sol:", sol.isBipartite(graph_1))

print("graph 2:", graph_2)
print("sol:", sol.isBipartite(graph_2))

print("graph 3:", graph_3)
print("sol:", sol.isBipartite(graph_3))
