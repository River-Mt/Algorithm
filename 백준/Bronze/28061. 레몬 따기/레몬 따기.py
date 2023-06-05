import sys

n = int(sys.stdin.readline().rstrip())
trees = [num - (n - i) for i, num in enumerate(list(map(int, sys.stdin.readline().split())))]
print(max(trees))


