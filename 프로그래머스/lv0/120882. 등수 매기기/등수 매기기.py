def solution(score):
    answer = []
    score_sum = [score[i][0] + score[i][1] for i in range(len(score))]
    dic = {}
    
    sorted_score = sorted(score_sum, reverse=True)
    
    rank = 1
    
    dic[sorted_score[0]] = dic.get(sorted_score[0], 1)
    cnt = 1
    for i in range(1, len(sorted_score)):
        if sorted_score[i] != sorted_score[i - 1]:
            rank += cnt
            cnt = 1
        else: 
            cnt += 1

        dic[sorted_score[i]] = dic.get(sorted_score[i], rank)
    
    for num in score_sum:
        answer.append(dic[num])
            
        
    return answer