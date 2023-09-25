def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        r = i // n
        c = i % n
        t = max(r, c) + 1
        answer.append(t)
    
    return answer