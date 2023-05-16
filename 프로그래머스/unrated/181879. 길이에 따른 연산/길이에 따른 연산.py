def solution(num_list):
    answer = 0
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        answer = 1
        for x in num_list: answer *= x
    return answer