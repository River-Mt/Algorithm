def solution(a, b, c):
    answer = 0
    dice = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    
    dice[a] += 1  
    dice[b] += 1
    dice[c] += 1
    
    sameCnt = max(dice.values())

    if sameCnt == 1:
        answer = a + b + c
    elif sameCnt == 2:
        answer = (a + b + c) * (a**2 + b**2 + c**2)
    else:
        answer = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    
    return answer