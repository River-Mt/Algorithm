def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    for i in range(len(answers)):
        ref = answers[i]
        if answers[i]==a[i%len(a)]:
            cnt1+=1
        if answers[i]==b[i%len(b)]:
            cnt2+=1
        if answers[i]==c[i%len(c)]:
            cnt3+=1
    
    tmp = []
    tmp.append((cnt1,1))
    tmp.append((cnt2,2))
    tmp.append((cnt3,3))
    
    tmp.sort(reverse=True)
    
    answer.append(tmp[0][1])
    
    for i in range(1,3):
        if tmp[i][0] != tmp[i-1][0]:
            break
        answer.append(tmp[i][1])
        
    answer.sort()
    
    
    return answer