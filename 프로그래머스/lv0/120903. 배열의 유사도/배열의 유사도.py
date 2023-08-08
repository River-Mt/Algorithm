def solution(s1, s2):
    answer = 0
    dic = {}
    for s in s1:
        dic[s] = 1
    for s in s2:
        if dic.get(s):
            answer += 1
    return answer