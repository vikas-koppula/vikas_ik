"""
LeetCode 909
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting
from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder
is board[r][c]. Squares 1 and n2 do not have a snake or ladder.
Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of
another snake or ladder, you do not follow the subsequent snake or ladder
Example 1:
Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],
                [-1,15,-1,-1,-1,-1]]
Output: 4

Example 2:
Input: board = [[-1,-1],[-1,3]]
Output: 1
"""
from collections import deque
from typing import List, Set, Deque


def snakes_ladders(board: List[List[int]]):
    board.reverse()
    target = len(board) * len(board)
    visited = [-1] * (target+1)
    level = [0] * (target+1)

    def get_index(num):
        n = len(board)
        q, mod = divmod(num - 1, n)
        if q % 2 == 0:
            return board[q][mod]
        else:
            return board[q][-(mod + 1)]

    def bfs(src):
        dq: Deque = deque()
        dq.appendleft(src)
        visited[src] = 1
        level[src] = 0
        while bool(dq):
            node = dq.pop()
            for dice_val in range(1, 7):
                dest = node + dice_val
                nbr = dest if get_index(dest) == -1 else get_index(dest)

                if visited[nbr] == -1:
                    visited[nbr] = 1
                    level[nbr] = level[node] + 1
                    dq.appendleft(nbr)
                    if nbr == target:
                        return level[nbr]
                else:
                    print('Already visited, nbr:', nbr)
        return -1
    level = bfs(1)
    return level


board = [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 15, -1, -1, -1, -1]]
print("case 1 snakes and ladders:", snakes_ladders(board))

# board = [[-1, -1], [-1, 3]]
# print("case 2 num islands:", snakes_ladders(board))
