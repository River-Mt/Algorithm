import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
ans = 2505


def solve():
    global ans
    n, m = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(n)]
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    def get_virus_loc_list(arr):
        virus_list = []
        rows, cols = len(arr), len(arr[0])

        for i in range(rows):
            for j in range(cols):
                if arr[i][j] == 2:
                    virus_list.append([i, j])

        return virus_list

    def is_over(r, c):
        if r < 0 or c < 0 or r >= n or c >= n:
            return True
        else:
            return False

    def bfs(v_list):
        q = deque([])
        dist = [[-1 for _ in range(n)] for _ in range(n)]
        max_dist = 0

        for loc in v_list:
            q.append(loc)
            dist[loc[0]][loc[1]] = 0

        while q:
            now = q.popleft()
            r, c = now[0], now[1]
            max_dist = max(dist[r][c], max_dist)

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                if is_over(nr, nc) or dist[nr][nc] != -1:
                    continue

                if lab[nr][nc] == 1:
                    continue

                dist[nr][nc] = dist[r][c] + 1
                q.append([nr, nc])

        for i in range(n):
            for j in range(n):
                if dist[i][j] == -1 and lab[i][j] != 1:
                    return 2505

        return max_dist

    virus_locs = get_virus_loc_list(lab)

    def select_virus(now, selected, v_list):
        global ans
        if selected == m:
            if not len(v_list):
                return
            ans = min(bfs(v_list), ans)
            return

        if now >= len(virus_locs):
            return

        select_virus(now + 1, selected, v_list)
        select_virus(now + 1, selected + 1, v_list + [virus_locs[now]])

    select_virus(0, 0, [])
    return ans if ans != 2505 else -1


print(solve())
