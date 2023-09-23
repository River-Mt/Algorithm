def solution(k, tangerine):
    answer = 0
    dic = {}
    
    for t in tangerine:
        dic[t] = dic.get(t, 0) + 1
    
    counts = sorted(list(dic.values()), reverse = True)
    for count in counts:
        k -= count
        answer += 1

        if k <= 0:
            break
    
    
    return answer