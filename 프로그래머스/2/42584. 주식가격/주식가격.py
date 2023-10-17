from collections import deque

def solution(prices):
    answer = [0 for _ in range(len(prices))]
    idx = 0
    dq = deque(prices)
    
    while dq:
        x = dq.popleft()
        
        for num in dq:
            if num < x:
                answer[idx] += 1
                break
            answer[idx] += 1
            
        idx += 1
        
    return answer