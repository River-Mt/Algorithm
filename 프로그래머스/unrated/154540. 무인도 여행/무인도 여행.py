import sys

def dfs(maps, chk, r, c, dr, dc, n, m):
    chk[r][c] = 1
    ret = 0
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if nr < 0 or nc < 0 or nr >= n or nc >= m:
            continue
        if not chk[nr][nc] and maps[nr][nc] != 'X': 
            ret += dfs(maps, chk, nr, nc, dr, dc, n, m) + int(maps[nr][nc])
    
    return ret
        

def solution(maps):
    sys.setrecursionlimit(10**6)
    answer = []
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    n = len(maps)
    m = len(maps[0])

    chk = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if not chk[i][j] and maps[i][j] != 'X':
                answer.append(int(maps[i][j]) + dfs(maps, chk, i, j, dr, dc, n, m))
    
    if len(answer) == 0:
        answer.append(-1)
        
    return sorted(answer)
