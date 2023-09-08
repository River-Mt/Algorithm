import sys
sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline
n, r, q = map(int, input().split())
tree = [[] for _ in range(n + 1)]
dp = [0 for _ in range(n + 1)]


def dfs(now):
    dp[now] = 1
    for i in range(len(tree[now])):
        next_node = tree[now][i]
        if dp[next_node] == 0:
            dp[now] += dfs(next_node)
    return dp[now]


def solve():
    for i in range(n-1):
        u, v = map(int, input().split())
        # undirected graph (tree)
        tree[u].append(v)
        tree[v].append(u)

    dfs(r)

    for i in range(q):
        u = int(input())
        print(dp[u])


solve()



