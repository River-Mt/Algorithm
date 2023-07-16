import sys
from collections import deque
input = sys.stdin.readline


def solve():
    n = int(input().rstrip())
    arr = []
    for i in range(n):
        arr.append(input().rstrip())

    decs = sorted(arr, reverse=True)
    inc = sorted(arr)

    if arr == inc:
        return "INCREASING"
    elif arr == decs:
        return "DECREASING"

    return "NEITHER"


print(solve())
