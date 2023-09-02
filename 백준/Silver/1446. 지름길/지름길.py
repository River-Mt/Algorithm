import heapq
import sys

input = sys.stdin.readline
n, d = map(int, input().split())


def dijkstra(adj, dist):
    pq = []
    st_cost = st = 0
    heapq.heappush(pq, [st_cost, st])
    dist[st] = 0

    while pq:
        cost, cur = heapq.heappop(pq)

        if dist[cur] < cost:
            continue

        for node in adj[cur]:
            nx, nc = node[0], dist[cur] + node[1]

            if dist[nx] > nc:
                dist[nx] = nc
                heapq.heappush(pq, [nc, nx])

    return dist[d]


def solve():
    inf = sys.maxsize
    dist = [inf for _ in range(d+1)]
    adj = [[] for _ in range(d+1)]

    for i in range(d):
        adj[i].append([i+1, 1])

    for i in range(n):
        u, v, c = map(int, input().split())
        if v <= d and u <= d:
            adj[u].append([v, c])

    return dijkstra(adj, dist)


print(solve())
