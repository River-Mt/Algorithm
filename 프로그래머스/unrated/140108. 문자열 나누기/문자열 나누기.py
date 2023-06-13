def solution(s):
    answer = 0
    front = 0
    other = 0
    
    for i in range(len(s)):
        if front == 0 and other == 0: cmp = s[i]
        if s[i] == cmp: front += 1
        else : other += 1
        
        if front == other:
            front = 0
            other = 0
            answer += 1
        
    if front != other: answer += 1
    return answer