def solution(myString):
    answer = ''
    for ch in myString:
        if ch == 'a':
            answer += 'A'
        elif ch.isupper() and ch != 'A':
            answer += ch.lower()
        else:
            answer += ch
    return answer