import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
num = 0


def solve():
    n, r, c = map(int, input().split())
    edge = 2 ** n

    def is_exit(cur_r, cur_c):
        return cur_r == r and cur_c == c

    def can_skip(cur_len, cur_r, cur_c):
        return not (cur_r <= r < cur_r + cur_len and cur_c <= c < cur_c + cur_len)

    def recur(cur_len, cur_r, cur_c):
        global num
        if is_exit(cur_r, cur_c):
            print(num)
            exit(0)

        if cur_len == 1:
            num += 1
            return

        if can_skip(cur_len, cur_r, cur_c):
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
