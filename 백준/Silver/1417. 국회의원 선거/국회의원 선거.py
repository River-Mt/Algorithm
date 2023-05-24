import sys
import heapq
from collections import deque

n = int(sys.stdin.readline().rstrip())
pq = []
candidates = [0] * (n + 1)
dasom = int(sys.stdin.readline().rstrip())

for i in range(1, n):
    vote = int(sys.stdin.readline().rstrip())
    heapq.heappush(pq, -vote)

cnt = 0

while pq:
    top = -heapq.heappop(pq)
    if top >= dasom:
        heapq.heappush(pq, -(top - 1))
        dasom += 1
        cnt += 1
    else:
        break

print(cnt)


