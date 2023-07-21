import sys
from collections import deque
input = sys.stdin.readline


def solve():
    s, c = map(int, input().split())
    arr = []
    ans = 0

    for i in range(s):
        arr.append(int(input().rstrip()))

    arr = sorted(arr)
    
    l = 1
    r = max(arr)

    while l <= r:
        mid = (l+r) // 2
        cnt = 0

        for i in range(s):
            cnt += arr[i] // mid

        if cnt < c:
            r = mid - 1

        else:
            ans = max(mid, ans)
            l = mid + 1

    print(sum(arr) - ans*c)


solve()
