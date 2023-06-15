def solution(s):
    answer = True
    p_cnt = 0
    y_cnt = 0
    
    for ch in s:
        if ch.lower() == 'p':
            p_cnt += 1
        elif ch.lower() == 'y':
            y_cnt += 1
   
    return p_cnt == y_cnt