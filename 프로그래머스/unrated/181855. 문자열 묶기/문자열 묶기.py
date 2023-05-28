from collections import defaultdict

def solution(strArr):
    answer = 0
    dic = defaultdict(list)
    
    for s in strArr:
        dic[len(s)].append(s)
    
    for k in dic.keys():
        answer = max(answer, len(dic[k]))

    return answer