from collections import deque
def solution(arr, flag):
    answer = deque()
    
    for i in range(len(arr)):
        if flag[i] == True:
            for _ in range(arr[i] * 2):
                answer.append(arr[i])

        else :
            for _ in range(arr[i]):
                answer.pop()
    
    return list(answer)