from copy import deepcopy
import math

def is_alp(s):
    if 'A' <= s <= 'Z':
        return True
    return False


def make_set(s):
    arr = {}
    for i in range(len(s)-1):
        if is_alp(s[i]) and is_alp(s[i+1]):
            #arr.append(s[i] + s[i+1])
            arr[s[i] + s[i+1]] = arr.get(s[i] + s[i+1], 0) + 1
            
    return arr



def solution(str1, str2):
    answer = 0
    set1 = make_set(str1.upper())
    set2 = make_set(str2.upper())
    
    inter_dic = deepcopy(set1)
    union_dic = deepcopy(set1)
    
    for key in inter_dic.keys():
        if not set2.get(key):
            inter_dic[key] = 0
        
        else:
            inter_dic[key] = min(set2[key], inter_dic[key])
    
    inter_cnt = sum(inter_dic.values())

    
    for key in set2.keys():
        if not union_dic.get(key):
            union_dic[key] = set2[key]
        
        else:
            union_dic[key] = max(set2[key], union_dic[key])
            
    union_cnt = sum(union_dic.values())
    

    return math.floor((inter_cnt / union_cnt) * 65536) if union_cnt != 0 else 65536