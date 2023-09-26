def solution(seoul):
    idx = 0
    for i, s in enumerate(seoul):
        if s == "Kim":
            idx = i
            break
        
    return str(f'김서방은 {idx}에 있다',)