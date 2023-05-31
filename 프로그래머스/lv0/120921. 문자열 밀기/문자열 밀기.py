from collections import deque

def solution(A, B):
    answer = 0
    dqA = deque(list(A))
    dqB = deque(list(B))
    
    while True:
        if dqA == dqB: break
        dqA.appendleft(dqA.pop())
        answer += 1
        if answer > len(dqA):
            return -1
        
    return answer