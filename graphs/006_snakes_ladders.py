"""
LeetCode 909
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting
from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder
is board[r][c]. Squares 1 and n2 do not have a snake or ladder.
Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of
another snake or ladder, you do not follow the subsequent snake or ladder
Example 1:
Input: board = [[-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1],
                [-1,35,-1,-1,13,-1],
                [-1,-1,-1,-1,-1,-1],
                [-1,15,-1,-1,-1,-1]]
Output: 4

Example 2:
Input: board = [[-1,-1],[-1,3]]
Output: 1
"""
from collections import deque
from typing import List, Set, Deque, Dict


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board_rows = len(board)
        row_len = len(board[0])
        visited: Set[int] = set()
        target = len(board) ** 2

        def grid_lookup(num, grid):
            q, r = divmod(num - 1, row_len)
            row_num = board_rows - q - 1
            cell_val = grid[row_num][r] if q % 2 == 0 else grid[row_num][-(r + 1)]
            return cell_val

        def bfs_least_hops():
            start = 0
            dq = deque()
            dq.append(start)
            visited.add(start)
            level: [Dict[int, int]] = dict()
            level[start] = 0
            while bool(dq):
                num = dq.pop()
                for dice_val in range(1,7):
                    nbr = dice_val + num
                    cell_val = grid_lookup(nbr, board)
                    nbr = nbr if cell_val == -1 else cell_val

                    if nbr not in visited:
                        visited.add(nbr)
                        dq.appendleft(nbr)
                        level[nbr] = level.get(num) + 1
                    if nbr == target:
                        return level[nbr]

            return 0

        return bfs_least_hops()



grid_1 = [[-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1],
          [-1,35,-1,-1,13,-1],
          [-1,-1,-1,-1,-1,-1],
          [-1,15,-1,-1,-1,-1]]

grid_2 = [[-1,-1],[-1,3]]

grid_3 = [[-1,1,2,-1],
          [2,13,15,-1],
          [-1,10,-1,-1],
          [-1,6,2,8]]

sol = Solution()

print("Grid 1:", grid_1)
print("sol:", sol.snakesAndLadders(grid_1))

print("Grid 2:", grid_2)
print("sol:", sol.snakesAndLadders(grid_2))

print("Grid 3:", grid_3)
print("sol:", sol.snakesAndLadders(grid_3))