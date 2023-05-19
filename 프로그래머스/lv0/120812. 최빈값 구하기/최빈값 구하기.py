def solution(array):
    answer = 0
    cnt = {}
    if len(array) == 1: return array[0]

    for num in array:
        cnt[num] = cnt.get(num, 0) + 1
    
    sorted_cnt = sorted(cnt.items(), key=lambda x : -x[1])
    
    if len(sorted_cnt) > 1 and sorted_cnt[0][1] == sorted_cnt[1][1]: return -1
    
    answer = sorted_cnt[0][0]
    
    return answer