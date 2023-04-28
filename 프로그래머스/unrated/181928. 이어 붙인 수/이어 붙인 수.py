def solution(num_list):
    answer = 0
    odd_str = ""
    even_str = ""
    
    for i in range(len(num_list)):
        if num_list[i]%2 :
            odd_str += str(num_list[i])
        else:
            even_str += str(num_list[i])
        
    answer = int(odd_str) + int(even_str)
        

    return answer