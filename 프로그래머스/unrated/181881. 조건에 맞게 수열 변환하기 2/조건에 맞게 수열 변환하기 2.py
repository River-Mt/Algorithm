def func(arr):
    tmp = []
    
    for num in arr:
        if num > 50 and not num % 2 : tmp.append(int(num / 2))
        elif num < 50 and num % 2 : tmp.append(num * 2 + 1)
        else: tmp.append(num)
            
    return tmp
    

def solution(arr):
    answer = 0
    
    while True:
        prev = arr 
        arr = func(prev)
        if arr == prev:
            break
        answer += 1
            
    return answer