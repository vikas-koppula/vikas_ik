"""
LeetCode 200
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

from collections import deque
from typing import List, Set, Deque, Tuple


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited: Set[Tuple[int,int]] = set()
        num_islands = 0

        def get_nbrs(m: int, n: int, grid):
            nbrs = []
            if m - 1 >= 0:
                nbrs.append((m - 1, n))
            if n - 1 >= 0:
                nbrs.append((m, n - 1))
            if m + 1 <= len(grid) - 1:
                nbrs.append((m + 1, n))
            if n + 1 <= len(grid[0]) - 1:
                nbrs.append((m, n + 1))
            return nbrs

        def bfs(x: int, y: int):
            visited.add((x, y))
            dq: Deque = deque()
            dq.appendleft((x,y))
            while bool(dq):
                m, n = dq.pop()
                for a,b in get_nbrs(m, n, grid):
                    if (a, b) not in visited and grid[a][b] == "1":
                        visited.add((a, b))
                        dq.appendleft((a, b))

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x, y) not in visited and grid[x][y] == "1":
                    num_islands+=1
                    bfs(x, y)
        return num_islands


grid_1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid_2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]


sol = Solution()

print("Grid 1:", grid_1)
print("sol:", sol.numIslands(grid_1))

print("Grid 2:", grid_2)
print("sol:", sol.numIslands(grid_2))
