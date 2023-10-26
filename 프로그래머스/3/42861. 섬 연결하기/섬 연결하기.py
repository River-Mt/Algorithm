def solution(n, costs):
    answer = 0
    p = [-1 for _ in range(n)]

    def find(u):
        if p[u] < 0:
            return u
        p[u] = find(p[u])
        return p[u]
    
    def union(u, v):
        u, v = find(u), find(v)
        
        if u == v:
            return False
        
        if p[u] > p[v]:
            u, v = v, u
        
        p[u] += p[v]
        p[v] = u
        
        return True
    
    for u, v, c in sorted(costs, key=lambda x: x[2]):
        if union(u, v):
            answer += c

    return answer