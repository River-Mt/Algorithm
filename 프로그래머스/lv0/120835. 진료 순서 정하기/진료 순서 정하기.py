def solution(emergency):
    answer = []
    order = {}
    idx = 1
    for e in sorted(emergency, reverse=True):
        order[e] = idx
        idx += 1
    
    for e in emergency:
        answer.append(order[e])
    return answer