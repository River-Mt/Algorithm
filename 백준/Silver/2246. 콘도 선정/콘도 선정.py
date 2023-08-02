import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())
condos = []
for i in range(n):
    l, p = map(int, input().split())
    condos.append([l, p])
condos.sort()
cost = 10001
result = 0
for i in condos:
    temp = i[1]
    if temp < cost:
        cost = temp
        result += 1
print(result)