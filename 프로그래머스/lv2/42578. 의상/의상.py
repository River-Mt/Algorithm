from itertools import combinations

def solution(clothes):
    answer = 1
    dict = {}
    for cloth in clothes:
        dict[cloth[1]] = dict.get(cloth[1], 0) + 1
    
    for num in list(dict.values()):
        answer *= (num + 1)
    
    answer -= 1
    
    return answer  