import heapq
import sys
def solution(alp, cop, problems):
    answer = 0
    pq = []
    
    problems.append([1, 0, 1, 0, 1])
    problems.append([0, 1, 0, 1, 1])
    
    problems.sort()
    
    alp_max, cop_max = 0, 0
    
    for p in problems:
        alp_max = max(alp_max, p[0])
        cop_max = max(cop_max, p[1])
    
    dist = [[300 * 100 for _ in range(cop_max + 1)] for _ in range(alp_max + 1)]
    
    alp, cop = min(alp, alp_max) , min(cop, cop_max)
    dist[alp][cop] = 0
    
    heapq.heappush(pq, [0, alp, cop])
    
    while pq:
        t, a, c = heapq.heappop(pq)
        
        if dist[a][c] < t:
            continue
        
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if a < alp_req or c < cop_req:
                continue
                
            if a < alp_req and c < cop_req:
                break
            
            na = min(alp_max, a + alp_rwd)
            nc = min(cop_max, c + cop_rwd)
            
            if dist[na][nc] > dist[a][c] + cost:
                dist[na][nc] = dist[a][c] + cost
                heapq.heappush(pq, [dist[na][nc], na, nc])
        
    
    return dist[alp_max][cop_max]