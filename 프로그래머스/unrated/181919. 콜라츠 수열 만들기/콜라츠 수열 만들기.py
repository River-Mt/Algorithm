def solution(n):
    answer = [n]
    while True:
        if n == 1:
            break
        if n%2:
            n = 3 * n + 1
        else:
            n /= 2
            
        answer.append(n)
    return answer