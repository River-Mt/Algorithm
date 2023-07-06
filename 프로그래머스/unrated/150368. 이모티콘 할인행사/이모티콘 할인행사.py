import sys
sys.setrecursionlimit(10000)

def solution(users, emoticons):
    answer = [0, 0]
    perms = []
    discounts = [10, 20, 30, 40]
    
    def rep_perm(d, arr, n):
        if d == n:
            perms.append(arr)
            return
        for i in range(4):
            rep_perm(d + 1, arr + [discounts[i]], n)
            
    rep_perm(0, [], len(emoticons))
    
    for perm in perms:
        cnt = 0
        credit = 0
        
        for user in users:
            user_credit = 0
            d, lim = user[0], user[1]
            
            for i in range(len(perm)):
                if d <= perm[i]:
                    user_credit += int(emoticons[i] * ((100 - perm[i])) // 100)
            
            if user_credit >= lim:
                cnt += 1
                
            else: 
                credit += user_credit
                
        if answer[0] < cnt:
            answer = [cnt, credit]
            
        elif answer[0] == cnt:
            if answer[1] < credit:
                answer = [cnt, credit]
    
    
    return answer