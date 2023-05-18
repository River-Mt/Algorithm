def getSafeCnt(bombs, n, m):
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    tmp = [[1] * m for _ in range(n)]
    
    for bomb in bombs:
        for d in dirs:
            r = bomb[0] + d[0]
            c = bomb[1] + d[1]
            if r < 0 or c < 0 or r >= n or c >= m: continue
            tmp[r][c] = 0
    
    ret = 0
    
    for rows in tmp:
        ret += sum(rows)
        
    return ret
                    

def check(board):
    
    n = len(board)
    m = len(board[0])
    
    bombs = []
    
    for r in range(n):
        for c in range(m):
            if board[r][c] == 1:
                bombs.append((r, c))
        
    return getSafeCnt(bombs, n, m)

    
def solution(board):
    answer = check(board)
    return answer