from collections import deque


def num_to_chr(num):
    return chr(num + ord('A'))


def init_order(order):
    for i in range(26):
        key = num_to_chr(i)
        order[key] = order.get(key, 0)
        
        
def set_skill_order(skill, order):
    idx = 1
    for s in skill:
        order[s] = idx
        idx += 1
        

def learn_skill(skill_tree, order):
    dq = deque([0])
    isCanLearn = True
    
    for skill in skill_tree:
        skill_order = order[skill]
        
        if skill_order != 0:
            recent_learned_order = dq.pop()
            
            if recent_learned_order + 1 != skill_order:
                isCanLearn = False
                break
                
            else:
                dq.append(recent_learned_order)
                dq.append(skill_order)
                
    return int(isCanLearn)
                        
        
def solution(skill, skill_trees):
    answer = 0
    order = {}
    
    init_order(order)
    set_skill_order(skill, order)
    
    for skill_tree in skill_trees:
        answer += learn_skill(skill_tree, order)
    
    
    return answer