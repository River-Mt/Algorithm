def solution(num, k):
    answer = 0
    arr = str(num)
    answer = arr.find(str(k))
    if answer != -1:
        answer += 1
    return answer