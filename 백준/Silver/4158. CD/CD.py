import sys
from collections import deque

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    cd = {}
    cnt = 0

    if n + m == 0:
        break

    # chk sy's cd
    for i in range(n):
        sy_cd_no = input().rstrip()
        cd[sy_cd_no] = 1

    # chk same cd
    for i in range(n):
        sg_cd_no = input().rstrip()
        if cd.get(sg_cd_no):
            cnt += 1

    print(cnt)


