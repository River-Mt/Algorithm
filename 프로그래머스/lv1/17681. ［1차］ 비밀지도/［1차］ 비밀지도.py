def to_bin(n, arr):
    ret = []
    
    for i in range(n):
        tmp = ''
        x = format(arr[i], 'b')
        pref = n - len(x)
        for p in range(pref):
            tmp += '0'
        tmp += x
        ret.append(tmp)
    
    return ret
    

def merge_map(n, arr1, arr2):
    arr = []
    
    for i in range(n):
        tmp = ''
        for j in range(n):
            x = (int(arr1[i][j]) or int(arr2[i][j]))
            if x == 1:
                tmp += '#'
            else: 
                tmp += ' '

        arr.append(tmp)
    
    return arr

    
def solution(n, arr1, arr2):
    answer = []
      
    answer = merge_map(n, to_bin(n, arr1), to_bin(n, arr2))
    
    return answer
