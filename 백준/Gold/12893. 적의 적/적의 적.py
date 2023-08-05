import sys
from collections import deque

input = sys.stdin.readline


class UnionFind:

    def __init__(self, n):
        self.p = [-1 for _ in range(n + 1)]
        self.e = [0 for _ in range(n + 1)]

    def find(self, u):
        if self.p[u] < 0:
            return u

        self.p[u] = self.find(self.p[u])

        return self.p[u]

    def union(self, u, v):
        u, v = self.find(u), self.find(v)

        if u == v:
            return 0

        if self.p[u] < self.p[v]:
            u, v = v, u

        self.p[v] += self.p[u]
        self.p[u] = v

        return 1


def solve():
    n, m = map(int, input().split())
    uf = UnionFind(n)
    ans = 1
    chk = [[0] * (n+1) for _ in range(n+1)]

    for _ in range(m):
        u, v = map(int, input().split())

        if uf.find(u) == uf.find(v):
            ans = 0

        if uf.e[u]:
            uf.union(uf.e[u], v)

        else:
            uf.e[u] = v

        if uf.e[v]:
            uf.union(uf.e[v], u)

        else:
            uf.e[v] = u

    return ans


print(solve())
