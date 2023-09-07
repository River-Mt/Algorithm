import sys

input = sys.stdin.readline


def solve():
    x, y, w, s = map(int, input().split())
    if x > y:
        x, y = y, x
    ans = min((x + y) * w, x * s + (y-x) * w)

    if (y-x) % 2 == 1:
        return min(ans, (y-1)*s + w)

    else:
        return min(ans, y*s)


print(solve())
