def solution(n, results):
    answer = 0
    f = [[0 for _ in range(n)] for _ in range(n)]
    
    for u, v in results:
        u -= 1
        v -= 1
        f[u][v] = 1
        f[v][u] = -1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or f[i][j] in [1, -1]:
                    continue
                    
                if f[i][k] == 1 and f[k][j] == 1:
                    f[i][j] = 1
                    f[j][i] = f[j][k] = f[k][i] = -1
    
    for row in f:
        if row.count(0) == 1:
            answer += 1
    
    return answer