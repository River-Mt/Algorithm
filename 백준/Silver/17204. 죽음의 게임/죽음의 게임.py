import sys
from collections import deque


def bfs(g, n, k):
    q = deque()
    dist = [-1] * n
    q.append(0)
    dist[0] = 0

    while q:
        cur = q.popleft()

        if cur == k:
            return dist[cur]

        for i in range(len(g[cur])):
            nx = g[cur][i]

            if dist[nx] == -1:
                dist[nx] = dist[cur] + 1
                q.append(nx)

    return -1


def solve():
    n, k = map(int, sys.stdin.readline().split())
    g = [[] for _ in range(n)]

    for i in range(n):
        c = int(sys.stdin.readline().rstrip())
        g[i].append(c)

    return bfs(g, n, k)


print(solve())