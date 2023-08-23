import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def get_start_loc_and_fish_locations(sea, n):
    fishes = []
    sr, sc = 0, 0
    for i in range(n):
        for j in range(n):
            if sea[i][j] == 9:
                sr, sc = i, j
                sea[i][j] = 0

            if sea[i][j] != 0 and sea[i][j] != 9:
                fishes.append([i, j])
    return sr, sc, fishes


def is_over(r, c, n):
    return r < 0 or c < 0 or r >= n or c >= n


def can_go(fish_size, shark_size):
    return shark_size >= fish_size


def can_eat(fish_size, shark_size):
    return shark_size > fish_size


def get_next_shark_info(sea, n, dir, shark_info):
    q = deque([])
    sr, sc, shark_size, shark_run, eat_cnt = shark_info
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    q.append([sr, sc])
    dist[sr][sc] = 0
    max_dist = 10000000

    while q:
        r, c = q.popleft()

        for d in dir:
            nr, nc = r + d[0], c + d[1]

            if is_over(nr, nc, n) or dist[nr][nc] != -1 or not can_go(sea[nr][nc], shark_size):
                continue

            dist[nr][nc] = dist[r][c] + 1
            q.append([nr, nc])

    min_dist = max_dist
    nsr, nsc = sr, sc

    for i in range(n):
        for j in range(n):
            if 1 <= sea[i][j] <= 6:
                if dist[i][j] != -1 and min_dist > dist[i][j] and can_eat(sea[i][j], shark_size):
                    min_dist = dist[i][j]
                    nsr, nsc = i, j

    if min_dist == max_dist:
        return [-1, -1, -1, shark_run]

    else:
        sea[nsr][nsc] = 0
        eat_cnt += 1

        if eat_cnt == shark_size:
            shark_size += 1
            eat_cnt = 0

        return [nsr, nsc, shark_size, shark_run + min_dist, eat_cnt]


def solve():
    n = int(input())
    sea = [list(map(int, input().split())) for _ in range(n)]
    sr, sc, fish_locations = get_start_loc_and_fish_locations(sea, n)
    shark_size = 2
    shark_run = 0
    eat_cnt = 0
    dir = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    shark_info = [sr, sc, shark_size, shark_run, eat_cnt]

    while True:
        next_shark_info = get_next_shark_info(sea, n, dir, shark_info)

        if next_shark_info[0] == -1:
            return next_shark_info[3]

        shark_info = next_shark_info



print(solve())