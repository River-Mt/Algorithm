def solution(my_string):
    answer = ''
    m = ['a', 'e', 'i', 'o', 'u']
    
    for ch in list(my_string):
        if ch in m:
            continue
        answer += ch
    
    return answer