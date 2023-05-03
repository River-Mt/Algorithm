def dfs(adj, chk, now):
    chk[now] = 1
    
    for node in adj[now]:
        if chk[node] == 0:
            chk[node] = 1
            dfs(adj, chk, node)
    
    
def solution(n, computers):
    answer = 0  
    adj = [[] for i in range(n)]
    chk = [0 for i in range(n)]
    
    for i in range(n):
        for j in range(i, n):
            if i != j and computers[i][j] == 1:
                adj[i].append(j)
                adj[j].append(i)

                
    print(adj)

    for i in range(n):
        if chk[i] == 0:
            dfs(adj, chk, i)
            answer += 1
            print(answer)
    
    return answer