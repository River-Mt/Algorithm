import sys


def is_desc(arr):
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            return True

    return False


n, m = map(int, sys.stdin.readline().split())
stacks = []

for i in range(m):
    k = int(sys.stdin.readline().rstrip())
    if is_desc(list(map(int, sys.stdin.readline().split()))):
        print("No")
        exit(0)

print("Yes")



