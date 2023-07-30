import sys
from collections import deque

input = sys.stdin.readline


def solve():
    tc = int(input().rstrip())

    for _ in range(tc):
        n = int(input().rstrip())
        adj = [[] for _ in range(n+1)]
        dist = [0] * (n+1)
        for i in range(1, n+1):
            adj[i].append(int(input().rstrip()))

        dq = deque(list())
        dq.append(1)
        dist[1] = 1
        while dq:
            cur = dq.popleft()
            for nx in adj[cur]:
                if dist[nx] == 0:
                    dist[nx] = dist[cur]+1
                    dq.append(nx)

        print(dist[n] - 1 if dist[n] > 0 else 0)


solve()
