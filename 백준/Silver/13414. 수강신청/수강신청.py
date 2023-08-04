import sys
from collections import deque

input = sys.stdin.readline

k, l = map(int, input().split())
dq = deque([])
count = {}

for i in range(l):
    num = input().rstrip()
    count[num] = i

idx = 0

for num in sorted(count, key=lambda x: count[x]):
    if idx == k:
        break
    print(num)
    idx += 1
