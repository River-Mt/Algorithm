from collections import deque


def append_doll(dq, target):
    if not len(dq):
        dq.append(target)
        return 0
    
    top = dq.pop()
    
    if top == target:
        return 2
    
    else:
        dq.append(top)
        dq.append(target)
        return 0
    

def select_doll(col, board, n, dq):
    idx = 0
    cnt = 0
    
    while idx < n:
        target = board[idx][col]
        if target != 0:
            board[idx][col] = 0
            return append_doll(dq, target)
        
        idx += 1
        
    return 0
        

def solution(board, moves):
    answer = 0
    n = len(board)
    dq = deque()
    for col in moves:
        answer += select_doll(col - 1, board, n, dq)
    
    return answer 