def solution(n):
    answer = 0
    if n%2 == 0:
        answer = sum((i+1)*(i+1) for i in range(n) if (i+1)%2 == 0)
    else:
        answer = sum((i+1) for i in range(n) if (i+1)%2 == 1)
    return answer