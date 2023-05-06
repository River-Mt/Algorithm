def solution(my_string, m, c):
    answer = ''
    for i in range(len(my_string)):
        if (i % m) + 1 == c:
            answer += my_string[i]
    return answer