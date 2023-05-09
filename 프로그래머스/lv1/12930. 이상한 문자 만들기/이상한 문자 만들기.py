def solution(s):
    answer = ''
    tokens = s.split(' ')
    for i in range(len(tokens)):
        for j in range(len(tokens[i])):
            if j % 2 == 0:
                answer += tokens[i][j].upper()
            else:
                answer += tokens[i][j].lower()
        if i == len(tokens) - 1:
            break
        answer += ' '
    return answer