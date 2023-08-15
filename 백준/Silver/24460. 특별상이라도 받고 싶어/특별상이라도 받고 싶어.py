import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    def part(cur, r, c):
        if cur == 1:
            return arr[r][c]

        cur = cur // 2

        ret = [part(cur, r, c),
               part(cur, r + cur, c),
               part(cur, r, c + cur),
               part(cur, r + cur, c + cur)]

        return sorted(ret)[1]

    return part(n, 0, 0)


print(solve())
