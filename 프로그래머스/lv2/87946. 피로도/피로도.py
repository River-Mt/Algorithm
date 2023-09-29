from itertools import permutations

def solution(k, dungeons):
    answer = -1
    arr = map(list,(permutations(dungeons)))
    
    for row in arr:
        p = k
        cnt = 0
        for min_p, use in row:
            if p >= min_p:
                p -= use
                cnt += 1
            else:
                break
        answer = max(answer, cnt)

        
    return answer