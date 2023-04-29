def solution(l, r):
    answer = []
    for i in range(l, r+1):
        cnt = 0
        for j in str(i):
            if j == '0' or j == '5':
                cnt += 1
        if len(str(i)) == cnt:
            answer.append(i)

    if len(answer) == 0:
        answer.append(-1)
    return answer