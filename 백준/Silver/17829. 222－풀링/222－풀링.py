import sys

n = int(sys.stdin.readline().rstrip())
board = [list(map(int, sys.stdin.readline().split())) for i in range(n)]


def partition(r, c, len):
    if len == 1:
        return board[r][c]

    mid = len // 2

    tmp = [partition(r, c, mid),
           partition(r + mid, c, mid),
           partition(r, c + mid, mid),
           partition(r + mid, c + mid, mid)
           ]

    tmp.sort(reverse=True)
    return tmp[1]


print(partition(0, 0, n))
