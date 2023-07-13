from collections import deque
import sys
sys.setrecursionlimit(10**8)


def solution(n, m, x, y, r, c, k):
    answer = "zzzz"
    dir = ["d", "l", "r", "u"]
    dr = [1, 0, 0, -1]
    dc = [0, -1, 1, 0]
    
    def get_dist(row, col):
        return abs(row - r) + abs(col - c)
    
    def is_not_over(row, col):
        if row <= 0 or col <= 0 or row > n or col > m:
            return False
        else:
            return True
    
    def is_impossible():
        mh_dist = get_dist(x, y)
        
        if mh_dist > k or (k - mh_dist) % 2 == 1:
            return True
        
        else:
            return False
    
    if is_impossible():
        return 'impossible'
        
    def dfs(x, y, state, cnt):
        nonlocal answer
        if k < cnt + get_dist(x, y):
            return
        
        if x == r and y == c and cnt == k:
            answer = state
            return
        
        for i in range(4):
            nx, ny = x + dr[i], y + dc[i]
            if is_not_over(nx, ny) and state < answer:
                dfs(nx, ny, state + dir[i], cnt + 1)
        
    dfs(x, y, "", 0)
    return answer
