def isEmpty(p):
    if len(p) == 0: return True
    else: return False


def isCorrectStr(s):
    st = []
    
    for b in s:
        if b == '(':
            st.append(b)
        elif st:
            st.pop()
        else:
            return False
        
    return True


def solve(p):
    if isEmpty(p): return ""
    
    open = 0
    p_len = len(p)
    
    for i in range(p_len):
        if p[i] == '(': open += 1
        else: open -= 1
        
        if open == 0:
            
            if isCorrectStr(p[:i + 1]):
                return ''.join([p[:i + 1], solve(p[i + 1:])])
            
            else:
                v = ['(', solve(p[i + 1:]), ')']
                for j in range(1, i):
                    if p[j] == '(':
                        v.append(')')
                    else:
                        v.append('(')
            
            return ''.join(v)
    

    
def solution(p):
    
    answer = solve(p)
    
    return answer