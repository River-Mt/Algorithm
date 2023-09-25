from collections import deque

def solution(s):
    answer = 0
    opens = ['[', '{', '(']
    closes = [']', '}', ')']
    dq = deque(list(s))
    
    def chk(s):
        st = []
        for b in s:
            idx = 0
            if not st:
                st.append(b)
                continue

            t = st[-1]
            flag = False    
            for i in range(3):
                if b == closes[i] and t == opens[i]:
                    st.pop()
                    flag = True

            if not flag:
                st.append(b)
        if not st:
            return 1
        else:
            return 0
        
    
    for i in range(len(s)):
        answer += chk(dq)            
        dq.rotate(-1)



    
    
    
    return answer