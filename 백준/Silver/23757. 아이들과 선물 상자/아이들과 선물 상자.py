import sys
import queue
input = sys.stdin.readline

q = queue.PriorityQueue()

n, m = map(int, input().split())
presents = list(map(int, input().split()))

for p in presents:
    q.put(-p)

child_needs = list(map(int, input().split()))

flag = True

for need in child_needs:
    max_p = -q.get()
    if max_p < need:
        flag = False
        break
    max_p -= need
    q.put(-max_p)

print(1 if flag else 0)


