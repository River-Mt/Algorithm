import sys
input = sys.stdin.readline


def solve():
    n = int(input().rstrip())
    arr = [[0, 0]]
    for i in range(n-1):
        arr.append(list(map(int, input().split())))
    k = int(input().rstrip())
    dp = [[sys.maxsize for _ in range(2)] for _ in range(n+1)]
    dp[1][0] = 0

    for i in range(2, n+1):
        dp[i][0] = min(arr[i-1][0] + dp[i-1][0],
                       arr[i-2][1] + dp[i-2][0])

        dp[i][1] = min(arr[i-1][0] + dp[i-1][1],
                       arr[i-2][1] + dp[i-2][1],
                       k + dp[i-3][0])

    print(min(dp[n][0], dp[n][1]))


solve()
