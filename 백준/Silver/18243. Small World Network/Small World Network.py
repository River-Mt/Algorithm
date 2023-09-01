import sys

input = sys.stdin.readline
inf = sys.maxsize


def print_world(n, f):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if f[i][j] > 6:
                return "Big World!"

    return "Small World!"


def floyd(n, f):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                f[i][j] = min(f[i][j], f[i][k] + f[k][j])

    return print_world(n, f)


def get_f(n, k):
    f = [[0 if i == j else inf for j in range(n + 1)] for i in range(n + 1)]

    for i in range(k):
        u, v = map(int, input().split())
        f[u][v] = f[v][u] = 1

    return f


def solve():
    n, k = map(int, input().split())
    return floyd(n, get_f(n, k))


print(solve())
