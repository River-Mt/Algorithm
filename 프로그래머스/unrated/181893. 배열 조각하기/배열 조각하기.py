def solution(arr, query):
    answer = arr
    evenMax = 0
    oddMin = 100005
    for i in range(len(query)):
        idx = query[i]
        if i%2 == 0:
            answer = answer[0:idx+1]
        else:
            answer = answer[idx:]        
            
    return answer