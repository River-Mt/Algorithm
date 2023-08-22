def solution(my_string, num1, num2):
    answer = ''
    tmp = list(my_string)
    tmp[num1], tmp[num2] = tmp[num2], tmp[num1]
    answer = "".join(tmp)
    return answer