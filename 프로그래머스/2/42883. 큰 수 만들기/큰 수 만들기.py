def solution(number, k):
    q = []
    answer = ''
    
    for num in number:
        while q and q[-1] < num and k > 0:
            q.pop()
            k -= 1
        q.append(num)
        
    
    if k > 0:
        q = q[:-k]

        
    return ''.join(q)