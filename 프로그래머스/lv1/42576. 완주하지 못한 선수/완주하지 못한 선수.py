def solution(participant, completion):
    answer = ''
    dict = {}
    for p in participant:
        dict[p] = dict.get(p, 0) + 1
    
    for c in completion:
        dict[c] -= 1
        
    for p in participant:
        if dict[p] != 0:
            answer =  p
            break
            
    return answer