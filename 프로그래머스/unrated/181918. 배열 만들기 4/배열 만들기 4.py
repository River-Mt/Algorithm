from collections import deque


def solution(arr):
    
    dq = deque()
    
    i = 0
    
    while(i < len(arr)):
        if len(dq) == 0:
            dq.append(arr[i])
            i+=1
            continue

        top = dq.pop()
        
        if top < arr[i]:
            dq.append(top)
            dq.append(arr[i])
            i+=1
        
    
    
    return list(dq)