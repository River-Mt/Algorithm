from collections import deque

def bfs(begin, target, words):
    q = deque()
    q.append([begin, 0])
    chk = [0] * (len(words))
    
    while q:
        w, c = q.popleft()
        
        if w == target:
            return c
        
        for i in range(len(words)):
            if not chk[i]:
                tmp = 0
                
                for j in range(len(words[i])):
                    if words[i][j] != w[j]:
                        tmp += 1
                
                if tmp == 1:
                    q.append([words[i], c+1])
                    chk[i] = 1
    return 0
    

def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer