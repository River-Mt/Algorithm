import sys
from collections import deque
input = sys.stdin.readline


def solve():
    t = int(input().rstrip())
    max_n = 100001
    mod = 1000000009
    dp = [[0 for _ in range(2)] for _ in range(max_n + 1)]
    # dp[n][0] : odd, dp[n][1] : even
    dp[1][0], dp[1][1] = 1, 0
    dp[2][0] = dp[2][1] = 1
    dp[3][0] = dp[3][1] = 2

    for i in range(4, max_n):
        dp[i][0] = (dp[i - 3][1] + dp[i - 2][1] + dp[i - 1][1]) % mod
        dp[i][1] = (dp[i - 3][0] + dp[i - 2][0] + dp[i - 1][0]) % mod

    for i in range(t):
        n = int(input().rstrip())
        print(dp[n][0] % mod, dp[n][1] % mod)


solve()
