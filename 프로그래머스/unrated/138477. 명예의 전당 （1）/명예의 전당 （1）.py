from collections import deque
import heapq

def pop_third(pq, k):
    tmp = deque([])
    cnt = 0
    while pq:
        if cnt == k:
            break
        tmp.append(heapq.heappop(pq))
        cnt += 1
    
    for num in tmp:
        heapq.heappush(pq, num)
    
    return tmp.pop()
    

def solution(k, score):
    answer = []
    pq = []

    for sco in score:
        heapq.heappush(pq, -sco)
        answer.append(-pop_third(pq, k))
        
    return answer