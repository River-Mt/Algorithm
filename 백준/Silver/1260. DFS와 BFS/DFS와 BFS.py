import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for j in range(1005)]
chk = [[0 for i in range(1005)] for j in range(1005)]
answer = [[] for j in range(2)]


def dfs(now):
    chk[now] = 1
    answer[0].append(now)
    for next in graph[now]:
        if chk[next] == 1:
            continue
        chk[next] = 1
        dfs(next)


def bfs(now):
    q = deque([now])
    chk[now] = 2
    while (len(q) > 0):
        front = q.popleft()
        answer[1].append(front)
        for next in graph[front]:
            if chk[next] == 2:
                continue
            chk[next] = 2
            q.append(next)


for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

for g in graph:
    g.sort()

dfs(v)
bfs(v)

for x in answer:
    print(*x)
