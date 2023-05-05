import sys

n = int(sys.stdin.readline().rstrip())
marbles = list(map(int, sys.stdin.readline().split()))
ans = 0


def go(arr, sum):
    global ans
    if len(arr) == 2:
        ans = max(ans, sum)
        return

    for i in range(1, len(arr) - 1):
        add = arr[i - 1] * arr[i + 1]
        removed = arr[i]
        del arr[i]
        go(arr, sum + add)
        arr.insert(i, removed)


go(marbles, 0)

print(ans)
