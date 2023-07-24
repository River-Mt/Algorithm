import sys
import math
input = sys.stdin.readline


def solve():
    n, k = map(int, input().split())
    dp = [sys.maxsize for _ in range(2*n)]

    def can_eat():
        if dp[n] <= k:
            return "minigimbob"
        else:
            return "water"

    dp[1] = 1
    for i in range(1, n+1):
        if i + 1 <= n:
            dp[i + 1] = min(dp[i + 1], dp[i] + 1)
        if i + i // 2 <= n: 
            dp[i + i // 2] = min(dp[i + i // 2], dp[i] + 1)

    print(can_eat())


solve()
