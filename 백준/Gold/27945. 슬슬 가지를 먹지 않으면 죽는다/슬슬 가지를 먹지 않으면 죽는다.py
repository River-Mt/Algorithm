import sys

input = sys.stdin.readline


def solve():
    n, m = map(int, input().split())
    edges = []
    par = [-1 for _ in range(n+1)]
    day = 1

    def find(cur):
        if par[cur] < 0:
            return cur
        par[cur] = find(par[cur])
        return par[cur]

    def union(u, v):
        u, v = find(u), find(v)
        if u == v:
            return False
        if par[u] < par[v]:
            u, v = v, u
        par[v] += par[u]
        par[u] = v
        return True

    for i in range(m):
        u, v, t = map(int, input().split())
        edges.append([u, v, t])

    # ASC sorting with t's value
    edges = sorted(edges, key=lambda x: x[2])

    for u, v, t in edges:
        if t != day:
            break
        if not union(u, v):
            break
        day += 1

    print(day)


solve()
