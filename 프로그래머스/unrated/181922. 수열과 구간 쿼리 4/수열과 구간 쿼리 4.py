def solution(arr, queries):
    answer = arr
    
    for query in queries:
        s,e,k = query
        for i in range(s, e+1):
            if i%k == 0:
                answer[i] += 1

    return answer