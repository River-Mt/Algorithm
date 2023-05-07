def solution(str_list):
    answer = []
    
    for i in range(len(str_list)):
        ch = str_list[i]
        if ch == 'l':
            answer = str_list[:i]
            break
        elif ch == 'r':
            answer = str_list[i+1:]
            break
            
    return answer