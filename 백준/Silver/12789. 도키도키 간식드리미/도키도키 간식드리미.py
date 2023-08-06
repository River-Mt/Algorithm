import sys
from collections import deque

input = sys.stdin.readline


def solve():
    n = int(input())
    dq = deque(map(int, input().split()))
    waits = deque([])
    ord = 1

    while dq:
        if dq and dq[0] == ord:
            ord += 1
            dq.popleft()

        else:
            top = dq.popleft()
            if waits and top > waits[-1]:
                break
            waits.append(top)

        while waits and waits[-1] == ord:
            waits.pop()
            ord += 1

    return "Nice" if not waits else "Sad"


print(solve())
