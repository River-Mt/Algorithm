import heapq
import sys

input = sys.stdin.readline


def solve():
    n, k = map(int, input().split())
    capacity = []

    for i in range(n):
        capacity.append(int(input()))

    left = 0
    right = 2 ** 31 - 1

    while left <= right:
        mid = (left + right) // 2
        cnt = 0

        for i in range(n):
            cnt += capacity[i] // mid

        if cnt >= k:
            left = mid + 1

        else:
            right = mid - 1

    return right


print(solve())
