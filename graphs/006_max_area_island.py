"""
Leetcode 695
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally
(horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.

Input: grid = [ [0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
"""
from collections import deque
from typing import List, Set, Deque, Tuple

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited: Set[Tuple[int, int]] = set()
        max_island_area = 0
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

        def bfs_island_area(m: int, n: int, grid) -> int:
            visited.add((m, n))
            dq = deque()
            dq.append((m, n))
            local_area = 1
            while bool(dq):
                a, b = dq.popleft()
                for x, y in get_nbrs(a, b, grid):
                    if (x, y) not in visited and grid[x][y] == 1:
                        visited.add((x,y))
                        dq.appendleft((x,y))
                        local_area += 1
            return local_area

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x,y) not in visited and grid[x][y] == 1:
                    island_area = bfs_island_area(x, y, grid)
                    if island_area > max_island_area:
                        max_island_area = island_area

        return max_island_area


grid_1 = [      [0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0] ]

grid_2 = [[0,0,0,0,0,0,0,0]]

grid_3 = [
                [1,0,1,0,0],
                [1,1,1,0,0],
                [0,0,1,0,0]]


sol = Solution()

print("Grid 1:", grid_1)
print("sol:", sol.maxAreaOfIsland(grid_1))

print("Grid 2:", grid_2)
print("sol:", sol.maxAreaOfIsland(grid_2))

print("Grid 3:", grid_3)
print("sol:", sol.maxAreaOfIsland(grid_3))
