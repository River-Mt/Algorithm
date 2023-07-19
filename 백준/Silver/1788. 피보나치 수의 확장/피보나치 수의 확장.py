import sys
input = sys.stdin.readline


def solve():
    n = int(input().rstrip())
    st = 1000000
    dp = [0] * (2*(st+1))
    mod = 1000000000

    dp[st] = 0
    dp[st + 1] = 1

    for i in range(st + 2, 2*(st+1)):
        dp[i] = (dp[i - 1] + dp[i-2]) % mod

    for i in range(st - 1, -1, -1):
        tmp = dp[i+2] - dp[i+1]
        if tmp < 0:
            tmp = -(abs(tmp) % mod)
        else:
            tmp = tmp % mod
        dp[i] = tmp

    ans = dp[st+n]
    print(-1 if ans < 0 else 1 if ans > 0 else 0)
    print(abs(ans))


solve()
