from collections import defaultdict

def dfs(g, p, c):
    if p:
        to = p[-1]
        if g[to]:
            p.append(g[to].pop(0))
        else:
            c.append(p.pop())
        dfs(g, p, c)
        
    return c[::-1]
    

def solution(tickets):
    answer = []
    g = defaultdict(list)
    tickets.sort()
    
    for u, v in tickets:
        g[u].append(v)
    
    return dfs(g, ['ICN'], [])