def solution(myString):
    answer = ''
    for ch in myString:
        if ord('l') > ord(ch):
            answer += 'l'
        else:
            answer += ch
    return answer