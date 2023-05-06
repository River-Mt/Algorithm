def solution(my_string, indices):
    answer = ''
    tmp = list(my_string)
    indices.sort()
    k = 0
    for i in indices:
        del tmp[i - k]
        k+=1
    
    answer = "".join(tmp)
    return answer