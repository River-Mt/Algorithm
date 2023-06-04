def solution(order):
    answer = 0
    menu = {'americano':4500, 'cafelatte' : 5000}
    
    for o in order:
        if 'americano' in o:
            answer += menu['americano']
        elif 'cafelatte' in o:
            answer += menu['cafelatte']
        else: 
            answer += menu['americano']
    
    return answer