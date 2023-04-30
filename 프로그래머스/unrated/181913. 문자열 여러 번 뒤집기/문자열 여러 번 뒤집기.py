from collections import deque

def solution(my_string, queries):
    answer = list(my_string)
    myLen = len(answer)
    
    for query in queries:
        s, e = query
        dq = deque(answer[s:e+1])
        for i in range(s, e + 1):
            answer[i] = dq.pop()
        
    return ''.join(answer)
