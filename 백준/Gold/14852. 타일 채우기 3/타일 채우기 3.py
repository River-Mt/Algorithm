import sys
input = sys.stdin.readline


def solve():
    mod = 1000000007
    n = int(input().rstrip())
    dp = [0 for _ in range(1000001)]
    psum = [0 for _ in range(1000001)]
    dp[1] = 2
    dp[2] = 7
    psum[2] = 1
    for i in range(3, 1000001):
        psum[i] = psum[i-1] + dp[i-3]
        dp[i] = (2*dp[i-1] + 3*dp[i-2] + 2*psum[i]) % mod

    print(dp[n] % mod)


solve()
