import sys

tc = int(sys.stdin.readline().rstrip())
mod = 1000000009
dp = [0] * 100005

dp[1] = 1
dp[2] = dp[3] = 2
dp[4] = dp[5] = 3
dp[6] = 6

for i in range(7, 100002):
    dp[i] = (dp[i-6] + dp[i-4] + dp[i-2]) % mod

while tc:
    n = int(sys.stdin.readline().rstrip())
    print(dp[n] % mod)
    tc -= 1
