def solution(arr):
    answer = []
    twoArea = []
    for i in range(len(arr)):
        if arr[i] == 2:
            twoArea.append(i)
    if len(twoArea) == 0:
        return [-1]
    
    answer = arr[min(twoArea): max(twoArea)+1]
        
    return answer