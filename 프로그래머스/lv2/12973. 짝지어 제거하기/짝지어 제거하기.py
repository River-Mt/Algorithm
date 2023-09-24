def solution(s):
    answer = -1
    st = []
    
    for ch in s:
        if not st:
            st.append(ch)
            
        elif st[-1] == ch:
            st.pop()
            
        else:
            st.append(ch)

    return 0 if len(st) else 1