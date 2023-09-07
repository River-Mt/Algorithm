import sys

input = sys.stdin.readline


def get_coins():
    return list(map(int, input().split()))


def get_dp(goal, coins):
    dp = [0 for _ in range(goal + 1)]
    dp[0] = 1
    for coin in coins:
        for i in range(coin, goal + 1):
            dp[i] += dp[i - coin]

    return dp[goal]


def solve():
    tc = int(input())

    for i in range(tc):
        n = int(input())
        coins = get_coins()
        goal = int(input())
        print(get_dp(goal, coins))


solve()
