import sys

input = sys.stdin.readline


def solve():
    n = int(input().rstrip())
    map = []
    rotate = []
    for i in range(n):
        map.append((input().rstrip()))
    for c in range(n):
        tmp = ""
        for r in range(n):
            tmp+=map[r][c]
        rotate.append(tmp)

    r_cnt = 0
    c_cnt = 0
    for row in map:
        tmp = row.split('X')
        for part in tmp:
            if len(part) >= 2:
                r_cnt += 1

    for row in rotate:
        tmp = row.split('X')
        for part in tmp:
            if len(part) >= 2:
                c_cnt += 1

    print(r_cnt, c_cnt)


solve()
