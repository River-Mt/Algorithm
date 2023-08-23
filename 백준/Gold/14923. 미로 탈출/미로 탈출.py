import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def solve():
    n, m = map(int, input().split())
    hx, hy = map(int, input().split())
    hx -= 1
    hy -= 1
    ex, ey = map(int, input().split())
    ex -= 1
    ey -= 1
    miro = [list(map(int, input().split())) for _ in range(n)]
    dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]

    def is_exit(r, c):
        return r == ex and c == ey

    def is_visit(r, c, m, dist):
        return dist[r][c][m] != -1

    def is_over(r, c):
        return r < 0 or c < 0 or r >= n or c >= m

    def is_not_wall(r, c):
        return miro[r][c] == 0

    def is_wall(r, c):
        return miro[r][c] == 1

    def bfs():
        q = deque([])
        dist = [[[-1 for _ in range(2)] for _ in range(m)] for _ in range(n)]
        q.append([hx, hy, 0])
        dist[hx][hy][0] = 0

        while q:
            now = q.popleft()
            r, c = now[0], now[1]
            used_wand = now[2]

            if is_exit(r, c):
                return dist[r][c][used_wand]

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                
                # 탐색 범위 초과 or 이미 방문했다면 continue
                if is_over(nr, nc) or is_visit(nr, nc, used_wand, dist):
                    continue
                
                # 다음 칸이 벽이 아닐 경우
                if is_not_wall(nr, nc):
                    dist[nr][nc][used_wand] = dist[r][c][used_wand] + 1
                    q.append([nr, nc, used_wand])
                
                # 다음 칸이 벽이고, 아직 벽을 통과하지 않았을 경우
                if is_wall(nr, nc) and not used_wand:
                    dist[nr][nc][1] = dist[r][c][0] + 1
                    q.append([nr, nc, 1])

        return -1

    return bfs()


print(solve())
