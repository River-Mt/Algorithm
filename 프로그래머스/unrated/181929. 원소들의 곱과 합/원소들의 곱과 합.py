def solution(num_list):
    answer = 0
    mul_val = 1
    sum_val = 0
    for x in num_list:
        mul_val *= x
        sum_val += x
    
    answer = 1 if mul_val < sum_val**2 else 0
    
    return answer