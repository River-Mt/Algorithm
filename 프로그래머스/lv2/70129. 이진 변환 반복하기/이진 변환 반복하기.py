def solution(s):
    answer = []
    rmv = 0
    idx = 0
    while True:
        if s == '1':
            break

        rmv += s.count('0')
        s = bin(s.count('1'))[2:]
        idx += 1


    return [idx, rmv]