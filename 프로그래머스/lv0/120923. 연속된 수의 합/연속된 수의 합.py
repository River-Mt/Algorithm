def solution(num, total):
    answer = []
    r = 1000
    l = 1000 - num + 1
    tmp = sum([i for i in range(l, r + 1)])
 
    while True:
        if tmp == total:
            return [i for i in range(l, r + 1)]
        tmp = tmp - r + l - 1
        r -= 1
        l -= 1
        
    return tmp





        
        
            
