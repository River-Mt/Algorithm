import sys


def check_board(check):
    bingo = 0

    for i in range(5):
        bingo += check_row(check, i)
        bingo += check_col(check, i)

    bingo += check_left_cross(check) + check_right_cross(check)

    if bingo >= 3:
        #print(bingo)
        return 1

    return 0


def check_row(check, r):
    for c in range(5):
        if not check[r][c]:
            return 0
    return 1


def check_col(check, c):
    for r in range(5):
        if not check[r][c]:
            return 0
    return 1


def check_left_cross(check):
    idx = 0
    while idx < 5:
        if not check[idx][idx]:
            return 0
        idx += 1
    return 1


def check_right_cross(check):
    r = 0
    c = 4
    while r < 5:
        if not check[r][c]:
            return 0
        r += 1
        c -= 1
    return 1


def solve():
    tmp = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
    orders = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
    check = [[0] * 5 for _ in range(5)]
    board = {}

    for i in range(5):
        for j in range(5):
            num = tmp[i][j]
            board[num] = board.get(num, (i, j))
    cnt = 0
    for i in range(5):
        for j in range(5):
            cnt += 1
            target = board.get(orders[i][j])
            r = target[0]
            c = target[1]
            check[r][c] = 1
            if check_board(check):
                print(cnt)
                return


solve()
