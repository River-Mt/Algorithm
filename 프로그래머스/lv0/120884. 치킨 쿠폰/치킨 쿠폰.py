def solution(chicken):
    answer = 0
    
    while True:
        if chicken < 10:
            break
        sv = chicken // 10
        remain = chicken % 10
        answer += sv
        chicken = chicken // 10 + remain
        
        
    
    return answer