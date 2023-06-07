import sys


def read_line():
    return sys.stdin.readline()


def read_int():
    return int(read_line().rstrip())


def find(parent, x):
    if parent[x] < 0:
        return x
    else:
        parent[x] = find(parent, parent[x])
        return parent[x]


def union(parent, u, v):
    u = find(parent, u)
    v = find(parent, v)

    if u == v:
        return

    if parent[u] < parent[v]:
        u, v = v, u

    parent[v] += parent[v]
    parent[u] = v


def solve_each_case():
    n = read_int()
    k = read_int()
    parent = [-1 for _ in range(n)]

    for i in range(k):
        u, v = map(int, read_line().split())
        union(parent, u, v)

    m = read_int()
    results = []
    for i in range(m):
        u, v = map(int, read_line().split())
        if find(parent, u) == find(parent, v):
            results.append(1)
        else:
            results.append(0)

    return results


def solve():
    tc = read_int()
    for i in range(1, tc + 1):
        print(f'Scenario {i}:')
        for result in solve_each_case():
            print(result)
        print()


solve()
