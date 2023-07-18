import sys
from collections import deque

input = sys.stdin.readline


def solve():
    n = int(input().rstrip())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[0] * (n+1) for _ in range(n+1)] for _ in range(3)]
    garo, sero, cross = 0, 1, 2
    dp[garo][1][2] = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 and j <= 2:
                continue
            if arr[i-1][j-1] == 1:
                continue
            if arr[i-1][j-2] == 0:
                dp[garo][i][j] = dp[cross][i][j-1] + dp[garo][i][j-1]
            if arr[i-2][j-1] == 0:
                dp[sero][i][j] = dp[cross][i-1][j] + dp[sero][i-1][j]
            if arr[i-2][j-2] == 0 and arr[i-2][j-1] == 0 and arr[i-1][j-2] == 0:
                dp[cross][i][j] = dp[cross][i-1][j-1] + dp[garo][i-1][j-1] + dp[sero][i-1][j-1]
    ans = 0
    for i in range(3):
        ans += dp[i][n][n]
    return ans


print(solve())
