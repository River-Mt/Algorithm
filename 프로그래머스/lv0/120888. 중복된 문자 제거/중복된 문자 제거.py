def solution(my_string):
    answer = ''
    d = {}
    for ch in my_string:
        if d.get(ch):
            continue
        else:
            answer += ch
            d[ch] = 1
    return answer