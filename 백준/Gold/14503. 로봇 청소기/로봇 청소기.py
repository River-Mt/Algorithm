import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# N E S W
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
cnt = 1
board[r][c] = -1

while True:
    is_empty = False

    for i in range(4):
        nd = ((d - 1) + 4) % 4
        nr = r + directions[nd][0]
        nc = c + directions[nd][1]
        d = nd
        if board[nr][nc] == 0:
            r = nr
            c = nc
            board[nr][nc] = -1
            is_empty = True
            cnt += 1
            break

    if not is_empty:
        br = r - directions[d][0]
        bc = c - directions[d][1]

        if board[br][bc] == 1:
            break

        else:
            r = br
            c = bc


print(cnt)