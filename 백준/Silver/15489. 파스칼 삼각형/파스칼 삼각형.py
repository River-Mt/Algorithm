import sys


# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

# arr[i][j] = arr[i-1][j-1] + arr[i-1][j]


def init_dp(table):
    for i in range(1, 30):
        for j in range(1, i + 1):
            if j == 0 or j == i:
                table[i][j] = 1
                continue

            table[i][j] = table[i - 1][j] + table[i - 1][j - 1]


def get_sum(dp, r, c, w):
    tmp = 0
    for i in range(r, r + w):
        for j in range(c, c + i - r + 1):
            tmp += dp[i][j]
    return tmp


dp = [[0 for _ in range(31)] for _ in range(31)]
init_dp(dp)
r, c, w = map(int, sys.stdin.readline().split())
print(get_sum(dp, r, c, w))

