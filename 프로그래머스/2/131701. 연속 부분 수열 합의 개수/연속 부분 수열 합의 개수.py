import copy

def solution(elements):
    answer = 0
    n = len(elements)
    new_arr = copy.deepcopy(elements)
    st = set([])
    for i in range(n-1):
        new_arr.append(elements[i])
    
    for i in range(1, n+1):
        for j in range(n):
            st.add(sum(new_arr[j:j+i]))            

    
    return len(st)