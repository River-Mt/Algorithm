import sys
input = sys.stdin.readline


def solve():
    n, snake = map(int, input().split())
    arr = sorted(list(map(int, input().split())))

    for h in arr:
        if snake >= h:
            snake += 1
        else:
            break
    print(snake)


solve()
