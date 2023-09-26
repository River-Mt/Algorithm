from heapq import heappush, heappop

def solution(n, k, enemy):
    pq = []
    
    for i, e in enumerate(enemy):
        heappush(pq, e)
        
        if len(pq) > k:
            n -= heappop(pq)
        
        if n < 0:
            return i
        
    return len(enemy)
            
    
            
            
        

    
    return answer