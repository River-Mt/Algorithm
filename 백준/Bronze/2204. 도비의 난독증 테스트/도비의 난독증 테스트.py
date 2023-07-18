import sys
input = sys.stdin.readline


def solve():
    while True:
        n = int(input().rstrip())
        if n == 0:
            break
        arr = []
        for i in range(n):
            arr.append(input().rstrip())
        print(sorted(arr, key=lambda x: x.lower())[0])


solve()
