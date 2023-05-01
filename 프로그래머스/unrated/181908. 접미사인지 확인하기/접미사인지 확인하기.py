def solution(my_string, is_suffix):
    answer = 0
    suffix = []
    for i in range(len(my_string)):
        suffix.append(my_string[i:])
        
    answer = int(is_suffix in suffix)
 
    return answer