def solution(name, yearning, photo):
    answer = []
    dic = {}
    for n, y in zip(name, yearning):
        dic[n] = y
        
    for row in photo:
        tmp = 0
        for p in row:
            if p in name:
                tmp += dic[p]
        answer.append(tmp)

        
    return answer