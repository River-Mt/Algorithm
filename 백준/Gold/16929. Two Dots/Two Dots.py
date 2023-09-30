from sys import stdin

input = stdin.readline

dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)


def dfs(r, c, color, br, bc, cnt):
    if check[r][c] and cnt >= 4:
        print("Yes")
        exit(0)

    check[r][c] = 1

    for d in range(4):
        nr, nc = r + dr[d],  c + dc[d]

        if not (0 <= nr < n and 0 <= nc < m) or board[nr][nc] != color or (nr, nc) == (br, bc):
            continue

        dfs(nr, nc, color, r, c, cnt + 1)


n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
check = [[0] * m for _ in range(n)]

for r in range(n):
    for c in range(m):
        if not check[r][c]:
            dfs(r, c, board[r][c], -1, -1, 0)
print("No")
