def solution(s):
    answer = []
    dic = {}
    for token in sorted(s[2:-2].split("},{"), key = lambda x : len(x)):
        nums = token.split(',')
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
    answer = list(map(int, dic.keys()))
    
    return answer