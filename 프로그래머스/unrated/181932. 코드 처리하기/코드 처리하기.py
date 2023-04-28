def solution(code):
    answer = ''
    mode = False
    for i in range(len(code)):
        ref = code[i]
        if ref == '1':
            mode = not mode
            continue
        if mode:
            if i%2:
                answer+=ref
        else:
            if not i%2:
                answer+=ref
                
    if len(answer) == 0:
        answer = "EMPTY"

    return answer