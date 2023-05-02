def solution(arr):
    answer = []
    
    prev = arr[0]
    answer.append(prev)
    
    for x in arr:
        if x != prev:
            answer.append(x)
        prev = x 

    return answer