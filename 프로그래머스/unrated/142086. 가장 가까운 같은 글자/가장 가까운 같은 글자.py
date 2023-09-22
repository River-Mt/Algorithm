def solution(s):
    answer = []
    for i in range(len(s)):
        cur = s[i]
        flag = False
        for j in range(i-1, -1, -1):
            if cur == s[j]:
                answer.append(i - j)
                flag = True
                break
                
        if not flag:
            answer.append(-1)
        
    return answer