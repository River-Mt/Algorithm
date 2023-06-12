def solution(my_str, n):
    answer = []
    idx = 0
    while idx + n < len(my_str):
        answer.append(my_str[idx: idx + n])
        idx+=n
    answer.append(my_str[idx:])
    return answer