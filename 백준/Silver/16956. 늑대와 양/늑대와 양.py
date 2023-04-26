import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for i in range(n)]
sheeps = []
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'S':
            sheeps.append((i, j))

for (r, c) in sheeps:
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if nr < 0 or nc < 0 or nr >= n or nc >= m or board[nr][nc] == 'S' or board[nr][nc] == 'D':
            continue
        if board[nr][nc] == 'D':
            continue
        if board[nr][nc] == 'W':
            print(0)
            exit()

        board[nr][nc] = 'D'

print(1)

for i in range(n):
    for j in range(m):
        print(f"{board[i][j]}", end="")
    print()
