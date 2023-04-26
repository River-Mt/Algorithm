import heapq


def solution(scoville, K):
    answer = 0
    q = []
    for i in scoville:
        heapq.heappush(q, i)
        
    while len(q) > 1:
        x = heapq.heappop(q)
        if x >= K: 
            break
        y = heapq.heappop(q)
        z = x+y*2
        heapq.heappush(q, z)
        answer+=1
    
    if len(q) > 0 and heapq.heappop(q) < K:
        answer = -1
        
    return answer