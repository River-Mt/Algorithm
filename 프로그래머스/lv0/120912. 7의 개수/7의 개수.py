def solution(array):
    answer = 0
    for num in array:
        for ch in str(num):
            if ch == '7':
                answer += 1
    return answer