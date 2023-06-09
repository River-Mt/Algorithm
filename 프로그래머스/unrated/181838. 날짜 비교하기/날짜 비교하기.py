def int_to_string(arr):
    s = ""
    for num in arr:
        if num < 10:
            s  += "0" + str(num)
        else:
            s += str(num)
            
    return s

def solution(date1, date2):
    s1 = int_to_string(date1)
    s2 = int_to_string(date2)

    
    return int(s1 < s2)
        
        


        



        
    
    
    
    
