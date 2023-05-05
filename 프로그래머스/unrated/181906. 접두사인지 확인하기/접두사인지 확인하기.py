def solution(my_string, is_prefix):
    answer = 0
    prefix = []
    
    for i in range(len(my_string)):
        prefix.append(my_string[0:i])    
        
    answer = int(is_prefix in prefix)
    return answer