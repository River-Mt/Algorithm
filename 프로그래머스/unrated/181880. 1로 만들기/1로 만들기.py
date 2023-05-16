def go(num):
    if num == 1:
        return 0
    ret = 0
    if num % 2:
        ret += go((num - 1) / 2) + 1
    else:
        ret += go(num / 2) + 1
    return ret

def solution(num_list):
    answer = 0

    for num in num_list:
        answer += go(num)
    return answer