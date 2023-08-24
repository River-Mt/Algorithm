import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
num = 0
ans = 0


def solve():
    n, r, c = map(int, input().split())
    edge = 2 ** n

    def recur(cur_len, cur_r, cur_c):
        global num, ans
        if cur_r == r and cur_c == c:
            print(num)
            exit(0)

        if cur_len == 1:
            num += 1
            return

        if not (cur_r <= r < cur_r + cur_len and cur_c <= c < cur_c + cur_len):
            num += cur_len ** 2
            return

        half = cur_len // 2
        recur(half, cur_r, cur_c)
        recur(half, cur_r, cur_c + half)
        recur(half, cur_r + half, cur_c)
        recur(half, cur_r + half, cur_c + half)

    recur(edge, 0, 0)

    return


solve()
