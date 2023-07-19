import sys
input = sys.stdin.readline


def solve():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[sys.maxsize for _ in range(3)] for _ in range(m+2)] for _ in range(n+1)]
    for i in range(1, m+1):
        for j in range(3):
            dp[1][i][j] = arr[0][i-1]

    for i in range(2, n+1):
        for j in range(1, m+1):
            add = arr[i - 1][j - 1]
            dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + add
            dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + add
            dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + add

    ans = sys.maxsize
    for i in range(1, m + 1):
        for j in range(3):
            ans = min(ans, dp[n][i][j])
    print(ans)

solve()
