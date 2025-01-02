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
from typing import List, Set, Deque


def num_islands(grid: List[List[str]]):
    visited: Set = set()
    num = 0

    def get_nbrs(m: int, n: int, grid):
        nbrs = [(x, y) for x, y in [(m - 1, n), (m, n + 1), (m + 1, n), (m, n - 1)]
                if int(x) in range(len(grid)) and int(y) in range(len(grid[0]))]
        return nbrs

    def bfs(x: int, y: int):
        dq: Deque = deque()
        dq.appendleft((x, y))
        visited.add((x, y))
        while bool(dq):
            a, b = dq.pop()
            for m, n in get_nbrs(a, b, grid):
                if (m, n) not in visited and grid[m][n] == "1":
                    visited.add((m, n))
                    dq.appendleft((m, n))

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) not in visited and grid[x][y] == "1":
                bfs(x, y)
                num += 1

    return num


grid_1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print("case 1 num islands:", num_islands(grid_1))

grid_2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print("case 2 num islands:", num_islands(grid_2))
