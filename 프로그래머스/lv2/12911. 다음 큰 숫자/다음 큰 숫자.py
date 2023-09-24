def solution(n):
    answer = 0
    nx = n+1
    one = bin(n)[2:].count('1')

    while True:
        if bin(nx)[2:].count('1') == one:
            answer = nx
            break
        nx += 1
        
    return answer