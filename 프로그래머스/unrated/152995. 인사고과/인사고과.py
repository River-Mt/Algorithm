def solution(scores):
    answer = 0
    wanho = scores[0]
    wanho_sco = sum(scores[0])
    tmp = 0
    sorted_scores = sorted(scores, key=lambda x: (-x[0], x[1]))
    
    for sco in sorted_scores:
        if wanho[0] < sco[0] and wanho[1] < sco[1]:
            return -1
        
        if tmp <= sco[1]:
            if sum(sco) > wanho_sco:
                answer += 1

            tmp = sco[1]
    
    return answer + 1