import sys
from collections import deque
input = sys.stdin.readline


def solve():
    max_len = 25
    dp = [[[0 for _ in range(max_len)] for _ in range(max_len)] for _ in range(max_len)]

    def recur(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return 1
        if a > 20 or b > 20 or c > 20:
            return recur(20, 20, 20)
        if dp[a][b][c]:
            return dp[a][b][c]
        if a < b < c:
            dp[a][b][c] = recur(a, b, c - 1) + \
                          recur(a, b-1, c-1) - \
                          recur(a, b-1, c)
            return dp[a][b][c]
        else:
            dp[a][b][c] = recur(a-1, b, c) + \
                          recur(a-1, b-1, c) + \
                          recur(a-1, b, c-1) - \
                          recur(a-1, b-1, c-1)
            return dp[a][b][c]

    while True:
        a, b, c = map(int, input().split())
        if a == -1 and b == -1 and c == -1:
            break
        print(f'w({a}, {b}, {c}) = {recur(a, b, c)}')


solve()
