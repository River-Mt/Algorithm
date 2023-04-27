def solution(a, b):
    answer = 0
    answer = max(str(a) + str(b), str(b) + str(a))
    return int(answer)