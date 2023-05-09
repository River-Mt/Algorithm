def lower_push(ch, n):
    return chr((ord(ch) - ord('a') + n) % 26 + ord('a'))

    
def upper_push(ch, n):
    return chr((ord(ch) - ord('A') + n) % 26 + ord('A'))


def solution(s, n):
    answer = ''
    for ch in s:
        if ch == ' ':
            answer += ch
        elif ch.islower():
            answer += lower_push(ch, n)
        else :
            answer += upper_push(ch, n)
        
    return answer