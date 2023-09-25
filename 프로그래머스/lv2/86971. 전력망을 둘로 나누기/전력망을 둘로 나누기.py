def dfs(adj, now, chk, remove):
    chk[now] = 1
    ret = 1
    for nx in adj[now]:
        if chk[nx] or [now, nx] == remove or [nx, now] == remove:
            continue
        ret += dfs(adj, nx, chk, remove)
    return ret

    
    

def solution(n, wires):
    answer = 100000000
    adj = [[] for _ in range(n+1)]
    
    for u, v in wires:
        adj[u].append(v)
        adj[v].append(u)
    
    for wire in wires:
        chk = [0 for _ in range(n+1)]
        tmp = []
        for i in range(1, n+1):
            if not chk[i]:
                tmp.append(dfs(adj, i, chk, wire))
        answer = min(abs(tmp[0] - tmp[1]), answer)
        
    return answer