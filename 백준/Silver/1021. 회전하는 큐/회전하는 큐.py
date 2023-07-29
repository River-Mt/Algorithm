import sys
from collections import deque
input = sys.stdin.readline


def solve():
   n, m = map(int, input().split())
   dq = deque([i+1 for i in range(n)])
   order = list(map(int, input().split()))
   cnt = 0
   for ord in order:
      size = len(dq)
      idx = dq.index(ord)
      if idx == 0:
         dq.popleft()
         continue
      elif idx < size - idx:
         for i in range(idx):
            dq.append(dq.popleft())
            cnt += 1
      else:
         for i in range(size-idx):
            dq.appendleft(dq.pop())
            cnt += 1
      dq.popleft()
   print(cnt)


solve()
