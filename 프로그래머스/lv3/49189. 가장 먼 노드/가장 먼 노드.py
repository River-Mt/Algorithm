from collections import deque


def bfs(n, adj):
    max_dist = 1
    dist = [0] * (n + 1)
    q = deque()
    q.append(1)
    dist[1] = 1
    
    while q:
        cur = q.popleft()
        for i in range(len(adj[cur])):
            next = adj[cur][i]
            if not dist[next]:
                dist[next] = dist[cur] + 1
                max_dist = max(max_dist, dist[next])
                q.append(next)
    
    cnt = 0
    
    for x in dist:
        if x == max_dist: cnt+=1
            
    return cnt
            

def makeGraph(n, edge):
    adj = [[] for _ in range(n + 1)]
    
    for u, v in edge:
        adj[u].append(v)
        adj[v].append(u)
    
    return adj
    
    
def solution(n, edge):
    answer  = bfs(n, makeGraph(n, edge))
    return answer