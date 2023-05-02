def solution(a, b, c, d):
    answer = 0
    li = [a, b, c, d]
    dice = [li.count(i) for i in li]
    
    if max(dice) == 4:
        answer = a * 1111
        
    elif max(dice) == 3:
        p = li[dice.index(max(dice))]
        q = li[dice.index(min(dice))]
        answer = (10 * p + q) ** 2
        
    elif max(dice) == 2 and min(dice) == 2:
        p = a
        q = a
        for i in li:
            if i != p:
                q = i
                break
        answer = (p + q) * abs(p - q)
        print(p, q)
        
    elif max(dice) == 2 or min(dice) == 2:
        p = li[dice.index(max(dice))]
        tmp = 1
        for i in li:
            if i != p:
                tmp *= i
        
        answer = tmp
        
    else:
        answer = min(a, b, c, d)

    return answer