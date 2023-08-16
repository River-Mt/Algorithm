import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def solve():
    n, m = map(int, input().split())
    arr = [[] for _ in range(n)]
    for i in range(n):
        tmp = list(map(int, input().split()))
        idx = 0
        while idx < m * 3:
            avg = sum(tmp[idx: idx + 3]) // 3
            arr[i].append(avg)
            idx += 3

    t = int(input())

    for i in range(n):
        for j in range(m):
            if arr[i][j] >= t:
                arr[i][j] = 1
            else:
                arr[i][j] = 0

    chk = [[0 for _ in range(m)] for _ in range(n)]
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    def is_over(r, c):
        if r < 0 or r >= n or c < 0 or c >= m:
            return True
        else:
            return False

    def dfs(r, c):
        chk[r][c] = 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_over(nr, nc) or chk[nr][nc] or arr[nr][nc] == 0:
                continue
            dfs(nr, nc)

    ans = 0

    for i in range(n):
        for j in range(m):
            if not chk[i][j] and arr[i][j]:
                dfs(i, j)
                ans += 1

    return ans


print(solve())
