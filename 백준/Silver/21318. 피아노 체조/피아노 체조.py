import sys
from collections import deque

input = sys.stdin.readline


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    p_sum = [0] * n
    chk = [0] * n
    q = int(input())

    for i in range(1, n):
        if arr[i-1] > arr[i]:
            chk[i] = 1

    for i in range(1, n):
        p_sum[i] = p_sum[i-1] + chk[i]

    p_sum = [0] + p_sum
    for i in range(q):
        s, e = map(int, input().split())
        print(p_sum[e] - p_sum[s])


solve()