import copy
import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
ans = sys.maxsize

def solve():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    # N E S W
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    directions = [
        [],
        [[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [0, 3]],
        [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
        [[0, 1, 2, 3]]
    ]

    def is_cctv(r, c):
        return 1 <= board[r][c] <= 5

    def is_wall(r, c):
        return board[r][c] == 6

    def is_over(r, c):
        return r < 0 or c < 0 or r >= n or c >= m

    def can_go(r, c):
        if is_over(r, c) or is_wall(r, c):
            return False
        else:
            return True

    def check_saw(direct, copied, r, c):
        for d in direct:
            cur_r, cur_c = r, c
            while True:
                nr, nc = cur_r + dr[d], cur_c + dc[d]
                if not can_go(nr, nc):
                    break
                copied[nr][nc] = -1
                cur_r, cur_c = nr, nc

    def count_blinds(grid):
        blinds = 0

        for row in grid:
            blinds += row.count(0)

        return blinds

    cctv_locations = []

    for i in range(n):
        for j in range(m):
            if is_cctv(i, j):
                cctv_locations.append([i, j])

    def dfs(now, grid):
        global ans

        if now == len(cctv_locations):
            ans = min(ans, count_blinds(grid))
            return

        copied = copy.deepcopy(grid)
        r, c = cctv_locations[now]
        cctv_no = board[r][c]

        for d in directions[cctv_no]:
            check_saw(d, copied, r, c)
            dfs(now + 1, copied)
            copied = copy.deepcopy(grid)

    dfs(0, board)
    return


solve()
print(ans)
