def solution(arr, queries):
    answer = []
    
    for i in range(len(queries)):
        s, e, k = queries[i]
        cmp = 1000005
        for x in arr[s:e+1]:
            if x > k:
                cmp = min(cmp, x)
        answer.append(cmp if cmp != 1000005 else -1)
    
    return answer